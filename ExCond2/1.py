p = (input("Digite o placar: "))

t1 = p[0]
t2 = p[1]

if t1 == t2:
    print("Empate")
elif t1 > t2:
    print("Time 1 ganhou")
elif t2 > t1:
    print("Time 2 ganhou")