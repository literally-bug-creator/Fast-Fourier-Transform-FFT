

def fft(A: list):
    return sec_fft(A, False)


def ifft(A: list):
    a = sec_fft(A, True)

    return a


MOD = 7340033
ROOT = 5
ROOT_INV = 4404020
ROOT_PW = 1 << 20


def sec_fft(a, invert):
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j >= bit:
            j -= bit
            bit >>= 1
        j += bit
        if i < j:
            a[i], a[j] = a[j], a[i]

    len_ = 2
    while len_ <= n:
        wlen = ROOT_INV if invert else ROOT
        i = len_
        while i < ROOT_PW:
            wlen = (wlen * wlen) % MOD
            i <<= 1
        i = 0
        while i < n:
            w = 1
            for j in range(len_ // 2):
                u = a[i + j]
                v = (a[i + j + len_ // 2] * w) % MOD
                a[i + j] = (u + v) % MOD if (u + v) < MOD else (u + v - MOD)
                a[i + j + len_ // 2] = (u - v) % MOD if (u - v) >= 0 else (u - v + MOD)
                w = (w * wlen) % MOD
            i += len_
        len_ <<= 1

    if invert:
        n_inv = pow(n, MOD - 2, MOD)
        for i in range(n):
            a[i] = (a[i] * n_inv) % MOD
    return a

