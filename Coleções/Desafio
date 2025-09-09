#Faça um programa que receba informações (nome, idade e número do calçado) de 5 pessoas distintas
#Depois de receber as informações você deve mostrar a relação completa das pessoas e suas informações em ordem alfabética (de nome)
#Ao final do relatório, você deve calcular e mostrar as seguintes informações:
#A média da idade das pessoas
#Número médio do calçado das pessoas pesquisadas 

informacoes = []

for i in range(1, 6):
  
  print(f"\nDigite as informações da {i}ª pessoa:")
  nome = input("Digite o nome: ")
  idade = int(input("Digite a idade: "))
  num_calcado = int(input("Digite o número do calçado: "))
  print("-" * 30)

  informacao = [nome, idade, num_calcado]
  informacoes.append(informacao)

#Cria uma nova lista em orfdem alfabética
informacoes_ordenadas = sorted(informacoes)

total_idades = 0
total_calcados = 0

print("\nRelação completa das pessoas e suas informações em ordem alfabética:")
for i in range(0, 5):
  total_idades += informacoes_ordenadas[i][1]
  total_calcados += informacoes_ordenadas[i][2] 
  print(f"Nome: {informacoes_ordenadas[i][0]} - Idade: {informacoes_ordenadas[i][1]} - Número do calçado: {informacoes_ordenadas[i][2]}")

media_idades = total_idades / 5
media_calcados = total_calcados / 5

print(f"\nMédia da idade das pessoas: {media_idades:.1f}")
print(f"Média do número do calçado das pessoas: {media_calcados:.1f}")
  