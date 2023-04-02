estado =  { "SP":67836.43,  "RJ":36678.66,  "MG":29229.88, "ES":27165.48, "OUTROS":19849.53}

total_faturado = sum(estado.values())

print(f'O valor da soma de todos os faturamentos e de: {total_faturado}')
print()
for nome, valor in estado.items():
    porcento = (valor/total_faturado) * 100
    print(f'{nome} teve o porcentual de: {porcento:,.2f}')
    