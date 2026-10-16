#Exemplo05 - Minutos em horas 
# Aluno:Ana Carolina Antunes Maragno
#Objetivo:Ler o tempo em minutos e mostrar o valor em horas.

#Entrada:Ler o tempo em minutos que foi digitado.
minutos = int(input("Digite o tempo em minutos:"))

#Processamento:
horas = minutos // 60
resto = minutos % 60
print("O tempo em horas é:", horas , "hora(s)e", resto , "minuto(s)")