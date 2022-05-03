# Задание 3 (3 варианта)
n = int(input("Введите число "))
nn = n * 11
nnn = n * 111
total = n + nn + nnn

print(f"{n}+{nn}+{nnn}={total}")

print(f"{n}+{n*11}+{n*111}={n+n*11+n*111}")

nn = int(str(n)+str(n))
nnn = int(str(nn)+str(n))
print(f"{n}+{nn}+{nnn}={n+nn+nnn}")
