def calculadora():
    try:
        numero1 = float(input("Digite um numero: "))
        numero2 = float(input("Digite um numero: "))

    except ValueError:
        print("ERRO. Porfavor insira números validos!")
        return 
    
    
    adicao = numero1 + numero2
    subtracao = numero1 - numero2
    multiplicacao = numero1 * numero2
    if numero2 != 0:
        divisao = numero1/ numero2
    else:
        divisao = "ERRO. Impossivel reconhecer divisão por zero!"
        
        
    print(f"A soma: {numero1} + {numero2} = {adicao}")
    print(f"A subtração: {numero1} - {numero2} = {subtracao}")
    print(f"A multiplicação: {numero1} * {numero2} = {multiplicacao}")
    print(f"A divisão: {numero1} / {numero2} = {divisao}")
    
calculadora()
