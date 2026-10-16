#Exmplo06 - Compra na cantina
#Aluno: Ana Carolina Antunes Maragno
#Objetivo:Ler o preço de um lanche a quantidade comprada e o valor que o cliente pagou e mostrar o troco 

#Entrada:Recebe o preco do lanche, a quantidade e o valor pago pelo cliente.
preco = float(input("Digite o preço do lanche:"))
quantidade = float(input("Digite a quantidade de compras:"))
valor_pago = float(input("Digite o valor que o cliente pagou:"))

#Processamento:
total = preco * quantidade
troco = valor_pago - total

#Saída:
print("Total:" ,total, "Troco:" ,troco)