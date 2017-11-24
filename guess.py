import random

zahl = random.randint (0,100)

bla=True

while bla:

    gesucht = int(input('Geben sie eine Zahl wischen 0 und 100 ein: '))

     

 

    if gesucht == zahl:

        print('Glückwunsch, Sie haben die Zahl erraten')

        bla=False

 

 

 

    elif gesucht < zahl:

        print('Geben sie eine größere Zahl ein')

 

 

 

    else:

        print('Geben sie eine kleinere Zahl ein')

