1. Estrutura condicionais
notaa = 6

if notaa >= 7:
    print('Aprovado')
    elif nota >= 5:
        print('Recuperação')
else:
print('Reprovado')
# 2. Cpndições com operadores lógicos
#and -> todas condicoes devem ser verdadeiras
#or -> pelo menos uma condição deve ser verdadeira
#not -> inverte o resultado


idade = 20

ingresso = True

if idade >= 18 and ingresso:
    print('Entrada permitida')
else:
    print("Entrada não permitida")

# 3. Estrutura de Repetição

contador = 1

while contador <= 10:
    print(contador)
    contador += 1

 # 4. estrutura de repetição for
 for numero in  range(1,6):
    print(numero)

 # 5. percorrendo uma Lista
 nomes = [ "Ana" , "Carlos" , "João" , "Maria"]

 for nome in nomes:
   print(nome)

   #6. break
   #0 breck intewrronpe  completamente a repetição
   #0 pass nao execulta nenhuma ação
   #0 continue interrompe apenas a repetiçao atual

   for numero in range(1,11):

    if numero == 7:
        #break
        #pass
       continue

        print (numero)
# 7. Condição dentro de repetição
for numero in range(1,11):
    if numero % 2 == 0:
        print (f"{numero} é par")
    else:
        print (f"{numero} é impar")
