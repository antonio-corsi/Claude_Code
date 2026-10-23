"""Test di caratterizzazione per ``report_mensile.py``.

Un "test di caratterizzazione" fotografa il comportamento ATTUALE di un
programma funzionante: non dice come il codice dovrebbe essere scritto,
dice solo quali risultati deve produrre. Durante il refactoring
(la riscrittura interna del codice senza cambiarne il comportamento)
questi test sono la nostra rete di sicurezza: finché restano tutti verdi,
sappiamo di non aver rotto nulla.

La regola dell'esercizio: si può riscrivere ``report_mensile.py`` quanto
si vuole, ma la funzione ``fai_tutto(file, mese, anno)`` deve continuare a
esistere e a restituire gli stessi risultati. I test NON si modificano.

Esecuzione, da questa cartella: ``python -m pytest``
"""

from pathlib import Path

import report_mensile

# Percorso del file dati accanto a questo file di test: così i test
# funzionano da qualunque cartella vengano lanciati.
CSV = str(Path(__file__).parent / "movimenti.csv")


# ---------------------------------------------------------------------------
# Report di settembre 2026 (il mese "pieno" del file di esempio)
# ---------------------------------------------------------------------------

def test_numero_movimenti_di_settembre():
    report = report_mensile.fai_tutto(CSV, 9, 2026)
    assert report["n_movimenti"] == 14


def test_totale_entrate_di_settembre():
    # Stipendio 1850,00 + rimborso 45,25 + vendita bici 120,00
    report = report_mensile.fai_tutto(CSV, 9, 2026)
    assert report["entrate"] == 2015.25


def test_totale_uscite_di_settembre():
    report = report_mensile.fai_tutto(CSV, 9, 2026)
    assert report["uscite"] == 1425.25


def test_saldo_di_settembre():
    report = report_mensile.fai_tutto(CSV, 9, 2026)
    assert report["saldo"] == 590.00


def test_totali_per_categoria_di_settembre():
    report = report_mensile.fai_tutto(CSV, 9, 2026)
    per_categoria = report["per_categoria"]
    assert per_categoria["stipendio"] == 1850.00
    assert per_categoria["bonifico_in"] == 165.25
    assert per_categoria["bonifico_out"] == -848.50
    assert per_categoria["prelievo"] == -250.00
    assert per_categoria["pos"] == -317.75
    assert per_categoria["commissioni"] == -9.00


def test_movimenti_grandi_di_settembre():
    # "Grandi" = importo oltre i 500 euro in valore assoluto.
    report = report_mensile.fai_tutto(CSV, 9, 2026)
    descrizioni = {descrizione for descrizione, _ in report["grandi"]}
    assert descrizioni == {"Stipendio settembre", "Affitto"}


# ---------------------------------------------------------------------------
# Il filtro per mese e anno deve escludere gli altri mesi
# ---------------------------------------------------------------------------

def test_agosto_e_separato_da_settembre():
    report = report_mensile.fai_tutto(CSV, 8, 2026)
    assert report["n_movimenti"] == 4
    assert report["entrate"] == 1850.00
    assert report["uscite"] == 226.75
    assert report["saldo"] == 1623.25
