# -*- coding: utf-8 -*-

# verificando se o número é par ou impar

class Number:
    def verificarNumero(self, number):
        number = number
        if (number % 2 == 0):
            print("Este número é par")
        else:
            print("Este número é impar")

number = input("Quero verificar este numero: ")
Number().verificarNumero(number)


# verificar se está frio não

class Temperatura:
    def getTemp(self, f):
        self.F = f
        self.C = 0
    def transformInC(self):
        self.C = (self.F - 32) * 5/9
        if(self.F >= 65):
            print(self.C,"graus. O clima é ideal para sair sem casaco")
        else:
            print(self.C,"graus. Fique em casa, está frio lá fora")
        return self.C

temperatura = Temperatura()
temperatura.getTemp(2)
tempC = temperatura.transformInC()
print(tempC)



# criar jogo do pedra papel tesoura lagarto spock

# tenho 5 “personagens” nesse jogo e oq podem fazer

# tesoura:
# - pode cortar o papel
# - matar o lagarto
# 
# 

# papel:
# - impedir o spock
# - embrulhar a pedra
# 
# 

# pedra: 
# - quebra a tesoura
# - esmagar o lagarto
# 
# 
# 

# lagarto:
# - come o papel
# - envenena o spock
# 
# 
# 

# spock:
# - vaporiza a pedra
# - quebra a tesoura
# 
# 

player_1 = input("Write the value chosen by player 1: ")
player_2 = input("Write the value chosen by player 2: ")

if player_1 == player_2:
    print("Empatou")

elif player_1 == "papel":

    if player_2 == "tesoura" or "lagarto":
        print("Player 2 é o vencedor")
    else:
        print("Player 1 é o vencedor")


elif player_1 == "pedra":

    if player_2 == "spock" or "papel":
        print("Player 2 é o vencedor")
    else:
        print("Player 1 é o vencedor")


elif player_1 == "tesoura":

    if player_2 == "pedra" or "spock":
        print("Player 2 é o vencedor")
    else:
        print("Player 1 é o vencedor")


elif player_1 == "lagarto":

    if player_2 == "tesoura" or "pedra":
        print("Player 2 é o vencedor")
    else:
        print("Player 1 é o vencedor")


elif player_1 == "spock":

    if player_2 == "pedra" or "lagarto":
        print("Player 2 é o vencedor")
    else:
        print("Player 1 é o vencedor")


    