faturamento =  { "01/01/23":500.00,  "02/01/23":700.00,  "03/01/23":200.00, "04/01/23":450.00, "05/01/23":900.00, "06/01/23":275.00,}

lista = faturamento.values()

lista_valores = list(lista)

tamanho_lista = len(lista_valores)

menor_valor = min(lista_valores)

maior_valor = max(lista_valores)

soma_dos_valores = sum(lista_valores)

media_mes = soma_dos_valores/tamanho_lista


print(f'O menor valor faturado nesse mes foi de: {menor_valor}')
print()
print(f'O maior valor faturado nesse mes foi de: {maior_valor}')
print()
print(f'A media desse mes foi de: {media_mes:,.2f}')
print()
dias_com_faturamento_maior_que_medias = 0

for valor in lista_valores:
    if valor > media_mes:
        dias_com_faturamento_maior_que_medias = dias_com_faturamento_maior_que_medias + 1

print(f'A quantidade de dias que o faturamento doi maior que a media e de: {dias_com_faturamento_maior_que_medias}')