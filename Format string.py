nome = 'Luiz otavio'
idade = 32
altura = 1.80
conta = idade * altura
# opção 1
print(f'{nome} tem {idade} anos e altura {altura} e imc {conta:.2f}')
#opção 2
print('{} tem {} anos e altura {} e imc {:.2f}'.format(nome, idade, altura, conta))
#opção 3
print('{0} tem {0} anos e altura {1} e imc {2:.2f}'.format(nome, idade, altura, conta))