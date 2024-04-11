# порождающий полином
p = [1, 0, 0, 0, 1, 1, 0, 1, 1]

# функции инжекции сообщения (для инициализации)
func_inj3 = [[3, 2, 2, 1], [2, 3, 2, 2], [2, 2, 3, 4]]
func_inj4 = [[4, 6, 6, 7, 1], [7, 4, 6, 6, 2], [6, 7, 4, 6, 4], [6, 6, 7, 4, 8]]
func_inj5 = [[15, 8, 10, 10, 8, 1], [8, 15, 8, 10, 10, 2], [10, 8, 15, 8, 10, 4], [10, 10, 8, 15, 8, 8], [8, 10, 10, 8, 15, 16]]

func_inj = [func_inj3, func_inj4, func_inj5]

# Блоки для замены SubCrumb
blocks_for_subcrumb = ['0111', '1101', '1011', '1010', '1100', '0100', '1000', '0011', '0101', '1111', '0110', '0000', '1001', '0001', '0010', '1110']

v0 = [109, 37, 30, 105, 68, 176, 81, 224, 78, 170, 111, 180, 219, 247, 132, 101, 110, 41, 32, 17, 144, 21, 45, 244, 238, 5, 129, 57, 222, 246, 16, 187]
v1 = [195, 180, 75, 149, 217, 210, 242, 86, 112, 238, 233, 160, 222, 9, 159, 163, 93, 155, 5, 87, 143, 201, 68, 179, 207, 28, 207, 14, 116, 108, 213, 129]
v2 = [247, 239, 200, 157, 93, 186, 87, 129, 4, 1, 108, 229, 173, 101, 156, 5, 3, 6, 25, 79, 102, 109, 24, 54, 36, 170, 35, 10, 139, 38, 74, 231]
v3 = [133, 128, 117, 213, 54, 215, 156, 206, 229, 113, 247, 215, 32, 75, 31, 103, 53, 135, 12, 106, 87, 233, 233, 35, 20, 188, 184, 8, 124, 222, 114, 206]
v4 = [108, 104, 233, 190, 94, 196, 30, 34, 200, 37, 183, 199, 175, 251, 67, 99, 245, 223, 57, 153, 15, 198, 136, 241, 176, 114, 36, 204, 3, 232, 108, 234]

initial_vectors = [v0, v1, v2, v3, v4]

""" # для нулевого блока (чередуются нулевой и четвёртый)
consts_0 = [[48, 57, 148, 166], [224, 51, 120, 24], [192, 230, 82, 153], [68, 27, 169, 13], [108, 195, 58, 18], [127, 52, 212, 66], [220, 86, 152, 62], [147, 137, 33, 127], [30, 0, 16, 143], [229, 168, 188, 230], [120, 0, 66, 61], [82, 116, 186, 244], [143, 91, 120, 130], [38, 136, 155, 167], [150, 225, 219, 18], [154, 34, 110, 157]]

# для первого блока (чередуются нулевой и четвёртый)
consts_1 = [[182, 222, 16, 237], [1, 104, 95, 61], [112, 244, 122, 174], [5, 161, 124, 244], [7, 7, 163, 212], [189, 9, 202, 202], [28, 30, 143, 81], [244, 39, 43, 40], [112, 122, 61, 69], [20, 74, 229, 204], [174, 178, 133, 98], [250, 167, 174, 43], [186, 202, 21, 137], [46, 72, 241, 193], [64, 164, 111, 62], [185, 35, 199, 4]]

# для второго блока (чередуются нулевой и четвёртый)
consts_2 = [[252, 32, 217, 210], [226, 94, 114, 193], [52, 85, 46, 37], [230, 35, 187, 114], [122, 216, 129, 143], [92, 88, 164, 164], [132, 56, 118, 74], [30, 56, 226, 231], [187, 109, 224, 50], [120, 227, 139, 157], [237, 183, 128, 200], [39, 88, 103, 25], [217, 132, 115, 86], [54, 237, 165, 127], [162, 199, 132, 52], [112, 58, 172, 231]]

# для третьего блока (чередуются нулевой и четвёртый)
consts_3 = [[178, 19, 175, 165], [224, 40, 201, 191], [200, 78, 190, 149], [68, 117, 111, 145], [78, 96, 138, 34], [126, 143, 206, 50], [86, 216, 88, 254], [149, 101, 72, 190], [52, 59, 19, 143], [254, 25, 27, 226], [208, 236, 78, 61], [60, 178, 38, 229], [44, 235, 72, 130], [89, 68, 162, 142], [179, 173, 34, 8], [161, 196, 195, 85]]

# для четвёртого блока (чередуются нулевой и четвёртый)
consts_4 = [[240, 210, 233, 227], [80, 144, 213, 119], [172, 17, 215, 250], [45, 25, 37, 171], [27, 203, 102, 242], [180, 100, 150, 172], [111, 45, 155, 201], [209, 146, 90, 176], [120, 96, 38, 73], [41, 19, 26, 182], [142, 218, 233, 82], [15, 192, 83, 195], [59, 107, 165, 72], [63, 1, 79, 12], [237, 174, 149, 32], [252, 5, 60, 49]]

consts = [consts_0, consts_1, consts_2, consts_3, consts_4] """

