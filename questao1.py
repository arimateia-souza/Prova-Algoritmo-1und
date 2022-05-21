nota1 = float(input("Digite sua nota do trabalho de laboratório: "))
nota2 = float(input("Digite sua nota do relatório: "))
nota3 = float(input("Digite sua nota da avaliação semestral: "))
nota4 = float(input("Digite sua nota do exame final: "))
media = (nota1 * 0.5 + nota2 * 2 + nota3 * 2.5 + nota4 * 5) / (0.5 + 2 + 2.5 + 5)
if (media >= 8.0 and media <= 10.0):
    conceito = 'A'
    print("sua média ponderada é: " + str(media) + " conceito: " + conceito)
elif (media >= 7.0 and media < 8.0 ):
    conceito = 'B'
    print("sua média ponderada é: " + str(media) + " conceito: " + conceito)
elif (media >= 6.0 and media < 7.0 ):
    conceito = 'C'
    print("sua média ponderada é: " + str(media) + " conceito: " + conceito)
elif (media >= 5.0 and media < 6.0 ):
    conceito = 'D'
    print("sua média ponderada é: " + str(media) + " conceito: " + conceito)
elif (media >= 0.0 and media < 5.0 ):
    conceito = 'F'
    print("sua média ponderada é: " + str(media) + " conceito: " + conceito)
elif (media > 10.0 or media < 0.0):
    print("Você digitou alguma(as) nota(as) invalida(as)")
