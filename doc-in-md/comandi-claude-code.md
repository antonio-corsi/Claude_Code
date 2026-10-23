# Comandi principali di Claude Code

## Gestione sessione
- `/help` — mostra l'aiuto e i comandi disponibili
- `/clear` — pulisce la cronologia della conversazione corrente
- `/config` — apre le impostazioni di configurazione (tema, modello, lingua dettatura, ecc.)
- `/theme` — cambia il tema dell'interfaccia
- `/fast` — attiva/disattiva la modalità fast (output più rapido)
- `/voice` — attiva/disattiva la modalità voce (hold, tap, off)

## Lavoro con il codice
- `/init` — inizializza un nuovo file CLAUDE.md con la documentazione del progetto
- `/code-review` — esegue una revisione del codice (diff corrente, PR, branch) con vari livelli di approfondimento
- `/simplify` — revisiona e semplifica il codice modificato (riuso, efficienza, pulizia)
- `/security-review` — esegue una revisione di sicurezza delle modifiche pendenti

## Automazione e pianificazione
- `/loop` — esegue un comando o prompt a intervalli regolari
- `/schedule` — crea, aggiorna o elenca agenti cloud pianificati (routine cron)

## Permessi e configurazione avanzata
- `/fewer-permission-prompts` — analizza le trascrizioni e aggiunge un allowlist per ridurre le richieste di permesso
- comandi di `update-config` — per modificare `settings.json` (permessi, variabili d'ambiente, hook)

## Produttività e contenuti
- `/spiega` — spiega in italiano semplice cosa fa un file, una cartella o del codice
- `/morning` — mostra o configura il briefing mattutino personale

## Browser e automazione desktop
- comandi legati a `claude-in-chrome` — automazione del browser Chrome
- comandi legati a `computer-use` — controllo del desktop (click, digitazione, screenshot)

## Assistenza e feedback
- `/help` — supporto su Claude Code
- segnalazione problemi: https://github.com/anthropics/claude-code/issues
