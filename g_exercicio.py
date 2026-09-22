# Qual o valor do produto final?

custo = float(input())
percentual = float(input())

valor_final = custo * (1 + percentual / 100)

print(f"Valor final do produto: R$ {valor_final:.4f}.")