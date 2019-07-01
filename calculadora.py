valorA = int(input("Digite um  valor"))
valorB = int(input("Digite outro valor"))
operacao = input("Digite a operação: ( +, -, *, /)")
resultado = 0

if operacao == "+":
    resultado =  valorA + valorB
elif operacao == "-":
    resultado = valorA - valorB
elif operacao == "*":
    resultado = valorA * valorB    
elif operacao == "/":
    resultado = valorA / valorB

print(resultado)    