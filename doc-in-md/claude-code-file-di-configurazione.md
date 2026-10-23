# I file di configurazione locale di Claude Code

> Riferimento completo, verificato sulla documentazione ufficiale (code.claude.com/docs) in data **20 ottobre 2026**.
> Nota: Claude Code evolve rapidamente; alcuni dettagli (percorsi, chiavi, versioni minime) possono cambiare tra una release e l'altra.

---

## 1. Premessa: livelli e formati

### 1.1 I quattro livelli (*scope*)

Il **livello** (in inglese *scope*) indica a chi e a cosa si applica una configurazione. Claude Code ne prevede quattro:

1. **Gestito / enterprise** (*managed*): imposto dall'organizzazione su tutte le macchine; il singolo sviluppatore non può scavalcarlo, salvo poche eccezioni di sicurezza in cui vale comunque il valore *più restrittivo*.
2. **Utente** (*user/global*): vale per la persona, in **tutti** i progetti sulla macchina. Vive in `~/.claude/`.
3. **Progetto condiviso** (*project*): vale per **chiunque** lavori in quella cartella di progetto; si committa in git per condividerlo col team. Vive in `.claude/` dentro il progetto (o alla radice, per alcuni file).
4. **Progetto locale** (*project local*): vale solo per la persona, solo in quel progetto; resta fuori da git.

### 1.2 I formati

- **JSON** (JavaScript Object Notation): formato dati a coppie chiave/valore. Claude Code usa JSON *stretto*: commenti `//` e virgole finali sono errori di sintassi e il file viene segnalato come rotto ("Settings Error") all'avvio.
- **Markdown con frontmatter YAML**: file di testo `.md` con contenuto in linguaggio naturale, preceduto in testa da un blocco di metadati delimitato da `---` scritto in YAML (formato `chiave: valore`). È il formato di CLAUDE.md, skill, agenti, comandi, regole e stili di output.

### 1.3 Nota per Windows

Su Windows `~/.claude` corrisponde a `%USERPROFILE%\.claude`. La variabile d'ambiente `CLAUDE_CONFIG_DIR` permette di spostare altrove l'intera cartella (impostazioni, cronologia, plugin).

---

## 2. Tabella riassuntiva

| File | Livello | Formato | Scopo in una riga |
|---|---|---|---|
| `managed-settings.json` (+ `managed-settings.d/`, `managed-mcp.json`, `CLAUDE.md` gestito) | Enterprise | JSON / Markdown | Policy e istruzioni imposte dall'organizzazione |
| `~/.claude/settings.json` | Utente | JSON | Impostazioni personali per tutti i progetti |
| `.claude/settings.json` | Progetto condiviso | JSON | Impostazioni di team (committate) |
| `.claude/settings.local.json` | Progetto locale | JSON | Override personali per un progetto (gitignorato) |
| `~/.claude.json` | Utente | JSON | Stato dell'app: OAuth, trust, server MCP personali |
| `CLAUDE.md` (radice o `.claude/`) | Progetto | Markdown | Istruzioni di progetto caricate a ogni sessione |
| `CLAUDE.local.md` | Progetto locale | Markdown | Istruzioni private per quel progetto |
| `~/.claude/CLAUDE.md` | Utente | Markdown | Istruzioni personali globali |
| `AGENTS.md` | Progetto | Markdown | Istruzioni "standard" per agenti AI, letto al posto di CLAUDE.md |
| `.claude/rules/*.md`, `~/.claude/rules/*.md` | Progetto / Utente | MD + frontmatter | Regole per argomento, anche condizionate ai percorsi dei file |
| `skills/<nome>/SKILL.md` | Progetto / Utente | MD + frontmatter | Competenze riusabili invocate con `/nome` o da Claude |
| `commands/*.md` | Progetto / Utente | MD + frontmatter | Comandi slash a file singolo (meccanismo ora unificato con le skill) |
| `agents/*.md` | Progetto / Utente | MD + frontmatter | Subagenti con prompt, strumenti e modello propri |
| `output-styles/*.md` | Utente / Progetto | MD + frontmatter | Stili di output che cambiano il comportamento di base |
| `workflows/*.js` | Progetto / Utente | JavaScript | Script che orchestrano più subagenti (`/nome`) |
| `agent-memory/` (3 varianti) | Progetto / Utente | Markdown | Memoria persistente dei subagenti |
| `.mcp.json` | Progetto (radice) | JSON | Server MCP condivisi col team |
| `~/.claude/keybindings.json` | Utente | JSON | Scorciatoie da tastiera personalizzate |
| `~/.claude/themes/*.json` | Utente | JSON | Temi colore personalizzati |
| `.worktreeinclude` | Progetto (radice) | testo (sintassi `.gitignore`) | File gitignorati da copiare nei worktree |
| `~/.claude/projects/<prog>/memory/` | Utente (per progetto) | Markdown | Auto-memory: appunti che Claude scrive da sé |

