estoque = [
    {
        "nome": "Notebook",
        "categoria": "Informática",
        "preco": 3500.00,
        "quantidade": 8
    },
    {
        "nome": "Mouse",
        "categoria": "Periféricos",
        "preco": 80.00,
        "quantidade": 25
    },
    {
        "nome": "Teclado",
        "categoria": "Periféricos",
        "preco": 150.00,
        "quantidade": 7
    },
    {
        "nome": "Monitor",
        "categoria": "Informática",
        "preco": 1200.00,
        "quantidade": 12
    },
    {
        "nome": "Headset",
        "categoria": "Periféricos",
        "preco": 250.00,
        "quantidade": 5
    }
]

print("=== PRODUTOS DO ESTOQUE ===")

for produto in estoque:
    print(f"Nome: {produto['nome']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Quantidade: {produto['quantidade']}")
    print("---------------------------")

quantidade_total = 0

for produto in estoque:
    quantidade_total += produto["quantidade"]

print("\nQuantidade total de itens:", quantidade_total)

valor_total = 0

for produto in estoque:
    valor_total += produto["preco"] * produto["quantidade"]

print(f"Valor total do estoque: R$ {valor_total:.2f}")

print("\nProdutos com menos de 10 unidades:")

for produto in estoque:
    if produto["quantidade"] < 10:
        print(produto["nome"])

produto_procurado = "Mouse"
encontrado = False

for produto in estoque:
    if produto["nome"] == produto_procurado:
        encontrado = True
        break

if encontrado:
    print(f"\n{produto_procurado} está cadastrado no estoque.")
else:
    print(f"\n{produto_procurado} não está cadastrado no estoque.")

for produto in estoque:
    if produto["nome"] == "Mouse":
        produto["quantidade"] = 30

print("\nQuantidade de Mouse alterada.")

novo_produto = {
    "nome": "Webcam",
    "categoria": "Periféricos",
    "preco": 300.00,
    "quantidade": 15
}

estoque.append(novo_produto)

print("Novo produto adicionado.")

print("\n================================")
print("       RELATÓRIO FINAL")
print("================================")

for produto in estoque:
    print(f"Nome: {produto['nome']}")
    print(f"Categoria: {produto['categoria']}")
    print(f"Preço: R$ {produto['preco']:.2f}")
    print(f"Quantidade: {produto['quantidade']}")
    print("--------------------------------")
