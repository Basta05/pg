def cislo_text(cislo):
    jednotky = ["nula", "jedna", "dva", "tři", "čtyři", "pět", "šest", "sedm", "osm", "devět", "deset"]
    nact = ["jedenáct", "dvanáct", "třináct", "čtrnáct", "patnáct", "šestnáct", "sedmnáct", "osmnáct", "devatenáct"]
    desitky = ["dvacet", "třicet", "čtyřicet", "padesát", "šedesát", "sedmdesát", "osmdesát", "devadesát"]
  
    if cislo < 11:
         return jednotky[cislo]
    elif cislo <20:
        return nact[cislo - 11]
    elif cislo < 100:
        des = desitky[cislo // 10 - 2]
        jed = cislo % 10
        if jed == 0:
            return des
        else:
            return des + " " + jednotky[jed]
    elif cislo == 100:
        return "sto"    
    else: 
        return "Neplatná hodnota"
    




if __name__ == "__main__":
    cislo = input("Zadej číslo: ")
    text = cislo_text(int(cislo))
    print(text)