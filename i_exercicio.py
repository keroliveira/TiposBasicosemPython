# Quero receber mais...

salario = float(input())
horas_por_dia = int(input())
dias_trabalhados = int(input())

total_horas = horas_por_dia * dias_trabalhados

valor_hora = salario / total_horas

print(f"Eu recebo uma mixuruca de R$ {valor_hora:.1f} por hora trabalhada.")