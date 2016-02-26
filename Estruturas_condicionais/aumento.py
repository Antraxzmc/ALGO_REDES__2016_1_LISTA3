nome = input("Coloque seu nome : ")
salario = float(input("Coloque seu salario :"))
if salario >= 300:
	soma = salario + salario * 0.30
	print ("Olá %s, seu novo salário será de %d reais." %(nome, soma))
if salario <= 300:
	soma = salario + salario * 0.15
	print ("Olá %s, seu novo salário será de %d reais." %(nome, soma))