---

## 3. I file di impostazioni (*settings*) — ciò che Claude Code **applica**

Questi file contengono configurazioni *vincolanti*: permessi, hook, variabili d'ambiente. A differenza di CLAUDE.md (guida testuale che Claude "legge"), queste impostazioni vengono fatte rispettare dal programma stesso.

### 3.1 Le chiavi principali (uguali a tutti i livelli)

- **`permissions`**: regole `allow` / `ask` / `deny` su strumenti e comandi, con pattern — es. `"Bash(npm test *)"`, `"Read(./.env)"`, `"WebFetch(domain:...)"`, `"mcp__<server>__<tool>"`. Include anche `defaultMode` (modalità di permesso predefinita, es. *plan*) e `additionalDirectories`.
- **`hooks`**: script propri eseguiti a eventi precisi della sessione. Gli hook **non hanno un file proprio**: si configurano qui (struttura: evento → *matcher* → handler). Eventi principali: `PreToolUse` e `PostToolUse` (prima/dopo una chiamata a strumento), `UserPromptSubmit`, `Stop`, `SubagentStop`, `SessionStart`, `SessionEnd`, `PreCompact`, `Notification`, `ConfigChange`, `WorktreeCreate` — in totale gli eventi disponibili sono ormai oltre trenta. Oltre al tipo `command` esistono handler `http`, `mcp_tool`, `prompt` e `agent`. Interruttori collegati: `disableAllHooks`, `allowManagedHooksOnly`.
- **`env`**: variabili d'ambiente impostate in ogni sessione.
- **`model`**: modello predefinito.
- **`statusLine`**: personalizza la riga di stato in fondo al terminale, tipicamente puntando a un comando/script che la genera — es. `{"type": "command", "command": "~/.claude/statusline.sh"}`. Esiste anche `subagentStatusLine`.
- **`outputStyle`**: seleziona uno stile da `output-styles/`.
- **`sandbox`**: isolamento dei comandi — es. `enabled`, scritture consentite sul filesystem (`filesystem.allowWrite`), domini di rete ammessi/negati (`network.allowedDomains` / `deniedDomains`), comandi esclusi.
- **`claudeMdExcludes`**: glob che escludono determinati CLAUDE.md dal caricamento.
- **`enabledPlugins`** ed **`extraKnownMarketplaces`**: plugin attivi e marketplace aggiuntivi; `pluginConfigs` per la configurazione dei singoli plugin.
- **`cleanupPeriodDays`** (e `desktopSessionCleanupPeriodDays`): retention dei dati di sessione.
- **`$schema`**: puntando a `https://json.schemastore.org/claude-code-settings.json` si ottengono autocompletamento e validazione in VS Code.

### 3.2 `managed-settings.json` — livello enterprise

