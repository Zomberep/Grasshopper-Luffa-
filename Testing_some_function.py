'''with open('file1.txt', 'wb') as file:
    text = '7f679d90bebc24305a468d42b9d4edcd'
    text = [int(text[2 * i:2 * i + 2], 16) for i in range(16)]
    key = '8899aabbccddeeff0011223344556677fedcba98765432100123456789abcdef'
    key = [int(key[2 * i:2 * i + 2], 16) for i in range(32)]
    file.write(b'1WTH')
    file.write(bytes(key))
    file.write(bytes(text))'''

with open('file1.txt', 'rb') as file:
    unness_info = file.read(4)
    init_vector = file.read(16)
    key = file.read(32)
    info = file.read()
    print(len(info))



