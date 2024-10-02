def calculadora():
    print("Escolha a operação:")
    print("1-Adição")
    print("2-Subtração")
    print("3-Multiplicação")
    print("4-Divisão")
    
    operacao = input("Digite o número da operação (1/2/3/4): ")
    
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    
    if operacao == '1':
        resultado = numero1 + numero2
        print(f"Resultado: {numero1} + {numero2} = {resultado}")
    elif operacao == '2':
        resultado = numero1 - numero2
        print(f"Resultado: {numero1} - {numero2} = {resultado}")
    elif operacao == '3':
        resultado = numero1 * numero2
        print(f"Resultado: {numero1} * {numero2} = {resultado}")
    elif operacao == '4':
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"Resultado: {numero1} / {numero2} = {resultado}")
        else:
            print("Erro: Impossivel reconhecer divisão por zero.")
    else:
        print("Erro: operação inválida.")

calculadora()
