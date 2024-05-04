import os.path
from functools import reduce
import time
import sys
import argparse

multi = (-1, 0, 1, 157, 2, 59, 158, 151, 3, 53, 60, 132, 159, 70, 152, 216, 4, 118, 54, 38, 61, 47, 133, 227, 160, 181,
         71, 210, 153, 34, 217, 16, 5, 173, 119, 221, 55, 43, 39, 191, 62, 88, 48, 83, 134, 112, 228, 247, 161, 28, 182,
         20, 72, 195, 211, 242, 154, 129, 35, 207, 218, 80, 17, 204, 6, 106, 174, 164, 120, 9, 222, 237, 56, 67, 44, 31,
         40, 109, 192, 77, 63, 140, 89, 185, 49, 177, 84, 125, 135, 144, 113, 23, 229, 167, 248, 97, 162, 235, 29, 75,
         183, 123, 21, 95, 73, 93, 196, 198, 212, 12, 243, 200, 155, 149, 130, 214, 36, 225, 208, 14, 219, 189, 81, 245,
         18, 240, 205, 202, 7, 104, 107, 65, 175, 138, 165, 142, 121, 233, 10, 91, 223, 147, 238, 187, 57, 253, 68, 51,
         45, 116, 32, 179, 41, 171, 110, 86, 193, 26, 78, 127, 64, 103, 141, 137, 90, 232, 186, 146, 50, 252, 178, 115,
         85, 170, 126, 25, 136, 102, 145, 231, 114, 251, 24, 169, 230, 101, 168, 250, 249, 100, 98, 99, 163, 105, 236,
         8, 30, 66, 76, 108, 184, 139, 124, 176, 22, 143, 96, 166, 74, 234, 94, 122, 197, 92, 199, 11, 213, 148, 13,
         224, 244, 188, 201, 239, 156, 254, 150, 58, 131, 52, 215, 69, 37, 117, 226, 46, 209, 180, 15, 33, 220, 172,
         190, 42, 82, 87, 246, 111, 19, 27, 241, 194, 206, 128, 203, 79)

nonlinear_vector = (252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35, 197, 4, 77, 233,
        119, 240, 219, 147, 46, 153, 186, 23, 54, 241, 187, 20, 205, 95, 193, 249, 24, 101,
        90, 226, 92, 239, 33, 129, 28, 60, 66, 139, 1, 142, 79, 5, 132, 2, 174, 227, 106, 143,
        160, 6, 11, 237, 152, 127, 212, 211, 31, 235, 52, 44, 81, 234, 200, 72, 171, 242, 42,
        104, 162, 253, 58, 206, 204, 181, 112, 14, 86, 8, 12, 118, 18, 191, 114, 19, 71, 156,
        183, 93, 135, 21, 161, 150, 41, 16, 123, 154, 199, 243, 145, 120, 111, 157, 158, 178,
        177, 50, 117, 25, 61, 255, 53, 138, 126, 109, 84, 198, 128, 195, 189, 13, 87, 223,
        245, 36, 169, 62, 168, 67, 201, 215, 121, 214, 246, 124, 34, 185, 3, 224, 15, 236,
        222, 122, 148, 176, 188, 220, 232, 40, 80, 78, 51, 10, 74, 167, 151, 96, 115, 30, 0,
        98, 68, 26, 184, 56, 130, 100, 159, 38, 65, 173, 69, 70, 146, 39, 94, 85, 47, 140, 163,
        165, 125, 105, 213, 149, 59, 7, 88, 179, 64, 134, 172, 29, 247, 48, 55, 107, 228, 136,
        217, 231, 137, 225, 27, 131, 73, 76, 63, 248, 254, 141, 83, 170, 144, 202, 216, 133,
        97, 32, 113, 103, 164, 45, 43, 9, 91, 203, 155, 37, 208, 190, 229, 108, 82, 89, 166,
        116, 210, 230, 244, 180, 192, 209, 102, 175, 194, 57, 75, 99, 182)

