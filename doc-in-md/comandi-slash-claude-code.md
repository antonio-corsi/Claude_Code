# I comandi slash più utili di Claude Code

> **Nota di versione.** Elenco verificato sulla documentazione ufficiale di Claude Code (code.claude.com/docs) il **21 ottobre 2026** (versioni 2.1.x). I comandi integrati cambiano di versione in versione: in caso di dubbio facciamo fede alla pagina ufficiale linkata in fondo, oppure a `/release-notes` dentro la sessione.

I **comandi slash** (così chiamati perché iniziano con la barra `/`) controllano Claude Code dall'interno di una sessione: cambiare modello, gestire i permessi, liberare il contesto, avviare flussi di lavoro. Digitando `/` compare il menu completo, che si filtra man mano che scriviamo; un comando è riconosciuto solo **all'inizio** del messaggio, e il testo che segue diventa il suo argomento.

Accanto ai comandi integrati, nel menu `/` compaiono anche le **skill** nostre (`/nome-skill`) e quelle dei plugin (`/plugin:nome`): dal punto di vista dell'invocazione sono comandi a tutti gli effetti. Alcuni degli stessi comandi integrati, segnalati più sotto, sono oggi implementati come skill incluse nel prodotto.

Di seguito i comandi più utili nell'uso quotidiano, raggruppati per funzione. Le parentesi quadre indicano argomenti opzionali.

---

## 1. Gestione del contesto e della sessione (i quotidiani)

| Comando | A cosa serve |
|---|---|
| `/clear [nome]` | Inizia una conversazione nuova con contesto vuoto; il nome opzionale etichetta quella precedente nel selettore di `/resume`. Per liberare contesto *continuando* la stessa conversazione usiamo invece `/compact` |
| `/compact [istruzioni]` | Libera contesto riassumendo la conversazione fin lì; possiamo passare istruzioni su cosa privilegiare nel riassunto |
| `/context` | Visualizza l'uso corrente del contesto come griglia colorata, con suggerimenti di ottimizzazione (strumenti pesanti, memoria gonfia, avvisi di capienza) |
| `/resume [sessione]` | Riprende una conversazione precedente, per nome o ID, oppure da un selettore |
| `/rewind` | Riporta la conversazione e/o il codice a un punto precedente (**checkpoint**, cioè un punto di ripristino salvato automaticamente). Alias: `/undo`, `/checkpoint` |
| `/usage` | Mostra il costo della sessione, i limiti del piano e le statistiche di attività; `/cost` e `/stats` sono suoi alias |

## 2. Impostazione del progetto

| Comando | A cosa serve |
|---|---|
| `/init` | Inizializza il progetto creando il file guida `CLAUDE.md` — la "memoria di progetto" che Claude legge all'avvio di ogni sessione |
| `/memory` | Modifica i file `CLAUDE.md` e gestisce la memoria automatica |
| `/permissions` | Gestisce le regole di permesso sugli strumenti (allow / ask / deny), per ambito; è il centro di controllo dell'autonomia dell'agente |
| `/add-dir <percorso>` | Aggiunge una directory di lavoro accessibile nella sessione corrente |
| `/plan [descrizione]` | Entra in **plan mode**: Claude propone un piano di lavoro senza toccare alcun file — ideale prima di un refactoring importante |
| `/sandbox` | Attiva/disattiva la **sandbox**, l'ambiente isolato per l'esecuzione dei comandi (solo sulle piattaforme supportate; su Windows nativo non è disponibile) |

## 3. Modello e comportamento

| Comando | A cosa serve |
|---|---|
| `/model [modello]` | Cambia il modello e lo salva come default per le nuove sessioni; con le frecce sinistra/destra si regola anche il livello di ragionamento |
| `/effort [livello]` | Imposta direttamente il livello di ragionamento: da `low` a `xhigh`, `max`, oppure `auto` |
| `/output-style [stile]` | Elenca gli stili di risposta o ne attiva uno (es. `/output-style concise`) |
| `/config [chiave=valore]` | Apre l'interfaccia delle impostazioni (tema, modello, modalità editor...); accetta anche coppie `chiave=valore` dirette |

