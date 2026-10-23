# Auto memory in Claude Code

**Al 13 ottobre 2026 l’auto memory esiste ancora ed è attiva per impostazione predefinita nelle sessioni locali di Claude Code**, salvo disabilitazione nelle impostazioni. È una funzione distinta sia da `CLAUDE.md` sia dall’*autocompact*. ([code.claude.com](https://code.claude.com/docs/en/memory))

## 1. Che cos’è l’auto memory

È una **memoria persistente su file che Claude Code aggiorna autonomamente**, selezionando informazioni utili per conversazioni successive: preferenze dell’utente, correzioni ricevute, decisioni di progetto e riferimenti a informazioni esterne. **Non è una registrazione completa delle conversazioni**: Claude decide che cosa vale la pena conservare. ([code.claude.com](https://code.claude.com/docs/en/memory))

La distinzione tecnica importante è questa: **“ricordare” non significa riaddestrare il modello o modificarne i pesi**. Il meccanismo descritto è una memoria esterna: le informazioni salvate vengono nuovamente fornite al modello come contesto. È quindi una capacità dell’ambiente agentico Claude Code, non un apprendimento permanente dentro la rete neurale. ([code.claude.com](https://code.claude.com/docs/en/how-claude-code-works))

## 2. Quando è stata introdotta?

Il riferimento ufficiale più chiaro è **Claude Code v2.1.59, pubblicata il 26 febbraio 2026**. Le note di rilascio annunciano esplicitamente:

> “Claude automatically saves useful context to auto-memory. Manage with /memory” ([github.com](https://github.com/anthropics/claude-code/releases/tag/v2.1.59))

C’è però una precisazione storica: **alcuni utenti la utilizzavano già prima di quella release**. Nel repository ufficiale esistono, per esempio, segnalazioni del **6 febbraio 2026** che descrivono la scrittura automatica della memoria e chiedono come disabilitarla. Sono testimonianze d’uso, non un annuncio ufficiale di lancio. ([github.com](https://github.com/anthropics/claude-code/issues/23750))

La formulazione più rigorosa per il materiale del corso è quindi:

**«Auto memory era già presente per alcuni utenti all’inizio di febbraio 2026; il salvataggio automatico viene annunciato esplicitamente nelle note della versione 2.1.59 del 26 febbraio 2026».** Non attribuirei a quest’ultima data la prima disponibilità assoluta. ([github.com](https://github.com/anthropics/claude-code/issues/23750))

## 3. Dove conserva le informazioni?

Per impostazione predefinita, in una directory del tipo:

```text
~/.claude/projects/<progetto>/memory/
```

Contiene un indice `MEMORY.md` e file tematici. La memoria è **locale alla macchina** e associata al repository; le sue sottocartelle e i relativi Git worktree condividono la stessa directory. Non viene automaticamente sincronizzata fra computer. ([code.claude.com](https://code.claude.com/docs/en/memory))

All’inizio di una conversazione vengono caricate **le prime 200 righe di `MEMORY.md`, oppure i primi 25 KB, a seconda del limite raggiunto prima**. Questo è un limite al caricamento iniziale dell’indice, non alla quantità complessiva di informazioni memorizzabili. ([code.claude.com](https://code.claude.com/docs/en/how-claude-code-works))

I file tematici vengono letti quando servono. Sono normali file Markdown: possono essere esaminati, corretti o eliminati. ([code.claude.com](https://code.claude.com/docs/en/memory))

## 4. Come verificarla nella CLI

All’interno della sessione Claude Code, esegua:

```text
/memory
```

Il comando permette di **abilitare o disabilitare l’auto memory, consultare le informazioni salvate e gestire i file di istruzioni `CLAUDE.md`**. È il punto di partenza per controllare la funzione nella Sua installazione. ([code.claude.com](https://code.claude.com/docs/en/commands))

### Una prova hands-on per il corso

In un progetto dimostrativo, può usare questo prompt:

```text
Ricorda per le prossime sessioni di questo progetto:
preferisco spiegazioni in italiano, mantenendo in inglese
i termini tecnici di programmazione.
```

Poi controlli con `/memory` che l’informazione sia stata effettivamente salvata. Avvii una nuova conversazione con `/clear` e chieda:

```text
Quale preferenza ho espresso sulla lingua delle spiegazioni?
```

`/clear` avvia una nuova conversazione senza eliminare la memoria di progetto. **Il controllo del file salvato è importante**: consente di verificare la persistenza, anziché affidarsi soltanto alla risposta verbale dell’agente. ([code.claude.com](https://code.claude.com/docs/en/commands))

## 5. Auto memory, CLAUDE.md e autocompact non sono la stessa cosa

| Meccanismo | A che cosa serve |
|---|---|
| **`CLAUDE.md`** | Fornire istruzioni persistenti ed esplicite: convenzioni, comandi di test e modalità di lavoro del progetto. |
| **Auto memory** | Riutilizzare informazioni che Claude ha selezionato e salvato durante il lavoro. |
| **Autocompact** | Ridurre il contesto occupato nella conversazione corrente, sintetizzandola quando necessario. |
| **`/context`** | Mostrare che cosa sta occupando la finestra di contesto. |

Queste funzioni sono complementari: **la persistenza fra sessioni e la gestione dello spazio nella conversazione risolvono problemi diversi**. Inoltre, la compattazione può perdere dettagli: non sostituisce le istruzioni persistenti. ([code.claude.com](https://code.claude.com/docs/en/how-claude-code-works))

**Nel Suo screenshot, dunque, “Autocompact buffer” non indica lo spazio dell’auto memory.** Per vedere il consumo di contesto si usa `/context`; per controllare la memoria persistente si usa `/memory`. ([code.claude.com](https://code.claude.com/docs/en/commands))
