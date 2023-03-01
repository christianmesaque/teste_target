num = int(input("Digite um número: "))

fibonacci = [0, 1]

while fibonacci[-1] < num:
    value = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(value)

if num in fibonacci:
    print(fibonacci)
    print(f'O número {num} pertence à sequência de Fibonacci')
else:
    print(fibonacci)
    print(f'O número {num} não pertence à sequência de Fibonacci')