class Pessoa:
    def __init__(self, nome, peso, idade,comer=False,falar=False,dormir=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comer = comer
        self.falar = falar
        self.dormir = dormir

    def comendo(self,alimento):
        if alimento == True:
            self.comer = True
            self.falar = False
            self.dormir = False
        print(f'{self.nome}, está comendo, por isso não pode falar ou dormir. ')

    def falando(self,conversar):
        if conversar == True:
            self.falar = True
            self.comer = False
            self.dormir = False
            print(f'{self.nome} está falando, por isso não pode dormir ou comer.')

    def dormindo(self,sono):
         if sono == True:
             self.falar = False
             self.comer = False
             self.dormir = True
             print(f'{self.nome}, está dormindo, por isso não pode falar ou comer.')

p1 = Pessoa('Yoongi',80,24)
p1.falando(True)