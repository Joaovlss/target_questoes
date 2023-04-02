anterior = 0
proximo = 0
lista = []

numero_usuario = int(input('Qual numero deseja encontrar na sequencia fibonacci?: '))

while(proximo < numero_usuario):
  proximo = proximo + anterior
  anterior = proximo - anterior

  lista.append(proximo)

  if(proximo == 0):
    proximo = proximo + 1

print(lista)

if (numero_usuario in lista):
  print('O seu numero pertence a sequencia fibonacci')
else:
  print('O seu numero NAO pertence a essa sequencia')