# Guida per il docente — Demo "Tre scenari di sviluppo con Claude Code"

Questo è il copione della demo: per ogni scenario trovate i prompt pronti da
incollare in Claude Code, le cose da far notare all'aula, gli imprevisti
possibili e — solo in questa guida — le soluzioni dei bug. (Con "copione"
intendiamo la scaletta operativa della demo: i passi nell'ordine in cui
conviene eseguirli e le frasi da usare.)

## Assunzioni

1. L'ambiente conda `demo-claude` è stato creato e provato come descritto nel
   `README.md` (Python 3.12 + pytest da conda-forge; **niente `uv`**).
2. Claude Code è installato, con login già effettuato, e si avvia con il
   comando `claude` da PowerShell in Windows Terminal.
3. La demo viene proiettata: conviene ingrandire il carattere del terminale e
   silenziare le notifiche.
4. Durata complessiva stimata: **75–90 minuti** (25–30 + 20 + 20–25, più
   apertura e chiusura). Ogni scenario regge anche da solo.
5. Le risposte di Claude Code **non sono deterministiche**: i testi e a volte
   le scelte di dettaglio cambiano a ogni esecuzione. È normale, e va detto
   all'aula; i punti di arrivo (i test verdi) restano invece stabili.

## Il filo conduttore

I tre scenari corrispondono a tre momenti della vita del software, e a tre
modi diversi di usare i test automatici:

| # | Scenario | Tipo di attività | Che cosa diamo a Claude Code | Ruolo dei test |
|---|----------|------------------|------------------------------|----------------|
| 1 | App da zero | Sviluppo "greenfield" (su prato verde: niente codice preesistente) | Una **specifica** scritta | Criterio di **accettazione**: dicono quando abbiamo finito |
| 2 | Caccia ai bug | Manutenzione **correttiva** | Codice rotto + **test rossi** | **Oracolo**: dicono che cosa è giusto e che cosa no |
| 3 | Refactoring | Manutenzione **perfettiva** | Codice brutto ma funzionante + **test verdi** | **Rete di sicurezza**: dicono che non abbiamo rotto nulla |

Questa tabella funziona bene sia in apertura (come promessa) sia in chiusura
(come riepilogo).

## Prima della lezione — lista di controllo

- [ ] Ambiente creato e attivato; `python -m pytest` provato nei due scenari
      con i risultati attesi (scenario 2: 6 verdi e 4 rossi; scenario 3:
      7 verdi).
- [ ] `claude` si avvia e risponde.
- [ ] La cartella `scenario-1-app-da-zero` contiene **solo** `SPECIFICA.md`
      (se restano file di una prova precedente, eliminarli: lo scenario deve
      partire "da zero").
- [ ] Provata almeno una volta l'intera demo: i tempi indicati valgono per
      chi l'ha già vista girare.

## Richiami essenziali su Claude Code usati nella demo

Spieghiamo qui, una volta sola, i meccanismi che useremo in tutti gli scenari:

- **Avvio**: `claude` lanciato **dentro la cartella dello scenario**
  (con l'ambiente conda già attivo in quel terminale).
- **`CLAUDE.md`**: Claude Code carica all'avvio i file `CLAUDE.md` della
  cartella corrente **e di tutte le cartelle superiori**: per questo il
  nostro, messo nella cartella principale, vale per tutti e tre gli scenari.
  Contiene le regole del gioco (ambiente conda già attivo, **niente `uv` né
  `venv` né installazioni**, test con `python -m pytest`, test intoccabili).
  Verifica dal vivo: digitare `/context` e mostrare il file nell'elenco dei
  "Memory files". Vale la pena citare anche `/init`, il comando che genera un
  `CLAUDE.md` iniziale analizzando il progetto: qui non serve perché il file
  è già pronto, ma è ciò che si userebbe su un progetto vero.
- **Modalità piano** (*plan mode*): premendo **Maiusc+Tab** più volte, finché
  la barra di stato mostra "plan mode on", Claude Code **legge e propone un
  piano ma non modifica nulla** finché non approviamo. (In alternativa si può
  avviare direttamente con `claude --permission-mode plan`.) È il momento
  "prima pensare, poi scrivere" ed è perfetto per l'aula.
- **Permessi**: prima di modificare file o eseguire comandi, Claude Code
  **chiede conferma** e mostra la differenza (il *diff*: le righe tolte e
  aggiunte). Far notare ogni richiesta: è il punto in cui resta il controllo
  umano.
- **`/clear`**: azzera la conversazione. Da usare **tra uno scenario e
  l'altro**, così ogni scenario parte con il contesto pulito (in alternativa:
  chiudere e riaprire `claude` nella nuova cartella, che è anche più pulito
  perché cambia la cartella di lavoro).
