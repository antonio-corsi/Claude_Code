# Scenario 3 — Refactoring

> In questo scenario usiamo Claude Code per fare **refactoring**
> (in italiano "rifattorizzazione"): riscrivere l'interno di un programma
> per renderlo più leggibile e manutenibile **senza cambiarne il
> comportamento**. È la cosiddetta manutenzione *perfettiva*: il programma
> funziona già, vogliamo solo che il codice sia scritto meglio.

## Che cosa c'è in questa cartella

- `report_mensile.py` — un programma **funzionante ma scritto male apposta**:
  legge `movimenti.csv` e produce il report mensile di un conto corrente.
- `movimenti.csv` — i dati di esempio: i movimenti di agosto e settembre 2026
  (colonne: data, descrizione, categoria, importo; separatore virgola,
  decimali con il punto).
- `test_report.py` — i **test di caratterizzazione**: fotografano i risultati
  che il programma produce oggi. Sono **tutti verdi** e devono restarlo.

## I difetti da riconoscere (i "code smell")

Un **code smell** ("odore di codice") è un sintomo di codice scritto male:
non è un bug, il programma funziona, ma il codice è difficile da leggere e
da modificare. In `report_mensile.py` ne abbiamo concentrati parecchi:

- una **variabile globale** (`RISULTATO`) modificata dentro la funzione;
- un'unica **funzione lunghissima** (`fai_tutto`) che fa tutto: legge il
  file, filtra, calcola e stampa;
- il file letto **due volte** per intero senza motivo;
- **sei blocchi quasi identici** per accumulare i totali per categoria
  (duplicazione) con nomi criptici (`t1..t6`, `n1..n6`);
- contatori calcolati e **mai usati** (codice morto);
- la data interpretata **a mano** con `split("-")` invece del modulo
  `datetime`, e il CSV letto a mano invece che con il modulo `csv`;
- il **numero magico** `500` (la soglia dei "movimenti grandi") ripetuto
  nel codice senza nome né spiegazione;
- **stampe mescolate ai calcoli** (`print` dentro la logica);
- niente **type hint** (le annotazioni dei tipi) né **docstring**
  (le stringhe di documentazione), e parametri dai nomi illeggibili
  (`f`, `m`, `a`).

## La regola del gioco

Si può riscrivere tutto, ma:

1. la funzione `fai_tutto(file, mese, anno)` deve continuare a esistere e a
   restituire gli stessi risultati (è la "facciata" che i test usano);
2. dopo **ogni** passo di refactoring si rieseguono i test con
   `python -m pytest`: devono restare **tutti verdi**;
3. i test **non si modificano** (regola scritta anche nel `CLAUDE.md` della
   cartella principale).

## Come si parte

Con l'ambiente conda attivo, in questa cartella:

```text
python -m pytest
```

Risultato atteso: **tutti i test verdi**. Questa è la fotografia di partenza:
la rete di sicurezza è tesa, si può cominciare a rifattorizzare. I prompt
da dare a Claude Code sono nella `GUIDA_DOCENTE.md` (cartella principale).

## Obiettivo didattico

Mostrare lo schema **as-is → idiomatico**: prima si osserva il codice così
com'è (*as-is*), poi lo si porta alla forma *idiomatica*, cioè scritta come
la comunità Python si aspetta (funzioni piccole, moduli standard `csv` e
`datetime`, nomi parlanti, costanti con nome, calcolo separato dalla
stampa). I test di caratterizzazione sono ciò che rende il viaggio sicuro.
