# report_mensile.py
#
# Genera il report mensile dei movimenti di un conto corrente leggendo
# il file movimenti.csv (colonne: data, descrizione, categoria, importo).
#
# IMPORTANTE (parte dell'esercizio): questo programma FUNZIONA, e infatti
# tutti i test in test_report.py sono verdi. Pero' il codice e' scritto
# male apposta: e' il punto di partenza dell'esercizio di refactoring.
# La regola: si puo' riscrivere tutto, purche' i test restino verdi.

RISULTATO = {}


def fai_tutto(f, m, a):
    global RISULTATO
    RISULTATO = {}

    # prima passata sul file: contiamo quante righe appartengono al mese
    cnt = 0
    file1 = open(f, "r", encoding="utf-8")
    tmp = file1.readlines()
    file1.close()
    for x in tmp[1:]:
        x = x.strip()
        if x == "":
            continue
        pezzi = x.split(",")
        d1 = pezzi[0].split("-")
        if int(d1[1]) == m and int(d1[0]) == a:
            cnt = cnt + 1

    # seconda passata sul file: facciamo tutti i calcoli
    t1 = 0.0
    n1 = 0
    t2 = 0.0
    n2 = 0
    t3 = 0.0
    n3 = 0
    t4 = 0.0
    n4 = 0
    t5 = 0.0
    n5 = 0
    t6 = 0.0
    n6 = 0
    entrate = 0.0
    uscite = 0.0
    grandi = []
    file2 = open(f, "r", encoding="utf-8")
    tmp2 = file2.readlines()
    file2.close()
    for x in tmp2[1:]:
        x = x.strip()
        if x == "":
            continue
        pezzi = x.split(",")
        d1 = pezzi[0].split("-")
        if int(d1[1]) == m and int(d1[0]) == a:
            imp = float(pezzi[3])
            print("elaboro:", pezzi[1], imp)
            if pezzi[2] == "stipendio":
                t1 = t1 + imp
                n1 = n1 + 1
            elif pezzi[2] == "bonifico_in":
                t2 = t2 + imp
                n2 = n2 + 1
            elif pezzi[2] == "bonifico_out":
                t3 = t3 + imp
                n3 = n3 + 1
            elif pezzi[2] == "prelievo":
                t4 = t4 + imp
                n4 = n4 + 1
            elif pezzi[2] == "pos":
                t5 = t5 + imp
                n5 = n5 + 1
            elif pezzi[2] == "commissioni":
                t6 = t6 + imp
                n6 = n6 + 1
            if imp > 0:
                entrate = entrate + imp
            else:
                uscite = uscite - imp
            if imp > 500 or imp < -500:
                grandi.append((pezzi[1], imp))

    RISULTATO["n_movimenti"] = cnt
    RISULTATO["entrate"] = entrate
    RISULTATO["uscite"] = uscite
    RISULTATO["saldo"] = entrate - uscite
    RISULTATO["per_categoria"] = {
        "stipendio": t1,
        "bonifico_in": t2,
        "bonifico_out": t3,
        "prelievo": t4,
        "pos": t5,
        "commissioni": t6,
    }
    RISULTATO["grandi"] = grandi

    print("=== REPORT", m, "/", a, "===")
    print("movimenti:", cnt)
    print("entrate:", entrate)
    print("uscite:", uscite)
    print("saldo:", entrate - uscite)
    print("movimenti grandi (oltre 500):")
    for g in grandi:
        print(" -", g[0], g[1])

    return RISULTATO


if __name__ == "__main__":
    fai_tutto("movimenti.csv", 9, 2026)
