#Oque é uma função:

# Uma função é um bloco de código criado para realizar
# uma determinada tarefa.
# Ela permite organizar e reutilizar código.

#1. Criando uma função
#utilizar a palavra def para uma função

def saudação():
    print("Olá seja bem-vindo!")

saudação()

#2. Criando uma função com parametro

#parametros permitem enviar informações para a função.
def saudacao(nome):
    print(f"olá {nome}")

saudacao("Ana")

#3. Mais de um parametro
def apresentar(nome , idade):
    print(f"nome: {nome}")
    print(f"idade: {idade}")


apresentar("Maria", 17)


#4 função com calculo

def somar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"Resultado {resultado}")

    somar(10 , 20)


#5 Retornando um valor
#Return devolve um valor par ao local onde
#a função foi chamada

def somar(numero1, numero2):
   return  numero1 + numero2

print(somar(10,5))

#6 Função com condição
def verificarIdade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

print(verificarIdade(20))

#7 Parametro com valor padrão
def sadacao():
    print(f"Ola {nome}")

    saudacao("Ana")
    saudacao()

#8 Função utilizando lista
def calcularMedia(notas)
    soma = 0
    for nota in notas:
        soma += nota
   return soma / len(nota)
notas = [8 ,]





