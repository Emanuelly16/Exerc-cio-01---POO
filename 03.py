class Pessoa:
    def __init__(self,nome,altura,peso,idade):
        self.nome = nome
        self.altura = altura
        self.peso = peso
        self.idade = idade

    def comer(self,comida):
        if comida == True:
            print(self.nome,' está comendo, por isso não pode falar e nem dormir')

    def falar(self,falando):
        if falando == True:
            print(self.nome, 'está falando, por isso não pode dormir e nem comer')
            
    def dormir(self,dormindo):
        if dormindo == True:
            print(self.nome,'está dormindo, por isso não pode falar nem comer')
        
