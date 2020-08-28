# Calculadora em Python
'''
	Laboratorio 02 do Treinamento em Python da DSA
	Author: Alessandro Chaves
	Data: 2020/08/27
'''
# Operacoes Matematicas
soma = lambda n1, n2: float(n1) + float(n2)
dife = lambda n1, n2: float(n1) - float(n2)
mult = lambda n1, n2: float(n1) * float(n2)
divi = lambda n1, n2: float(n1) / float(n2)

def onlyNumber_f(valor):
	print ( 'Apenas Números devem ser informado! "{}" não é um número válido!' .format( valor ) )

# Validar ser os valores são numericos
def isNumber(value):
	try:
		int(value)
	except ValueError:
		try:
			float(value)
		except ValueError:
			onlyNumber_f(value)
			return False
	return True		

# Opcoes para o usuario
tp_options = ('1 - Soma', '2 - Subtração', '3 - Multiplicação', '4 - Divisão')

print('Selecione o Número da Opção Desejada')

for i in tp_options:
	print(i)

ln_option = input( "Digite sua Opção (1/2/3/4): " )


if isNumber(ln_option):
	
	ln_option = int(ln_option)
	if ln_option <= 0 or ln_option >= 5:

		print('A Opção Informada é Inválida!')
	else:
	
		ln_num1 = input('Digite o primeiro número: ')
		if isNumber(ln_num1):
	
			ln_num2 = input('Digite o segundo número: ')
			if isNumber(ln_num2):
				
				if ln_option == 1:
					print( '{} + {} = {}' .format( ln_num1, ln_num2, soma( ln_num1, ln_num2 ) ) )
	
				elif ln_option == 2:
					print( '{} - {} = {}' .format( ln_num1, ln_num2, dife( ln_num1, ln_num2 ) ) )
	
				elif ln_option == 3:
					print( '{} * {} = {}' .format( ln_num1, ln_num2, mult( ln_num1, ln_num2 ) ) )
	
				elif ln_option == 4:
					print( '{} / {} = {}' .format( ln_num1, ln_num2, divi( ln_num1, ln_num2 ) ) )
