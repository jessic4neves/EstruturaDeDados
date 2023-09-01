nomes = input("Digite uma lista de nomes separados por vírgulas: ")

lista_de_nomes = nomes.split(',')

nomes_com_A = []

for nome in lista_de_nomes:
    nome = nome.strip()
    if nome.startswith('A') or nome.startswith('a'):
        nomes_com_A.append(nome)

print("Nomes que começam com 'A':")
for nome in nomes_com_A:
    print(nome)
