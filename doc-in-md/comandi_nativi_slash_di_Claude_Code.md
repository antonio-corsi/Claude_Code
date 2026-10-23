# I comandi nativi slash di Claude Code

Guida operativa e repertorio dei comandi distribuiti con Claude Code

**Lingua:** italiano · **Documentazione verificata:** 14 ottobre 2026

> Il riferimento riguarda principalmente Claude Code nel terminale. L'elenco effettivo dipende dalla versione installata, dal piano, dal sistema operativo, dal provider e dalle policy dell'organizzazione. La documentazione online può descrivere funzionalità non ancora disponibili nella propria installazione. Le sintassi riportate riprendono il riferimento ufficiale consultato; non è stata eseguita una verifica su una specifica installazione locale.

## Indice

1. [Che cosa sono](#1-che-cosa-sono)
2. [Come si usano](#2-come-si-usano)
3. [Nativi, skill, workflow e integrazioni](#3-nativi-skill-workflow-e-integrazioni)
4. [Repertorio completo](#4-repertorio-completo)
5. [Contesto, memoria e conversazione](#5-contesto-memoria-e-conversazione)
6. [Configurazione, modelli e autorizzazioni](#6-configurazione-modelli-e-autorizzazioni)
7. [Sessioni e lavoro in parallelo](#7-sessioni-e-lavoro-in-parallelo)
8. [Workflow pratici](#8-workflow-pratici)
9. [Alias e compatibilità](#9-alias-e-compatibilità)
10. [Problemi comuni](#10-problemi-comuni)
11. [Scheda rapida](#11-scheda-rapida)
12. [Fonti ufficiali](#12-fonti-ufficiali)

## 1. Che cosa sono

I comandi slash sono istruzioni riconosciute da Claude Code all'interno della sessione. Iniziano con `/` e servono a governare la sessione, interrogare lo stato, configurare strumenti o avviare attività specializzate.

Esempi:

```text
/help
/status
/model sonnet
/compact Conserva requisiti, decisioni, file modificati e problemi aperti.
```

Un comando **nativo**, in senso stretto, è implementato nel programma: la CLI interpreta la richiesta ed esegue una logica prevista dal prodotto. Una skill, invece, consegna istruzioni al modello, che decide come svolgere il lavoro usando gli strumenti disponibili. La stessa sintassi `/nome` può quindi nascondere meccanismi diversi.

Questa distinzione è utile per prevedere il risultato: `/context` mostra informazioni sulla finestra di contesto; `/simplify` avvia un'attività di analisi e modifica del codice. Non tutti i comandi sono semplici menu e non tutti sono operazioni prive di consumo del modello.

### Slash, shell e opzioni di avvio

| Forma | Dove si scrive | Significato |
| --- | --- | --- |
| `claude` | Terminale del sistema operativo | Avvia Claude Code. |
| `claude --version` | Terminale del sistema operativo | Mostra la versione installata. |
| `claude --help` | Terminale del sistema operativo | Mostra comandi e opzioni della CLI. |
| `/help` | Prompt di Claude Code | Mostra la guida della sessione. |
| `/model sonnet` | Prompt di Claude Code | Cambia il modello tramite un comando interno. |
| `!git status` | Prompt di Claude Code | Esegue un comando nella modalità shell e porta l'output nella sessione. |
| `@src/main.py` | Prompt di Claude Code | Riferisce un file usando il completamento dei percorsi. |

`/help` e `claude --help` appartengono a livelli diversi. Anche `/cd` e `!cd` non vanno assimilati: il primo cambia la directory di lavoro della sessione secondo le regole di Claude Code; il secondo è un comando eseguito nella shell.

## 2. Come si usano

1. Avviare Claude Code con `claude` nella directory del progetto.
2. Digitare `/` all'inizio del messaggio per aprire il menu.
3. Aggiungere lettere per filtrare; selezionare la voce e premere Invio.
4. Inserire gli eventuali argomenti dopo il nome.

La notazione del repertorio usa `<argomento>` per un valore obbligatorio e `[argomento]` per uno facoltativo. Questi delimitatori non vanno digitati. Il simbolo `|` separa alternative.

```text
/add-dir ../documentazione
/rename Analisi API credito
/export sessione-credito.txt
/plan Progetta la gestione dei duplicati nel servizio prestiti.
```

Un comando viene riconosciuto all'inizio del messaggio. Scrivere «spiegami /compact» è una domanda, non l'esecuzione del comando.

Non concatenare arbitrariamente comandi nativi: `/status /context` non è una sequenza garantita. Per le skill la documentazione prevede invece concatenazioni iniziali, fino a sei, con testo finale passato come argomento a ciascuna; è una regola specifica delle skill.

### Mentre Claude sta lavorando

Molti comandi vengono accodati ed eseguiti alla fine del turno. Alcuni, come `/status`, `/tasks` e `/usage`, possono funzionare subito. Per altri il comportamento cambia con versione e renderer: non assumere che un comando accodato interrompa il lavoro in corso.

### Menu e comandi nascosti

Il menu comprende anche alias e comandi aggiunti dalle integrazioni. Un errore di digitazione può lasciare suggerimenti simili senza selezionarne nessuno: Invio potrebbe inviare il testo errato. Alcuni comandi, come `/heapdump`, sono intenzionalmente nascosti e richiedono il nome completo. Il menu non è quindi un inventario assoluto di ogni funzione interna.

## 3. Nativi, skill, workflow e integrazioni

| Categoria | Origine | Modalità di funzionamento | Esempi |
| --- | --- | --- | --- |
| Nativo | Implementazione della CLI | Logica del programma, menu o controllo della sessione | `/help`, `/clear`, `/context`, `/memory` |
| Skill inclusa | Istruzioni distribuite con il prodotto | Il modello segue un prompt specializzato | `/doctor`, `/debug`, `/batch`, `/simplify` |
| Workflow incluso | Workflow dinamico distribuito con il prodotto | Orchestrazione di lavoro in background con subagenti | `/deep-research` |
| Skill personale o di progetto | File definiti dall'utente | Istruzioni personalizzate | `/deploy`, se definito nel progetto |
| Comando da plugin | Estensione installata | Funzioni o skill aggiuntive | Dipende dal plugin. |
| Prompt MCP | Server MCP collegato | Prompt pubblicato dal server | Dipende dal server. |

**Distribuito con Claude Code** non significa necessariamente **nativo implementato nella CLI**. Il repertorio seguente separa queste categorie. In particolare il riferimento corrente classifica `/doctor` come skill: vecchie guide possono presentarlo genericamente come comando nativo.

I vecchi comandi personalizzati in `.claude/commands/` continuano a funzionare; il formato più ricco delle skill usa `.claude/skills/<nome>/SKILL.md`. Non è necessario creare questi file per usare i comandi nativi.

## 4. Repertorio completo

Le tabelle coprono le voci della pagina ufficiale **Commands** consultata. Le descrizioni sono sintetizzate in italiano; la colonna delle note riporta vincoli importanti, senza riprodurre tutta la cronologia di ogni release. Gli alias supplementari sono raccolti nella sezione 9. Per requisiti puntuali di piano, provider e versione consultare la voce corrente nella fonte ufficiale.

### 4.1 Comandi nativi e altre voci non marcate come skill o workflow

| Comando e sintassi | Funzione e impiego |
| --- | --- |
| `/add-dir <path>` | Aggiunge una directory accessibile nella sessione. Non carica automaticamente la maggior parte delle configurazioni `.claude/` di quella directory; molti percorsi di rete non sono supportati. |
| `/advisor [model\|off]` | Abilita un secondo modello come consulente oppure lo disabilita con `off`. Senza argomenti apre il selettore; disponibilità dei modelli e forme testuali dipendono dall’ambiente. |
| `/agents` | Nel riferimento corrente ricorda di chiedere a Claude di creare o gestire subagenti, oppure di editarne i file. L’interfaccia interattiva descritta nelle vecchie guide riguarda v2.1.197 e precedenti. |
| `/artifacts` | Elenca artefatti propri o condivisi e consente di allegarli, aprirli o copiarne il link. Richiede disponibilità degli artefatti. |
| `/auto-mode-setup` | Prepara impostazioni dell’ambiente per la modalità automatica partendo dal progetto e dalle sessioni recenti; permette di revisionarle prima del salvataggio. Requisiti di piano e versione. |
| `/autocompact [auto\|<tokens>]` | Imposta la soglia della compattazione automatica; `auto` ripristina quella adattata al modello. Salva la preferenza nelle impostazioni utente. |
| `/autofix-pr [prompt]` | Avvia una sessione cloud che osserva la PR del branch corrente e propone o invia correzioni a CI e commenti secondo le istruzioni. Richiede `gh` e accesso alle sessioni cloud; può effettuare push. |
| `/background [prompt]` | Distacca la sessione facendola continuare in background. Un prompt opzionale aggiunge un’ultima istruzione. Alias `/bg`. |
| `/branch [name]` | Crea una diramazione della conversazione e vi passa. Conserva l’originale recuperabile con `/resume`; non equivale alla creazione di un branch Git. |
| `/btw [question]` | Pone una domanda laterale senza aggiungerla alla conversazione principale. Senza domanda permette di rivedere domande laterali precedenti, nelle versioni recenti. |
| `/bug [report]` | Apre una segnalazione con scelta della cronologia e consenso prima dell’invio. Su connessione diretta può inviare ad Anthropic; con provider terzi può produrre un archivio locale. Alias `/share`. |
| `/cd <path>` | Sposta la directory di lavoro della sessione mantenendo la conversazione. Differisce da `/add-dir`, che aggiunge accesso senza cambiare la directory principale. |
| `/chrome` | Configura l’integrazione Claude in Chrome. |
| `/clear [name]` | Avvia una nuova conversazione con contesto vuoto. Il nome opzionale etichetta quella precedente, recuperabile con `/resume`. Alias `/reset` e `/new`. |
| `/color [color\|default]` | Cambia colore della barra del prompt: red, blue, green, yellow, purple, orange, pink, cyan o default. Senza valore sceglie un colore casuale. |
| `/compact [instructions]` | Riassume la conversazione liberando contesto, con eventuali istruzioni su cosa preservare. |
| `/config [key=value ...]` | Apre le impostazioni; accetta anche coppie `key=value`. `/config --help` elenca le chiavi accettate. Alias `/settings`. |
| `/context [all]` | Mostra occupazione del contesto, ripartizione e suggerimenti. In fullscreen `all` espande il dettaglio. |
| `/copy [N]` | Copia l’ultima risposta o la N-esima più recente. Il selettore permette blocchi singoli e, con `w`, scrittura su file. |
| `/cost` | Alias di `/usage` nel riferimento corrente; vecchie versioni possono avere un pannello distinto. |
| `/design-login` | Autorizza l’accesso al design system usato da `/design-sync` tramite l’account claude.ai. |
| `/desktop` | Continua la sessione nell’app desktop Claude Code. Richiede macOS o Windows x64 e abbonamento Claude. Alias `/app`. |
| `/diff` | Mostra le modifiche nel working tree, comprese quelle effettuate da Claude. È una revisione visiva, non una prova di correttezza. |
| `/effort [level\|auto\|status\|ultracode [on\|off]]` | Imposta il livello di ragionamento o mostra quello corrente con `status`. Include opzioni ultracode nelle versioni compatibili. `max` vale per la sessione. |
| `/exit` | Esce dalla CLI; in una sessione background collegata distacca il terminale e lascia proseguire la sessione. Alias `/quit`. |
| `/export [filename]` | Esporta la conversazione come testo semplice. Con nome file salva direttamente, senza apre una finestra di scelta. |
| `/fast [on\|off]` | Attiva o disattiva fast mode dove disponibile. Non equivale genericamente a selezionare un modello più piccolo. |
| `/feedback [report]` | Apre il feedback sul prodotto con consenso e regole di invio analoghe a `/bug`; può mostrare la coda di bozze preparate da Claude. |
| `/focus` | Attiva una vista concentrata su ultimo prompt, riepilogo strumenti e risposta. Principalmente fullscreen; estensioni e Remote Control hanno comportamenti propri. |
| `/fork [prompt]` | Copia la conversazione in una sessione background separata, opzionalmente avviandola con un prompt. Il comportamento storico come subagente dipende da versione e agent view. |
| `/goal [condition\|clear]` | Definisce una condizione che Claude cerca di raggiungere proseguendo tra turni. `clear` rimuove l’obiettivo; senza argomenti mostra lo stato. |
| `/heapdump` | Scrive snapshot dell’heap e diagnostica della memoria. Comando nascosto: digitare il nome completo. Lo snapshot può contenere conversazione e credenziali; per segnalazioni usare solo il file diagnostico indicato dalla guida. |
| `/help` | Mostra guida e comandi disponibili nella sessione. |
| `/hooks` | Mostra le configurazioni degli hook, automazioni eseguite in corrispondenza di eventi. |
| `/ide` | Gestisce le integrazioni IDE e ne mostra lo stato. |
| `/import [codex\|gemini\|cursor] [--dry-run] [--yes]` | Importa configurazioni da Codex, Gemini CLI o Cursor. `--dry-run` anteprima senza scrittura; `--yes` evita il selettore. Requisiti di versione e limitazioni sui provider. |
| `/init` | Inizializza la guida del progetto `CLAUDE.md`. Il flusso interattivo esteso richiede `CLAUDE_CODE_NEW_INIT=1`; può offrire importazioni da altri strumenti. |
| `/insights` | Genera un report HTML sull’uso recente delle sessioni locali. Non disponibile nelle sessioni cloud. |
| `/install-github-app` | Guida l’installazione della Claude GitHub App e l’eventuale configurazione di Actions e segreti. Per repository github.com. |
| `/install-slack-app` | Avvia l’installazione dell’app Claude per Slack tramite autorizzazione OAuth nel browser. |
| `/keybindings` | Apre il file di configurazione delle scorciatoie da tastiera. |
| `/list-agents` | Elenca subagenti, membri del team e altre sessioni raggiungibili tramite messaggi. Richiede cross-session messaging. Alias `/peers`. |
| `/login` | Esegue l’accesso all’account Anthropic. |
| `/logout` | Disconnette l’account Anthropic. |
| `/mcp [reconnect (<server>\|all)\|enable\|disable [<server>\|all]]` | Gestisce server MCP e autenticazioni OAuth; può riconnettere, abilitare o disabilitare server. In modalità non interattiva può stampare lo stato. |
| `/memory` | Mostra e apre file di istruzioni e memorie, permette di controllare auto memory e visitarne le voci o la cartella. |
| `/mobile` | Mostra un QR code per scaricare l’app Claude mobile. Alias `/ios` e `/android`. |
| `/model [model]` | Seleziona il modello e, nel flusso interattivo corrente, può salvarlo come default. Il selettore offre anche il cambio solo per la sessione; in `-p` il cambio resta locale alla sessione. |
| `/output-style [style]` | Elenca o cambia lo stile delle risposte, ad esempio `concise`; richiede una versione compatibile. |
| `/passes` | Consente la condivisione di un periodo promozionale di Claude Code, soltanto agli account idonei. |
| `/permissions` | Gestisce regole allow, ask e deny, scope e directory; include opzioni auto mode dove disponibili. Alias `/allowed-tools`. |
| `/plan [description]` | Entra in modalità pianificazione, con una descrizione opzionale del lavoro da analizzare. |
| `/plugin [subcommand]` | Apre la gestione plugin o esegue sottocomandi come list, install, enable e disable. |
| `/powerup` | Propone brevi lezioni interattive con dimostrazioni delle funzionalità. |
| `/privacy-settings` | Mostra e aggiorna le impostazioni privacy per gli abbonati Pro e Max. |
| `/radio` | Apre Claude FM nel browser oppure stampa il riferimento allo stream. |
| `/rate-limit-options` | Mostra alternative al raggiungimento dei limiti: attesa, continuazione al reset, crediti o upgrade, secondo disponibilità. |
| `/recap` | Genera un riepilogo di una riga della sessione corrente. |
| `/release-notes` | Mostra il changelog con selettore delle versioni. Le note entrano nel transcript visibile senza diventare contesto del modello. |
| `/reload-plugins [--force]` | Ricarica i plugin attivi. Se cambiare gli strumenti MCP invaliderebbe la cache, può richiedere `--force`; alcune interfacce non applicano i cambiamenti MCP. |
| `/reload-skills` | Rilegge directory di skill e comandi per rendere disponibili aggiunte e modifiche senza riavvio. |
| `/remote-control` | Rende accessibile la sessione locale da claude.ai tramite Remote Control. Richiede autenticazione e disponibilità della funzione. Alias `/rc`. |
| `/remote-env` | Seleziona l’ambiente cloud predefinito per le sessioni avviate dalla CLI. |
| `/rename [name]` | Rinomina la sessione; senza nome ne propone uno dalla conversazione. Non rinomina repository o branch Git. |
| `/resume [session]` | Riprende una conversazione per ID o nome, oppure apre il selettore. Nelle versioni recenti può collegarsi a una sessione background ancora attiva. Alias `/continue`. |
| `/rewind` | Torna a un checkpoint della conversazione e/o del codice, oppure riassume da un messaggio selezionato. Alias `/checkpoint` e `/undo`. |
| `/sandbox` | Attiva o disattiva il sandboxing sulle piattaforme supportate; non coincide con le regole di autorizzazione degli strumenti. |
| `/schedule [description]` | Crea, aggiorna, elenca o esegue routine cloud tramite un flusso conversazionale. Alias `/routines`; disponibilità dipendente dall’account. |
| `/scroll-speed` | Regola lo scorrimento della rotella in fullscreen; non disponibile nel terminale JetBrains. |
| `/security-review` | Analizza il diff rispetto al branch predefinito di origin per vulnerabilità. Richiede il remote origin e un riferimento base valido. |
| `/setup-bedrock` | Configurazione guidata di autenticazione, regione e modelli Amazon Bedrock. Può essere nascosto fino all’attivazione del relativo ambiente. |
| `/setup-vertex` | Configurazione guidata per Google Cloud: autenticazione, progetto, regione e modelli. Può essere nascosto fino all’attivazione del relativo ambiente. |
| `/skill-doctor` | Mostra costo in contesto e uso delle skill per individuare quelle da disabilitare; richiede versione e feature flag compatibili. |
| `/skills` | Elenca e filtra skill; può ordinarle per token e modificarne la visibilità, con restrizioni per plugin, policy e frontmatter. |
| `/stats` | Alias di `/usage` che apre la scheda delle statistiche. |
| `/status` | Mostra versione, modello, account e connettività nella scheda Status. Funziona anche mentre Claude risponde. |
| `/statusline` | Configura la riga di stato; accetta una descrizione oppure prova una configurazione automatica dal prompt della shell. |
| `/stickers` | Permette di ordinare adesivi Claude Code. |
| `/stop` | Ferma la sessione background collegata o destinataria del comando. Mantiene transcript ed eventuale worktree; distinto dal semplice distacco. |
| `/subtask <task>` | Avvia un subagente background che eredita la conversazione e restituisce il risultato qui. Diverso da una sessione background indipendente. |
| `/tasks` | Mostra e gestisce il lavoro background della sessione, inclusi subagenti terminati. Alias `/bashes`. |
| `/team-onboarding` | Genera una guida Markdown di onboarding dalle attività degli ultimi 30 giorni; su abbonamenti compatibili può produrre un link condivisibile. |
| `/teleport` | Porta una sessione cloud nel terminale, recuperando branch e conversazione. Richiede abbonamento claude.ai. Alias `/tp`. |
| `/terminal-setup` | Configura scorciatoie e funzioni del terminale, secondo l’applicazione: nuove righe, Option+Enter o accesso agli appunti. |
| `/theme` | Sceglie tema, varianti accessibili, colori ANSI o temi personalizzati. Include auto e creazione di nuovi temi. |
| `/tui [default\|fullscreen]` | Cambia renderer terminale tra default e fullscreen, rilanciando l’interfaccia mantenendo la conversazione. |
| `/ultrareview [PR or branch]` | Alias per la revisione cloud approfondita; la forma preferita è `/code-review ultra`. Disponibilità e costi dipendono dal piano. |
| `/upgrade` | Apre il percorso di upgrade del piano; non disponibile su tutti i piani. |
| `/usage` | Mostra costo della sessione, limiti del piano e statistiche di attività. Alias `/cost` e `/stats`. |
| `/usage-credits` | Configura crediti aggiuntivi o permette di chiederli all’amministratore, con conferma dell’invio della richiesta. In passato `/extra-usage`. |
| `/voice [hold\|tap\|off]` | Controlla dettatura vocale: hold, tap o off; richiede un account Claude.ai. |
| `/web-setup` | Collega GitHub per le sessioni cloud usando credenziali della CLI gh. |
| `/workflows` | Mostra avanzamento dei workflow e permette di osservarli, sospenderli, riprenderli o salvarli. |

### 4.2 Skill distribuite con Claude Code

| Comando e sintassi | Funzione e impiego |
| --- | --- |
| `/artifact-capabilities` | Carica la guida alle capacità runtime degli artefatti, comprese integrazioni e download disponibili all’account. |
| `/artifact-diagramming` | Carica indicazioni per diagrammi leggibili negli artefatti, inclusi SVG e temi chiaro/scuro. |
| `/batch <instruction>` | Scompone modifiche estese in unità indipendenti, propone il piano e dopo approvazione usa subagenti in worktree isolati. Può pubblicare modifiche. |
| `/claude-api [migrate\|upgrade\|managed-agents-onboard\|prompt-audit\|cost-optimize\|build-eval\|hillclimb\|preserved-thinking-migration]` | Carica riferimenti API Claude e Managed Agents per il progetto. Offre sottocomandi per migrazione, upgrade, valutazioni e ottimizzazione. |
| `/claude-in-chrome [task]` | Esegue attività nel browser tramite l’integrazione Chrome: verifiche UI, moduli e console. Richiede integrazione disponibile. |
| `/code-review [low\|medium\|high\|xhigh\|max\|ultra] [--fix] [--comment] [--max-findings n\|all\|default] [pr#\|branch\|path]` | Ricerca bug nel diff o in PR, branch e percorsi. `--fix` applica correzioni, `--comment` pubblica commenti, `ultra` avvia la revisione cloud. Alias `/review`. |
| `/dataviz [request]` | Carica indicazioni per grafici e dashboard, scelta della visualizzazione, palette, contrasto e accessibilità. |
| `/debug [description]` | Attiva il logging diagnostico e analizza problemi runtime. Se avviato a metà sessione, cattura eventi da quel momento. |
| `/design [brief]` | Genera mockup e flussi su una canvas Claude Design. Richiede artefatti, template e provider compatibili. |
| `/design-sync [hint]` | Converte e carica il design system React del repository in Claude Design. La prima verifica può essere lunga; provider limitati. |
| `/doctor [prompt-audit [path]]` | Diagnostica installazione, configurazione, estensioni e istruzioni; propone correzioni da confermare. Include prompt-audit nelle versioni recenti. Alias `/checkup`. |
| `/fewer-permission-prompts` | Analizza transcript e propone una allowlist di chiamate frequenti in sola lettura, modificando le impostazioni del progetto. |
| `/loop [interval] [prompt]` | Ripete un prompt mentre la sessione resta aperta. Esempio `/loop 5m controlla il deploy`. Senza intervallo si autoregola; senza prompt usa quello di manutenzione. Alias `/proactive`. |
| `/plugin-authoring` | Carica la guida per scrivere mod; è una skill di un plugin incluso, disattivabile tramite `/plugin`. |
| `/review [low\|medium\|high\|xhigh\|max\|ultra] [--fix] [--comment] [--max-findings n\|all\|default] [pr#\|branch\|path]` | Alias corrente di `/code-review`, con gli stessi livelli e flag. Nelle vecchie release aveva un comportamento diverso. |
| `/run` | Avvia e guida l’applicazione del progetto per osservare il comportamento reale. |
| `/run-skill-generator` | Genera una skill del progetto che insegna a `/run` e `/verify` come costruire, avviare e pilotare l’app. |
| `/simplify [target]` | Analizza il codice con più agenti per riuso, semplicità, efficienza e livello di astrazione, applicando correzioni. Non sostituisce la ricerca di bug. |
| `/slides [brief]` | Crea una presentazione come artefatto Claude Slides, dove template e artefatti sono disponibili. |
| `/update-config [request]` | Interpreta una richiesta di configurazione e modifica il settings.json appropriato; per preferenze semplici usare `/config`. |
| `/verify` | Verifica un cambiamento costruendo, eseguendo e osservando l’app, oltre ai soli test e controlli statici. |
| `/workflow-authoring` | Carica il riferimento per scrivere workflow dinamici: API, ripresa, qualità ed esempi. |

### 4.3 Workflow distribuiti con Claude Code

| Comando e sintassi | Funzione e impiego |
| --- | --- |
| `/deep-research <question>` | Esegue ricerca web distribuita, confronto delle fonti e sintesi con citazioni tramite workflow dinamico. |

### 4.4 Voci storiche rimosse

| Comando e sintassi | Funzione e impiego |
| --- | --- |
| `/pr-comments [PR]` | Rimosso in v2.1.91; chiedere direttamente a Claude di leggere i commenti della PR. |
| `/ultraplan <prompt>` | Rimosso; usare la modalità pianificazione con `/plan`. |
| `/vim` | Rimosso in v2.1.92; cambiare Editor mode in `/config`. |

## 5. Contesto, memoria e conversazione

### 5.1 Cinque concetti da tenere separati

| Concetto | Contenuto | Comandi pertinenti |
| --- | --- | --- |
| Contesto corrente | Informazioni utilizzabili dal modello nella richiesta attuale | `/context`, `/compact`, `/autocompact` |
| Conversazione | Messaggi e risultati del lavoro nella sessione | `/clear`, `/resume`, `/export` |
| Istruzioni persistenti | Regole scritte nei file `CLAUDE.md` e file collegati | `/init`, `/memory` |
| Auto memory | Note persistenti che Claude salva e richiama | `/memory` |
| Checkpoint | Punti da cui ripristinare conversazione e modifiche tracciate | `/rewind` |

Una conversazione salvata su disco non è necessariamente tutta presente nella finestra del modello. Analogamente, vedere un file nel menu `/memory` non dimostra che ogni sua parte sia caricata nel contesto.

### 5.2 `/context`: capire che cosa occupa la finestra

```text
/context
/context all
```

Il comando rende visibile il consumo del contesto. Le categorie possono includere istruzioni di sistema, strumenti, file di memoria, skill e messaggi. La ripartizione effettiva cambia con versione e configurazione.

È utile prima di un task lungo o quando molti strumenti e istruzioni riducono lo spazio disponibile. La categoria “Memory files” permette di controllare i file di istruzioni caricati. Non va interpretato come un misuratore della RAM del computer: la finestra di contesto riguarda token e informazioni per il modello, mentre `/heapdump` riguarda memoria del processo.

### 5.3 `/compact`: continuare con un riassunto

```text
/compact Conserva gli obiettivi, le decisioni architetturali, i file modificati, i test eseguiti e le attività ancora aperte.
```

La compattazione sostituisce parte della cronologia operativa con una sintesi e libera spazio. È utile se il lavoro continua sullo stesso problema. Può perdere dettagli: requisiti importanti e decisioni definitive vanno anche mantenuti nei documenti del progetto.

Una buona istruzione di compattazione specifica ciò che conta per il prossimo passo. “Riassumi tutto” è meno mirato di “preserva il contratto API, le regole di idempotenza e i test ancora falliti”. La compattazione automatica è regolata da `/autocompact`, nelle versioni che lo supportano.

### 5.4 `/clear`: iniziare un nuovo task

```text
/clear Analisi iniziale del sistema prestiti
```

Avvia una conversazione con contesto vuoto, etichettando quella precedente se viene passato un nome. Non elimina i file del progetto né le memorie persistenti. I file di istruzioni pertinenti restano parte del meccanismo di caricamento delle nuove conversazioni.

Non usare `/clear` come comando di cancellazione della auto memory, pulizia del repository o annullamento di modifiche. Per riprendere la conversazione precedente usare `/resume`.

### 5.5 `/memory`: istruzioni e auto memory

```text
/memory
```

Il menu elenca posizioni di file di istruzioni nei diversi scope, permette di aprirli nell’editor, controllare la auto memory e accedere alla relativa cartella. Può mostrare anche file non ancora esistenti: selezionarli può crearli. Per verificare le istruzioni effettivamente caricate utilizzare `/context`.

La distinzione fondamentale è:

- **`CLAUDE.md`**: istruzioni esplicite per il comportamento nel progetto o nell’ambiente dell’utente.
- **Auto memory**: note che Claude gestisce per ricordare informazioni utili tra sessioni.

La posizione predefinita della auto memory è `~/.claude/projects/<project>/memory/`, con un indice `MEMORY.md` e file tematici. Il riferimento corrente indica che all’avvio vengono caricati i primi **200 righe o 25 KB** dell’indice, secondo il limite raggiunto per primo. I file tematici sono letti quando pertinenti. Il limite non va esteso per analogia ai file `CLAUDE.md`.

Disabilitare auto memory e cancellare i file già salvati sono operazioni diverse. Se si vuole rimuovere una nota, occorre editarla o eliminarla esplicitamente. Se si vuole una regola nel `CLAUDE.md`, è meglio chiedere esplicitamente di aggiungerla a quel file, oppure editarlo via `/memory`.

Esempi di richieste in linguaggio naturale, non di nuovi comandi slash:

```text
Ricorda che i test di integrazione richiedono un'istanza Redis locale.
Aggiungi a CLAUDE.md la regola di eseguire pytest prima di proporre il commit.
```

### 5.6 `/init`: costruire una base di istruzioni

`/init` esplora il progetto e genera un punto di partenza per `CLAUDE.md`. Il risultato va revisionato: comandi di test, struttura e convenzioni devono corrispondere davvero al repository.

È opportuno usarlo all’inizio e poi curare il file nel tempo. Non sostituisce la documentazione architetturale né garantisce che tutte le regole aziendali siano state inferite correttamente.

### 5.7 `/rewind`: tornare a un checkpoint

Il menu consente di ripristinare conversazione, codice o entrambi, oppure riassumere da un punto selezionato. Non è una transazione universale: effetti su servizi esterni, database e comandi shell non sono automaticamente annullati. Anche le modifiche non coperte dal tracciamento dei checkpoint richiedono strumenti appropriati.

Git resta lo strumento per versionare il codice e gestire commit, branch e collaborazioni. `/rewind` serve a recuperare punti del lavoro con Claude.

## 6. Configurazione, modelli e autorizzazioni

### Modello, effort e fast mode

| Esigenza | Comando | Interpretazione |
| --- | --- | --- |
| Scegliere il modello | `/model` | Cambia il modello disponibile all’account. |
| Regolare il ragionamento | `/effort` | Modifica il livello di effort supportato. |
| Attivare elaborazione veloce | `/fast on` | Usa fast mode dove previsto. |
| Consultare un secondo modello | `/advisor` | Configura il modello consulente. |
| Vedere consumi e limiti | `/usage` | Mostra indicatori del piano e della sessione. |

Esempi:

```text
/model sonnet
/effort high
/effort status
/usage
```

Più effort può richiedere più tempo e risorse. Fast mode non va descritto come sinonimo di riduzione dell’effort. I nomi e i livelli ammessi dipendono dal modello e dalla release: usare il selettore quando non si conoscono i valori validi.

### Permessi, pianificazione e sandbox

`/permissions` gestisce le regole per gli strumenti: allow, ask e deny, con scope diversi. `/plan` seleziona una modalità orientata all’analisi prima dell’implementazione. `/sandbox` controlla l’isolamento del processo sulle piattaforme supportate.

Sono livelli distinti: un sandbox non rende superflue le autorizzazioni e una modalità di pianificazione non sostituisce i controlli dell’infrastruttura. Se un’azione è bloccata, verificare la regola e il suo scope prima di modificare l’impostazione.

```text
/plan Definisci una strategia di migrazione dell'API senza iniziare l'implementazione.
/permissions
/config
```

`/update-config` è una skill che può modificare file di configurazione sulla base di una richiesta descrittiva. `/config` è il comando per preferenze e impostazioni supportate dal suo pannello o dalle coppie `key=value`.

### Directory e configurazione

`/add-dir ../documentazione` aggiunge accesso a una cartella. `/cd ../altro-progetto` cambia la directory principale mantenendo la conversazione. L’accesso a una cartella non implica che tutti i suoi plugin, hook, MCP e file di configurazione vengano importati.

Usare `/status`, `/memory` e `/context` per verificare l’ambiente effettivo dopo uno spostamento importante.

## 7. Sessioni e lavoro in parallelo

| Comando | Che cosa succede | Quando usarlo |
| --- | --- | --- |
| `/branch` | Si passa a una diramazione della conversazione. | Provare una strada alternativa. |
| `/fork` | Si crea una sessione background separata mantenendo questa aperta. | Avviare un lavoro indipendente. |
| `/subtask` | Si crea un subagente che restituisce risultati nella conversazione corrente. | Delegare un’attività laterale. |
| `/background` | La sessione corrente prosegue in background. | Liberare il terminale. |
| `/tasks` | Si osserva il lavoro background della sessione. | Monitorare agenti e shell. |
| `/resume` | Si riprende o si collega una conversazione esistente. | Tornare a un lavoro precedente. |
| `/stop` | Si ferma la sessione background destinataria. | Arrestare il lavoro. |

La separazione tra `/fork` e `/subtask` è particolarmente sensibile alla versione. Nelle release indicate dal riferimento corrente, `/fork` crea una sessione separata; in alcune release precedenti o con agent view disabilitata può invece creare un subagente.

Una conversazione separata non garantisce da sola isolamento dei file: verificare se le modifiche avvengono in un worktree dedicato o nella stessa directory. `/batch`, che è una skill, organizza appositamente unità di lavoro in worktree e può pubblicare risultati dopo l’approvazione del piano.

### Locale, desktop, remoto e cloud

- `/desktop` passa all’app desktop compatibile.
- `/remote-control` espone la sessione locale a un client remoto; il lavoro continua nell’ambiente locale.
- `/teleport` recupera una sessione cloud nel terminale.
- `/remote-env` sceglie l’ambiente per nuove sessioni cloud.

Per attività ricorrenti distinguere `/loop`, skill che lavora mentre la sessione è aperta, da `/schedule`, che configura routine cloud. Non promettere esecuzioni future persistenti sulla sola base di un loop locale.

## 8. Workflow pratici

Le sequenze seguenti sono esempi didattici. I comandi vanno inviati uno alla volta e le risposte controllate prima del passo successivo.

### 8.1 Primo ingresso in un repository

```text
/status
/init
/memory
/permissions
/mcp
```

Controllare prima l’ambiente, generare e revisionare le istruzioni, definire le autorizzazioni necessarie e verificare le integrazioni. `/mcp` serve solo se il progetto usa quei collegamenti.

### 8.2 Analisi di una modifica architetturale

```text
/rename LAS - Idempotenza delle richieste
/plan Progetta la gestione delle richieste duplicate nel Loan Application System.
/context
```

Prima dell’implementazione verificare contratto API, chiave di idempotenza, persistenza, timeout e risposta al cliente. Approvato il piano, proseguire nel flusso di implementazione previsto dall’interfaccia.

### 8.3 Conversazione lunga

```text
/context
/compact Conserva i requisiti LAS, le decisioni sulla coda, i file modificati e i test ancora falliti.
/context
```

Il confronto aiuta a capire lo spazio liberato. Per cambiare completamente argomento utilizzare invece `/clear` e riprendere il lavoro precedente con `/resume` quando serve.

### 8.4 Revisione prima della consegna

```text
/diff
/code-review high
/security-review
/verify
```

La revisione visiva, la ricerca di bug, l’analisi sicurezza e l’osservazione dell’app verificano aspetti diversi. `/code-review` e `/verify` sono skill; `/security-review` richiede un riferimento valido al branch predefinito di origin. Per applicare automaticamente findings di code review esiste `--fix`; per pubblicare commenti esiste `--comment`. Questi flag introducono azioni ulteriori rispetto alla sola lettura.

### 8.5 Chiudere lasciando traccia

```text
/rename LAS - Analisi completata
/export sessione-LAS.txt
/usage
/exit
```

L’export della conversazione non è un backup del repository, dei file modificati o delle integrazioni. Salvare separatamente gli artefatti necessari alla consegna.

### 8.6 Diagnosticare un problema

```text
/status
/release-notes
/doctor
/debug Il collegamento MCP si interrompe dopo l'autenticazione.
```

`/doctor` può proporre modifiche da confermare. `/debug` raccoglie log da quando è attivato. Usare `/bug` o `/feedback` se occorre una segnalazione, controllando nel dialogo quali dati saranno inclusi.

## 9. Alias e compatibilità

### Alias nel riferimento consultato

| Alias | Comando di riferimento |
| --- | --- |
| `/reset`, `/new` | `/clear` |
| `/settings` | `/config` |
| `/allowed-tools` | `/permissions` |
| `/checkpoint`, `/undo` | `/rewind` |
| `/quit` | `/exit` |
| `/bg` | `/background` |
| `/continue` | `/resume` |
| `/rc` | `/remote-control` |
| `/tp` | `/teleport` |
| `/app` | `/desktop` |
| `/ios`, `/android` | `/mobile` |
| `/peers` | `/list-agents` |
| `/bashes` | `/tasks` |
| `/routines` | `/schedule` |
| `/proactive` | `/loop` |
| `/checkup` | `/doctor` |
| `/review` | `/code-review` |
| `/cost`, `/stats` | `/usage`; `/stats` seleziona la scheda Stats |
| `/share` | `/bug` |
| `/ultrareview` | Forma alternativa della revisione `/code-review ultra` |

### Cambiamenti da non ignorare

- `/vim` è stato rimosso in v2.1.92: usare Editor mode in `/config`.
- `/pr-comments` è stato rimosso in v2.1.91: chiedere a Claude di leggere i commenti della PR.
- `/ultraplan` è rimosso nel riferimento corrente: usare plan mode.
- `/extra-usage` è il nome precedente della funzione ora documentata come `/usage-credits`.
- `/agents` non apre più il vecchio gestore interattivo nel comportamento corrente documentato.
- `/review`, `/fork`, `/cost` e `/stats` hanno avuto comportamenti differenti nel tempo.

Un elenco trovato in un articolo storico può essere corretto per quella versione e sbagliato per quella attuale. Per una guida interna di team annotare la release installata con `claude --version` e verificare il menu locale.

## 10. Problemi comuni

### “Unknown command”

Controllare nome, posizione all’inizio del messaggio, versione, piano, provider e policy. Se è una skill personale, verificarne posizione e nome, poi eseguire `/reload-skills`. Se proviene da un plugin, controllare `/plugin` e l’eventuale necessità di `/reload-plugins`.

Un comando documentato può essere assente perché non disponibile all’account. Un comando nascosto può invece funzionare digitando il nome completo: l’assenza dal menu non distingue da sola questi due casi.

### “Ho fatto `/clear`, ma Claude ricorda ancora le regole”

È coerente: la nuova conversazione ricarica le istruzioni pertinenti e può utilizzare memorie persistenti. `/clear` azzera il contesto della conversazione, non i file di memoria.

### “`/memory` mostra un file: allora è tutto nel contesto?”

Non necessariamente. Il menu può includere posizioni candidate o file non ancora creati. `/context` serve a controllare le istruzioni caricate; l’indice auto memory ha inoltre limiti di lettura e i file tematici sono richiamati quando utili.

### “`/rewind` ha annullato anche il deploy?”

Non dedurlo. I checkpoint non sono un rollback generale di effetti esterni. Per deployment, database e servizi occorrono le rispettive procedure di ripristino.

### “Posso usare tutto con `claude -p`?”

No. La modalità non interattiva non dispone automaticamente dei dialoghi terminali. Alcuni comandi supportano forme testuali, altri no. Il riferimento headless documenta, tra gli altri, argomenti espliciti per `/model`, `/effort`, `/fast`, `/color`, `/rename`, coppie `key=value` per `/config` e riepilogo testuale per `/mcp`. La disponibilità varia con versione e comando; non trasporre ogni esempio interattivo in `-p`.

### “Un comando slash non costa token?”

Non è una regola generale. Un menu o una visualizzazione di stato differiscono da compattazione, revisione, ricerca e generazione. Le skill orchestrano lavoro del modello; alcune funzioni cloud possono utilizzare crediti. `/usage` mostra gli indicatori disponibili, ma non è un preventivo universale per ogni comando.

## 11. Scheda rapida

| Obiettivo | Prima scelta |
| --- | --- |
| Scoprire i comandi | `/help` oppure `/` |
| Verificare versione e account | `/status` |
| Avviare istruzioni di progetto | `/init` |
| Gestire istruzioni e auto memory | `/memory` |
| Vedere occupazione del contesto | `/context` |
| Proseguire liberando contesto | `/compact` |
| Iniziare un’altra conversazione | `/clear` |
| Recuperare una conversazione | `/resume` |
| Pianificare un cambiamento | `/plan` |
| Cambiare modello | `/model` |
| Regolare ragionamento | `/effort` |
| Controllare consumi | `/usage` |
| Gestire autorizzazioni | `/permissions` |
| Gestire server MCP | `/mcp` |
| Ispezionare modifiche | `/diff` |
| Cercare bug | `/code-review` — skill |
| Semplificare codice | `/simplify` — skill |
| Verificare l’app in esecuzione | `/verify` — skill |
| Monitorare lavoro background | `/tasks` |
| Ripristinare un checkpoint | `/rewind` |
| Esportare la conversazione | `/export` |
| Diagnosticare configurazione | `/doctor` — skill |

## 12. Fonti ufficiali

Fonti consultate per questa guida, con riferimento alla documentazione disponibile il 14 ottobre 2026:

1. [Commands — riferimento completo](https://code.claude.com/docs/en/commands): repertorio, sintassi, classificazione, alias, disponibilità e note di versione. È la fonte principale delle tabelle.
2. [Commands — versione Markdown](https://code.claude.com/docs/en/commands.md): testo ufficiale usato per controllare la copertura delle voci del repertorio.
3. [Interactive mode](https://code.claude.com/docs/en/interactive-mode): modalità interattiva, menu, prefissi e comportamento durante il lavoro.
4. [Memory — versione Markdown](https://code.claude.com/docs/en/memory.md): `/memory`, istruzioni, auto memory, indice e limiti di caricamento.
5. [Extend Claude with skills](https://code.claude.com/docs/en/skills): skill incluse, personalizzazioni e compatibilità con `.claude/commands/`.
6. [Run Claude Code programmatically](https://code.claude.com/docs/en/headless): differenze della modalità non interattiva.

I rimandi tematici inseriti nel riferimento Commands permettono di approfondire permessi, sandbox, checkpoint, sessioni, routine, workflow e integrazioni. Per una specifica installazione fanno fede la sua versione, il menu effettivamente disponibile e le policy applicate.
