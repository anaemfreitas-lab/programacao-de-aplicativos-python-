funcionario = {
    "nome": "Carlos",
    "idade": 30,
    "cargo": "Analista de Sistemas",
    "salario": 4500.00,
    "setor": "Tecnologia"
}

print("Nome:", funcionario["nome"])
print("Idade:", funcionario["idade"])
print("Cargo:", funcionario["cargo"])
print("Salário:", funcionario["salario"])
print("Setor:", funcionario["setor"])

funcionario["salario"] = 5000.00

print("\nNovo salário:", funcionario["salario"])

funcionario["email"] = "carlos@email.com"

del funcionario["idade"]

if "cargo" in funcionario:
    print("\nA chave 'cargo' existe no cadastro.")
else:
    print("\nA chave 'cargo' não existe no cadastro.")

print("\nCadastro final:")

for chave, valor in funcionario.items():
    print(f"{chave}: {valor}")