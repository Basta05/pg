def je_prvocislo(cislo):
    if cislo < 2:
        return False
    for i in range(2, cislo):
        if cislo % i == 0:
            return False
    return True
    
    
    

def vrat_prvocisla(maximum):

    maximum = int(maximum)
    seznam_prvocisla = []

    for n in range(2, maximum + 1):
        if je_prvocislo(n):
            seznam_prvocisla.append(n)
    return seznam_prvocisla

if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)
