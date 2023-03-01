import json

with open('dados.json') as f:
    faturamento_mensal = json.load(f)

menor_faturamento = min(faturamento_mensal.values())

# Calculando o maior valor de faturamento diário
maior_faturamento = max(faturamento_mensal.values())

# Calculando a média de faturamento diário, ignorando os dias sem faturamento
dias_com_faturamento = [faturamento for faturamento in faturamento_mensal.values() if faturamento > 0]
media_faturamento = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Calculando o número de dias com faturamento superior à média mensal
dias_acima_da_media = sum(1 for faturamento in dias_com_faturamento if faturamento > media_faturamento)

print("Menor faturamento diário: R$ {:.2f}".format(menor_faturamento))
print("Maior faturamento diário: R$ {:.2f}".format(maior_faturamento))
print("Média de faturamento diário: R$ {:.2f}".format(media_faturamento))
print("Número de dias com faturamento acima da média: {}".format(dias_acima_da_media))