# Также чередуются
consts_0 = [809079974, 3761469464, 3236319897, 1142663437, 1824733714, 2134168642, 3696662590, 2475237759, 503320719, 3853040870, 2013282877, 1383381748, 2405136514, 646486951, 2531384082, 2585947805]

consts_1 = [3068006637, 23617341, 1895070382, 94469364, 117941204, 3171535562, 471764817, 4096207656, 1887059269, 340452812, 2930935138, 4205293099, 3133805961, 776532417, 1084518206, 3106129668]

consts_2 = [4230011346, 3797840577, 877997605, 3861101426, 2061009295, 1549313188, 2218292810, 507044583, 3144540210, 2028178333, 3988226248, 660104985, 3649336150, 921544063, 2730984500, 1882893543]

consts_3 = [2987634597, 3760769471, 3360603797, 1148546961, 1314949666, 2123353650, 1457019134, 2506442942, 876286863, 4263058402, 3505147453, 1018308325, 753617026, 1497670286, 3014468104, 2714026837]

consts_4 = [4040354275, 1351669111, 2886850554, 756622763, 466314994, 3026491052, 1865259977, 3516029616, 2019567177, 689117878, 2396711250, 264262595, 996910408, 1057050380, 3987641632, 4228201521]

consts = [consts_0, consts_1, consts_2, consts_3, consts_4]

def amount_of_zeros(l):
    return 255 - (l*8 % 256)

def Add(a, b):
    return a ^ b

def Div(a):
    curr = 15
    for i in range(15):
        if a[i] == 1:
            curr = i
            break
    while curr < 7:
        for j in range(9):
            a[j+curr] = (p[j] + a[j+curr]) % 2
        for i in range(15):
            if a[i] == 1:
                curr = i
                break
    return int(''.join([str(x) for x in a]), 2)

def Multi(a, b):
    a, b = bin(a)[2:], [int(x) for x in bin(b)[2:]]
    l, c = len(a), [0 for _ in range(15)]
    for i in range(l-1, -1, -1):
        if a[i] == '1':
            start, l_b = 14 - ((l-1) - i), len(b)
            end, diff = start - l_b, start - (l_b - 1)
            for j in range(start, end, -1):
                c[j] = (c[j] + b[j-diff]) % 2
    return Div(c)

def Multi_Matrix(b, w): # b - blocks
    injection = func_inj[w-3] # выбираем нужные векторы
    res = [[0 for _ in range(32)] for _ in range(w)]
    for i in range(w):
        for j in range(w+1):
            curr, z = injection[i][j], []
            for each in b[j]:
                value = Multi(each, curr)
                z.append(value)
            for k in range(32):
                res[i][k] = Add(res[i][k], z[k])
    return res

def Trans(a): # переводит массив байт в строку соответствующего числа бит
    result = ''
    for number in a:
        curr_byte = bin(number)[2:]
        result += ('0'*(8-len(curr_byte)) + curr_byte)
    return result

def MegaTrans(words):
    return [Trans(x) for x in words]

def Shift(n, d): # реализует сдвиг на d
    return ( (n << d) % 4294967296 ) | (n >> (32 - d))