- **Esc**: interrompe Claude Code mentre sta lavorando, se vogliamo
  correggere la rotta.
- **Riferimenti con `@`**: scrivendo `@SPECIFICA.md` dentro un prompt, il
  contenuto del file viene incluso nel messaggio.

---

## Scenario 1 — Costruire un'app da zero (≈ 25–30 minuti)

**Obiettivo didattico**: mostrare il ciclo completo *specifica → piano →
implementazione → verifica → iterazione*, e che la qualità del risultato
dipende dalla qualità della specifica.

**Preparazione** (da fare davanti all'aula):

```text
conda activate demo-claude
cd scenario-1-app-da-zero
claude
```

Prima di lanciare i prompt, aprire `SPECIFICA.md` sul proiettore (basta un
minuto): l'aula deve sapere che cosa stiamo chiedendo. Sottolineare RF4
(chiusura esatta a 0,00): è il requisito "insidioso" che distingue una
specifica pensata da una buttata giù.

**Svolgimento**:

1. Attivare la **modalità piano** (Maiusc+Tab fino a "plan mode on") e
   incollare:

   ```text
   Leggi @SPECIFICA.md e proponi un piano di lavoro per realizzare
   l'applicazione descritta, senza ancora scrivere codice. Elenca i file
   che creerai e i punti delicati che vedi nei requisiti.
   ```

   *Da far notare*: Claude Code legge la specifica e in genere individua da
   solo il punto delicato degli arrotondamenti (RF4). Il piano si legge
   insieme all'aula.

2. **Approvare il piano** (Claude Code lo propone e chiede come procedere):
   parte l'implementazione. *Da far notare*: le richieste di permesso per la
   creazione dei file, e il fatto che — grazie al `CLAUDE.md` — non prova a
   creare ambienti o a installare nulla.

3. Se non l'ha già fatto da solo:

   ```text
   Esegui i test con python -m pytest e sistema quello che non va.
   ```

4. Vedere il programma all'opera:

   ```text
   Esegui python ammortamento.py --importo 10000 --tan 4.8 --mesi 12,
   mostra la tabella e verifica che l'ultima riga abbia debito residuo 0,00.
   ```

   *Da far notare*: la rata attorno agli 855 € e l'ultima rata leggermente
   diversa (l'aggiustamento di RF4).

5. **Iterazione a sorpresa** — il "cliente" cambia idea (questa richiesta non
   è nella specifica, apposta):

   ```text
   Nuova richiesta del cliente: aggiungi l'opzione --riepilogo-annuale che,
   dopo la tabella, stampa per ogni anno il totale della quota capitale e
   della quota interessi pagate. Aggiorna anche i test.
   ```

   *Da far notare*: lo sviluppo con Claude Code è una **conversazione**, non
   un colpo solo; i test crescono insieme al codice.

**Imprevisti possibili**: se Claude Code fa domande di chiarimento sulla
specifica, benissimo: rispondere davanti all'aula e farne un punto didattico
("la specifica è un dialogo"). Se un test da lui scritto fallisce, lasciarlo
correggere da solo: anche questo è il ciclo normale.

**Se il tempo stringe**: fermarsi dopo il passo 4.

---

## Scenario 2 — Caccia ai bug (≈ 20 minuti)

**Obiettivo didattico**: i test come **oracolo** (la fonte che dice che cosa
è giusto): il ciclo rosso → correzione → verde rende la caccia ai bug
oggettiva e ripetibile.

**Preparazione**:

```text
cd ..\scenario-2-caccia-ai-bug
python -m pytest
```

Eseguire i test **a mano, prima di aprire Claude Code**: compaiono
**6 verdi e 4 rossi**. Leggere con l'aula uno dei messaggi di fallimento
(pytest mostra l'assert fallito e i valori in gioco): è il "sintomo" dal
quale partirà la diagnosi. Poi avviare `claude` (o, se la sessione dello
scenario 1 è ancora aperta nella cartella sbagliata, chiuderla e riaprirla
qui).

**Svolgimento**:

1. Prompt principale:

   ```text
   Esegui python -m pytest. Per ogni test fallito spiega prima la causa
   del problema, poi correggi conto.py un bug alla volta, rieseguendo i
   test dopo ogni correzione. Non modificare i test.
   ```

2. Variante più guidata, se si vuole rallentare e gustarsi il bug più
   istruttivo (si può usare al posto del prompt 1, o prima di esso):

   ```text
   Concentrati solo sul test test_due_conti_distinti_non_condividono_i_movimenti:
   spiega perché fallisce e qual è il meccanismo di Python che lo causa,
   prima di correggere qualsiasi cosa.
   ```

3. Chiusura dello scenario:

   ```text
   Riassumi i quattro bug in una tabella: test che falliva, sintomo,
   causa, correzione applicata.
   ```

**Soluzioni — solo per il docente** (Claude Code può scegliere correzioni
leggermente diverse ma equivalenti: va bene, purché i test diventino verdi
senza essere toccati):

| Test che fallisce | Sintomo | Causa | Correzione attesa |
|---|---|---|---|
| `test_due_conti_distinti_non_condividono_i_movimenti` | I movimenti di Bruno compaiono anche sul conto di Carla | **Argomento di default mutabile**: `movimenti=[]` viene valutato **una volta sola**, alla definizione del metodo, quindi tutti i conti creati senza passare la lista condividono **la stessa** lista. È uno dei trabocchetti più classici di Python | Default `movimenti=None` e, dentro `__init__`, creare la lista: `self.movimenti = movimenti if movimenti is not None else []` |
| `test_prelievo_fino_al_limite_del_fido_consentito` | Un prelievo lecito, che porta il saldo esattamente a −fido, viene rifiutato | **Errore di confine** sulla disuguaglianza: il controllo usa `<=` dove serve `<` (il limite è compreso) | `if self.saldo() - importo < -self.fido:` |
| `test_commissione_addebitata_arrotondata_ai_centesimi` | Addebito registrato 12.69705 invece di 12.70 | **Manca l'arrotondamento** ai centesimi; occasione per parlare dei numeri in virgola mobile e del denaro | `addebito = round(self.saldo() * percentuale / 100, 2)` |
| `test_movimenti_del_mese_filtra_anche_per_anno` | Chiedendo marzo 2026 arriva anche marzo 2025 | Il filtro controlla **solo il mese** e ignora il parametro `anno` (che infatti non è usato: indizio visibile a occhio) | `if m.data.year == anno and m.data.month == mese` |

**Da far notare**:

- il bug dell'argomento di default mutabile vale da solo il prezzo del
  biglietto: chiedere all'aula di spiegarlo *prima* di far parlare Claude Code;
- la regola "non toccare i test" è scritta in `CLAUDE.md`: se qualcuno chiede
  "e se fosse il test a essere sbagliato?", è un'ottima domanda per la
  discussione finale (succede, ma la decisione è umana);
- notare che gli indizi c'erano anche "a occhio": le **docstring** di
  `conto.py` descrivono il comportamento corretto, il codice le contraddice.

---

## Scenario 3 — Refactoring (≈ 20–25 minuti)

**Obiettivo didattico**: i test di caratterizzazione come **rete di
sicurezza**, e lo schema **as-is → idiomatico** (prima il codice così com'è,
poi la forma che la comunità Python si aspetta).

**Preparazione**:

```text
cd ..\scenario-3-refactoring
python -m pytest
```

Eseguire i test a mano: **7 verdi su 7**. Poi aprire `report_mensile.py` sul
proiettore e chiedere all'aula: "il programma funziona; che cosa vi dà
fastidio di questo codice?". Raccogliere 2–3 risposte (la lista completa dei
difetti è nel `README.md` dello scenario). Poi avviare `claude`.

**Svolgimento**:

1. In **modalità piano** (Maiusc+Tab):

   ```text
   Leggi report_mensile.py e proponi un piano di refactoring: elenca i
   code smell che trovi e come li risolveresti, senza cambiare il
   comportamento osservabile. I test in test_report.py devono restare
   verdi e non vanno modificati.
   ```

   *Da far notare*: confrontare la lista di Claude Code con quella raccolta
   dall'aula un minuto prima.

2. Approvare e procedere:

   ```text
   Procedi a piccoli passi: dopo ogni passo esegui python -m pytest e
   fermati subito se un test diventa rosso. Obiettivi: eliminare la
   variabile globale, spezzare fai_tutto in funzioni piccole con nomi
   parlanti, usare i moduli csv e datetime della libreria standard,
   eliminare duplicazioni e codice morto, dare un nome alla soglia 500,
   separare il calcolo dalla stampa, aggiungere type hint e docstring in
   italiano. La funzione fai_tutto(file, mese, anno) deve restare, con la
   stessa firma e gli stessi risultati.
   ```

3. Il confronto **as-is → idiomatico** (prima com'era, poi com'è diventato):

   ```text
   Mostra un confronto per il blocco che accumula i totali per categoria:
   prima il codice com'era (as-is), poi come è diventato (idiomatico),
   e spiega in tre punti i vantaggi della nuova forma.
   ```

**Da far notare**:

- i test che restano verdi a ogni passo sono la **definizione operativa** di
  "non ho rotto nulla";
- i sei blocchi `t1..t6` che collassano tipicamente in un dizionario o in un
  `defaultdict`: è il momento "idiomatico" per eccellenza;
- "piccoli passi + test" è esattamente come lavorerebbe un bravo sviluppatore
  umano: Claude Code non cambia il metodo, lo accelera.

**Imprevisto utile**: se Claude Code prova a rinominare `fai_tutto` o a
cambiarne la firma, i test diventano rossi: **la rete di sicurezza ha
funzionato**. Non è un incidente, è la dimostrazione dal vivo del perché i
test esistono (e la regola è comunque scritta nel `CLAUDE.md`).

---

## Suggerimenti trasversali

- **Tra uno scenario e l'altro**: `/clear` (o meglio: chiudere `claude`,
  cambiare cartella, riaprirlo) per partire con il contesto pulito.
- **Se Claude Code propone `uv`, `venv` o un'installazione**: aprire il
  `CLAUDE.md` e mostrarlo all'aula. È il motivo per cui l'abbiamo scritto, e
  diventa il momento perfetto per spiegare che le "regole di progetto" si
  danno per iscritto, non si ripetono a voce a ogni sessione.
- **Rivedere sempre i diff** prima di approvare: il controllo di qualità
  resta umano.
- **Variabilità**: a ogni esecuzione i testi e qualche scelta cambiano;
  ancorare la narrazione ai punti stabili (i test rossi/verdi, i criteri di
  accettazione della specifica).
- **Tempi lunghi**: lo scenario 1 è il più lungo; i passi 3–5 si possono
  comprimere. Gli scenari 2 e 3 sono i più "sicuri" come resa in aula.

## Domande per la discussione in aula

- *Scenario 1*: che cosa succederebbe con una specifica ambigua? (esperimento:
  immaginare la specifica senza RF4 e chiedersi che cosa avrebbe deciso
  Claude Code da solo).
- *Scenario 2*: perché la regola "non toccare i test"? E quando invece è il
  test a essere sbagliato? (risposta da costruire: capita, ma deciderlo è una
  responsabilità umana e va motivato).
- *Scenario 3*: come si fa refactoring in sicurezza su codice **senza** test?
  (risposta: prima si scrivono i test di caratterizzazione — e anche quelli
  si possono far scrivere a Claude Code, facendoli però rivedere con cura).
- *Trasversale*: dove restano le responsabilità umane? (la specifica, le
  regole in `CLAUDE.md`, la revisione dei diff, l'accettazione finale).

## Chiusura suggerita (5 minuti)

Rimettere sul proiettore la tabella del filo conduttore e chiudere con il
messaggio unificante: **in tutti e tre gli scenari, Claude Code lavora bene
quando ha un modo concreto di verificare il proprio lavoro** — una specifica
con criteri di accettazione, dei test che fanno da oracolo, una rete di
sicurezza che deve restare verde. Il mestiere di chi sviluppa si sposta a
monte (scrivere bene specifiche, regole e test) e a valle (rivedere e
accettare), ed è lì che si gioca la qualità.
