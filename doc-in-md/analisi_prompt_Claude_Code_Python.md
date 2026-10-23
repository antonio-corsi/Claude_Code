Il prompt chiede a Claude Code di **creare la struttura iniziale di un progetto Python, con ambiente di sviluppo, logging, test e documentazione già predisposti**. Il termine *scaffold* indica proprio questa “impalcatura”: una base organizzata sulla quale sviluppare l’applicazione.

**L’unica funzionalità applicativa iniziale è scrivere un messaggio di saluto nel log.** Gran parte del prompt serve a definire come organizzare, eseguire, verificare e documentare il futuro codice. filecitefile_00000000c86081f494d917023564ea65

È quindi una richiesta operativa: una volta fornito a Claude Code, gli chiede di **scrivere file e cartelle, installare dipendenze ed eseguire un test**.

## 1. Prima raccoglie tre informazioni

Il prompt impone a Claude Code di chiedere:

| Informazione | A cosa serve |
|---|---|
| **Nome del progetto/package** | Determina i nomi del progetto, del package Python e del comando con cui avviarlo. |
| **Versione iniziale**, con valore predefinito `0.0.1` | Viene registrata nel file `pyproject.toml`. |
| **Posizione**: cartella corrente oppure nuova sottocartella | Stabilisce dove creare tutti i file. |

Poi distingue tra **nome del progetto** e **nome importabile in Python**, adattando il testo inserito alle rispettive convenzioni.

Per esempio, con il nome **“Analisi Clienti”**:

| Elemento | Nome risultante |
|---|---|
| Progetto e nuova cartella, se richiesta | `analisi-clienti` |
| Package Python | `analisi_clienti` |
| Cartella del codice | `src/analisi_clienti/` |
| Comando dell’applicazione | `analisi_clienti` |

Per il package richiede minuscole, sostituzione dei caratteri non ammessi con underscore e rimozione delle cifre iniziali.

## 2. Crea un progetto Python installabile e organizzato

La struttura richiesta separa il codice applicativo, i test, la documentazione e gli script di servizio.

| File o cartella | Funzione |
|---|---|
| `src/<packagename>/` | Contiene il codice dell’applicazione. |
| `__init__.py` | Identifica il package; il prompt lo vuole vuoto. |
| `app.py` | Contiene la configurazione del logging e la funzione principale `main()`. |
| `__main__.py` | Permette di avviare il package con `python -m <packagename>`. |
| `tests/test_app.py` | Contiene il primo test automatico. |
| `tests/conftest.py` | Predispone la configurazione condivisa dei test. |
| `docs/` | Contiene la documentazione in Markdown. |
| `scripts/serve_docs.py` | Avvia l’anteprima della documentazione e ne salva i log. |
| `pyproject.toml` | Raccoglie metadati, dipendenze e configurazioni degli strumenti di sviluppo. |
| `mkdocs.yml` | Configura il sito della documentazione. |
| `README.md` | Spiega installazione, esecuzione, test e documentazione. |
| `.gitignore` | Specifica i file da escludere dal versionamento Git. |
| `.env.example`, `.env`, `.env.test` | Predispongono le variabili d’ambiente per sviluppo e test. |

Il risultato è un **package installabile nell’ambiente Python del progetto**, con un proprio comando di avvio. La versione dell’applicazione deve essere dichiarata soltanto in `pyproject.toml`, evitando copie dello stesso numero in più file. filecitefile_00000000c86081f494d917023564ea65

### Le scelte tecniche sono già fissate

Il prompt decide in anticipo lo stack:

| Strumento o scelta | Scopo |
|---|---|
| **Python ≥ 3.13** | Versione minima dichiarata dal progetto. |
| **uv** | Gestione dell’ambiente, delle dipendenze e dell’esecuzione dei comandi. |
| **uv_build** | Backend per costruire il package Python. |
| **Ruff** | Controllo statico del codice e formattazione. |
| **Loguru** | Registrazione dei messaggi e delle eccezioni nei log. |
| **pytest** | Esecuzione dei test. |
| **pytest-cov** | Misurazione della copertura dei test. |
| **pytest-env** | Impostazione delle variabili d’ambiente durante i test. |
| **MkDocs + Material** | Generazione di un sito di documentazione. |
| **mkdocstrings** | Produzione della documentazione API a partire dal codice e dalle docstring. |

Richiede inoltre **assenza di type hint**: è una scelta esplicita dell’autore del prompt.

## 3. Che cosa fa l’applicazione appena creata

La funzione `main()` svolge due operazioni:

1. Configura il logging.
2. Registra un messaggio come:

```text
Hello from analisi_clienti!
```

Questo serve a verificare che il package, il comando di avvio e il logging funzionino.

### Il logging va sia sul terminale sia su file

