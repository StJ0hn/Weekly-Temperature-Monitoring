import pandas as pd
#Criando dados das temperaturas semanais:
dados = [20, 21, 23, 19, 18, 21]
#Criando uma lista com os dias da semana:
dias_da_semana = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado"]
#Impondo uma serie que faz a relação entre índices e valores:
temp_semanais = pd.Series(dados, index= dias_da_semana)
print(temp_semanais)