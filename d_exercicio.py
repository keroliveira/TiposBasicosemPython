# Volume do cilindro

altura = float(input())
raio = float(input())

# V=π⋅r2⋅h

pi = 3.14
volume = pi * (raio ** 2) * altura

print(f"O volume do cilindro que tem {altura} de altura e {raio} de raio é igual a {volume:.2f}")