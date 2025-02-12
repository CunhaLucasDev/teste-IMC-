#Programa cadastro e  calculo de IMC :
nome=input("Qual é o seu nome ?")
cidade=input("Qual é a sua cidade Natal?")
idade=int(input("Qual é a sua idade ?"))
print(f"Bem vindo, {nome} , iremos completar teu cadastro para calculo do IMC, ok ?")
peso=int(input("Qual é o seu peso ?"))
altura=float(input("Qual é a sua altura ?"))
indice=peso/(altura*altura)
print(f"{nome}, natural de  {cidade} com {idade} anos, esta com um indice de Massa Corporal de {indice}  !")
if indice >= 40 :
    print("Voce esta no Grau IV de Obesidade")

