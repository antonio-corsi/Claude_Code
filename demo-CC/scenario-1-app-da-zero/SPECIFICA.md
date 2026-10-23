# SPECIFICA — Calcolatore di piano di ammortamento (applicazione a riga di comando)

> Questo file è la **specifica** dell'applicazione che costruiremo da zero con Claude Code:
> descrive *che cosa* il programma deve fare, non *come* farlo. Sarà Claude Code,
> guidato da noi, a proporre il come.

## Assunzioni

Prima di iniziare, esplicitiamo le condizioni in cui lavoreremo:

1. L'ambiente conda del corso è già attivo nel terminale (vedere il `README.md` nella cartella principale).
2. Claude Code viene avviato **da questa cartella** (`scenario-1-app-da-zero`), così legge anche le regole di progetto nel file `CLAUDE.md` della cartella principale.
3. Si usa **solo la libreria standard** di Python: nessun pacchetto esterno, tranne `pytest` per eseguire i test (già installato nell'ambiente).
4. Gli importi sono in euro e si arrotondano sempre a 2 decimali (i centesimi).

## Glossario minimo

Spieghiamo i termini che useremo, nell'ordine in cui compaiono:

- **Piano di ammortamento**: la tabella che mostra, rata per rata, come viene restituito un prestito.
- **Ammortamento "alla francese"**: il metodo più diffuso in Italia: la **rata** (l'importo pagato ogni mese) è **costante** per tutta la durata del prestito.
- **Quota capitale**: la parte della rata che restituisce il denaro prestato.
- **Quota interessi**: la parte della rata che paga gli interessi sul debito ancora da restituire.
- **Debito residuo**: quanto resta da restituire dopo aver pagato una certa rata.
- **TAN (Tasso Annuo Nominale)**: il tasso di interesse annuo del prestito, espresso in percentuale (es. 4,8).
- **CLI (Command Line Interface)**: interfaccia a riga di comando; il programma si usa dal terminale, senza finestre grafiche.
- **`argparse`**: il modulo della libreria standard di Python che legge le opzioni scritte sulla riga di comando (es. `--importo 10000`).

## Requisiti funzionali

- **RF1 — Input da riga di comando.** Il programma si chiama `ammortamento.py` e accetta, tramite `argparse`, le opzioni:
  - `--importo` : capitale prestato in euro (numero decimale, obbligatorio);
  - `--tan` : TAN annuo in percentuale (numero decimale, obbligatorio; es. `4.8` significa 4,8%);
  - `--mesi` : durata del prestito in mesi (numero intero, obbligatorio);
  - `--csv PERCORSO` : opzionale; se presente, salva il piano anche in un file CSV in quel percorso.
- **RF2 — Calcolo della rata costante.** Con tasso mensile `i = TAN / 100 / 12` e durata `n` mesi, la rata è
  `R = C * i / (1 - (1 + i) ** -n)`; se il TAN è 0, la rata è semplicemente `C / n`.
- **RF3 — Tabella del piano.** Per ogni mese il programma stampa: numero rata, quota interessi (`debito residuo precedente * i`), quota capitale (`rata - quota interessi`), rata, debito residuo. Tutti gli importi arrotondati a 2 decimali.
- **RF4 — Chiusura esatta.** L'**ultima rata viene aggiustata** (può differire di qualche centesimo dalle altre) in modo che il debito residuo finale sia **esattamente 0,00**: gli arrotondamenti non devono lasciare residui.
- **RF5 — Riepilogo.** In fondo alla tabella: totale rate pagate e totale interessi pagati.
- **RF6 — Validazione.** Importo e mesi devono essere positivi, il TAN non negativo; in caso contrario il programma termina con un messaggio d'errore chiaro in italiano (senza traceback).

## Requisiti non funzionali e vincoli

- **RNF1 — Solo libreria standard** (`argparse`, `csv`, ecc.): nessuna installazione aggiuntiva.
- **RNF2 — Test automatici** in `test_ammortamento.py`, eseguibili con `python -m pytest`, che verifichino almeno:
  1. il valore della rata su un caso noto;
  2. che l'ultima riga del piano abbia debito residuo 0,00;
  3. che la somma delle quote capitale sia pari all'importo prestato;
  4. il caso TAN = 0;
  5. il rifiuto degli input non validi.
- **RNF3 — Lingua.** Codice, commenti, docstring e messaggi in italiano, con nomi di variabili parlanti.
- **RNF4 — Ambiente.** Non creare ambienti virtuali, non usare `uv`, non installare pacchetti: l'ambiente conda è già pronto (regola ribadita in `CLAUDE.md`).

## Esempio di esecuzione attesa

```text
python ammortamento.py --importo 10000 --tan 4.8 --mesi 12
```

Deve produrre una tabella di 12 righe con rata costante dell'ordine di 855 € al mese
(l'ultima rata può differire di qualche centesimo per via dell'aggiustamento) e il riepilogo finale.

## Criteri di accettazione (lista di controllo)

- [ ] `python ammortamento.py --importo 10000 --tan 4.8 --mesi 12` stampa il piano completo senza errori.
- [ ] `python -m pytest` termina con tutti i test verdi.
- [ ] Il debito residuo dell'ultima rata è 0,00.
- [ ] Con `--csv piano.csv` viene creato un file CSV con le stesse colonne della tabella.
- [ ] Input non validi producono un messaggio d'errore chiaro, non un traceback.
