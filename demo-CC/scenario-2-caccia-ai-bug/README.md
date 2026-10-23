# Scenario 2 — Caccia ai bug

> In questo scenario usiamo Claude Code per fare **manutenzione correttiva**:
> trovare e correggere i **bug** (in italiano "bachi", cioè errori di
> programmazione) nascosti in un piccolo modulo bancario.

## Che cosa c'è in questa cartella

- `conto.py` — una mini-libreria per la gestione di un conto corrente con fido
  (lo scoperto massimo consentito). **Contiene alcuni bug nascosti.**
- `test_conto.py` — i test automatici, scritti con `pytest`. Descrivono il
  comportamento **corretto** atteso: con il codice così com'è, alcuni test
  falliscono proprio a causa dei bug.

## La regola del gioco

**Si corregge `conto.py`, non si toccano i test.** I test sono il "contratto"
che il codice deve rispettare: se un test è rosso, è il codice a essere
sbagliato, non il test. (La regola è scritta anche nel file `CLAUDE.md` della
cartella principale, che Claude Code legge automaticamente.)

## Come si parte (prima ancora di aprire Claude Code)

Con l'ambiente conda attivo, in questa cartella eseguiamo i test a mano,
per vedere la situazione di partenza:

```text
python -m pytest
```

Il risultato atteso è: **6 test verdi e 4 rossi** (un rosso per ogni bug).
Leggere con calma i messaggi di errore: pytest dice quale assert è fallito e
con quali valori. Quali siano i bug, e come si correggano, è scritto solo
nella guida del docente: niente spoiler qui.

## Come si prosegue (con Claude Code)

Avviamo Claude Code **da questa cartella** con il comando `claude` e usiamo
i prompt suggeriti nella `GUIDA_DOCENTE.md` (cartella principale). L'idea di
fondo è sempre la stessa:

1. far **eseguire i test** a Claude Code, così "vede" gli stessi errori che
   vediamo noi;
2. chiedergli di **spiegare la causa** di ogni fallimento prima di correggere;
3. correggere **un bug alla volta**, rieseguendo i test dopo ogni correzione;
4. alla fine: tutti i test verdi, e una tabella riassuntiva dei bug trovati.

## Obiettivo didattico

Mostrare che i test automatici trasformano la caccia ai bug in un ciclo
oggettivo e ripetibile (rosso → correzione → verde), e che Claude Code lavora
molto meglio quando ha un modo concreto per **verificare** il proprio lavoro
(qui: eseguire `python -m pytest`).