def bin32(a): # переводит число к 32 символьной двоичной строке
    result = bin(a)[2:]
    return (32-len(result))*'0'+result

def opp_Trans(a): # переводит 32-символьную строку в массив из 4 байт
    result = []
    for i in range(4):
        curr = a[i*8:i*8+8]
        result.append(int(curr, 2))
    return result

def SubCrumb(a): # a - список из 4-ёх 4-байтовых списков
    a = MegaTrans(a)
    new_a = ['' for _ in range(4)]
    for l in range(32):
        number_of_block = int(a[3][l] + a[2][l] + a[1][l] + a[0][l], 2)
        curr_block = blocks_for_subcrumb[number_of_block]
        for j in range(3, -1, -1):
            new_a[j] += curr_block[3-j]
    return [opp_Trans(x) for x in new_a]

def Mix_Word(x, x4):
    x, x4 = int(Trans(x), 2), int(Trans(x4), 2) ## переводим числа
    y4 = Add(x, x4)
    y = Shift(x, 2)
    y = Add(y, y4)
    y4 = Shift(y4, 14)
    y4 = Add(y, y4)
    y = Shift(y, 10)
    y = Add(y, y4)
    y4 = Shift(y4, 1)
    return opp_Trans(bin32(y)), opp_Trans(bin32(y4))

def Add_Constant(a0, a4, num_of_block, num_of_round):
    a0, a4 = int(Trans(a0), 2), int(Trans(a4), 2)
    add1, add2 = consts[num_of_block][2*num_of_round], consts[num_of_block][2*num_of_round+1]
    a0, a4 = Add(a0, add1), Add(a4, add2)
    return opp_Trans(bin32(a0)), opp_Trans(bin32(a4))

def Permutation(b): ## на входе блоки 1..w
    ready_blocks = []
    for j, curr_block in enumerate(b):
        words = []
        for i in range(8):
            words.append(curr_block[4*i:4*i+4])
        words = Tweak(words)
        for round in range(8):
            words[:4] = SubCrumb(words[:4])
            words[4:] = SubCrumb(words[4:])
            for k in range(4):
                words[k], words[k+4] = Mix_Word(words[k], words[k+4])
            Add_Constant(words[0], words[4], j, round)
        ready_block = []
        for x in words:
            ready_block.extend(x)
        ready_blocks.append(ready_block)
    return ready_blocks

def Tweak(words):
    for j in range(4, 8):
        curr_word = Trans(words[j])
        words[j] = opp_Trans(curr_word[-j:] + curr_word[:-j])
    return words

with open('file1.txt', 'rb') as file:
    w = ord(file.read(1)) - 48
    if not(w in [3, 4, 5]):
        print('Введите корректное значение w')
    blocks, curr_block = list(), list()
    while True:
        curr_block = list(file.read(32))                           # считываем блок
        if len(curr_block) != 32:
            if len(curr_block) != 0:                                # пока что думаю, что по байтам
                q = amount_of_zeros(len(curr_block))                # количество нулей, что нужно добавить
                adding_str, adding_list = '1' + '0'*q, []
                for j in range(32 - len(curr_block)):               # собираем оставшийся блок
                    curr_byte = adding_str[j*8:j*8+8]
                    adding_list.append(int(curr_byte, 2))
                curr_block.extend(adding_list)
                blocks.append(curr_block)                           # формируем итоговый результат
            break
        blocks.append(curr_block)
    l, previous_blocks = len(blocks), initial_vectors[:w]           # фиксируем количество раундов; выбираем векторы по параметру w
    for i in range(l):
        curr_blocks = previous_blocks + [blocks[i]]                 # основная
        MI = Multi_Matrix(curr_blocks, w)                           # часть
        previous_blocks = Permutation(MI)                           # хэш-функции
    block_of_zeros = [0 for _ in range(32)]
    curr_blocks = previous_blocks + [block_of_zeros]
    result_block = Multi_Matrix(curr_blocks, w)
    result = [0 for _ in range(32)]
    for i in range(w):
        result = [Add(result[j], result_block[i][j]) for j in range(32)]
    print(*[hex(x)[2:] for x in result])

a, start = [], 1
for i in range(255):
    start = Multi(start, 2)
    a.append(start)
print(a)







        















