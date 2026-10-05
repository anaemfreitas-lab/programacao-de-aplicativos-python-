notas = [8.5, 7.0, 9.0, 6.5, 10.0]

print("Notas:")
for nota in notas:
    print(nota)

soma = sum(notas)
print("\nSoma das notas:", soma)

media = soma / len(notas)
print("Média:", media)

print("Maior nota:", max(notas))

print("Menor nota:", min(notas))

if 10 in notas:
    print("Existe uma nota igual a 10.")
else:
    print("Não existe uma nota igual a 10.")

if media >= 7:
    print("Estudante aprovado!")
else:
    print("Estudante reprovado!")