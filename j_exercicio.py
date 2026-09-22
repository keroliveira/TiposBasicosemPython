# Faturamento do show

total = int(input())
percentual_meia = int(input())
valor_inteira = float(input())

# Forçando inteiro com //
total_meia = total * percentual_meia // 100
total_inteira = total - total_meia

valor_meia = valor_inteira / 2

faturamento_meia = total_meia * valor_meia
faturamento_inteira = total_inteira * valor_inteira
faturamento_total = faturamento_meia + faturamento_inteira

print(f"Quantidade de ingressos meia-entrada: {total_meia}")
print(f"Quantidade de ingressos inteiros: {total_inteira}")
print(f"Faturamento com meia-entrada: R${faturamento_meia:.2f}")
print(f"Faturamento com inteira: R${faturamento_inteira:.2f}")
print(f"Faturamento total: R${faturamento_total:.2f}")