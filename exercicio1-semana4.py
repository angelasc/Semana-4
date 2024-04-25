numero_tabuada = int(input("Digite um número para montar a tabuada: "))
inicio_tabuada = int(input("Digite um número para dar início à tabuada: "))
final_tabuada = int(input("Digite um número para finalizar a tabuada: "))

multiplicacao_tabuada = range(inicio_tabuada, final_tabuada+1, 1)

for itens in multiplicacao_tabuada:
    print(numero_tabuada*itens)