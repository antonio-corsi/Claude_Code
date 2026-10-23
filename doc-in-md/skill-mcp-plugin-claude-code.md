# Skill, server MCP e plugin in Claude Code

> **Nota di versione.** I contenuti di questo documento sono stati verificati sulla documentazione ufficiale di Claude Code (code.claude.com/docs) il **21 ottobre 2026** (versioni 2.1.x). Claude Code evolve rapidamente: in caso di dubbio facciamo sempre fede ai link raccolti in fondo al documento.

Claude Code si può estendere in tre modi principali, che nella pratica vengono spesso confusi tra loro: le **skill**, i **server MCP** e i **plugin**. In questo documento li esaminiamo uno per uno — che cosa sono, come si configurano, quando usarli — e poi li mettiamo in relazione, perché è proprio nella combinazione dei tre che si ottiene il massimo.

---

## 1. Il quadro in trenta secondi

| Concetto | Risponde alla domanda | In una frase |
|---|---|---|
| **Skill** | *Come* si fa questa cosa? | Istruzioni e conoscenza procedurale che Claude carica solo quando servono |
| **Server MCP** | *A che cosa* può accedere Claude? | Un ponte verso sistemi esterni, che espone strumenti e dati |
| **Plugin** | Come *distribuiamo* il tutto? | Un pacchetto installabile che raggruppa skill, server MCP, hook e altri componenti |

La distinzione ufficiale tra i primi due, citata testualmente dalla documentazione:

> *"MCP connects Claude to external services. Skills extend what Claude knows, including how to use those services effectively."*

In altre parole: **MCP collega, le skill insegnano**. Il plugin, infine, è la scatola con cui consegniamo entrambi a un team.

---

## 2. Le skill

### 2.1 Che cosa sono

Una **skill** (per esteso *Agent Skill*) è una cartella che contiene un file obbligatorio, `SKILL.md`, più eventuali file di supporto. Il file `SKILL.md` è composto da due parti:

1. il **frontmatter**: un blocco di metadati in formato YAML (un formato testuale `chiave: valore`) racchiuso tra due righe `---` all'inizio del file;
2. il **corpo**: istruzioni in Markdown che spiegano a Claude come svolgere un certo compito.

Una skill **non aggiunge capacità nuove** a Claude Code: gli insegna a usare meglio gli strumenti che già possiede (shell, lettura e scrittura di file, ricerca web...). Possiamo pensarla come un manuale di procedura aziendale.

### 2.2 Anatomia di una skill

Vediamo un esempio in ambito bancario — una skill che standardizza la produzione del report mensile sui crediti deteriorati (in gergo **NPL**, *Non-Performing Loans*):

```markdown
---
name: report-npl
description: Genera il report mensile sui crediti deteriorati (NPL) nel formato
  standard dell'ufficio rischi. Usare quando viene chiesto un report NPL o
  un'analisi dei crediti deteriorati.
---

Per generare il report seguiamo questi passi:

1. Leggere i dati aggiornati da `data/npl.csv`.
2. Calcolare l'incidenza NPL per filiale (sofferenze / impieghi totali).
3. Eseguire i controlli di qualità con lo script `scripts/valida_dati.py`.
4. Produrre il report seguendo il modello in `templates/report.md`.
```

Punti da notare:

- **Tutti i campi del frontmatter sono opzionali.** Se omettiamo `name`, viene usato il nome della cartella; se omettiamo `description`, viene usata la prima riga non vuota del corpo. La `description` resta però fortemente raccomandata: è ciò che permette a Claude di capire *quando* attivare la skill.
- La cartella può contenere **file di supporto** (script, modelli, documenti di riferimento) richiamati con percorsi relativi. Gli script vengono *eseguiti*, non caricati nel contesto: una differenza importante per il consumo di token. Dentro gli script possiamo usare la variabile `${CLAUDE_SKILL_DIR}` per riferirci alla cartella della skill.
- La documentazione consiglia di tenere `SKILL.md` **sotto le 500 righe**: il materiale più voluminoso va nei file di supporto, da leggere solo quando serve.

### 2.3 I campi del frontmatter più utili

| Campo | Effetto |
|---|---|
| `name` | Nome della skill (default: nome della cartella) |
| `description` | Quando e perché usare la skill: guida l'attivazione automatica |
| `when_to_use` | Frasi di innesco aggiuntive, in appoggio alla `description` |
| `argument-hint` | Suggerimento sugli argomenti attesi quando la invochiamo a mano |
| `disable-model-invocation: true` | Solo invocazione manuale: Claude non la attiva mai da solo |
| `user-invocable: false` | L'inverso: solo Claude può attivarla, non compare tra i comandi |
| `context: fork` | La skill viene eseguita in un **subagente**, cioè un agente separato con un proprio contesto, che riporta solo il risultato |
| `allowed-tools` / `disallowed-tools` | Strumenti utilizzabili (o vietati) senza richieste di conferma durante l'esecuzione |
| `paths` | Caricamento automatico solo quando si lavora su file che corrispondono ai pattern indicati |

