#algoritmo
#declarar
vet = []
valor = 0
cta = 0
soma = 0
media = 0

#inicio
for i in range(10):
    valor = int(input(f"Digite o {i + 1}° valor: "))
    vet.append(valor)
    if (valor >= 10 and valor <= 200):
        media = media + valor
        cta = cta + 1
    elif (valor % 2 == 1):
        soma = soma + valor

media = media / cta
print("O média é de ", media)
print("Asoma dos ímpares é de ", soma)
