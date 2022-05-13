

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3)/3

if (nota1 > 10.0 or nota1 < 0.0 or nota2 > 10.0 or nota2 < 0.0 or nota3 > 10.0 or nota3 < 0.0 ):
    print("Você digitou alguma(as) nota(as) invalida(as)")
elif (media <3.0):
    print("Candidato reprovado")
elif (media >=7.0):
    print("Candidato Aprovado")
elif (media >=5.0 and media < 7.0 and nota1 >3.0 or nota2 >3.0 or nota3 > 3.0):
    print("Candidato em recuperação")
elif (nota1 < 3.0 or nota2 < 3.0 or nota3 < 3.0 and media >=5.0):
    print("Candidato aprovado por nota")












