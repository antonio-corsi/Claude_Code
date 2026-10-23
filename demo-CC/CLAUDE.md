# Istruzioni di progetto (lette automaticamente da Claude Code)

Questo repository contiene il materiale di una demo didattica su Claude Code.
Le regole che seguono valgono in tutte le cartelle.

## Ambiente Python

- Usare l'interprete Python dell'ambiente conda **già attivo** nel terminale.
- NON creare ambienti virtuali, NON usare `uv`, NON usare `venv`.
- NON installare pacchetti (`pip install`, `conda install`): tutto il
  necessario è già installato nell'ambiente del corso.
- Eseguire i test sempre con: `python -m pytest`

## Regole per gli esercizi

- Codice, commenti, docstring e messaggi in italiano, con nomi parlanti.
- Non modificare i file `README.md`, `SPECIFICA.md` e questo `CLAUDE.md`:
  sono la traccia degli esercizi.
- Scenario 2 (`scenario-2-caccia-ai-bug`): i test descrivono il comportamento
  corretto. Correggere `conto.py`, mai i test.
- Scenario 3 (`scenario-3-refactoring`): i test non si modificano e devono
  restare verdi dopo ogni passo; la funzione `fai_tutto(file, mese, anno)`
  deve continuare a esistere con la stessa firma e gli stessi risultati.
- Gli importi in euro si arrotondano sempre a 2 decimali.
- Procedere a piccoli passi, eseguendo i test dopo ogni modifica.
