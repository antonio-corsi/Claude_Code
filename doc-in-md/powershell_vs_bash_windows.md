# Bash su Windows vs PowerShell — pro e contro

## Premessa terminologica

- **PowerShell**: la shell moderna nativa di Windows. Non lavora passando testo tra i comandi ma **oggetti** .NET strutturati (un file non è una riga di testo, è un oggetto con proprietà: nome, dimensione, data).
- **Bash su Windows** non è una cosa sola, ma due:
  - **Git Bash**: versione "portata" di Bash inclusa in Git for Windows. Gira direttamente su Windows ed emula l'ambiente Unix (`ls`, `grep`, `sed`).
  - **WSL** (Windows Subsystem for Linux): un vero Linux che gira dentro Windows. È il Bash "autentico", con tutto l'ecosistema Linux, ma è un mondo separato con un suo filesystem.

## PowerShell

### Pro
- **Nativo**: già installato, zero setup, integrazione perfetta con Windows (registro, servizi, Active Directory, COM, .NET).
- **Oggetti invece di testo**: `Get-Process | Where-Object CPU -gt 100` filtra per proprietà senza "parsare" colonne di testo con `awk`/`cut`. Meno fragile, meno errori.
- **Sintassi leggibile**: comandi autoesplicativi (`Get-ChildItem`, `Copy-Item`) con alias brevi (`ls`, `cp`).
- **Percorsi Windows gestiti correttamente**: `C:\Users\...` funziona senza problemi di backslash.
- **JSON integrato**: `ConvertFrom-Json` è incluso; in Bash serve installare `jq`.

### Contro
- **Verboso**: gli one-liner tendono a essere più lunghi dei corrispondenti Bash.
- **Ecosistema didattico/open-source minoritario**: tutorial, README, risposte su Stack Overflow danno quasi sempre comandi Bash; chi usa PowerShell deve continuamente "tradurre".
- **Non portabile verso i server**: server, container e cloud sono in larga parte Linux; gli script PowerShell non ci girano (PowerShell Core per Linux esiste, ma è poco usato lì).
- Alcune stranezze storiche: execution policy che blocca gli script, differenze tra PowerShell 5.1 e 7.

## Bash (Git Bash / WSL)

### Pro
- **Lingua franca del mondo tecnico**: documentazione, esempi AI/ML, repository GitHub, pipeline CI/CD, Docker — tutto assume Bash (Colab, server GPU, HuggingFace inclusi).
- **Conciso e componibile**: pipe di testo (`grep | sort | uniq -c`) potentissime per manipolazioni rapide.
- **Competenza trasferibile**: vale identica su Mac, Linux, server remoti.
- **Con WSL hai un Linux vero**: `apt install`, supporto GPU/CUDA (WSL2), ambienti identici a quelli di produzione.

### Contro
- **Non nativo**: va installato (Git for Windows o WSL); se manca, i comandi falliscono.
- **Frizione sui percorsi**: `C:\Users` diventa `/c/Users` (Git Bash) o `/mnt/c/Users` (WSL); i backslash vengono interpretati come caratteri di escape.
- **Git Bash è un'emulazione parziale**: alcuni comandi mancano o si comportano diversamente dal Linux vero.
- **WSL è un mondo a parte**: due filesystem, due Python, due set di pacchetti; accesso incrociato ai file lento.
- **Fragilità del testo**: tutto è stringhe; il parsing con `awk`/`sed` si rompe facilmente su spazi, nomi strani, encoding.

## Quale scegliere

| Scenario | Scelta consigliata |
|---|---|
| Automazione su Windows (status line, script locali, gestione file) | **PowerShell** — nativo, robusto, niente problemi di percorsi |
| Seguire tutorial, repo GitHub, lavorare come su un server Linux | **WSL** — vale la pena installarlo, anche per sfruttare CUDA sulla GPU |
| Solo comandi Unix occasionali + Git | **Git Bash** — leggero, arriva "gratis" con Git for Windows |

Non è una scelta esclusiva: molti sviluppatori Windows usano PowerShell per il sistema e WSL/Git Bash per il lavoro "stile Linux".