Il prompt prevede due destinazioni distinte:

| Destinazione | Comportamento |
|---|---|
| **Terminale, tramite `stderr`** | Mostra i messaggi a partire dal livello indicato da `LOG_LEVEL`, con valore predefinito `INFO`. |
| **File di log** | Registra i messaggi a partire da `DEBUG`, nel percorso indicato da `LOG_FILE`, con valore predefinito `app.log`. |

Il file viene ruotato al raggiungimento della dimensione configurata di **50 KB**, conservando **un file precedente**, senza compressione.

Un dettaglio utile: **`LOG_LEVEL` controlla soltanto il livello del terminale**. Nel codice richiesto, il livello del file rimane fissato a `DEBUG`.

### Le impostazioni di sviluppo si caricano esplicitamente

Il prompt crea `.env` con:

```dotenv
LOG_LEVEL=DEBUG
LOG_FILE=app.log
```

Tuttavia, **la semplice presenza di `.env` non basta a caricarlo**. Il comando previsto è:

```bash
uv run --env-file .env analisi_clienti
```

Il comando senza `--env-file`:

```bash
uv run analisi_clienti
```

usa invece le variabili eventualmente già presenti nell’ambiente del processo e, in loro assenza, i valori predefiniti del codice.

Quindi il commento “production defaults” nel prompt indica soprattutto l’uso di quei valori predefiniti; non costituisce una configurazione completa per la produzione.

## 4. Predispone un test automatico e la copertura

Il test iniziale richiesto è molto semplice:

1. Chiama `main()`.
2. Cattura ciò che viene scritto su `stderr`.
3. Verifica che sia presente il messaggio di saluto.

È un controllo utile per verificare l’avvio della base di progetto. La futura logica applicativa dovrà avere test aggiuntivi.

Inoltre, una *fixture* automatica modifica `LOG_FILE` durante ogni test, indirizzandolo verso una cartella temporanea. In questo modo, **i test non scrivono nel normale `app.log` del progetto**.

Il prompt configura anche:

- la misurazione della copertura dei rami del codice;
- la visualizzazione delle parti non coperte;
- una soglia minima di copertura dell’**80%**;
- l’esclusione di alcuni elementi, tra cui `__main__.py`.

**La soglia dell’80%, però, è soltanto predisposta: la verifica finale richiesta dal prompt non la applica**, perché esegue `uv run pytest` senza attivare la copertura. Per misurarla bisogna usare il comando separato `uv run pytest --cov`, già previsto nel README. genui{"citation":{"ref":"turn17view1"}}

## 5. Prepara un piccolo sito di documentazione

La documentazione è articolata in tre parti:

| Pagina | Contenuto |
|---|---|
| **Home** | Presentazione iniziale del progetto. |
| **Usage** | Installazione, avvio e variabili d’ambiente. |
| **API Reference** | Documentazione ricavata dal codice e dalle docstring. |

La configurazione grafica richiesta comprende tema chiaro/scuro, ricerca, copia dei blocchi di codice e navigazione.

Lo script `scripts/serve_docs.py` aggiunge una comodità specifica per lavorare con Claude Code: quando viene avviato, **mostra i messaggi del server MkDocs nel terminale e contemporaneamente li scrive in `mkdocs.log`**.

Claude Code può così leggere quel file per esaminare eventuali errori della documentazione. Lo script, di per sé, avvia MkDocs e raccoglie l’output; non contiene chiamate a Claude.

## 6. Quali operazioni esegue davvero alla fine

Questa è una distinzione importante per comprendere l’effetto del prompt.

| Operazione | Che cosa richiede il prompt |
|---|---|
| Creazione dei file e delle cartelle | **Eseguirla.** |
| Download del modello di `.gitignore` dal repository pubblico `github/gitignore` | **Eseguirlo** e aggiungere le esclusioni specifiche. |
| Preparazione dell’ambiente con `uv sync` | **Eseguirla.** |
| Primo test con `uv run pytest` | **Eseguirlo.** |
| Test con copertura | Documentare il comando per l’utente. |
| Controlli e formattazione con Ruff | Installare e configurare lo strumento; non ne richiede esplicitamente l’esecuzione finale. |
| Anteprima della documentazione | Creare lo script e suggerire all’utente di avviarlo. |
| Generazione della documentazione statica | Documentare il comando `uv run mkdocs build`. |
| Commit di `uv.lock` | Ricordare all’utente di farlo. |

Nel normale funzionamento di uv, `uv sync` prepara l’ambiente virtuale del progetto, generalmente nella cartella `.venv`, installa il progetto e le dipendenze e genera o aggiorna `uv.lock`. Il gruppo di dipendenze `dev` viene incluso per impostazione predefinita. Questo comporta normalmente download dalla rete, quando i componenti necessari non sono già disponibili nella cache. genui{"citation":{"refs":["turn13view2","turn13view1"]}}

