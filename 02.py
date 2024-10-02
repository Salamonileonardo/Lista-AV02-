def contar_num(numeros):
    return len(str( abs(numeros)))


numero = int(input("Digite um numero inteiro: "))
quantidade_num = contar_num(numero)

print(f"A quantidade de dígitos do número {numero} é: {quantidade_num}")