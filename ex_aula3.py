# # 1
#
# vel = int(input("Coloque a velocidade do veículo: "))
#
# if vel > 80:
#     high_velocity = (vel - 80) * 5
#     print(f"O valor da multa é R${high_velocity},00 ")
#
# # 2
#
# a = int(input("Valor de a: "))
# b = int(input("Valor de b: "))
# c = int(input("Valor de c: "))
#
# maior = a
# menor = a
# if b >= a and b >= c:
#     maior = b
# if c >= a and c >= b:
#     maior = c
#
# if b <= a and b <= c:
#     menor = b
# if c <= a and c <= b:
#     menor = c
#
# print(f"O menor valor é: {menor} e o maior é {maior}")
#
# # 3
#
# salary = int(input("Qual teu salário? "))
#
# if salary > 1250:
#     aumento = (salary * 10/100)
#     salary = salary + aumento
#     print(f"O salário agora é R${salary} e o aumento foi de R${aumento},00")
# else:
#     aumento = (salary * 15/100)
#     salary = salary + aumento
#     print(f"O salário agora é {salary} e o aumento foi de R${aumento},00")

# 4

distance = int(input("Digite a distância a ser percorrida: "))

if distance <= 200:
    valor = distance * 0.5
    print(f"Valor da viagem: R${valor:.2f}")
else:
    valor = distance * 0.45
    print(f"Valor da viagem: R${valor:.2f}")