## 4. Estensioni: MCP, plugin, skill, hook, subagenti

| Comando | A cosa serve |
|---|---|
| `/mcp` | Stato e gestione dei server MCP: connessioni, autenticazione OAuth, `enable`/`disable`/`reconnect` |
| `/plugin [sottocomando]` | Gestore dei plugin: scoperta, installazione, marketplace; accetta sottocomandi diretti come `install`, `list`, `enable` |
| `/skills` | Elenca le skill disponibili, filtrabili per nome o fonte, con ordinamento per costo in token |
| `/skill-doctor` | Mostra quanto contesto costa ogni skill e quanto viene usata davvero: serve a individuare cosa spegnere |
| `/hooks` | Visualizza le configurazioni degli hook (i comandi automatici agganciati agli eventi del ciclo di vita) |
| `/agents` | Promemoria per creare o gestire i subagenti; le definizioni stanno in `.claude/agents/` (di progetto) o `~/.claude/agents/` (personali) |

## 5. Codice e Git/GitHub

| Comando | A cosa serve |
|---|---|
| `/diff` | Mostra le modifiche nell'albero di lavoro, incluse quelle fatte da Claude nella sessione |
| `/code-review [opzioni]` | Revisione del diff corrente — o di un PR, branch o percorso indicato — a caccia di bug di correttezza; `/review` è un alias; opzioni utili: livello di severità e `--fix` |
| `/security-review` | Analizza le modifiche del branch corrente cercando vulnerabilità di sicurezza (injection, problemi di autenticazione, esposizione di dati) |
| `/install-github-app` | Installa la GitHub App di Claude su un repository, con setup opzionale delle GitHub Actions |

## 6. Diagnostica e utilità

| Comando | A cosa serve |
|---|---|
| `/status` | Versione, modello, account e connettività della sessione |
| `/doctor` | Check-up completo: diagnostica installazione, impostazioni e problemi nei `CLAUDE.md`, proponendo correzioni da confermare (oggi è una skill inclusa) |
| `/help` | Guida e comandi disponibili |
| `/export [file]` | Esporta la conversazione come testo, su file o negli appunti |
| `/tasks` | Mostra e gestisce il lavoro in background della sessione, subagenti conclusi inclusi |
| `/release-notes` | Changelog interattivo, versione per versione |
| `/login` / `/logout` | Accesso e uscita dall'account Anthropic |
| `/terminal-setup` | Configura Shift+Invio per andare a capo nel terminale (VS Code e altri) |
| `/theme` | Cambia il tema colori (incluse varianti accessibili per daltonismo) |
| `/bug [segnalazione]` | Segnala un bug ad Anthropic, scegliendo quanta cronologia includere e con schermata di consenso |

---

## Avvertenze (comandi che non esistono più)

Due comandi ancora citati in molti tutorial in rete sono stati **rimossi**:

- `/vim` (rimosso nella 2.1.92) — la modalità di editing Vim si attiva ora da `/config` → *Editor mode*;
- `/pr-comments` (rimosso nella 2.1.91) — per i commenti di una pull request basta ora chiederlo a Claude in linguaggio naturale.

Meglio non inserirli nel materiale didattico.

## I sei essenziali

Se dobbiamo insegnarne solo sei, questi coprono l'intero ciclo di lavoro quotidiano:

1. `/init` — prepariamo il progetto;
2. `/model` — scegliamo il modello;
3. `/permissions` — decidiamo quanta autonomia dare;
4. `/compact` — teniamo sotto controllo il contesto;
5. `/rewind` — torniamo indietro quando serve;
6. `/resume` — riprendiamo il lavoro il giorno dopo.

---

## Fonti

- Riferimento completo dei comandi: <https://code.claude.com/docs/en/commands>
- Skill (comandi personalizzati): <https://code.claude.com/docs/en/skills>
- Changelog: <https://code.claude.com/docs/en/changelog>