- **Percorsi** (file di sistema, varia per OS):
  - macOS: `/Library/Application Support/ClaudeCode/managed-settings.json`
  - Linux e WSL: `/etc/claude-code/managed-settings.json`
  - Windows: `C:\Program Files\ClaudeCode\managed-settings.json` — **attenzione**: il vecchio percorso `C:\ProgramData\ClaudeCode\` **non viene più letto**.
- **Significato**: policy di sicurezza e conformità che nessun file personale, di progetto o flag `--settings` può scavalcare.
- **Nella stessa cartella** possono esserci anche:
  - `managed-settings.d/` — directory di file JSON aggiuntivi, fusi in ordine alfabetico dopo il file principale (utile quando più team gestiscono parti diverse della policy; nomi con prefisso numerico per controllare l'ordine);
  - `managed-mcp.json` — server MCP imposti dall'organizzazione;
  - `CLAUDE.md` **gestito** — istruzioni caricate a ogni sessione su tutte le macchine (vedi § 4.4).
- **Altre vie di distribuzione** delle policy gestite:
  - *server-managed settings*: scaricate dalla console di amministrazione claude.ai (o da un gateway self-hosted), verificate all'avvio e ogni ora; copia cache locale in `~/.claude/remote-settings.json`;
  - su macOS: profilo di configurazione MDM con dominio `com.anthropic.claudecode` (stesse chiavi del JSON, come plist);
  - su Windows: registro di sistema, chiave `HKLM\SOFTWARE\Policies\ClaudeCode`, valore `Settings` contenente il JSON.
- **Combinazione di più fonti gestite**: il comportamento predefinito è *first-wins* (vale la prima fonte nella gerarchia); dalla v2.1.242 è disponibile la fusione con `managedSourcesBehavior: merge`.
- **Chiavi tipiche solo gestite**: `allowManagedPermissionRulesOnly`, `allowManagedHooksOnly`, `managedMcpServers`, `claudeMd`, `forceLoginMethod`, `wslInheritsWindowsSettings`.

### 3.3 `~/.claude/settings.json` — livello utente

- **Significato**: le proprie impostazioni predefinite per tutti i progetti: permessi che si concedono sempre (es. `Bash(git log *)`), modello preferito, hook di notifica, tema. Claude Code lo crea da sé la prima volta che si cambia un'opzione dal menù `/config`.

### 3.4 `.claude/settings.json` — livello progetto condiviso

- **Significato**: la configurazione di squadra: permessi, hook, plugin e variabili d'ambiente che il progetto richiede. Si **committa in git** così ogni collega che clona il repository la riceve.
- **Nota di sicurezza**: le regole `allow`, `additionalDirectories` e la maggior parte di `env` da questo file entrano in vigore solo dopo che ciascuna persona ha dato fiducia alla cartella (*workspace trust*); le regole `deny` e `ask` valgono subito. Alcune chiavi (scope "User", "Managed", "Global config") non hanno mai effetto da un file di repository.

### 3.5 `.claude/settings.local.json` — livello progetto locale

- **Significato**: gli override personali per quel singolo progetto, con precedenza sul file condiviso. È anche il file in cui Claude Code **scrive da solo** quando a un prompt di permesso si risponde "Sì, e non chiedere più".
- La prima volta che lo scrive, Claude Code lo aggiunge automaticamente agli esclusi globali di git; se lo si crea a mano, va messo in `.gitignore` da sé.
- In un repository git, dalla v2.1.211 il file vive **alla radice del repository**, non nella sottocartella da cui si è avviato Claude Code.

### 3.6 `~/.claude.json` — stato globale dell'applicazione

Da non confondere con `~/.claude/settings.json` (nome simile, ruolo diverso). È un file che **Claude Code gestisce per sé** e che di norma non va modificato a mano:

- sessione di accesso (OAuth);
- **server MCP personali**: quelli aggiunti con `claude mcp add --scope user` (chiave `mcpServers` al livello più alto, validi in tutti i progetti) e quelli `--scope local` (sotto `projects["<percorso>"].mcpServers`, per un progetto ma non condivisi);
- stato per progetto sotto la chiave `projects`: decisioni di fiducia (*trust*), metriche dell'ultima sessione;
- le opzioni "global config" scritte da `/config` e interruttori dell'interfaccia (es. `autoConnectIde`, `diffTool`).

Se il file si corrompe, Claude Code ne conserva copie di backup (le cinque più recenti) in `~/.claude/backups/`.

---

## 4. I file di istruzioni ("memoria") — ciò che Claude **legge come guida**

### 4.1 `CLAUDE.md` (radice del progetto, oppure `.claude/CLAUDE.md`)

- **Formato**: Markdown libero.
- **Significato**: le istruzioni di progetto caricate nel contesto **all'inizio di ogni sessione**: convenzioni del team, comandi di build/test/lint, architettura, regole di stile.
- **Consigli ufficiali**: tenerlo sotto le ~200 righe (file più lunghi vengono comunque caricati ma l'aderenza cala); modificarlo da dentro la sessione con `/memory`.
- Si committa.

### 4.2 `CLAUDE.local.md` (radice del progetto)

- **Significato**: la variante **privata** di CLAUDE.md: preferenze personali per quel progetto, caricate accanto al CLAUDE.md condiviso, subito dopo di esso. Va creato a mano e aggiunto a `.gitignore` da sé. È supportato (non deprecato).

### 4.3 `~/.claude/CLAUDE.md` (utente)

- **Significato**: istruzioni personali valide ovunque (stile di risposta, formato dei commit, convenzioni proprie). Viene caricato insieme a quello di progetto; in caso di conflitto prevalgono le istruzioni di progetto. Da tenere corto, perché pesa sul contesto di ogni sessione.

### 4.4 CLAUDE.md gestito (enterprise)

- **Percorsi**: `/Library/Application Support/ClaudeCode/CLAUDE.md` (macOS), `/etc/claude-code/CLAUDE.md` (Linux/WSL), `C:\Program Files\ClaudeCode\CLAUDE.md` (Windows).
- **Significato**: istruzioni distribuite dall'organizzazione e caricate a ogni sessione su tutte le macchine. Collegata c'è la chiave `claudeMd`, valida solo nelle impostazioni gestite.

### 4.5 `AGENTS.md`

- **Significato**: formato "neutro" di istruzioni per agenti di coding adottato da più strumenti. Claude Code (v2.1.277+) lo legge **al posto** di CLAUDE.md, ma **solo se** nella cartella di lavoro (o sopra) non esiste già un CLAUDE.md o CLAUDE.local.md. Il comportamento è configurabile su tre modalità: `claude-md-or-agents-md` (predefinita), `claude-md-and-agents-md` (entrambi), `managed-only`.

### 4.6 Ordine di caricamento e import

- I CLAUDE.md vengono **concatenati** (non fusi chiave per chiave) partendo dalla radice del filesystem fino alla cartella di lavoro; nella stessa cartella, CLAUDE.local.md segue CLAUDE.md. I CLAUDE.md presenti in sottocartelle vengono invece letti **su richiesta**, quando Claude lavora su file lì dentro.
- Gli import con la sintassi `@percorso/file` includono altri file, fino a **4 livelli** di profondità.
- Logica diversa dai settings: utente e progetto vengono **entrambi caricati** nel contesto, con priorità alle istruzioni di progetto in caso di conflitto.

### 4.7 `.claude/rules/*.md` e `~/.claude/rules/*.md` — le "regole"

- **Formato**: Markdown con frontmatter YAML opzionale (campo `paths`).
- **Significato**: istruzioni spezzate per argomento (es. `testing.md`, `api-design.md`), alternativa modulare a un CLAUDE.md che cresce troppo.
- **La novità è `paths:`**: una regola **senza** `paths` si carica a inizio sessione come CLAUDE.md; una regola **con** `paths` (elenco di glob, es. `**/*.test.ts`) si carica **solo quando** Claude legge, scrive o modifica un file corrispondente — così il contesto non si riempie di regole irrilevanti. Le sottocartelle (es. `rules/frontend/react.md`) vengono scoperte automaticamente.

```markdown
---
paths:
  - "**/*.test.ts"
