from Buses import HauntedBus, TwilightBus

alunos = ["Joao", "Luan"]
bus1 = HauntedBus(alunos)
print(bus1.passengers)

bus2 = HauntedBus()
bus2.pick("Alex")
bus3 = HauntedBus()

print(bus2.passengers)
print(bus3.passengers)

print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)

tBus = TwilightBus(alunos)
tBus.drop("Joao") 

# Tanto TwilightBus e Haunted bus ferem  o princípio de mínima surpresa
print(tBus.passengers)
print(bus1.passengers)
print(alunos)

# princípio da mínima surpresa
# call by sharing