### 2.4 Come si attivano

Esistono due vie, non esclusive:

1. **Attivazione automatica** (*model-invoked*): Claude confronta la richiesta in corso con `description` e `when_to_use` di tutte le skill disponibili e carica il corpo di quella pertinente. Il meccanismo si chiama **progressive disclosure** (rivelazione progressiva): nel contesto risiedono stabilmente solo nome e descrizione — poche righe — mentre il corpo entra solo al momento del bisogno. È ciò che rende le skill economiche in termini di token.
2. **Slash command**: digitiamo `/report-npl` all'inizio del messaggio; il resto del messaggio diventa l'argomento della skill. Possiamo concatenare fino a sei skill nello stesso messaggio (`/skill-a /skill-b fai XYZ`).

Comando utile per la manutenzione: `/skill-doctor` mostra le skill caricate ma mai usate e quanto contesto ci stanno costando.

### 2.5 Dove vivono le skill

| Livello | Percorso | Vale per |
|---|---|---|
| Enterprise | `.claude/skills/<nome>/SKILL.md` nella directory delle impostazioni gestite dall'organizzazione | Macchine amministrate centralmente |
| Personale | `~/.claude/skills/<nome>/SKILL.md` | Tutti i nostri progetti |
| Progetto | `.claude/skills/<nome>/SKILL.md` | Quel repository; si committa per condividerla col team |
| Plugin | `<plugin>/skills/<nome>/SKILL.md` | Ovunque il plugin sia abilitato; invocazione `/<plugin>:<nome>` |
| Sincronizzate da claude.ai | `~/.claude/skills/synced/` | Le skill abilitate sul nostro account claude.ai compaiono anche nel terminale (dalla versione 2.1.275) |

In caso di omonimia la precedenza è: **enterprise > personale > progetto**. Le skill dei plugin non entrano mai in conflitto perché hanno il prefisso del plugin nel nome.

### 2.6 Skill e vecchi comandi personalizzati

I "custom slash command" (file `.claude/commands/<nome>.md`) sono il meccanismo storico precedente alle skill. La documentazione oggi dichiara: *"Custom commands have been merged into skills"* — i comandi personalizzati sono stati fusi nelle skill. I vecchi file continuano a funzionare e creano lo stesso tipo di comando `/<nome>`, ma per il materiale nuovo la via raccomandata è il formato skill; a parità di nome, vince la skill.

---

## 3. I server MCP

### 3.1 Che cos'è MCP

**MCP** (*Model Context Protocol*) è un protocollo aperto, creato da Anthropic, che standardizza il modo in cui un'applicazione AI si collega a strumenti e dati esterni. Un **server MCP** è un programma (locale o remoto) che "parla" questo protocollo e mette a disposizione di Claude delle capacità che altrimenti non avrebbe: interrogare un database, leggere i ticket di Jira, cercare nelle email, e così via. Claude Code fa da **client MCP**: si collega ai server configurati e ne usa le capacità.

### 3.2 Che cosa espone un server MCP

Tre tipi di capacità:

- **tools** (strumenti): azioni che Claude può invocare — "cerca nelle email", "esegui questa query", "crea un ticket";
- **resources** (risorse): dati che Claude può leggere;
- **prompts**: richieste predefinite riutilizzabili, pronte da richiamare.

Gli strumenti MCP compaiono a Claude con nomi nel formato `mcp__<server>__<tool>` (ad esempio `mcp__jira__create_issue`): è il formato da usare anche nelle regole di permesso e negli hook.

### 3.3 Trasporti: server remoti e locali

Il **trasporto** è il canale con cui Claude Code comunica col server:

- `http` — server **remoto**, raggiunto via rete: è la modalità consigliata per i servizi in cloud (il vecchio trasporto `sse` è deprecato);
- `stdio` — server **locale**: un processo avviato sulla nostra macchina, con cui Claude Code dialoga attraverso lo standard input/output.

### 3.4 Configurazione

Dalla riga di comando:

```bash
# server remoto (HTTP)
claude mcp add --transport http nome-server https://esempio.com/mcp

# server locale (processo stdio); il "--" separa i flag di Claude dal comando del server
claude mcp add nome-server -- npx -y pacchetto-server-mcp
```

Comandi di gestione: `claude mcp list`, `claude mcp get <nome>`, `claude mcp remove <nome>`, `claude mcp login <nome>` (per i server che richiedono autenticazione). Dentro una sessione, `/mcp` mostra lo stato delle connessioni.

