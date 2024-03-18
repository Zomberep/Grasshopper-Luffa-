# w = 4

def amount_of_zeros(l):
    return 255 - (l % 256)

def Add(a, b):
    return a ^ b

def M(a, b):
    return multi.index((multi[a] + multi[b]) % 255) * (a != 0) * (b != 0)