opp_nonlinear_vector = (165, 45, 50, 143, 14, 48, 56, 192, 84, 230, 158, 57, 85, 126, 82, 145, 100, 3, 87, 90, 28, 96, 7, 24, 33, 114,
       168, 209, 41, 198, 164, 63, 224, 39, 141, 12, 130, 234, 174, 180, 154, 99, 73, 229, 66, 228, 21, 183, 200, 6,
       112, 157, 65, 117, 25, 201, 170, 252, 77, 191, 42, 115, 132, 213, 195, 175, 43, 134, 167, 177, 178, 91, 70, 211,
       159, 253, 212, 15, 156, 47, 155, 67, 239, 217, 121, 182, 83, 127, 193, 240, 35, 231, 37, 94, 181, 30, 162, 223,
       166, 254, 172, 34, 249, 226, 74, 188, 53, 202, 238, 120, 5, 107, 81, 225, 89, 163, 242, 113, 86, 17, 106, 137,
       148, 101, 140, 187, 119, 60, 123, 40, 171, 210, 49, 222, 196, 95, 204, 207, 118, 44, 184, 216, 46, 54, 219, 105,
       179, 20, 149, 190, 98, 161, 59, 22, 102, 233, 92, 108, 109, 173, 55, 97, 75, 185, 227, 186, 241, 160, 133, 131,
       218, 71, 197, 176, 51, 250, 150, 111, 110, 194, 246, 80, 255, 93, 169, 142, 23, 27, 151, 125, 236, 88, 247, 31,
       251, 124, 9, 13, 122, 103, 69, 135, 220, 232, 79, 29, 78, 4, 235, 248, 243, 62, 61, 189, 138, 136, 221, 205, 11,
       19, 152, 2, 147, 128, 144, 208, 36, 52, 203, 237, 244, 206, 153, 16, 68, 64, 146, 58, 1, 38, 18, 26, 72, 104,
       245, 129, 139, 199, 214, 32, 10, 8, 0, 76, 215, 116)

const = ('110 162 118 114 108 72 122 184 93 39 189 16 221 132 148 1',
         '220 135 236 228 216 144 244 179 186 78 185 32 121 203 235 2',
         '178 37 154 150 180 216 142 11 231 105 4 48 164 79 127 3',
         '123 205 27 11 115 227 43 165 183 156 177 64 242 85 21 4',
         '21 111 109 121 31 171 81 29 234 187 12 80 47 209 129 5',
         '167 74 247 239 171 115 223 22 13 210 8 96 139 158 254 6',
         '201 232 129 157 199 59 165 174 80 245 181 112 86 26 106 7',
         '246 89 54 22 230 5 86 137 173 251 161 128 39 170 42 8',
         '152 251 64 100 138 77 44 49 240 220 28 144 250 46 190 9',
         '42 222 218 242 62 149 162 58 23 181 24 160 94 97 193 10',
         '68 124 172 128 82 221 216 130 74 146 165 176 131 229 85 11',
         '141 148 45 29 149 230 125 44 26 103 16 192 213 255 63 12',
         '227 54 91 111 249 174 7 148 71 64 173 208 8 123 171 13',
         '81 19 193 249 77 118 137 159 160 41 169 224 172 52 212 14',
         '63 177 183 139 33 62 243 39 253 14 20 240 113 176 64 15',
         '47 178 108 44 15 10 172 209 153 53 129 195 78 151 84 16',
         '65 16 26 94 99 66 214 105 196 18 60 211 147 19 192 17',
         '243 53 128 200 215 154 88 98 35 123 56 227 55 92 191 18',
         '157 151 246 186 187 210 34 218 126 92 133 243 234 216 43 19',
         '84 127 119 39 124 233 135 116 46 169 48 131 188 194 65 20',
         '58 221 1 85 16 161 253 204 115 142 141 147 97 70 213 21',
         '136 248 155 195 164 121 115 199 148 231 137 163 197 9 170 22',
         '230 90 237 177 200 49 9 127 201 192 52 179 24 141 62 23',
         '217 235 90 58 233 15 250 88 52 206 32 67 105 61 126 24',
         '183 73 44 72 133 71 128 224 105 233 157 83 180 185 234 25',
         '5 108 182 222 49 159 14 235 142 128 153 99 16 246 149 26',
         '107 206 192 172 93 215 116 83 211 167 36 115 205 114 1 27',
         '162 38 65 49 154 236 209 253 131 82 145 3 155 104 107 28',
         '204 132 55 67 246 164 171 69 222 117 44 19 70 236 255 29',
         '126 161 173 213 66 124 37 78 57 28 40 35 226 163 128 30',
         '16 3 219 167 46 52 95 246 100 59 149 51 63 39 20 31',
         '94 167 216 88 30 20 155 97 241 106 193 69 156 237 168 32')

all_files = []

def bypass(path):
    current_directory = os.listdir(path)
    for file in current_directory:
        if os.path.isdir(path+'/'+file):
            bypass(path+'/'+file)
        else:
            all_files.append(path+'/'+file)
    return 0

def Add(a, b):
    return a ^ b

def M(a, b):
    return multi.index((multi[a] + multi[b]) % 255) * (a != 0) * (b != 0)

