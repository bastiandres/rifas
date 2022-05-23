import random

def returnOneWinner(lista):
    
    magic_number = random.randint(1,len(lista))
    return lista[magic_number-1]

def returnNWinner(n, lista):
    winners_list = []
    while (len(winners_list)<=n):
        winner = returnOneWinner(lista)
        if winner not in winners_list:
            winners_list.append(winner)
        if len(winners_list) == n:
            break
    
    return winners_list
