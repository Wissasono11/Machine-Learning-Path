def func(x):
    return x**2-5*x + 4
def regular_falsi(a, b, tolerance):
    if func(a) * func(b) >= 0:
        print("Metode regular falsi tidak dapat digunakan pada interval ini.")
        return None

    iterasi = 0
    while (b - a) >= tolerance:
        c = (a * func(b) - b * func(a)) / (func(b) - func(a))
        if abs(func(c)) < tolerance:
            break
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

        iterasi += 1
    print(f"Akar yang ditemukan: {c}")
    print(f"Jumlah iterasi: {iterasi}")

a = 2
b = 5
tolerance = 0.001
regular_falsi(a, b, tolerance)
