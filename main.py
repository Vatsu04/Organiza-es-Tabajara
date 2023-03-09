'''

-As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
	
-Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

-salários até R$ 280,00 (incluindo) : aumento de 20%
	
-salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
	
-salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
	
-salários de R$ 1500,00 em diante : aumento de 5% Após 
o aumento ser realizado, informe na tela:

-o salário antes do reajuste;

-o percentual de aumento aplicado;

-o valor do aumento;

-o novo salário, após o aumento.

'''



def reajuste(salario):
	
	if (salario < 280.00):
		aumento = salario/5
		salario_reajuste = salario + aumento
		percentual = "20%"
		
	elif (salario >= 280.00) and  (salario <= 700.00):
		aumento = (salario*15)/100
		salario_reajuste = salario+ aumento 
		percentual = "15%"
	elif (salario>= 700.00) and (salario<=1500.00):
		aumento = salario/10 
		percentual = "10%"
		salario_reajuste = salario+ aumento
		
	elif (salario > 1500):
		aumento = salario/20 
		salario_reajuste = salario+aumento
		percentual = "5%"

	
	
	print("Salario antes do reajuste: ", salario )
	print(f"O percentual de aumento aplicado : {percentual}")
	print("O valor do aumento: ", aumento)
	print("O novo salario, após o aumento: " ,salario_reajuste)
	
salario = 0


salario = float(input("Bem vindo ao programa de aumento de salário, por favor digite seu salário atual: "))
print("\n\n")
reajuste(salario)
