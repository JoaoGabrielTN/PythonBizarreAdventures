class HauntedBus:
    """Um ônibus assombrado por passageiros fantasmas"""
    def __init__(self, passengers=[]): # Como passengers recebe uma lista como valor default, caso nenhum argumento seja passado
        self.passengers = passengers   # o valor default será referênciado por todos os ônibus setados com default.
    
    def pick(self, name):
        self.passengers.append(name)
        
    def drop(self, name):
        self.passengers.remove(name)

class TwilightBus:
    """Um modelo de ônibus que faz os passageiros desaparecerem e aparecerem"""
    def __init__(self, passengers=None):
        if(passengers is None):
            self.passengers = []
        else:
            self.passengers = passengers # self.passengers está referenciado o argumento passado (nesse caso, ele altera o argumento). 
    
    def pick(self, name):
        self.passengers.append(name)
        
    def drop(self, name):
        self.passengers.remove(name)