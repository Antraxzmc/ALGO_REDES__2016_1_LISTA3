codigo = int(input("Coloque 1 para adição ou 2 para subtração : "))
if codigo == 1:
 print ("Muito bem você escolheu ADIÇÃO")
 um = float(input("Coloque o primeiro numéro : "))
 dois = float(input("Coloque o segundo numéro : "))
 soma = float(um) + float(dois)
 print ("O resultado da soma é %d" %(soma))
if codigo == 2:
 print ("Muito bem você escolheu SUBTRAÇÃO")
 um = float(input("Coloque o primeiro numéro : "))
 dois = float(input("Coloque o segundo numéro : "))
 soma = um - dois
 print ("O resultado da subtração é %d" %(soma))
if codigo >= 3:
	print("Apenas coloque 1 ou 2")
if codigo <= 0:
	print("Apenas coloque 1 ou 2")