def L(a):
    while len(a) < 16:
        a.append(0)
    linear_vector = (148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148, 1)
    for _ in range(16):
        elem = reduce(Add, [M(a[i], linear_vector[i]) for i in range(16)], 0)
        a = [elem] + a[:15]
    return a

def opp_L(a):
    linear_vector = (1, 148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148)
    for _ in range(16):
        elem = reduce(Add, [M(a[i], linear_vector[i]) for i in range(16)], 0)
        a.pop(0)
        a.append(elem)
    return a

def S(a):
    while len(a) < 16:
        a.append(0)
    return [nonlinear_vector[x] for x in a]

def opp_S(a):
    return [opp_nonlinear_vector[x] for x in a]

def Keys_for_encryption(main_key):
    key1, key2 = main_key[:16], main_key[16:]
    keys = []
    for i in range(32):
        if i % 8 == 0:
            keys.append(key1)
            keys.append(key2)
        curr_const, curr_key = [int(x) for x in const[i].split()], key1.copy()
        curr_key = [Add(curr_key[j], curr_const[j]) for j in range(16)]
        curr_key = L(S(curr_key))
        curr_key = [Add(curr_key[j], key2[j]) for j in range(16)]
        key1, key2 = curr_key, key1
    keys.append(key1)
    keys.append(key2)
    return keys

def Coding(block, keys):
    for i in range(9):
        curr_key = keys[i]
        block = [Add(curr_key[j], block[j]) for j in range(16)]
        block = L(S(block))
    block = [Add(keys[9][j], block[j]) for j in range(16)]
    return block

def DeCoding(block, keys):
    block = [Add(keys[9][j], block[j]) for j in range(16)]
    for i in range(9):
        block = opp_L(block)
        block = opp_S(block)
        curr_key = keys[8-i]
        block = [Add(curr_key[j], block[j]) for j in range(16)]
    return block

def Standart_Coding(data, key):
    i, l, blocks = 16, len(data), []
    while i < l:
        blocks.append(list(data[i - 16:i]))
        i += 16
    last_block = list(data[i - 16:])
    l = len(last_block)
    while l != 16:
        last_block.append(0)
        l += 1
    blocks.append(last_block)
    keys, ready_blocks = Keys_for_encryption(key), []
    for block in blocks:
        ready_block = Coding(block, keys)
        ready_blocks.append(ready_block)
    return ready_blocks

def Standart_Decoding(data, key):
    i, l, blocks = 16, len(data), []
    while i < l:
        blocks.append(list(data[i - 16:i]))
        i += 16
    last_block = list(data[i - 16:])
    blocks.append(last_block)
    keys, ready_blocks = Keys_for_encryption(key), []
    for block in blocks:
        ready_block = DeCoding(block, keys)
        ready_blocks.append(ready_block)
    return ready_blocks

def CBC_Decoding(data, init_vector, key):
    i, l, blocks = 16, len(data), []
    while i < l:
        blocks.append(data[i-16:i])
        i += 16
    blocks.append(list(data[i-16:]))
    blocks_decoded, i, keys = [], len(blocks), Keys_for_encryption(key)
    while i > 1:
        curr_block = DeCoding(blocks[i - 1], keys)
        curr_block = [Add(curr_block[j], blocks[i - 2][j]) for j in range(16)]
        blocks_decoded.append(curr_block)
        i -= 1
    first_block = DeCoding(blocks[0], keys)
    blocks_decoded.append([Add(first_block[j], init_vector[j]) for j in range(16)])
    return blocks_decoded

def CBC_Coding(data, init_vector, key):
    i, l, blocks = 16, len(data), []
    while i < l:
        blocks.append(list(data[i - 16:i]))
        i += 16
    last_block = list(data[i - 16:])
    add_value = 16 - len(last_block)
    while len(last_block) != 16:
        last_block.append(add_value)
    blocks.append(last_block)
    keys, i, l, blocks_coded = Keys_for_encryption(key), 1, len(blocks), []
    previous_block = Coding([Add(init_vector[i], blocks[0][i]) for i in range(16)], keys)
    while i < l:
        curr_block = Coding([Add(previous_block[j], blocks[i][j]) for j in range(16)], keys)
        blocks_coded.append(previous_block)
        previous_block, i = curr_block, i + 1
    blocks_coded.append(previous_block)
    return blocks_coded

