str = 'c (0) 4,0 = 0xf0d2e9e3, c (0) 4,4 = 0x5090d577 c (1) 4,0 = 0xac11d7fa, c (1) 4,4 = 0x2d1925ab c (2) 4,0 = 0x1bcb66f2, c (2) 4,4 = 0xb46496ac c (3) 4,0 = 0x6f2d9bc9, c (3) 4,4 = 0xd1925ab0 c (4) 4,0 = 0x78602649, c (4) 4,4 = 0x29131ab6 c (5) 4,0 = 0x8edae952, c (5) 4,4 = 0x0fc053c3 c (6) 4,0 = 0x3b6ba548, c (6) 4,4 = 0x3f014f0c c (7) 4,0 = 0xedae9520, c (7) 4,4 = 0xfc053c31'

l = str.split(' = ')
res = []
for x in l:
    if x[:2] == '0x':
        res.append(x[2:10])
print(res)
res1 = []
for x in res:
    res1.append([int(x[:2], 16), int(x[2:4], 16), int(x[4:6], 16), int(x[6:], 16)])
print(res1)


