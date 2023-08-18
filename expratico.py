cardict = {
    "ki" : 7400,
    "tecnicas" : 6000,
    "velocidade" : 66,
    "trasnsformacoes" : 3
}

nova_caracteristica = input("Digite uma nova caracteristica: ").strip().lower()
novo_valor = input(f"Digite o novo valor para {nova_caracteristica}: ").strip()
cardict[nova_caracteristica] = novo_valor

print("Caracteristicas disponiveis: ")
for keys in cardict.keys():
    print(keys)

escolhas = input("Escolha entre uma das caracteristicas a cima: ").strip().lower()

if escolhas in cardict:
    print(f"A caecteristica escolhida foi {escolhas} e o valor {cardict[escolhas]}")
else:
    print("A escolha não existe")