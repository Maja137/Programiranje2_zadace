def prva(ime):
    print('Pozdrav,',ime,'!')

druga = lambda name: "Dobro dosla, " + name + "!"

def treca(druga):
    druga('Maja')

treca(prva)


