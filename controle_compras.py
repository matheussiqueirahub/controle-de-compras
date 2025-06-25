produtos = {}

for i in range(5):
    nome = input(f"Digite o nome do produto {i + 1}: ")
    preco = float(input(f"Digite o preço de '{nome}': R$ "))
    produtos[nome] = preco  # Armazena no dicionário

total = sum(produtos.values())

print("\nResumo da compra:")
for produto, preco in produtos.items():
    print(f"- {produto}: R$ {preco:.2f}")

print(f"\nValor total da compra: R$ {total:.2f}")