def CTR(ctr):
    ctr[-1] += 1
    for i in range(14, 0, -1):
        ctr[i] = ctr[i] + (ctr[i+1] // 256)
    ctr = [x % 256 for x in ctr]
    return ctr

def ACPKM_Coding(data, ctr, key):  # s = 128 N = 256 n = 128
    i, sections, l = 32, [], len(data)
    while i < l:
        sections.append(data[i - 32:i])
        i += 32
    sections.append(data[i - 32:])
    ctr = list(ctr)
    ctr.extend([0, 0, 0, 0, 0, 0, 0, 0])
    curr_section_key, curr_section_keys, completed_sections = key, Keys_for_encryption(key), []
    for section in sections:
        blocks, completed_section = [section[:16]], []
        if len(section) > 16:
            blocks.append(section[16:])
        for block in blocks:
            gamma = Coding(ctr, curr_section_keys)
            completed_block = [Add(gamma[i], block[i]) for i in range(len(block))]
            completed_section.append(completed_block)
            ctr = CTR(ctr)
        completed_sections.extend(completed_section)
        curr_section_key = ACPKM(curr_section_key)
        curr_section_keys = Keys_for_encryption(curr_section_key)
    return completed_sections

def ACPKM(key):
    keys = Keys_for_encryption(key)
    d1 = [128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143]
    d2 = [144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159]
    return Coding(d1, keys) + Coding(d2, keys)

def usage():
    print(f"[***] Usage: {sys.argv[0]} -r <regime (0 or 1)>, -m <mode (CTR, CBC, ECB)>, -i1 <filename>, -i2 <filename>, -i3 <filename>")
    exit()

def get_bytes_from_file(path):
    with open(path, 'rb') as file:
        data = file.read()
    return data

def get_key_from_file(path):
    with open(path, 'rb') as file:
        key = file.read()
        if len(key) != 32:
            print('The key of the Grasshopper is 32 bytes. File you wrote includes more ones. Please, try again\n')
            usage()
    return key

def get_init_vector_from_file(path, mode):
    with open(path, 'rb') as file:
        init_vector = file.read()
        if mode == 'CBC':
            if len(init_vector) != 16:
                print('For mode CBC init-vector must be 16 bytes. Please, try again\n')
                usage()
        elif mode == 'CTR':
            if len(init_vector) != 8:
                print('For mode CTR-ACPKM ctr-vector must be 8 bytes. Please, try again\n')
                usage()
    return init_vector

def put_result_in_file(data):
    with open('result.txt', 'wb') as file:
        for block in data:
            file.write(bytes(block))
    return 0

def main():
    start = time.time()
    parser = argparse.ArgumentParser(description='Parser for getting nessecary info from command line')
    parser.add_argument('-r', '--regime', type=int, help='Regime (0 for coding; 1 for decoding)')
    parser.add_argument('-m', '--mode', type=str, help='Mode of Grasshopper (CTR, CBC, ECB)')
    parser.add_argument('-i1', '--input_data', type=str, help='File, which include the only data')
    parser.add_argument('-i2', '--input_key', type=str, help='File, which includes the only key')
    parser.add_argument('-i3', '--input_init_vector', type=str, help='File, which includes the only init_vector')

    args = parser.parse_args()
    regime = args.regime
    mode = args.mode

    input_data, data = args.input_data, bytes()
    if not(input_data is None):
        all_files.append(os.path.abspath(input_data))
        if os.path.isdir(all_files[0]):
            bypass(all_files[0])
        for curr_file in all_files:
            data += get_bytes_from_file(curr_file)

    input_key = args.input_key
    if input_key is None:
        usage()
    key = list(get_key_from_file(input_key))

    input_init_vector = args.input_init_vector

    if not(regime in (0, 1) and mode in ('CBC', 'CTR', 'ECB')):
        usage()
    if input_init_vector is None:
        if mode != 'ECB':
            print('Chosen mode requires init_vector')
            usage()
        if regime == 0:
            put_result_in_file(Standart_Coding(data, key))
            end = time.time()
            print(f'Время выполнения программы: {end - start}')
            exit()
        else:
            put_result_in_file(Standart_Decoding(data, key))
            end = time.time()
            print(f'Время выполнения программы: {end - start}')
            exit()
    else:
        input_init_vector = get_init_vector_from_file(input_init_vector, mode)

    if mode == 'CBC' and len(input_init_vector) == 16:
        if regime == 0:
            put_result_in_file(CBC_Coding(data, input_init_vector, key))
        else:
            put_result_in_file(CBC_Decoding(data, input_init_vector, key))
    elif mode == 'CTR':
        put_result_in_file(ACPKM_Coding(data, input_init_vector, key))
    else:
        if regime == 0:
            put_result_in_file(Standart_Coding(data, key))
        else:
            put_result_in_file(Standart_Decoding(data, key))
    end = time.time()
    print(f'Время выполнения программы: {end - start}')

if __name__ == '__main__':
    main()


































