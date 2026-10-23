"""Mini-libreria didattica per la gestione di un conto corrente bancario.

Il modulo contiene due elementi:

- ``Movimento``: un singolo movimento del conto (data, descrizione, importo);
- ``ContoCorrente``: il conto vero e proprio, con depositi, prelievi,
  fido e alcune operazioni di consultazione.

ATTENZIONE (parte dell'esercizio): in questo modulo sono nascosti alcuni
bug, cioè errori di programmazione. I test in ``test_conto.py`` descrivono
il comportamento CORRETTO atteso: alcuni di essi falliscono proprio a causa
dei bug. L'esercizio consiste nel correggere questo file, mai i test.
"""

from dataclasses import dataclass
from datetime import date


@dataclass
class Movimento:
    """Un singolo movimento di conto corrente.

    Convenzione sugli importi: ``importo > 0`` per le entrate (depositi),
    ``importo < 0`` per le uscite (prelievi, commissioni).
    """

    data: date
    descrizione: str
    importo: float


class ContoCorrente:
    """Conto corrente con fido.

    Il fido è lo scoperto massimo consentito: con ``fido = 200`` il saldo
    può scendere fino a -200,00 euro (limite compreso), ma non oltre.
    Ogni conto parte senza movimenti e tiene il proprio elenco separato.
    """

    def __init__(self, intestatario: str, fido: float = 0.0, movimenti=[]):
        self.intestatario = intestatario
        self.fido = fido
        self.movimenti = movimenti

    def saldo(self) -> float:
        """Restituisce il saldo corrente: la somma di tutti i movimenti."""
        return sum(m.importo for m in self.movimenti)

    def deposita(self, importo: float, data: date | None = None,
                 descrizione: str = "Deposito") -> None:
        """Registra un deposito (entrata) sul conto.

        L'importo deve essere positivo; se la data non viene indicata,
        si usa la data odierna.
        """
        if importo <= 0:
            raise ValueError("L'importo di un deposito deve essere positivo.")
        if data is None:
            data = date.today()
        self.movimenti.append(Movimento(data, descrizione, importo))

    def preleva(self, importo: float, data: date | None = None,
                descrizione: str = "Prelievo") -> None:
        """Registra un prelievo (uscita) dal conto.

        Il prelievo è consentito finché il saldo risultante non scende
        sotto ``-fido``: il limite ``-fido`` esatto è ancora consentito.
        Oltre quel limite viene sollevato un ``ValueError``.
        """
        if importo <= 0:
            raise ValueError("L'importo di un prelievo deve essere positivo.")
        if self.saldo() - importo <= -self.fido:
            raise ValueError("Fondi insufficienti: il prelievo supera il fido.")
        if data is None:
            data = date.today()
        self.movimenti.append(Movimento(data, descrizione, -importo))

    def commissione_percentuale(self, percentuale: float,
                                data: date | None = None) -> None:
        """Addebita una commissione pari a una percentuale del saldo attuale.

        L'addebito viene arrotondato ai centesimi (2 decimali) e registrato
        come movimento in uscita, con descrizione esplicativa.
        """
        addebito = self.saldo() * percentuale / 100
        if data is None:
            data = date.today()
        self.movimenti.append(
            Movimento(data, f"Commissione {percentuale}%", -addebito)
        )

    def movimenti_del_mese(self, anno: int, mese: int) -> list[Movimento]:
        """Restituisce i movimenti del mese indicato di quell'anno.

        Esempio: ``movimenti_del_mese(2026, 3)`` restituisce solo i movimenti
        di marzo 2026, non quelli di marzo di altri anni.
        """
        return [m for m in self.movimenti if m.data.month == mese]
