# Scegliere il giusto modello in Claude Code

**GUIDA OPERATIVA · CORSO HANDS-ON · METÀ OTTOBRE 2026**  
**Data di verifica: 13 ottobre 2026** · Prezzi in dollari USA · Focus: Claude Code nella CLI

> **Come leggere questa guida**  
> Le specifiche, i prezzi e i comportamenti documentati hanno riferimenti alle fonti ufficiali Anthropic. Le configurazioni consigliate e gli esercizi sono proposte didattiche, non risultati di benchmark eseguiti dall’autore. La fotografia è quella del **13 ottobre 2026**: non anticipa eventuali cambiamenti successivi. Comandi verificati nella documentazione, non eseguiti su un account Claude del lettore.

[01 Modelli](#modelli) · [02 Cambiare modello](#cambio) · [03 Effort](#effort) · [04 Piani](#piani) · [05 Quick tips](#tips) · [06 Quick reference](#reference)

---

<a id="modelli"></a>
## 01 — I modelli disponibili: caratteristiche, confronto e costi

### Prima distinzione: Claude Code non è il modello

Claude Code è l’ambiente agentico che coordina conversazione, contesto, strumenti e ciclo di lavoro. Il modello è uno dei suoi componenti: interpreta la richiesta e decide le azioni, mentre l’ambiente rende disponibili lettura dei file, modifiche, shell e integrazioni. Cambiare modello non equivale a cambiare repository o ad autorizzare nuove operazioni. [Funzionamento di Claude Code][funzionamento]

La scelta utile non è «qual è il modello migliore in assoluto?», ma:

> **Quale combinazione di modello, effort e contesto risolve questo compito con qualità verificabile, entro tempi e costi accettabili?**

### 1.1 La gamma corrente da usare come riferimento

Il catalogo corrente comprende **Fable 5.1, Opus 5.5, Sonnet 5.5 e Haiku 5.5**. Tutti supportano input testuale e immagini, output testuale, uso di strumenti e ragionamento adattivo. La latenza sotto indicata è una classificazione qualitativa del produttore, non una promessa di secondi o token al secondo. [Catalogo ufficiale][catalogo]

| Modello | ID Anthropic da fissare negli esercizi | Contesto massimo | Output massimo API | Latenza relativa |
|---|---|---:|---:|---|
| **Fable 5.1** | `claude-fable-5-1` | 1M token | 128K token | Più elevata |
| **Opus 5.5** | `claude-opus-5-5` | 1M token | 128K token | Intermedia |
| **Sonnet 5.5** | `claude-sonnet-5-5` | 1M token | 128K token | Bassa |
| **Haiku 5.5** | `claude-haiku-5-5` | 1M token | 128K token | La più bassa |

Fonti per ciascuna riga: [Fable 5.1][fable], [Opus 5.5][opus], [Sonnet 5.5][sonnet], [Haiku 5.5][haiku]. **K** indica migliaia di token; **M** un milione. Il limite di output è una specifica API, non la lunghezza garantita di una risposta in Claude Code. Il contesto comprende anche istruzioni, cronologia e risultati degli strumenti: non è tutto spazio libero per il codice. [Contesto nell’ambiente agentico][funzionamento]

**Perché 1M di contesto non rende equivalenti i modelli.** La capacità di contenere informazioni non misura, da sola, la capacità di collegarle correttamente. Nel corso, confrontare quindi la qualità delle diagnosi e delle modifiche, non soltanto la dimensione del repository caricabile.

### 1.2 Che cosa scegliere, concretamente

Le seguenti sono **indicazioni operative proposte per il corso**, basate sul posizionamento ufficiale dei modelli; vanno validate sui propri repository.

| Modello | Quando lo proporrei | Esempio hands-on | Quando non lo sceglierei per primo |
|---|---|---|---|
| **Haiku 5.5** | Operazioni piccole, esplicite e facilmente controllabili | Classificare errori già raccolti; documentare una funzione; generare casi di test semplici | Diagnosi ambigua tra più servizi o modifica ad alto impatto senza supervisione |
| **Sonnet 5.5** | Esercizi ordinari con requisiti chiari e feedback rapido | Implementare la validazione di un input; aggiungere test; correggere un bug localizzato | Problema architetturale aperto dopo tentativi ben contestualizzati ma falliti |
| **Opus 5.5** | Coding agentico articolato, dipendenze tra file e verifica approfondita | Refactoring multi-modulo; analisi di regressioni; modifica che deve preservare contratti esistenti | Attività puramente meccanica per la quale una soluzione più economica supera già i test |
| **Fable 5.1** | Problemi difficili, ambigui, lunghi o con molte ipotesi da investigare | Ricostruire una causa radice complessa; confrontare strategie di migrazione e verificarne una | Ogni piccolo esercizio introduttivo o task con costo molto vincolato |

Posizionamento di riferimento: [Fable][fable], [Opus][opus], [Sonnet][sonnet], [Haiku][haiku]. Anthropic indica **Opus 5.5** come punto di partenza generale nel catalogo; qui propongo **Sonnet 5.5 per i laboratori ordinari** per privilegiare interazione e controllo del costo. Sono due criteri diversi, non una contraddizione. [Catalogo][catalogo]

### 1.3 Listino API aggiornato

**Unità: USD per 1 milione di token, per ciascuna categoria fatturata.** Questi sono prezzi API standard: non sono il canone mensile di Claude e non permettono di ricavare un numero garantito di richieste incluse nell’abbonamento.

| Modello / dimensione del prompt | Input non in cache | Output | Lettura cache | Scrittura cache, 5 minuti | Scrittura cache, 1 ora |
|---|---:|---:|---:|---:|---:|
| **Fable 5.1** | $10,00 | $50,00 | $0,25 | $12,50 | $20,00 |
| **Opus 5.5** | $4,00 | $20,00 | $0,20 | $5,00 | $8,00 |
| **Sonnet 5.5** | $2,00 | $10,00 | $0,10 | $2,50 | $4,00 |
| **Haiku 5.5 — prompt ≤ 100.000 token** | $0,10 | $0,50 | $0,01 | $0,125 | $0,20 |
| **Haiku 5.5 — prompt > 100.000 token** | $0,50 | $2,50 | $0,05 | $0,625 | $1,00 |

Prezzi verificati nelle schede [Fable][fable], [Opus][opus], [Sonnet][sonnet], [Haiku][haiku] e incrociati con il [listino API][prezzi-api]. La lettura cache di **Sonnet 5.5 è scesa a $0,10/MTok il 7 ottobre 2026**; nello stesso giorno è stato annunciato Haiku 5.5. [Release notes][rilasci]

> **Attenzione a Haiku 5.5: la soglia riguarda ogni singola richiesta.**  
> I 100.000 token comprendono tutto l’input, anche letture e scritture della cache. Sopra soglia si applica il listino superiore alla richiesta, **anche all’output**: non soltanto ai token eccedenti. Non è la somma dei token consumati nell’intera sessione. Per gli altri tre modelli correnti, il contesto fino a 1M mantiene le tariffe standard per token. [Regole di long-context pricing][prezzi-api]

**Come interpretare la cache.** Una scrittura memorizza un prefisso riutilizzabile; una lettura fattura il successivo riuso. Le colonne non si sommano automaticamente sugli stessi token. Il prezzo inferiore della lettura non elimina il costo iniziale di popolamento né quello dei nuovi token. [Prompt caching][cache]

### 1.4 Dal prezzo per token al costo di un’attività

Per una sessione con più richieste e, eventualmente, più modelli:

```text
Costo token = somma, per tutte le richieste, di:

  input non in cache × tariffa input
+ output fatturato   × tariffa output
+ cache scritta      × tariffa di scrittura applicabile
+ cache letta        × tariffa di lettura

Se le tariffe sono per MTok, dividere ciascun prodotto per 1.000.000.
```

È una formula contabile: occorre usare categorie di token **non sovrapposte** e la tariffa effettiva di ciascuna richiesta. Eventuali servizi aggiuntivi e imposte sono separati. [Categorie di fatturazione della cache][cache] [Listino][prezzi-api]

**Esempio calcolato, non benchmark.** Una richiesta ipotetica con 20.000 token di input, 5.000 token di output complessivamente fatturato e nessuna cache costa:

| Modello | Costo calcolato della richiesta |
|---|---:|
| Haiku 5.5, fascia ≤ 100K | **$0,0045** |
| Sonnet 5.5 | **$0,09** |
| Opus 5.5 | **$0,18** |
| Fable 5.1 | **$0,45** |

Per Opus: `20.000 / 1.000.000 × $4 + 5.000 / 1.000.000 × $20 = $0,18`. I quattro modelli **non necessariamente consumano gli stessi token sullo stesso compito**: questa tabella spiega il listino, non prevede il costo di un laboratorio.

Per decidere, propongo di misurare il **costo per attività accettata**: spesa totale dei tentativi divisa per i risultati che superano i criteri di accettazione, affiancata da tempo di revisione e difetti residui. Un modello più economico per token può richiedere più tentativi. [Criteri di scelta Anthropic][scelta-blog]

**Altri modificatori da non confondere.** La Batch API applica uno sconto del 50%, ma non è la normale sessione interattiva né la skill `/batch` di Claude Code. Le tariffe dei provider cloud vanno controllate sul relativo listino; non assumere che coincidano con quelle qui riportate. [Prezzi API][prezzi-api] [Comando `/batch`][comandi]

### 1.5 Modelli precedenti e disponibilità riservata

«Non è l’ultima versione» non significa necessariamente «ritirato». Nel catalogo API risultano ancora attivi i seguenti modelli precedenti; l’accesso concreto in Claude Code dipende da account, provider e policy. [Ciclo di vita][deprecazioni]

| Versioni precedenti | Stato API al 13/10/2026 | Input / output, USD per MTok |
|---|---|---:|
| Fable 5 | Attivo | $10 / $50 |
| Opus 5, 4.8, 4.7, 4.6, 4.5 | Attivi | $5 / $25 |
| Sonnet 5 | Attivo | $2 / $10 |
| Sonnet 4.6 | Attivo | $3 / $15 |
| Haiku 4.5 | Attivo | $1 / $5 |
| Sonnet 4.5 | **Deprecato**, ritiro previsto il 30/11/2026 | $3 / $15 |

Stato: [deprecazioni][deprecazioni]. Prezzi base, senza cache e opzioni aggiuntive: [listino][prezzi-api]. La presenza di un prezzo nella documentazione non prova, da sola, che un modello sia utilizzabile: **Opus 4.1 e Opus 4 risultano già ritirati**. [Stati ufficiali][deprecazioni]

**Indicazione per il corso:** mantenere una vecchia versione solo per riprodurre un ambiente esistente o verificare una migrazione; non impostarla come base di un nuovo laboratorio senza una ragione esplicita.

**Mythos: caso separato.** Mythos 5.1 ha specifiche e prezzi di Fable 5.1, ma l’accesso è subordinato ai programmi di verifica Anthropic. Non va presentato come opzione ordinaria disponibile a tutti gli iscritti. Mythos 5 è ancora attivo con accesso riservato; Mythos Preview è deprecato, con data di ritiro non ancora annunciata. [Mythos 5.1][mythos] [Programma di verifica][cvp] [Ciclo di vita][deprecazioni]

---

<a id="cambio"></a>
## 02 — Come passare da un modello all’altro

### 2.1 Dentro una sessione: `/model`

Aprire il selettore con:

```text
/model
```

Oppure selezionare direttamente un modello, per esempio:

```text
/model claude-sonnet-5-5
```

Nella CLI attuale, **Invio salva la scelta anche come default per le nuove sessioni**; digitare `/model <nome>` ha lo stesso effetto. Per cambiare **soltanto nella sessione corrente**, aprire il selettore e premere **`s`** sulla riga desiderata. [Comando `/model`][comandi]

La scorciatoia **Alt+P** su Windows/Linux, oppure **Option+P** su macOS, apre il cambio modello senza cancellare il prompt in composizione. Sui quattro modelli correnti, la scorciatoia per disattivare il thinking non lo disabilita. [Interazione nella CLI][interattivo]

### 2.2 All’avvio: opzione esplicita e riproducibile

Esempi da eseguire **nella shell**, non nel prompt di Claude Code:

```bash
# Un laboratorio con modello ed effort espliciti
claude --model claude-sonnet-5-5 --effort medium

# Una sessione di analisi più impegnativa
claude --model claude-opus-5-5 --effort high

# Lavoro complesso: controllare prima accesso e fatturazione
claude --model claude-fable-5-1 --effort high
```

`--model` seleziona il modello per l’avvio corrente; `--effort` imposta il livello della sessione. Per il corso è il metodo preferibile: il comando documenta la configurazione e non dipende dal default lasciato dall’esercizio precedente. [CLI reference][cli]

### 2.3 Alias: comodi, ma non immutabili

| Alias su accesso Anthropic diretto, nella versione corrente | Risoluzione documentata |
|---|---|
| `haiku` | Haiku 5.5 |
| `sonnet` | Sonnet 5.5 |
| `opus` | Opus 5.5 |
| `fable` | Fable 5.1 |
| `opusplan` | Opus durante Plan Mode, Sonnet durante l’esecuzione |

Gli alias dipendono da provider e versione. **Negli esperimenti fissare l’ID completo e verificare il modello effettivo**; nei cloud aziendali possono servire identificatori specifici. `opusplan` è una strategia, non un modello: richiede **Plan Mode**, non semplicemente un prompt che chieda un piano. [Configurazione dei modelli][config-modelli]

### 2.4 Impostazione persistente e diagnosi dei conflitti

Per un default personale, aggiungere la chiave `model` al file `~/.claude/settings.json`, **senza sovrascrivere le altre impostazioni**:

```json
{
  "model": "claude-sonnet-5-5"
}
```

Le impostazioni condivise del progetto sono in `.claude/settings.json`; quelle personali per quel progetto in `.claude/settings.local.json`. Configurazioni locali, di progetto, organizzative e variabili d’ambiente possono prevalere sul default personale. Le restrizioni amministrative ai modelli non si aggirano con un flag. `/status` mostra anche le sorgenti di configurazione attive. [File e precedenze][impostazioni]

> **Controllo iniziale del laboratorio**  
> Nella shell: `claude --version`. Per questi esercizi usare una CLI aggiornata; la documentazione indica **2.1.293 o successiva per Haiku 5.5**. Dentro Claude Code controllare `/status`, `/model`, `/effort status` e `/usage`. Se si aggiorna con `claude update`, farlo prima della lezione e riprovare gli esercizi. [Requisiti dei modelli][config-modelli] [CLI][cli] [Comandi][comandi]

**Cambiare modello non è un reset metodologico.** Per lavorare sullo stesso task è utile conservare la conversazione; per confrontare modelli in aula, iniziare invece sessioni indipendenti dallo stesso stato del repository. Altrimenti il secondo candidato può beneficiare della diagnosi prodotta dal primo.

---

<a id="effort"></a>
## 03 — I livelli di effort

### 3.1 Modello ed effort sono due leve diverse

**Il modello** determina le capacità disponibili. **L’effort** orienta quanto lavoro il modello investe nella risposta: non soltanto ragionamento, ma anche esplorazione, uso degli strumenti e verifica. Aumentarlo non allena nuovamente il modello e non modifica i suoi pesi. [Spiegazione Anthropic][scelta-blog]

L’effort è un segnale comportamentale, **non un budget rigido di token, secondi o dollari**. Lo stesso nome non implica la stessa quantità di calcolo tra modelli. [Parametro effort][effort-api]

### 3.2 I cinque livelli, applicati al lavoro in aula

Le situazioni sotto sono esempi didattici, non soglie garantite di qualità.

| Livello | Intento operativo | Esercizio adatto | Attenzione |
|---|---|---|---|
| **`low`** | Ottenere rapidamente una prima soluzione controllabile | Spiegare poche righe; rinominare un simbolo con perimetro chiaro | Non confondere una risposta rapida con una verifica completa |
| **`medium`** | Bilanciare approfondimento e consumo | Funzionalità circoscritta, test ordinari, laboratorio guidato | Rendere espliciti criteri di accettazione e file rilevanti |
| **`high`** | Investire di più in analisi e controlli | Bug con casi limite; regressione; modifica multi-file | Misurare il beneficio rispetto a `medium` |
| **`xhigh`** | Approfondire problemi particolarmente impegnativi | Analisi di concorrenza; refactoring delicato | Confrontare anche un modello superiore, non soltanto più effort |
| **`max`** | Riservare il massimo approfondimento ai casi che lo giustificano | Esperimento su un problema difficile con valutazione indipendente | Non è «qualità garantita»; può aggiungere costo senza vantaggi proporzionati |

I quattro modelli correnti supportano questi cinque livelli. La scelta va verificata sul proprio insieme di compiti. [Effort API][effort-api]

### 3.3 I default corretti: Claude Code non è sempre l’API

| Modello corrente | Default in **Claude Code** | Default nella **Claude API** |
|---|---|---|
| Fable 5.1 | `high` | `high` |
| Opus 5.5 | `medium` | `medium` |
| Sonnet 5.5 | **`medium`** | **`high`** |
| Haiku 5.5 | `medium` | `medium` |

Fonti: [default Claude Code][config-modelli], [default API][effort-api]. Valori validi in assenza di override personali, di progetto o organizzativi.

> **Errore da evitare**  
> «Sonnet 5.5 usa `high` per default» è incompleto: è vero per l’API, non per il default attuale di Claude Code. Nel laboratorio dichiarare esplicitamente l’effort, soprattutto quando si confrontano una chiamata API e una sessione CLI.

### 3.4 Comandi operativi

Dentro Claude Code, inviare **una riga alla volta**:

```text
/effort status
/effort medium
/effort high
/effort max
/effort auto
```

`status` mostra il livello; `auto` rimuove la scelta salvata per il modello attivo e torna alla risoluzione automatica. `max` è normalmente limitato alla sessione. Per un override isolato è semplice usare `claude --effort high` all’avvio. [Comandi][comandi] [CLI][cli]

Le scelte salvate sono gestite per modello; controllare nuovamente il livello dopo un cambio. [Impostazioni per modello][impostazioni] Per ridurre il consumo, abbassare l’effort: sui quattro modelli correnti Claude Code non offre un’effettiva disattivazione del thinking tramite il normale toggle. [Interfaccia interattiva][interattivo]

### 3.5 Tre cose che non sono livelli equivalenti

| Impostazione | Che cosa cambia | Implicazione pratica |
|---|---|---|
| **Effort** | Approfondimento e impiego di token | Può modificare lavoro svolto e costo complessivo |
| **Fast mode** | Latenza dello stesso modello Opus supportato | Prezzo per token superiore; non è «effort basso» |
| **Ultracode** | Orchestrazione di workflow dinamici in Claude Code | Non è un sesto livello della scala `low`–`max`; può avviare più subagent |

Ultracode aggiunge orchestrazione al livello di effort della sessione: per questo il consumo va valutato anche sul numero di agenti attivati. [Workflow dinamici][workflow]

Fast mode è in research preview. Su **Opus 5.5 costa $8 input / $40 output per MTok**, contro $4/$20 standard; negli abbonamenti richiede usage credits. Non è disponibile su Sonnet o Haiku. Attivarlo da un modello non supportato può anche selezionare Opus: controllare il modello, non solo l’icona di velocità. [Fast mode][fast]

`ultrathink` è invece una parola riconosciuta nel prompt: aggiunge un’istruzione di approfondimento per quel turno, **senza cambiare il livello effort inviato all’API**. Non usarla al posto di una configurazione esplicita negli esperimenti. [Configurazione][config-modelli]

---

<a id="piani"></a>
## 04 — Sintesi dei piani disponibili

### 4.1 Canone, accesso a Claude Code e uso incluso

**Prezzi pubblici web in USD, imposte escluse.** Per acquisti locali, mobile o contratti negoziati, verificare il checkout o l’accordo applicabile. I moltiplicatori di utilizzo non sono garanzie di un numero fisso di prompt. [Listino piani][piani-prezzi] [Limiti Max][max]

| Piano / modalità | Prezzo pubblico | Rapporto con Claude Code | Impiego suggerito nel corso |
|---|---|---|---|
| **Free** | $0 | Claude Code non incluso nel piano gratuito | Non usarlo come prerequisito sufficiente per i laboratori |
| **Pro** | $20/mese; oppure $200/anno | Claude Code incluso, entro i limiti del piano | Avvio individuale e uso moderato |
| **Max 5x** | $100/mese | Più capacità d’uso rispetto a Pro | Uso individuale frequente e laboratori estesi |
| **Max 20x** | $200/mese | Capacità superiore a Max 5x | Uso intensivo, dopo aver misurato il bisogno |
| **Team — Standard** | $25/utente/mese; $20 con fatturazione annuale | Claude Code e amministrazione condivisa | Aula aziendale con gestione centralizzata |
| **Team — Premium** | $125/utente/mese; $100 con fatturazione annuale | Uso superiore alla seat Standard | Partecipanti con impiego più intenso |
| **Enterprise, offerta usage-based corrente** | $20/utente/mese, fatturazione annuale, **più consumo a tariffe API** | Governance e consumo fatturato | Adozione aziendale governata |
| **Console / API pay-as-you-go** | Consumo, non canone Pro/Max | Claude Code autenticato sull’account API | Misurazione economica e automazioni |

Fonti: [listino][piani-prezzi], [Max][max], [Claude Code con Pro/Max][pro-max], [Enterprise usage-based][enterprise-usage]. Pro annuale equivale matematicamente a circa **$16,67/mese**, pur essendo mostrato sul sito come circa $17: l’addebito è di $200 anticipati. Max è mensile. [Listino][piani-prezzi] [Max][max]

Team è attualmente proposto per **2–150 utenti**. Esistono anche offerte Education istituzionali: non assumere che il contratto della propria università coincida con Pro o Team. [Listino][piani-prezzi]

### 4.2 Tre contatori diversi da tenere separati

| Contatore | Che cosa rappresenta | Dove verificare |
|---|---|---|
| **Uso incluso nell’abbonamento** | Capacità d’uso del piano, non un portafoglio API convertibile | `/usage` e impostazioni Usage |
| **Usage credits** | Consumo aggiuntivo nelle applicazioni Claude; possono finanziare funzioni non incluse | Impostazioni di fatturazione/Usage del piano |
| **Crediti Claude Platform / API** | Saldo della Console per utilizzi API ammessi | Billing e Usage della Console |

Pro e Max condividono i limiti tra Claude e Claude Code, con limiti di sessione e settimanali. I nuovi Enterprise usage-based, invece, fatturano il consumo da subito; non vanno descritti con le regole dei vecchi Enterprise basati su quote incluse. [Pro/Max][pro-max] [Enterprise][enterprise-usage]

### 4.3 Fable: disponibile non significa incluso

**Pro e Team Standard:** Fable 5/5.1 richiedono usage credits fin dall’inizio. **Max e Team Premium:** possono usare Fable entro un massimo del **50% della quota settimanale**, che fa comunque parte della quota totale, non si aggiunge a essa. Al raggiungimento della soglia occorre cambiare modello oppure usare crediti aggiuntivi. Negli Enterprise usage-based si applicano le tariffe API. [Fable sui diversi piani][fable-piani]

Le vecchie offerte Enterprise con seat Standard/Premium hanno regole specifiche: verificare il contratto. Per gli utenti autorizzati a Mythos, la sua quota su Max è condivisa con Fable, non separata. [Fable][fable-piani] [Mythos e verifica][cvp]

### 4.4 Novità del 7 ottobre: crediti API inclusi, ma con un perimetro preciso

Max 5x include **$100/mese**, Max 20x **$200/mese** di crediti API. Per Team, $20 per seat Standard e $100 per seat Premium confluiscono in un **saldo comune fino a $500/mese**. Pro, Free ed Enterprise non sono eleggibili a questa offerta. [Crediti inclusi][crediti-platform] [Aggiornamento del 7 ottobre][sdk-piano]

Il beneficio richiede il collegamento a un’organizzazione Console; i nuovi abbonati diventano eleggibili dopo sette giorni e i crediti inutilizzati non si accumulano. Sono distinti dalle quote dell’applicazione. [Condizioni dei crediti][crediti-platform]

> **Essenziale per i laboratori**  
> I crediti API inclusi **non coprono Claude Code interattivo** né gli usage credits extra. Possono coprire **`claude -p` e Agent SDK eseguiti direttamente con una chiave API dell’organizzazione Console collegata**. Con login dell’abbonamento, quei programmi usano invece le quote del piano. L’avvio da GitHub Action, IDE o app desktop non gode automaticamente dell’eccezione per `-p`. [Regole ufficiali, inclusa la FAQ su `claude -p`][crediti-help]

**Rischio operativo:** la presenza di `ANTHROPIC_API_KEY` può indirizzare la sessione alla fatturazione API anziché al piano. Prima di iniziare l’esercizio verificare account e modalità di autenticazione; non limitarsi a controllare il nome del modello. [Uso di Claude Code con l’abbonamento][pro-max]

---

<a id="tips"></a>
## 05 — Quick tips: scegliere bene durante un’attività reale

### 5.1 Una matrice di partenza, non una graduatoria universale

Queste combinazioni sono **proposte per i laboratori**. Non sostituiscono una valutazione sul codice e sui criteri di accettazione del corso.

| Situazione | Prima prova | Segnale per cambiare |
|---|---|---|
| Spiegazione o classificazione circoscritta | **Haiku 5.5 · medium** | Manca una distinzione importante anche dopo chiarimenti |
| Prima implementazione ben specificata | **Sonnet 5.5 · medium** | Non rispetta vincoli tra file o contratti esistenti |
| Bug localizzato con casi limite | **Sonnet 5.5 · high** | Analisi completa ma causa radice errata |
| Refactoring multi-file | **Opus 5.5 · medium**, poi high se utile | Servono più verifiche oppure un’indagine più ampia |
| Problema ambiguo, sistemico o persistente | **Fable 5.1 · high** | Costo alto senza convergenza: restringere il problema e rivalutare il piano |
| Demo live con Opus già adeguato | **Opus 5.5 · medium**; valutare Fast separatamente | La latenza ostacola la lezione e il costo premium è accettato |

La matrice traduce in esercizi il principio Anthropic: distinguere **problema troppo difficile** da **analisi troppo superficiale**. Il primo può richiedere un altro modello; la seconda può richiedere più effort. Prima di entrambi, verificare la qualità del contesto. [Guida alla scelta][scelta-blog]

### 5.2 Sei regole pratiche

**1 · Correggere prima il compito.** Fornire il comportamento osservato, quello atteso, un test riproducibile e i vincoli. Il prompt «sistema tutto» non è un esperimento utile. Esempio:

```text
Il test test_empty_customer_id fallisce.
Atteso: errore di validazione; osservato: record accettato.
Non cambiare la firma pubblica della funzione.
Individua la causa, proponi la modifica minima e verifica i casi limite.
```

**2 · Non usare più effort per compensare informazioni assenti.** Se manca lo stack trace o il test non è eseguibile, chiarire il contesto. Passare a `max` non crea i requisiti mancanti.

**3 · Delegare compiti piccoli, non responsabilità indistinte.** Un subagent con modello più economico può raccogliere evidenze o classificare risultati; mantenere la sintesi critica su un modello adeguato. I subagent hanno contesto e consumo propri: parallelismo non significa costo nullo. [Subagent][subagent]

**4 · Non riempire il contesto per principio.** Controllare `/context`; usare `/compact` quando serve continuare lo stesso lavoro con una sintesi. Per Haiku, monitorare anche la soglia tariffaria di 100K: la capienza di 1M non mantiene automaticamente il prezzo della fascia inferiore. [Gestione del contesto][comandi] [Tariffe Haiku][haiku]

**5 · Misurare una soluzione accettata, non una risposta convincente.** Test, invarianti, diff e revisione indipendente sono criteri migliori della lunghezza della spiegazione. Per ogni prova annotare errori residui e interventi manuali.

**6 · Controllare i due tipi di limite.** Un limite di turni arresta il ciclo; un limite di spesa stimata controlla il consumo. Non garantiscono che il task sia completato. Per un test non interattivo, questa è una configurazione possibile in **Bash, Zsh o Git Bash**:

```bash
claude -p \
  --model claude-sonnet-5-5 \
  --effort medium \
  --permission-mode plan \
  --max-turns 5 \
  --max-budget-usd 1.00 \
  --output-format json \
  "Analizza il progetto senza modificare il codice. Individua tre rischi di manutenzione e cita i file."
```

In PowerShell, riunire il comando su una sola riga, rimuovendo i backslash di continuazione.

`--max-budget-usd` funziona in print mode, si basa sulla stima client e **può essere superato** prima dell’arresto; non è un tetto contabile infallibile. Le spese dei subagent concorrono al limite. Affiancarlo ai controlli di spesa dell’account. [CLI e limiti][cli]

### 5.3 Mini-laboratorio: separare l’effetto del modello da quello dell’effort

**Obiettivo didattico:** verificare se una maggiore spesa produce un risultato migliore su un bug reale del repository didattico.

Usare lo stesso commit, lo stesso prompt e gli stessi test in quattro **sessioni indipendenti**: Haiku/medium, Sonnet/medium, Opus/medium e Opus/high. Fable/high è una quinta prova facoltativa solo quando accesso e budget sono stati chiariti.

Prima di ciascuna prova ripristinare una copia pulita del progetto; fissare modello completo, strumenti disponibili e permessi. Non passare al modello successivo la soluzione di quello precedente. Ripetere almeno tre volte ogni configurazione, annotando se la cache è calda o fredda.

| Evidenza da raccogliere | Domanda di valutazione |
|---|---|
| Test iniziale e test dopo la correzione | Il difetto è riprodotto e risolto? |
| Diff finale e regressioni | È una modifica minima e corretta? |
| Tempo totale e revisione umana | Quanto lavoro resta allo sviluppatore? |
| Token e costo per modello | Quanto è costato arrivare al risultato? |
| Casi riusciti / tentativi | Quanto è stabile il comportamento osservato? |

`/usage` presenta il consumo e una **stima locale del costo**. Per fatturazione API effettiva, usare la Console; in abbonamento distinguere il costo stimato dalle quote consumate. [Misurazione dei costi][costi]

**Conclusione da discutere in aula:** «Opus ha vinto in due casi su tre» è un’osservazione sul laboratorio; «Opus è sempre migliore» non ne segue. Lo stesso vale per il confronto tra livelli di effort.

---

<a id="reference"></a>
## 06 — Quick reference finale

### La scelta in trenta secondi

| Necessità | Configurazione iniziale suggerita |
|---|---|
| Attività semplice e verificabile | **Haiku 5.5 / medium** |
| Coding ordinario con requisiti chiari | **Sonnet 5.5 / medium** |
| Dipendenze complesse e qualità critica | **Opus 5.5 / medium → high** |
| Indagine difficile e lunga | **Fable 5.1 / high** |
| Risposta incompleta perché ha verificato poco | Migliorare istruzioni di verifica; valutare più effort |
| Risposta errata nonostante un’analisi pertinente | Valutare un modello più capace |
| Contesto insufficiente o test mancanti | Sistemare il contesto prima delle impostazioni |

*Promemoria delle proposte didattiche della sezione 05, non garanzie di prestazione.*

### I comandi da tenere accanto alla tastiera

| Azione | Comando / gesto |
|---|---|
| Verificare versione della CLI | `claude --version` nella shell |
| Avviare una configurazione riproducibile | `claude --model claude-sonnet-5-5 --effort medium` |
| Aprire il selettore dei modelli | `/model` |
| Cambiare e salvare il default | `/model claude-opus-5-5` |
| Cambiare solo per questa sessione | `/model`, poi **`s`** sulla scelta |
| Controllare account, modello e configurazione | `/status` |
| Controllare l’effort effettivo | `/effort status` |
| Impostare / ripristinare l’effort | `/effort high` · `/effort auto` |
| Controllare token, costo stimato e quote | `/usage` |
| Vedere / sintetizzare il contesto | `/context` · `/compact` |
| Disattivare Fast mode | `/fast off` |

Riferimenti operativi: [CLI][cli], [comandi][comandi], [impostazioni][impostazioni], [costi][costi].

### Prezzi API da ricordare

| Modello | Input / output, USD per MTok |
|---|---:|
| Haiku 5.5, prompt ≤ 100K | **$0,10 / $0,50** |
| Haiku 5.5, prompt > 100K | **$0,50 / $2,50** |
| Sonnet 5.5 | **$2 / $10** |
| Opus 5.5 standard | **$4 / $20** |
| Fable 5.1 | **$10 / $50** |
| Opus 5.5 Fast | **$8 / $40** |

Per cache e condizioni: tabelle della sezione 01 e [schede dei modelli][catalogo]; per Fast: [documentazione dedicata][fast].

> **Le cinque verifiche prima di premere Invio**  
> **Modello effettivo · Effort effettivo · Account di fatturazione · Perimetro del compito · Criterio di accettazione.**  
> Per il corso: scegliere una configurazione iniziale ragionevole, osservare le evidenze e cambiare una leva alla volta.

<!-- Riferimenti Markdown: le definizioni non aggiungono una sezione visiva dopo la quick reference. Tutte le fonti sono ufficiali Anthropic e sono state consultate il 13 ottobre 2026. -->

[funzionamento]: https://code.claude.com/docs/en/how-claude-code-works "Anthropic — How Claude Code works; consultato 13/10/2026"
[catalogo]: https://platform.claude.com/docs/en/models/overview "Anthropic — Models overview; consultato 13/10/2026"
[fable]: https://platform.claude.com/docs/en/models/fable-5-1/overview "Anthropic — Claude Fable 5.1; consultato 13/10/2026"
[opus]: https://platform.claude.com/docs/en/models/opus-5-5/overview "Anthropic — Claude Opus 5.5; consultato 13/10/2026"
[sonnet]: https://platform.claude.com/docs/en/models/sonnet-5-5/overview "Anthropic — Claude Sonnet 5.5; consultato 13/10/2026"
[haiku]: https://platform.claude.com/docs/en/models/haiku-5-5/overview "Anthropic — Claude Haiku 5.5; consultato 13/10/2026"
[prezzi-api]: https://platform.claude.com/docs/en/about-claude/pricing "Anthropic — API pricing; consultato 13/10/2026"
[rilasci]: https://platform.claude.com/docs/en/release-notes/overview "Anthropic — Platform release notes; consultato 13/10/2026"
[cache]: https://platform.claude.com/docs/en/build-with-claude/prompt-caching "Anthropic — Prompt caching; consultato 13/10/2026"
[scelta-blog]: https://claude.com/resources/articles/claude-model-and-effort-level-in-claude-code "Anthropic — Claude Code effort level and model selection; consultato 13/10/2026"
[deprecazioni]: https://platform.claude.com/docs/en/about-claude/model-deprecations "Anthropic — Model deprecations; consultato 13/10/2026"
[mythos]: https://platform.claude.com/docs/en/models/mythos-5-1/overview "Anthropic — Claude Mythos 5.1; consultato 13/10/2026"
[cvp]: https://support.claude.com/en/articles/14604842-cyber-verification-program "Anthropic — Cyber Verification Program; consultato 13/10/2026"
[config-modelli]: https://code.claude.com/docs/en/model-config "Anthropic — Model configuration; consultato 13/10/2026"
[comandi]: https://code.claude.com/docs/en/commands "Anthropic — Commands; consultato 13/10/2026"
[cli]: https://code.claude.com/docs/en/cli-reference "Anthropic — CLI reference; consultato 13/10/2026"
[interattivo]: https://code.claude.com/docs/en/interactive-mode "Anthropic — Interactive mode; consultato 13/10/2026"
[impostazioni]: https://code.claude.com/docs/en/settings "Anthropic — Settings files and precedence; consultato 13/10/2026"
[effort-api]: https://platform.claude.com/docs/en/build-with-claude/effort "Anthropic — Effort; consultato 13/10/2026"
[fast]: https://code.claude.com/docs/en/fast-mode "Anthropic — Fast mode; consultato 13/10/2026"
[piani-prezzi]: https://claude.com/pricing "Anthropic — Plans and pricing; consultato 13/10/2026"
[max]: https://support.claude.com/en/articles/11049741-what-is-the-max-plan "Anthropic — Max plan; consultato 13/10/2026"
[pro-max]: https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan "Anthropic — Claude Code with Pro or Max; consultato 13/10/2026"
[enterprise-usage]: https://support.claude.com/en/articles/12005970-manage-usage-credits-for-team-and-seat-based-enterprise-plans "Anthropic — Usage credits and usage-based Enterprise distinction; consultato 13/10/2026"
[fable-piani]: https://support.claude.com/en/articles/15424964-claude-fable-models-on-your-plan "Anthropic — Fable models on your plan; consultato 13/10/2026"
[crediti-help]: https://support.claude.com/en/articles/17154008-monthly-api-credits-for-max-and-team-plans "Anthropic — Monthly API credits for Max and Team; consultato 13/10/2026"
[sdk-piano]: https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan "Anthropic — Agent SDK with your Claude plan; consultato 13/10/2026"
[subagent]: https://code.claude.com/docs/en/sub-agents "Anthropic — Custom subagents; consultato 13/10/2026"
[costi]: https://code.claude.com/docs/en/costs "Anthropic — Manage costs effectively; consultato 13/10/2026"

[workflow]: https://code.claude.com/docs/en/workflows "Anthropic — Dynamic workflows and Ultracode; consultato 13/10/2026"
[crediti-platform]: https://platform.claude.com/docs/en/about-claude/api-credits-for-subscribers "Anthropic — API credits for subscribers; consultato 13/10/2026"
