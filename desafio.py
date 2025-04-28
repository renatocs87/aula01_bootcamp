
# 1) Solicita ao usuário que digite seu nome


# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante


# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante


# 4) Calcule o valor do bônus final



# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bonus


# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?
'''
- Possibilidade de o usuário digitar número no campo de Nome;
- Possibilidade de o usuário dgitar texto nos campos de numéricos(inteiro, float...)
'''

# Variáveis
bonus = 1000
nome = str(input("Digite o nome do usuário: "))
salario = float(input("Digite o valor salário do usuário: "))
percentualBonus = float(input("Digite o porcentual do bônus a receber: "))

#Cálculo do bônus
bonusFinal = round(bonus + ( salario * percentualBonus),2)

print(f"O salário do {nome} é de R${salario}, e seu bônus final é de R${bonusFinal} ")



