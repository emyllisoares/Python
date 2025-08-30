numero = int(input('Digite um número inteiro positivo: '))
fatorial = 1 

if numero < 0:
    print("Fatorial não existe.")
elif numero == 0:
    print("Fatorial de 0 é igual  1.")
else: 
    for i in range(1, numero + 1):
        fatorial = fatorial * i
        
    print(f"Fatorial de {numero} é igual a {fatorial}.")