import sys
import time
import numpy as np
import argparse
import os

l = 6
w = (2 ** l)    ## константы, фиксированные для хэш-функции
b = 25 * w

all_files = []

shifts = [[0, 36, 3, 41, 18],   ## значения, нужные для фунции rho
          [1, 44, 10, 45, 2],
          [62, 6, 43, 15, 61],
          [28, 55, 25, 21, 56],
          [27, 20, 39, 8, 14]]

RCs = [0x0000000000000001, 0x0000000000008082, 0x800000000000808a,  ## значения для функции iota
       0x8000000080008000, 0x000000000000808b, 0x0000000080000001,
       0x8000000080008081, 0x8000000000008009, 0x000000000000008a,
       0x0000000000000088, 0x0000000080008009, 0x000000008000000a,
       0x000000008000808b, 0x800000000000008b, 0x8000000000008089,
       0x8000000000008003, 0x8000000000008002, 0x8000000000000080,
       0x000000000000800a, 0x800000008000000a, 0x8000000080008081,
       0x8000000000008080, 0x0000000080000001, 0x8000000080008008]

def bypass(path):
    current_directory = os.listdir(path)
    for file in current_directory:
        if os.path.isdir(path+'/'+file):
            bypass(path+'/'+file)
        else:
            all_files.append(path+'/'+file)
    return 0

def get_bitstring(message): ## переводит строковое сообщение в битовое представление
    bitstring = ''
    for character in message:
        byte = '{0:08b}'.format(ord(character))
        byte = byte[::-1]
        bitstring += byte
    bitstring += '01100000'
    return bitstring

def get_bitstring_from_file(filename): ## считывает все байты из файла
    with open(filename, 'rb') as fh:
        bytetext = fh.read()
    return bytes_to_bitstring(bytetext)

def bytes_to_bitstring(in_bytes): ## переводит считанные байты в битовое представление
    bitstring = ''
    for bytechar in in_bytes:
        byte = '{0:08b}'.format(bytechar)
        byte = byte[::-1]
        bitstring += byte
    bitstring += '01100000'
    return bitstring

def string_to_array(string,w=64): ## переводит строку в массив
    state_array = np.zeros([5,5,w], dtype=int) ## задаём массив
    for x in range(5):
        for y in range(5):
            for z in range(w):
                if (w*(5*x+y)+z) < len(string):
                    state_array[y][x][z] = int(string[w*(5*x+y)+z])
    return state_array

def hex_to_array(hexnum, w=64): ## переводит шестнадцатеричное число в массив
    bitstring = '{0:064b}'.format(hexnum)
    bitstring = bitstring[-w:]
    array = np.array([int(bitstring[i]) for i in range(w)])
    return array

def pad(rate, message_length): ## дополнение сообщения до нужной длины
    j = (-(message_length + 1)) % rate
    return '0' * j + '1'

def theta(array, w=64): ## функция тетта
    array_prime = array.copy()
    C, D = np.zeros([5,w], dtype=int), np.zeros([5,w], dtype=int)
    for x in range(5):
        for y in range(5):
            C[x] ^= array[x][y]
    for x in range(5):
        D[x] = C[(x-1) % 5] ^ np.roll(C[(x+1) % 5],1)
    for x in range(5):
        for y in range(5):
            array_prime[x][y] ^= D[x]
    return array_prime

def rho(array, w=64): ## функция ро
    array_prime = array.copy()
    for x in range(5):
        for y in range(5):
            array_prime[x][y] = np.roll(array[x][y], shifts[x][y]) ## реализуем сдвиги согласно спецификации
    return array_prime

def pi(array, w=64): ## функция пи
    array_prime = array.copy()
    for x in range(5):
        for y in range(5):
            array_prime[x][y] = array[(x + (3 * y)) % 5][x]
    return array_prime

def chi(array, w=64): ## функция хи
    array_prime = np.zeros(array.shape, dtype=int)
    for x in range(5):
        for y in range(5):
            array_prime[x][y] = array[x][y] ^ ((array[(x + 1) % 5][y] ^ 1) & (array[(x + 2) % 5][y]))
    return array_prime

def iota(array, round_index, w=64): ## функция йота
    RC = hex_to_array(RCs[round_index], w)
    RC = np.flip(RC)
    array_prime = array.copy()
    array_prime[0][0] ^= RC
    return array_prime

def keccak(state): ## реализует алгоритм над массивом
    for round_index in range(24):
        state = iota(chi(pi(rho(theta(state)))), round_index)
    return state

def squeeze(array, bits):
    hash = ''
    for i in range(5):
        for j in range(5):
            lane = array[j][i]
            lanestring = ''
            for m in range(len(lane)):
                lanestring += str(lane[m])
            for n in range(0,len(lanestring),8):
                byte = lanestring[n:n+8]
                byte = byte[::-1]
                hash += '{0:02x}'.format(int(byte,2))
    return hash[:int(bits/4)]

def usage():
    print(f"[***] Usage: {sys.argv[0]} [-m <message string> | -i <filename>] -o <output-bits (224, 256, 384, or 512)>")
    exit()

def main():
    start = time.time()
    parser = argparse.ArgumentParser(description='parser_main_info') ## создали парсер командной строки

    group = parser.add_mutually_exclusive_group() ## создали менеджер, который будет следить за взаимоисключением аргументов
    group.add_argument("-m", "--message", type=str, help="string to be hashed")
    group.add_argument("-i", "--input_file", type=str, help="input file to be hashed")
    parser.add_argument("-o", "--output_bits", type=str, help="hash function output bits (224, 256, 384, 512)")

    args = parser.parse_args() ## забираем
    message = args.message ## аргументы
    filename = args.input_file ## из парсера

    if not args.output_bits:
        outbits = 256
    elif args.output_bits in ['224','256','384','512']:
        outbits = int(args.output_bits)
    else:
        usage()

    capacity = 2 * outbits ## параметры, нужные для алгоритма
    rate = b - capacity
    bitstring = ''

    if message: ## разбираемся с тем, что получили
        bitstring = get_bitstring(message)
    elif filename:
        path = os.path.abspath(filename)
        if os.path.isdir(filename):
            bypass(path)
            for curr_file in all_files:
                bitstring += get_bitstring_from_file(curr_file)
        else:
            bitstring = get_bitstring_from_file(path)
    else:
        bitstring = get_bitstring('')

    padded = bitstring + pad(rate, len(bitstring) % rate) ## дополняем до нужной длины (padding)
    sponge_rounds = len(padded) // rate ## количество раундов функции
    state = np.zeros(b, dtype=int).reshape(5, 5, w) ## привели массив к другой форме

    for i in range(sponge_rounds):
        current_string = padded[(i*rate):(i*rate) + rate]
        array = string_to_array(current_string, w=64)
        state = np.bitwise_xor(state, array)
        state = keccak(state)

    print(squeeze(state, outbits))
    end = time.time()
    print(f'Время выполнения программы: {end - start}')
    exit()

if __name__ == '__main__':
    main()