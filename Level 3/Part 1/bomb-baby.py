def solution(x, y):
    gen = 0
    m = int(x)
    f = int(y)
    while True:
        if m == 1 and f == 1:
            return str(gen)
        elif m < 1 or f < 1 or m == f:
            return "impossible"
        else:
            if m > f:
                if m > 100 * f:
                    gen += int(m / f)
                    m = m - (int(m / f) * f)
                else:
                    m -= f
                    gen += 1
            else:
                if f > 100 * m:
                    gen += int(f / m)
                    f = f - (int(f / m) * m)
                else:
                    f -= m
                    gen += 1
