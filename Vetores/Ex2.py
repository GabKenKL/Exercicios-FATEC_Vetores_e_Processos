#algoritmo
#declarar
vetor = []
valor = 0
maior = 0
menor = 0
media = 0
cta = 0

for i in range(10):
    valor = int(input(f"Digite o {i + 1}° valor: "))
    if (i == 0):
        maior = valor
        menor = valor
    else:
        if (valor > maior):
            maior = valor
        elif (valor < menor):
            menor = valor
    media = media + valor
    cta = cta + 1

media = media / cta

print("O maior valor é ", maior, "e o menor valor é ", menor)
print("A média é de ", media)
