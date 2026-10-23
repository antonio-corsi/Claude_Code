# Demo Claude Code — Tre scenari di sviluppo software

Questo pacchetto contiene il materiale per una demo d'aula in tre scenari,
che mostrano Claude Code in tre momenti tipici della vita del software:

1. **Costruire un'applicazione da zero** (cartella `scenario-1-app-da-zero`)
2. **Caccia ai bug**, cioè trovare e correggere errori (cartella `scenario-2-caccia-ai-bug`)
3. **Refactoring**, cioè riscrivere codice brutto senza cambiarne il comportamento (cartella `scenario-3-refactoring`)

Gli esempi sono tutti in **dominio bancario** (piano di ammortamento, conto
corrente con fido, report mensile dei movimenti).

## Assunzioni

Esplicitiamo le condizioni in cui il materiale è pensato per funzionare:

1. **Sistema operativo**: Windows 10/11, comandi lanciati da **PowerShell**
   in Windows Terminal (su macOS/Linux i comandi sono identici).
2. **Claude Code** è già installato e l'accesso (login) è già stato fatto.
3. **Conda** (Miniconda o Anaconda) è installato: l'ambiente del corso si
   crea con conda, come descritto sotto. **Non si usa `uv`** (un gestore di
   pacchetti alternativo molto citato nei tutorial in rete): la regola è
   scritta anche nel file `CLAUDE.md`, così Claude Code non lo propone.
4. **Python 3.12** nell'ambiente dedicato; l'unico pacchetto esterno
   necessario è `pytest`.
5. Serve una **connessione a internet** (Claude Code dialoga con il modello
   in rete).

## Contenuto del pacchetto

```text
demo-claude-code-3-scenari/
├── README.md                     ← questo file
├── CLAUDE.md                     ← regole di progetto lette da Claude Code
├── GUIDA_DOCENTE.md              ← copione della demo, con i prompt pronti
├── scenario-1-app-da-zero/
│   └── SPECIFICA.md              ← la specifica dell'app da costruire
├── scenario-2-caccia-ai-bug/
│   ├── README.md
│   ├── conto.py                  ← modulo con 4 bug nascosti
│   └── test_conto.py             ← test pytest: 6 verdi, 4 rossi
└── scenario-3-refactoring/
    ├── README.md
    ├── report_mensile.py         ← programma funzionante ma scritto male
    ├── movimenti.csv             ← dati di esempio (agosto e settembre 2026)
    └── test_report.py            ← test di caratterizzazione: tutti verdi
```

## Glossario rapido

Definiamo i termini principali, una volta per tutte:

- **Claude Code**: lo strumento a riga di comando di Anthropic che permette
  di sviluppare software dialogando in linguaggio naturale; legge, scrive ed
  esegue codice nella cartella in cui lo avviamo.
- **Prompt**: il messaggio che scriviamo a Claude Code per dirgli che cosa fare.
- **Test automatico**: una piccola funzione che verifica da sola un pezzo di
  comportamento del programma; "verde" significa superato, "rosso" fallito.
- **pytest**: il programma che trova ed esegue i test; si lancia con
  `python -m pytest`.
- **conda**: il gestore di ambienti e pacchetti Python che usiamo nel corso;
  **conda-forge** è il canale (archivio) comunitario da cui installiamo.
- **Bug** (o "baco"): un errore di programmazione; la **caccia ai bug** è
  l'attività di trovarli e correggerli (manutenzione *correttiva*).
- **Refactoring** ("rifattorizzazione"): riscrivere l'interno del codice per
  migliorarne leggibilità e manutenibilità senza cambiarne il comportamento
  (manutenzione *perfettiva*).
- **CLAUDE.md**: un file di istruzioni che Claude Code legge automaticamente
  all'avvio, dalla cartella corrente e da tutte quelle superiori; qui
  contiene le regole degli esercizi (ambiente conda, niente `uv`,
  test con pytest, test intoccabili).

## Preparazione dell'ambiente (una sola volta)

Da PowerShell, in una cartella qualsiasi:

```text
conda create -n demo-claude python=3.12 -y
conda activate demo-claude
conda install -c conda-forge --override-channels pytest -y
```

Che cosa fanno i tre comandi:

1. `conda create -n demo-claude python=3.12 -y` crea un ambiente isolato
   chiamato `demo-claude` con Python 3.12 (`-y` risponde "sì" alle conferme).
2. `conda activate demo-claude` attiva l'ambiente: da questo momento
   `python` è quello dell'ambiente.
3. `conda install -c conda-forge --override-channels pytest -y` installa
   pytest prendendolo **solo** dal canale conda-forge
   (`--override-channels` ignora gli altri canali configurati, per avere
   installazioni riproducibili).

**Importante**: l'ambiente va attivato (`conda activate demo-claude`) in ogni
nuovo terminale, **prima** di eseguire i test o di avviare Claude Code.

## Verifica rapida (prima della lezione)

Con l'ambiente attivo, dalla cartella del pacchetto:

```text
cd scenario-2-caccia-ai-bug
python -m pytest
```

Atteso: **6 test verdi e 4 rossi** (i rossi sono voluti: sono i bug).

```text
cd ..\scenario-3-refactoring
python -m pytest
```

Atteso: **7 test, tutti verdi**.

Lo scenario 1 non contiene ancora codice (solo la specifica): è normale,
il codice lo scriverà Claude Code durante la demo.

## Avviare Claude Code in uno scenario

Sempre con l'ambiente conda attivo:

```text
cd scenario-1-app-da-zero
claude
```

Claude Code legge automaticamente il `CLAUDE.md` della cartella principale
(viene caricato dalla cartella corrente **e da tutte quelle superiori**).
Per verificarlo, dentro la sessione si può digitare `/context` e controllare
che il file compaia nell'elenco dei "Memory files".

## E adesso?

Il copione completo della demo — prompt pronti da incollare, tempi, cose da
far notare, imprevisti possibili e **le soluzioni dei 4 bug** — è nella
`GUIDA_DOCENTE.md`.
