#TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:
def recomendar_plano(consumo):
  if consumo <= 10.0:
    return 'Plano Essencial Fibra - 50Mbps'
  elif 10.0 < consumo <= 20.0:
    return 'Plano Prata Fibra - 100Mbps'
  else:
    return 'Plano Premium Fibra - 300Mbps'
  
    
# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# TODO: Retorne o plano de internet adequado:
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input())
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
print(recomendar_plano(consumo))