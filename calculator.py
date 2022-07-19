# -*- coding: utf-8 -*-
"""### **Calculadora básica**"""

num1 = int(input("Digite o primeiro valor:"))
num2 = int(input("Digite o segundo valor:"))
operacao = input("Qual operação você deseja fazer?")

if operacao == "soma":
  result = (num1+num2)
  print("Você escolheu somar: ",result)
elif operacao == "subtracao":
  result = (num1-num2)
  print("Você escolheu subtração: ",result)
elif operacao == "multiplicacao":
  result = (num1*num2)
  print("Você escolheu multiplicacao: ",result)
elif operacao == "divisao":
  result = (num1/num2)
  print("Você escolheu divisao: ",result)
else:
  print("Escolha uma opção válida")