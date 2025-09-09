#Faça um programa que receba uma quantidade variável de strings (termine a digitação com string vazia = '')
#Guarde essas informações em uma lista
#Criar outra lista onde cada elemento (palavra) se tranformará numa lista de carcateres únicos (não repetidos)
#Por exemplo:
#Se uma palavra da lista for igual a: 'barbante'
#A nova lista deverá conter: ['b', 'a', 'r', 't', 'n', 'e']
#Em seguida, mostre a lista modificada

palavras = []
lista = []

while True:
  palavra = input("Digite uma palavra (ou pressione Enter para sair): ")
  if palavra == '':
    break
  else:
    palavras.append(palavra)

for palavra in palavras:
  lista.append(list(set(palavra)))

print("\nLista de caracteres únicos para cada palavra:")
for item in lista:
  print(item)