---
# Regole di testing
- Nomi descrittivi: "should [atteso] when [condizione]"
```

### 4.8 Auto-memory: `~/.claude/projects/<progetto>/memory/`

- **Significato**: gli **appunti che Claude scrive da sé** sessione dopo sessione (comandi di build scoperti, insidie di debug, note di architettura). Attiva per default; si gestisce con `/memory` o con la chiave `autoMemoryEnabled`.
- `MEMORY.md` è l'indice caricato a ogni avvio (prime 200 righe, max 25 KB); i file tematici (es. `debugging.md`) vengono letti solo quando servono. Sono semplici Markdown: si possono leggere, correggere o cancellare.

### 4.9 Nota: `.claudeignore` non esiste

Un'idea diffusa ma errata: un file `.claudeignore` **non ha alcun effetto**. Per impedire la lettura di percorsi sensibili si usano le regole `deny` sui permessi, es. `Read(./secrets/**)`.

---

## 5. I file di estensione (quasi tutti Markdown + frontmatter YAML)

Ognuno esiste in doppia versione: in `.claude/<cartella>/` del progetto (condiviso, committato) e in `~/.claude/<cartella>/` (personale, ovunque). A parità di nome prevale la versione di progetto.

### 5.1 `skills/<nome>/SKILL.md` — le skill

- **Significato**: una "competenza" riusabile: una cartella con un file `SKILL.md` (istruzioni + frontmatter) più eventuali file di supporto (checklist, template, script). Si invoca digitando `/nome argomenti` oppure la invoca Claude da sé quando il compito corrisponde alla `description` del frontmatter.
- **Campi frontmatter notevoli**: `description` (decide l'auto-invocazione), `disable-model-invocation: true` (solo invocazione umana, es. `/deploy`), `user-invocable: false` (nascosta dal menù `/`), `allowed-tools`, `model`, `argument-hint`.
- Nel corpo, `$ARGUMENTS` sostituisce ciò che si è digitato dopo il nome (con `$0`, `$1`… per gli argomenti posizionali), e la sintassi `` !`comando` `` esegue un comando di shell iniettandone l'output nel prompt.

### 5.2 `commands/*.md` — i comandi slash

- **Significato**: la versione "a file singolo" delle skill: `commands/fix-issue.md` crea `/fix-issue`. La documentazione attuale precisa che **comandi e skill sono ormai lo stesso meccanismo**: per i nuovi flussi si consiglia di usare le skill (che permettono di allegare file di supporto); i file comando esistenti continuano a funzionare. A parità di nome, vince la skill.

### 5.3 `agents/*.md` — i subagenti

- **Significato**: ogni file definisce un **subagente**, cioè un agente specializzato che gira in una finestra di contesto propria, separata dalla conversazione principale (utile per compiti isolati o paralleli, es. revisione del codice in sola lettura).
- **Frontmatter**: `name` e `description` obbligatori ("description" dice a Claude quando delegargli il lavoro); poi `tools` (limitare gli strumenti, es. solo Read/Grep/Glob), `model`, `permissionMode`, `memory`, `maxTurns`, `isolation` e altri. Il corpo del file diventa il suo system prompt.
- **Conflitti di nome** (priorità, dal più alto): impostazioni gestite → flag `--agents` → `.claude/agents/` di progetto → `~/.claude/agents/` utente → `agents/` dei plugin.

### 5.4 `output-styles/*.md` — gli stili di output

- **Significato**: insiemi di istruzioni che **sostituiscono** (o, con `keep-coding-instructions: true`, affiancano) le istruzioni di base di Claude Code, per adattarlo a modalità diverse: insegnamento, revisione, usi non di coding.
- Stili incorporati: Default, Proactive, Concise, Explanatory, Learning; quelli personali vanno in `~/.claude/output-styles/`. Si selezionano con `/output-style` o con la chiave `outputStyle` dei settings.

### 5.5 `workflows/*.js` — i workflow dinamici

- **Significato** (funzionalità recente): script **JavaScript** che orchestrano molti subagenti; ogni file diventa un comando `/<nome>`. Non si scrivono a mano: li genera Claude e si salvano da `/workflows`. Un workflow di progetto prevale su uno personale omonimo.

### 5.6 `agent-memory/` — memoria persistente dei subagenti

- **Significato**: i subagenti con il campo `memory:` nel frontmatter mantengono un proprio `MEMORY.md` tra una esecuzione e l'altra.
- Tre destinazioni a seconda del valore: `memory: project` → `.claude/agent-memory/<nome>/` (committata, condivisa col team); `memory: local` → `.claude/agent-memory-local/` (fuori da git); `memory: user` → `~/.claude/agent-memory/` (personale, tra tutti i progetti). È distinta dall'auto-memory della sessione principale (§ 4.8).

---

## 6. Server MCP (Model Context Protocol)

MCP è il protocollo con cui Claude si collega a strumenti esterni (database, API, browser…). La configurazione ha **tre scope principali**:

- **`.mcp.json`** — alla **radice del progetto** (non dentro `.claude/`), formato JSON con la chiave `mcpServers`. Sono i server condivisi col team, committati. Per i segreti si usano riferimenti a variabili d'ambiente (`${NOTION_TOKEN}`, anche con default `${VAR:-valore}`), così il token non finisce nel file.
- **Scope `user` e `local`** — memorizzati dentro **`~/.claude.json`** (si aggiungono con `claude mcp add --scope user/local`): rispettivamente server personali validi ovunque, e server personali limitati a un progetto ma non condivisi.
- **`managed-mcp.json`** — nella cartella delle impostazioni gestite: server imposti dall'organizzazione (o chiave `managedMcpServers`).

**Conflitti di nome** tra server omonimi (priorità, dal più alto): local → project → user → plugin → connettori claude.ai.

```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "@notionhq/notion-mcp-server"],
      "env": { "NOTION_TOKEN": "${NOTION_TOKEN}" }
    }
  }
}
```

---

## 7. Interfaccia del terminale (solo livello utente)

- **`~/.claude/keybindings.json`** (JSON): rimappa le scorciatoie da tastiera della CLI interattiva; si crea con `/keybindings`, ha un proprio schema, viene ricaricato a caldo. Un valore `null` rimuove una scorciatoia. Ctrl+C, Ctrl+D, Ctrl+M e Bloc Maiusc sono riservati.
- **`~/.claude/themes/*.json`** (JSON): temi colore personalizzati — un preset `base` (dark/light) più una mappa `overrides` di token colore. Si creano con `/theme`.

---

## 8. Altri file a livello di progetto

- **`.worktreeinclude`** (radice del progetto, sintassi tipo `.gitignore`): elenca i file *gitignorati* (es. `.env`) da copiare nei nuovi **worktree** — i checkout paralleli dello stesso repository che Claude crea per lavorare in isolamento (`--worktree` o subagenti isolati): essendo checkout freschi, i file non tracciati altrimenti mancherebbero. Funziona solo con git.

---

## 9. File che Claude Code scrive da sé (dati, non configurazione)

Sotto `~/.claude/` vivono anche dati applicativi, **in chiaro** (la sola protezione sono i permessi del filesystem — punto rilevante per la sicurezza):

| Percorso | Contenuto |
|---|---|
| `projects/<progetto>/<sessione>.jsonl` | Trascrizioni complete delle sessioni (messaggi, chiamate a strumenti e relativi output — inclusi eventuali segreti letti o stampati) |
| `history.jsonl` | Ogni prompt digitato (richiamo con freccia su, Ctrl+R) |
| `.credentials.json` | Credenziali di accesso — **da non toccare** |
| `plugins/` | Marketplace clonati, versioni installate, `installed_plugins.json` — **da non cancellare** |
| `file-history/` | Snapshot pre-modifica per il ripristino dei checkpoint |
| `backups/` | Copie di sicurezza di `~/.claude.json` |
| `remote-settings.json` | Cache delle impostazioni gestite dal server |
| `shell-snapshots/`, `plans/`, `debug/`, `paste-cache/`, `tasks/`, `stats-cache.json`, … | Altri dati di sessione e cache |

- Le trascrizioni e gli altri dati di sessione vengono ripuliti dopo **`cleanupPeriodDays`** (default 30 giorni, minimo 1); per le sessioni di Claude Desktop/Cowork vale `desktopSessionCleanupPeriodDays`.
- **`claude purge <percorso>`** cancella lo stato di un singolo progetto (trascrizioni, auto-memory, voce in `~/.claude.json`, righe di cronologia); `--dry-run` mostra prima il piano.
- Per non scrivere affatto trascrizioni e cronologia: variabile `CLAUDE_CODE_SKIP_PROMPT_HISTORY`, oppure `--no-session-persistence` insieme a `-p`.

---

## 10. Ordine di precedenza delle impostazioni

Quando la stessa chiave compare in più file, vince il livello più alto:

1. **Impostazioni gestite** (file di sistema, MDM/registro o console claude.ai) — insuperabili, salvo rare eccezioni in cui vale comunque il valore *più restrittivo* da qualunque livello;
2. **Riga di comando** (`--settings`, per quella sola sessione);
3. **`.claude/settings.local.json`** (progetto locale);
4. **`.claude/settings.json`** (progetto condiviso);
5. **`~/.claude/settings.json`** (utente).

Tre sfumature da ricordare:

- le chiavi **a lista** (come `permissions.allow`) **si fondono** tra i livelli invece di sovrascriversi (salvo `allowManagedPermissionRulesOnly`), mentre le chiavi scalari (come `model`) prendono il valore del livello più alto;
- le **variabili d'ambiente** non sono un livello della pila: per ciascuna coppia variabile/chiave la documentazione dice quale prevale (es. `ANTHROPIC_MODEL` vince su `model` da qualunque file);
- per **CLAUDE.md** la logica è diversa: i file dei vari livelli vengono tutti caricati e concatenati, non fusi chiave per chiave (§ 4.6).

---

## 11. Cosa versionare in git

- **Da committare**: `CLAUDE.md`, `.claude/settings.json`, `.mcp.json`, `.worktreeinclude`, `rules/`, `skills/`, `commands/`, `agents/`, `workflows/`, `output-styles/` di progetto, `agent-memory/`.
- **Da tenere fuori**: `.claude/settings.local.json` (Claude Code lo esclude da sé quando lo crea lui), `CLAUDE.local.md`, `.claude/agent-memory-local/`, e naturalmente tutto ciò che sta in `~/.claude/` e `~/.claude.json`.

---

## 12. Variabili d'ambiente legate ai file

| Variabile | Effetto |
|---|---|
| `CLAUDE_CONFIG_DIR` | Sposta l'intera cartella `~/.claude` (impostazioni, cronologia, plugin) in un'altra directory |
| `CLAUDE_CODE_PROJECT_DIR_NAME` | (v2.1.234+, con `CLAUDE_CONFIG_DIR`) Nome della cartella progetto sotto `projects/`: fa condividere a più progetti la stessa auto-memory |
| `CLAUDE_CODE_TMPDIR` | Sposta l'albero temporaneo (scratchpad di sessione, immagini incollate) |
| `CLAUDE_CODE_SKIP_PROMPT_HISTORY` | Non scrive trascrizioni né cronologia dei prompt (riservatezza) |
| `CLAUDE_CODE_DISABLE_AUTO_MEMORY` | Disattiva l'auto-memory |
| `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` | Carica i CLAUDE.md anche dalle directory aggiunte con `--add-dir` |

---

## 13. Comandi diagnostici

- **`/status`**: elenca le fonti di impostazioni caricate nella sessione (riga *Setting sources*), incluse quelle gestite e come sono arrivate;
- **`/config`**: modifica le opzioni personali dall'interno della sessione;
- **`claude doctor`**: dettaglia errori e voci scartate nei file di impostazioni;
- **`/doctor prompt-audit`**: verifica le dimensioni di CLAUDE.md, AGENTS.md, regole, skill e subagenti (cosa pesa sul contesto);
- **`/memory`**: apre e modifica CLAUDE.md e l'auto-memory;
- **`claude --debug`** e **`/debug`**: log diagnostici di sessione.

---

## 14. Fonti (documentazione ufficiale)

- Settings files and precedence — <https://code.claude.com/docs/en/settings>
- All settings (reference) — <https://code.claude.com/docs/en/settings-reference>
- Explore the .claude directory — <https://code.claude.com/docs/en/claude-directory>
- Deploy managed settings — <https://code.claude.com/docs/en/managed-settings>
- Manage Claude's memory — <https://code.claude.com/docs/en/memory>
- Configure permissions — <https://code.claude.com/docs/en/permissions>
- Hooks — <https://code.claude.com/docs/en/hooks>
- MCP — <https://code.claude.com/docs/en/mcp>
- Subagents — <https://code.claude.com/docs/en/sub-agents>
- Skills — <https://code.claude.com/docs/en/skills>
- Output styles — <https://code.claude.com/docs/en/output-styles>
- Environment variables — <https://code.claude.com/docs/en/env-vars>
