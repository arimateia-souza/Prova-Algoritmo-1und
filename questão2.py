
#questão 2

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
opcao = int(input("\n1 - Aritmética \n2 - Ponderada \n3 - Harmônica \nDigite o tipo de média que deseja: "))
if (opcao !=1 and opcao !=2 and opcao !=3 ):
    print("você digitou a opção errada, só poderá tentar novamente quando eu aprender laço de repetição :)")
elif (opcao == 1):
    media = (nota1 + nota2 + nota3)/3
    print("você digitou tipo de média aritmética, sua nota é: " + str(media))
elif (opcao == 2):
    media = (nota1 * 4 + nota2 * 5 + nota3 * 6)/ 15 #soma do peso junto
    print("você digitou tipo de média ponderada, sua nota é: " + str(media))
elif (opcao == 3):
    media = 3/(1/nota1 + 1/nota2 + 1/nota3)
    print("você digitou tipo de média harmônica, sua nota é: " + str(media))










