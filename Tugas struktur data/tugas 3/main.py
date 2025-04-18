# tugas 3

jumlah = int(input("Masukkan jumlah deret Fibonacci: "))
a, b = 1, 1
fibonacci = []

for i in range(jumlah):
    fibonacci.append(str(a))
    a, b = b, a + b

print(', '.join(fibonacci))