### 3.5 Gli scope (ambiti) di configurazione

Lo **scope** stabilisce dove viene salvata la configurazione e chi la eredita:

| Scope | File | Vale per |
|---|---|---|
| `local` (default) | `~/.claude.json`, nella voce del progetto corrente | Solo noi, solo in quel progetto |
| `project` | `.mcp.json` nella radice del progetto | Tutto il team: si committa nel repository (alla prima apertura viene chiesta l'approvazione) |
| `user` | `~/.claude.json`, a livello globale | Tutti i nostri progetti |

Se lo stesso nome di server è definito in più posti, la precedenza completa è:

**local > project > user > server forniti dai plugin > connettori claude.ai**

e la voce vincente viene usata per intero, senza fusione di campi. I server imposti dall'organizzazione (`managedMcpServers`) prevalgono su tutti.

### 3.6 "Connettore" = server MCP, visto da claude.ai

Nell'app Claude (claude.ai e desktop) le integrazioni con i servizi esterni si chiamano **connettori** (*connectors*): sotto il cofano sono server MCP remoti. La documentazione di Claude Code lo dice esplicitamente, con una conseguenza pratica utile: **i connettori aggiunti su claude.ai diventano automaticamente disponibili anche in Claude Code**, se abbiamo effettuato l'accesso con lo stesso account. Viceversa, un server MCP remoto incluso in un plugin viene offerto come connettore su claude.ai; un server locale `stdio`, invece, non può raggiungere claude.ai.

---

## 4. I plugin

### 4.1 Che cosa sono

Un **plugin** è un'unità di confezionamento e distribuzione: una directory con un **manifest** (file di metadati) in `.claude-plugin/plugin.json` — dove l'unico campo obbligatorio è `name` — più i componenti veri e propri. Serve quando vogliamo consegnare a un team, in un colpo solo, un intero "kit di lavoro" invece di far copiare a mano skill, hook e configurazioni a ogni persona.

> **Attenzione alla sicurezza.** Un plugin viene eseguito con i privilegi del nostro utente: prima di installarne uno di terze parti, esaminiamone il contenuto.

### 4.2 Che cosa può contenere

| Componente | Posizione nel plugin | Note |
|---|---|---|
| Skill | `skills/<nome>/SKILL.md` | Invocabili come `/<plugin>:<nome>` |
| Comandi (storici) | `commands/<file>.md` | Funzionano ancora; per il nuovo materiale si preferiscono le skill |
| Subagenti | `agents/<nome>.md` | Assistenti specializzati con un proprio contesto; invocabili come `@agent-<plugin>:<nome>` |
| Hook | `hooks/hooks.json` | Comandi automatici agganciati a eventi del ciclo di vita (ad esempio *prima* che Claude esegua uno strumento); scattano al caricamento del plugin |
| Server MCP | `.mcp.json` | Compaiono in `/mcp` come `plugin:<plugin>:<server>` |
| Server LSP | `.lsp.json` | **LSP** (*Language Server Protocol*) è il protocollo che fornisce navigazione del codice e diagnostica; il binario del server va installato a parte |
| Monitor | `monitors/monitors.json` | Comandi in background il cui output arriva a Claude |
| Workflow | `workflows/*.js` | Script che orchestrano più subagenti |
| Eseguibili | `bin/` | Aggiunti al PATH dello strumento Bash finché il plugin è abilitato |
| Stili e temi | `output-styles/`, `themes/` | Alcuni marcati come sperimentali |

### 4.3 Installazione e marketplace

Un **marketplace** è un catalogo di plugin, non un negozio: un repository (tipicamente Git) con un file `.claude-plugin/marketplace.json` che elenca i plugin e le loro sorgenti. Chiunque può pubblicarne uno — anche un'azienda, per distribuire internamente i propri plugin. Il marketplace ufficiale `claude-plugins-official` viene aggiunto automaticamente alla prima sessione.

Le vie di installazione:

```bash
# dentro una sessione: gestore interattivo (schede Discover, Installed, Marketplaces, Errors)
/plugin

# aggiungere un marketplace e installare da lì
/plugin marketplace add mia-org/claude-plugins
/plugin install analisi-rischio@mia-org

# dalla shell, con scelta dello scope
claude plugin install analisi-rischio@mia-org --scope project

# solo per la sessione corrente, senza installare (utile in sviluppo)
claude --plugin-dir ./mio-plugin
```

### 4.4 Gli scope dei plugin

| Scope | Registrato in | Vale per |
|---|---|---|
| `user` | `~/.claude/settings.json` (`enabledPlugins`) | Noi, in ogni progetto |
| `project` | `.claude/settings.json` committato | Tutto il team del repository |
| `local` | `.claude/settings.local.json` | Noi, solo in quel repository |
| `managed` | Impostazioni gestite dall'organizzazione | Imposto centralmente, non disattivabile da `/plugin` |

In caso di sovrapposizione: **local > project > user**. I file installati vivono in `~/.claude/plugins/`.

### 4.5 Il costo in contesto

Ogni plugin abilitato aggiunge a **ogni turno** il nome e la descrizione di tutte le sue skill, subagenti e comandi attivabili dal modello, anche quando non li usiamo. Conviene quindi abilitare solo ciò che serve: `/skill-doctor` e il gruppo "Not used recently" nella scheda Installed di `/plugin` aiutano a individuare il materiale inutilizzato.

---

## 5. Mettere tutto insieme

### 5.1 Tabella comparativa

| | **Skill** | **Server MCP** | **Plugin** |
|---|---|---|---|
| Che cos'è | Istruzioni e know-how procedurale | Accesso a strumenti e dati esterni | Pacchetto di componenti installabile come unità |
| Che cosa ottiene Claude | Il *come fare* un compito | Strumenti invocabili, risorse leggibili, prompt | Tutto ciò che il pacchetto contiene |
| Nel contesto | Descrizione a ogni turno; corpo solo all'uso | Nomi degli strumenti; schemi completi su richiesta | Ogni componente abilitato, con le proprie regole |
| Attivazione | Corrispondenza con la descrizione, o `/<nome>` | Claude invoca uno strumento quando pertinente | I suoi hook, agenti e skill, ciascuno con le proprie regole |
| Configurazione | `SKILL.md` in una cartella skills | `claude mcp add`, `.mcp.json`, `~/.claude.json` | `plugin.json` + `enabledPlugins` nei settings |

### 5.2 Un esempio completo in ambito bancario

Immaginiamo di dover attrezzare il team "rischio di credito" della banca. Costruiamo un plugin `rischio-credito` che contiene:

- un **server MCP** verso il data warehouse dei crediti → *accesso*: Claude può interrogare le tabelle (strumenti `mcp__dwh-crediti__query`, ecc.);
- una **skill** `analisi-npl` che documenta lo schema delle tabelle, le convenzioni di calcolo (incidenza NPL, coperture) e il formato standard dei report → *conoscenza*: Claude sa usare bene quegli strumenti;
- un **hook** `PreToolUse` che blocca qualunque query sulle tabelle contenenti dati personali dei clienti → *controllo*: il vincolo è imposto, non solo suggerito;
- un **subagente** `revisore-report` che rilegge ogni report prodotto prima della consegna.

Chi entra nel team esegue una sola installazione dal marketplace interno e ha tutto: accesso, procedura e vincoli. È esattamente il pattern dell'esempio ufficiale della documentazione (server MCP verso un database + skill che ne documenta schema e pattern di interrogazione).

### 5.3 Le skill suggeriscono, gli hook impongono

Un principio da tenere a mente, dichiarato dalla documentazione: *"An instruction like 'never edit .env' in CLAUDE.md or a skill is a request, not a guarantee"* — un'istruzione scritta in una skill (o in CLAUDE.md) è una richiesta, non una garanzia. Quando un vincolo deve essere **certo**, va implementato come hook, che blocca l'azione a livello di meccanismo e non di persuasione.

### 5.4 Quale usare quando

- Solo know-how ripetibile (una procedura, una checklist, un formato) → **una skill**, in `.claude/skills/` del progetto se va condivisa col team.
- Solo accesso a un sistema esterno → **un server MCP**, con lo scope adatto alla platea (`project` per il team).
- Know-how **e** accesso, da distribuire e aggiornare come un tutt'uno, magari con vincoli automatici → **un plugin** pubblicato su un marketplace.
- Un sistema esterno già collegato ma usato male o in modo incoerente → aggiungiamo **una skill che documenta come usarlo**: è la combinazione raccomandata dalla documentazione.

---

## Fonti

- Skill: <https://code.claude.com/docs/en/skills>
- Panoramica delle funzionalità (con i confronti "MCP vs Skill", "Hook vs Skill", ecc.): <https://code.claude.com/docs/en/features-overview>
- Plugin — panoramica: <https://code.claude.com/docs/en/plugins/overview>
- Plugin — componenti: <https://code.claude.com/docs/en/plugins/components>
- Plugin — installazione: <https://code.claude.com/docs/en/plugins/install>
- Marketplace — riferimento: <https://code.claude.com/docs/en/plugins/marketplace-reference>
- MCP in Claude Code: <https://code.claude.com/docs/en/mcp>
- Comandi slash: <https://code.claude.com/docs/en/commands>
- Riferimento CLI: <https://code.claude.com/docs/en/cli-reference>
