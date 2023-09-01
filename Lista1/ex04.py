entrada = input("Digite a lista de números separados por espaços: ")

numeros = [float(numero) for numero in entrada.split()]

if len(numeros) == 0:
    print("A lista está vazia.")
else:

    maior_valor = max(numeros)
    menor_valor = min(numeros)

    
    print(f"O maior valor na lista é: {maior_valor}")
    print(f"O menor valor na lista é: {menor_valor}")
