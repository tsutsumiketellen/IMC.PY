sentinela = 1
 
while (sentinela == 1) :
    seu_peso= float (input("informe o seu peso: "))
    altura = float (input ("informe a sua altura:"))
 
    IMC = seu_peso/(altura*altura)
 
    print (" Seu IMC é :", IMC)
 
    if( IMC<= 18.5):
        print ( "Você está em estado de Magreza! OBESIDADE GRAU 0")
 
    elif( IMC<=25.0):
        print ( "Você está em estado normal! OBESIDADE GRAU 0")
 
    elif( IMC<=30):
        print ( "Você está em estado de sobrepeso! OBESIDADE GRAU 1")
 
    elif(IMC<=40):
        print ( "Você está em estado de OBESIDADE! OBESIDADE GRAU 2")
 
    elif( IMC>=40):
        print ( "Você está em estado de OBESIDADE GRAVE! OBESIDADE GRAU 3")
 
 
    print (" deseja continuar?")
    print ( " 1- SIM ")
    print (" 2- NÃO")
    sentinela = (int(input(" informe a opção: ")))