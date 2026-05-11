#algoritmo
#declarar
vet = []
vet2 = []
media = 0
cta = 0
valor = 0
qta_acima = 0

for i in range(30):
    valor = float(input(f"Digite a {i + 1}° nota: "))
    vet.append(valor)
    media = media + valor
    cta = cta + 1

media = media / cta

for i in range(30):
    valor = vet[i]
    if (valor > media):
        qta_acima = qta_acima + 1
    elif (valor < media):
        vet2.append(i)

print("A média do grupo é ", media)
print("A quantidade de notas acima do grupo é de ", qta_acima)
print("As posições dos valores menores estão em: ", )
