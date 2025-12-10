def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    
    typ = figurka["typ"]
    (x_start, y_start) = figurka["pozice"]
    (x_cil, y_cil) = cilova_pozice

    if not (1 <= x_cil <= 8 and 1 <= y_cil <= 8):
        return False
    
    if cilova_pozice in obsazene_pozice:
        return False
    
    if figurka["pozice"] == cilova_pozice:
        return False

    dr = (x_start - x_cil) #row
    dc = (y_start - y_cil) #col

    if typ == "pěšec":
        if dr == -1 and dc == 0:
            return True
        
    if typ == "jezdec":
        abs_dr = abs(dr)
        abs_dc = abs(dc)
        if (abs_dr == 2 and abs_dc == 1) or (abs_dr == 1 and abs_dc == 2):
            return True
        
    if typ == "věž":
        rovne = (dc == 0) or (dr == 0)
        if rovne:
            x_krok = 0
            if dr < 0:
                x_krok = 1
            elif dr > 0:
                x_krok = -1
                
            y_krok = 0
            if dc < 0:
                y_krok = 1
            elif dc > 0:
                y_krok = -1
                
            x_cesta = x_start + x_krok
            y_cesta = y_start + y_krok

            while (x_cesta, y_cesta) != (x_cil, y_cil):
                if (x_cesta, y_cesta) in obsazene_pozice:
                    return False
                x_cesta += x_krok
                y_cesta += y_krok
            return True
        return False

    if typ == "střelec":
        diagonal = (abs(dr) == abs(dc))

        if diagonal:
            x_krok = 0
            if dr < 0:      
                x_krok = 1
            elif dr > 0:    
                x_krok = -1
                
            y_krok = 0
            if dc < 0:      
                y_krok = 1
            elif dc > 0:    
                y_krok = -1
 
            x_cesta = x_start + x_krok
            y_cesta = y_start + y_krok
            
            while (x_cesta, y_cesta) != (x_cil, y_cil):
                if (x_cesta, y_cesta) in obsazene_pozice:
                    return False 
                
                x_cesta += x_krok
                y_cesta += y_krok
            return True
        return False
        
    if typ == "dáma":
        rovne = (dr == 0 or dc == 0)
        diagonal = (abs(dr) == abs(dc))

        if rovne or diagonal:
            x_krok = 0
            if dr < 0:
                x_krok = 1
            elif dr > 0:
                x_krok = -1
                
            y_krok = 0
            if dc < 0:
                y_krok = 1
            elif dc > 0:
                y_krok = -1

            x_cesta = x_start + x_krok
            y_cesta = y_start + y_krok
            
            while (x_cesta, y_cesta) != (x_cil, y_cil):
                if (x_cesta, y_cesta) in obsazene_pozice:
                    return False
                
                x_cesta += x_krok
                y_cesta += y_krok
            
            return True
    if typ == "král":
        if abs(dr) <= 1 and abs(dc) <= 1:
            return True
        
    return False

if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))
