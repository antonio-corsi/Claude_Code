"""Test automatici per il modulo ``conto.py``.

Questi test descrivono il COMPORTAMENTO CORRETTO atteso dal conto corrente.
Con il codice fornito, alcuni test falliscono: è voluto, perché in
``conto.py`` sono nascosti alcuni bug. La regola dell'esercizio è:

    si corregge ``conto.py``, NON si toccano i test.

I test si eseguono dal terminale, in questa cartella, con:

    python -m pytest

Nota sui termini: una "fixture" è una funzione speciale di pytest che
prepara un oggetto di partenza pulito per ogni test; qui prepara un conto
nuovo, senza movimenti, con un fido di 200 euro.
"""

from datetime import date

import pytest

from conto import ContoCorrente


@pytest.fixture
def conto() -> ContoCorrente:
    """Un conto nuovo di zecca, con fido di 200 euro e nessun movimento."""
    return ContoCorrente("Mario Rossi", fido=200.0, movimenti=[])


# ---------------------------------------------------------------------------
# Operazioni di base
# ---------------------------------------------------------------------------

def test_saldo_iniziale_e_zero(conto):
    # Un conto appena aperto non ha movimenti, quindi il saldo è 0.
    assert conto.saldo() == 0.0


def test_deposito_aumenta_il_saldo(conto):
    conto.deposita(100.50, date(2026, 1, 10))
    assert conto.saldo() == 100.50


def test_prelievo_riduce_il_saldo(conto):
    conto.deposita(100.50, date(2026, 1, 10))
    conto.preleva(40.25, date(2026, 1, 12))
    assert conto.saldo() == 60.25


def test_importi_non_positivi_rifiutati(conto):
    # Depositi e prelievi di importo nullo o negativo non hanno senso:
    # il conto deve rifiutarli sollevando un ValueError.
    with pytest.raises(ValueError):
        conto.deposita(0)
    with pytest.raises(ValueError):
        conto.preleva(-5)


# ---------------------------------------------------------------------------
# Gestione del fido (lo scoperto massimo consentito)
# ---------------------------------------------------------------------------

def test_prelievo_oltre_il_fido_rifiutato(conto):
    # Con saldo 100 e fido 200, il saldo può scendere al massimo a -200:
    # un prelievo di 301 porterebbe a -201 e deve essere rifiutato.
    conto.deposita(100.0, date(2026, 2, 1))
    with pytest.raises(ValueError):
        conto.preleva(301.0, date(2026, 2, 2))


def test_prelievo_fino_al_limite_del_fido_consentito(conto):
    # Il limite del fido è COMPRESO: con saldo 100 e fido 200,
    # un prelievo di 300 porta il saldo esattamente a -200 ed è lecito.
    conto.deposita(100.0, date(2026, 2, 1))
    conto.preleva(300.0, date(2026, 2, 2))
    assert conto.saldo() == -200.0


# ---------------------------------------------------------------------------
# Indipendenza tra conti diversi
# ---------------------------------------------------------------------------

def test_due_conti_distinti_non_condividono_i_movimenti():
    # Due conti creati separatamente devono avere elenchi di movimenti
    # separati: un deposito sul primo non deve comparire sul secondo.
    conto_bruno = ContoCorrente("Bruno Bianchi")
    conto_carla = ContoCorrente("Carla Verdi")

    conto_bruno.deposita(100.0, date(2026, 5, 2))

    assert conto_bruno.saldo() == 100.0
    assert conto_carla.saldo() == 0.0, (
        "Il conto di Carla deve restare vuoto: i movimenti di Bruno "
        "non devono 'trasbordare' su un altro conto."
    )


# ---------------------------------------------------------------------------
# Arrotondamenti sugli importi in euro
# ---------------------------------------------------------------------------

def test_commissione_addebitata_arrotondata_ai_centesimi(conto):
    # Una commissione dell'1,5% su 846,47 euro vale 12,69705 euro:
    # l'addebito registrato deve essere arrotondato ai centesimi, -12,70.
    conto.deposita(846.47, date(2026, 3, 1))
    conto.commissione_percentuale(1.5, date(2026, 3, 31))

    ultimo_movimento = conto.movimenti[-1]
    assert ultimo_movimento.importo == -12.70


# ---------------------------------------------------------------------------
# Filtri sui movimenti
# ---------------------------------------------------------------------------

def test_movimenti_del_mese_filtra_anche_per_anno(conto):
    # Marzo 2025 e marzo 2026 sono mesi DIVERSI: chiedendo marzo 2026
    # deve tornare solo il movimento del 2026.
    conto.deposita(100.0, date(2025, 3, 10), "Vecchio deposito")
    conto.deposita(200.0, date(2026, 3, 5), "Deposito recente")

    del_mese = conto.movimenti_del_mese(2026, 3)

    assert len(del_mese) == 1
    assert del_mese[0].importo == 200.0


def test_movimenti_del_mese_seleziona_il_mese_giusto(conto):
    conto.deposita(50.0, date(2026, 1, 15), "Deposito di gennaio")
    conto.deposita(80.0, date(2026, 2, 10), "Deposito di febbraio")

    di_gennaio = conto.movimenti_del_mese(2026, 1)

    assert len(di_gennaio) == 1
    assert di_gennaio[0].descrizione == "Deposito di gennaio"
