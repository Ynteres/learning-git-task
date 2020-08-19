""" Stwórz funkcję, w której dodasz dwie liczby 
i wyświetl to na ekranie. Jak ją nazwiesz? 
Funkcję stworzysz z użyciem def. 
W ciele umieść operację i funkcję print."""

def sum_ab():
    a=0
    b=0
    c=0
    print("podaj liczbę A :")
    a = int(input())
    print("podaj liczbe B :")
    b = int(input())
    c = a+b
    print("suma liczb A=%d i B=%d to : %d" %(a,b,c))

sum_ab()

