def sudy_nebo_lichy(cislo):
    #cislo = int(input("Zadejte cislo: "))
    if cislo % 2 == 0:
        print(f"Číslo {cislo} je sudé")
    else: 
        print(f"Číslo {cislo} je liché")



if __name__ == "__main__":
    sudy_nebo_lichy(5)
    sudy_nebo_lichy(1000000)