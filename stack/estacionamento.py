from stack import Stack

estacionamento = Stack()
fora = Stack()

estacionamento.push('CARRO1')
estacionamento.push('CARRO2')
estacionamento.push('CARRO3')
estacionamento.push('CARRO4')
estacionamento.push('CARRO5')
estacionamento.push('CARRO6')

placa = input('Insira o carro que sera retirado ')

print(estacionamento)
retirado = False

while not retirado:
    carroRetirado = estacionamento.pop()
    print(f'carro retirado: {carroRetirado}')
    if carroRetirado == placa:
        retirado = True
        print('O carro foi encontrado.')
    else:
        fora.push(carroRetirado)
    
    print(f'dentro do patio: {estacionamento}')
    print(f'fora do patio: {fora}')


while not fora.is_empty():
    estacionamento.push(fora.pop())

print(f'estacionamento final {estacionamento}')