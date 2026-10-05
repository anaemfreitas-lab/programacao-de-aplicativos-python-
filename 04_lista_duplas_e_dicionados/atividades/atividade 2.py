produto = (
    "Notebook",
    "Informática",
    3500.00,
    "NB001"
)

print("Nome:", produto[0])
print("Categoria:", produto[1])
print("Preço:", produto[2])
print("Código:", produto[3])

print("\nInformações do produto:")

for informacao in produto:
    print(informacao)

print("\nQuantidade de informações:", len(produto))

try:
    produto[2] = 3000.00
except TypeError:
    print("\nNão é possível alterar um elemento da tupla.")

print("As tuplas são imutáveis, ou seja, depois de criadas")
print("não podemos modificar, adicionar ou remover seus elementos.")