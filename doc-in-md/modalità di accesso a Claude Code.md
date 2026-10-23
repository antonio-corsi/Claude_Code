# Modalità di accesso a Claude Code

Oct 19, 2026 · @Antonio

Le «modalità di accesso» — la documentazione le chiama *superfici* (surfaces) — sono sei, più alcune integrazioni. Tutte si collegano allo stesso motore, quindi i file `CLAUDE.md`, le impostazioni e i server MCP del repository valgono ovunque; quasi tutte richiedono un abbonamento Claude o un account Console, mentre CLI, VS Code e JetBrains supportano anche provider di terze parti.

## Le sei superfici a confronto

| Superficie | Caratteristiche | Pro | Contro / limiti |
| --- | --- | --- | --- |
| **Terminale (CLI)** | Interfaccia completa e originaria; installer nativo (PowerShell: `irm https://claude.ai/install.ps1 \| iex`; macOS/Linux/WSL: `curl … install.sh`; anche Homebrew, WinGet, apt/dnf); avvio con `claude` nel progetto; print mode `-p` per script e pipe | Insieme completo delle funzioni; componibile e scriptabile (pipe, `-p`, CI); leggero, funziona anche via SSH; l'installazione nativa si aggiorna da sola | Niente interfaccia grafica, diff come testo; richiede dimestichezza col terminale; su Windows nativo serve Git for Windows per il tool Bash (altrimenti PowerShell) |
| **Estensione VS Code (e Cursor)** | Pannello nell'editor con diff inline, @-menzioni di file, revisione dei piani, cronologia conversazioni | Revisione visuale delle modifiche nel contesto del codice; indicatore cliccabile per cambiare permission mode; naturale per chi vive nell'editor | Legata all'editor e al progetto aperto; poco adatta ad automazione; `claudeCode.initialPermissionMode` accetta tutti i valori tranne `auto` |
| **Plugin JetBrains** | Plugin per IntelliJ IDEA, PyCharm, WebStorm ecc., con diff interattivi e condivisione della selezione come contesto | La comodità dell'IDE per chi usa la suite JetBrains (es. PyCharm per Python) | Richiede la CLI installata separatamente: il plugin è solo l'interfaccia (installazione dal Marketplace + riavvio IDE) |
| **App desktop** | Applicazione autonoma (macOS, Windows x64/ARM64; Ubuntu/Debian in beta via apt) che include Claude Code; diff visuali, sessioni affiancate, attività pianificate locali, sessioni cloud; dal terminale: `/desktop` | La via più comoda senza terminale; sessioni parallele e pianificate; accesso diretto a file e strumenti locali; non serve installare la CLI | Richiede abbonamento a pagamento; su Linux in beta; handoff `/desktop` solo macOS e Windows x64, con abbonamento claude.ai |
| **Web — claude.ai/code** | Claude Code nel browser, zero installazione; task lunghi da lanciare e riprendere, repo non in locale, più task in parallelo (coordinabili in un Project); verso il terminale con `claude --teleport` | Zero setup; i task girano nel cloud anche a computer spento; parallelismo; si parte da qualunque macchina | Ambiente cloud isolato: niente accesso ai file e strumenti locali (si lavora su repository collegati); il teleport richiede abbonamento claude.ai |
| **App mobile (iOS/Android)** | Le stesse sessioni web dall'app Claude; Dispatch manda un task al desktop, Remote Control continua dal telefono una sessione locale | Avvio e supervisione ovunque; continuità tra dispositivi | Adatta a lanciare e rivedere più che a sviluppare in modo interattivo (schermo piccolo per i diff); stessi vincoli dell'ambiente cloud |

## Altre vie d'accesso (integrazioni)

Non sono sessioni interattive, ma modi di portare Claude Code dentro pipeline e strumenti di team.

| Integrazione | A cosa serve |
| --- | --- |
| GitHub Actions / GitLab CI-CD | Review del codice e triage delle issue nelle pipeline |
| GitHub Code Review | Revisione automatica di ogni pull request |
| Slack | Menzione `@Claude` con un bug report → torna una pull request |
| Chrome | Debug di web app direttamente nel browser |
| Channels | Eventi in ingresso da Telegram, Discord, iMessage o webhook propri |
| Agent SDK | Costruire agenti personalizzati sopra il motore di Claude Code |

## Sintesi operativa

Per il lavoro quotidiano e la didattica hands-on la scelta tipica è CLI + estensione per l'editor; l'app desktop serve a chi vuole la via grafica completa senza terminale; web e mobile coprono i task lunghi e il lavoro «da fuori»; le integrazioni portano Claude Code dentro pipeline e strumenti di team.

## Fonti

Documentazione ufficiale, verificata il 19 ottobre 2026:

- [Overview — Claude Code](https://code.claude.com/docs/en/overview)
- [Permission modes](https://code.claude.com/docs/en/permission-modes)
