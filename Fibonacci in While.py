end = 0
quant = 1

print("Calculo Fibonacci")

while (quant !=0):
    quant = int(input("\n\nDigite a quantidade que deseja calcular, ou 0 para parar: "))
    num1 = 0
    num2 = 1
    num3 = 0
    cont = 0

    print("fibonacci: ", end = " ")
    

    while(cont < quant): 
        print(num3, end = " ")

        num1 = num2
        num2 = num3
        num3 = num1 + num2
        cont += 1