Il prompt prepara quindi anche l’uso di Git, ma **non richiede esplicitamente `git init`, un commit o la creazione di un repository su GitHub**. Analogamente, il riferimento a “clone the repository” nel README è un’istruzione destinata a chi userà in seguito il progetto.

## 7. I punti che rivedrei prima di usarlo come standard

L’impostazione è utile, ma l’espressione *best practice* nel titolo va letta come una proposta dell’autore. Ho individuato alcuni punti concreti da migliorare.

### A. La verifica finale è incompleta rispetto agli strumenti predisposti

Il prompt installa Ruff, configura la copertura e prepara MkDocs, ma alla fine controlla soltanto il test del saluto.

Per validare anche quelle parti, una revisione potrebbe aggiungere:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest --cov
uv run mkdocs build --strict
```

Questi sarebbero **controlli aggiuntivi rispetto al prompt allegato**.

### B. `@logger.catch` può nascondere un fallimento al sistema che avvia il programma

Il prompt chiede di decorare `main()` con:

```python
@logger.catch
```

Loguru registra l’eccezione, ma il comportamento predefinito è `reraise=False`: l’eccezione viene intercettata senza essere rilanciata. Con l’avvio previsto, il programma potrebbe quindi registrare un errore e terminare comunque con **codice di uscita 0**, che per una shell o un’automazione significa successo.

Se si vuole che l’errore si propaghi, una scelta possibile è:

```python
@logger.catch(reraise=True)
```

È un dettaglio rilevante per script batch, pipeline e applicazioni eseguite da altri programmi. genui{"citation":{"ref":"turn16view1"}}

### C. Il requisito minimo di `pytest-env` è troppo permissivo

La configurazione:

```toml
[tool.pytest_env]
env_files = [".env.test"]
```

è supportata dalle versioni attuali. Tuttavia, il caricamento dei file `.env` è stato introdotto in **pytest-env 1.3.0**, mentre il prompt consente `pytest-env>=1.1`.

Per rendere coerente la dipendenza dichiarata con la funzionalità utilizzata, il requisito dovrebbe essere almeno:

```toml
"pytest-env>=1.3"
```

Un’installazione nuova può comunque scegliere una versione recente e funzionare; il problema è che il vincolo ammette anche versioni troppo vecchie. genui{"citation":{"ref":"turn16view0"}}

### D. La configurazione dei test non è interamente riproducibile dopo un clone

`.env.test` viene creato sul primo computer, ma escluso da Git. Chi clona il progetto non riceverà quindi quel file.

Nelle versioni attuali di pytest-env, un file configurato ma mancante viene ignorato silenziosamente: il primo test potrebbe passare ugualmente, usando però un ambiente diverso. Poiché qui l’unica impostazione è `LOG_LEVEL=DEBUG`, sarebbe semplice dichiararla direttamente in `pyproject.toml`, oppure fornire un modello dedicato. genui{"citation":{"ref":"turn9search0"}}

### E. La trasformazione dei nomi presenta qualche caso limite

Con nomi normali, come `Analisi Clienti`, la trasformazione è coerente. Con un nome come `123demo`, invece:

- il progetto potrebbe chiamarsi `123demo`;
- il package Python diventerebbe `demo`;
- `uv_build`, in assenza di una configurazione esplicita, ricaverebbe il nome del modulo dal nome del progetto.

Per gestire questa differenza in modo affidabile, il prompt dovrebbe chiedere di impostare anche `module-name` nella configurazione del backend quando necessario. genui{"citation":{"ref":"turn16view2"}}

### F. Ci sono due dettagli formali da ripulire

Il prompt chiama lo strumento per le domande `askuser`; il nome documentato dello strumento integrato è **`AskUserQuestion`**. L’intenzione è comprensibile, ma usare il nome corretto rende l’istruzione più precisa. genui{"citation":{"ref":"turn17view0"}}

Inoltre, l’allegato contiene molti caratteri di escape Markdown, per esempio negli underscore e nei delimitatori dei blocchi di codice. Li ripulirei prima di riutilizzarlo, soprattutto per evitare che gli esempi siano copiati letteralmente nei file.

---

**Lo considererei una buona base per standardizzare l’avvio di piccoli progetti Python**, soprattutto nel passaggio da script o notebook isolati a codice organizzato, installabile e verificabile. Il suo valore principale è fissare fin dall’inizio convenzioni condivise per struttura, dipendenze, logging, test e documentazione. Le funzionalità dell’applicazione — analisi dei dati, elaborazioni, integrazioni o AI — andranno poi sviluppate dentro questa struttura.
