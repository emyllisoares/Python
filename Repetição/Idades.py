idade = 0
soma = 0 
quantidade = 0

while idade < 150:
    idade = int(input(f"Digite a idade {quantidade+1}: "))
    if idade < 150:
        soma += idade
        quantidade += 1

if quantidade == 0:
    print|("Não foi digitada idade alguma.")
else:
    media = soma / quantidade
    print(f"A média das {quantidade} idades é: {media}")