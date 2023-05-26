v = float(input("Digite o valor da compra: "))
p = float(input("Digite o valor de prestação: "))

r = v / p

if r > 500:
    print("Não pague")
else:
    print("Pague")