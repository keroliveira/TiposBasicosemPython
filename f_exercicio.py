# Passou ou reprovou?

nota1 = float(input())
nota2 = float(input())

distancia1 = 10 - nota1
distancia2 = 10 - nota2
media = (nota1 + nota2) / 2
distancia_media = 10 - media

print(f"{distancia1:.1f}")
print(f"{distancia2:.1f}")
print(f"{media:.1f}")
print(f"{distancia_media:.1f}")
