class Obj:
    vida = 10
    dano = 1

hero = Obj() #estanciando o objeto HERO é a variavel do objeto
hero.vida = 100 #adicionando novos valores ao objeto
hero.dano = 5

slime = Obj()
slime.vida = 11
slime.dano = 1

print(slime.vida, hero.vida) #printando as variaveis
print(slime.dano, hero.dano)