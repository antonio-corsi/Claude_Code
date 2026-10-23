# Claude Code: configurazioni e settings — il subset essenziale per chi inizia

> Sintesi per utenti alle prime armi, estratta dal riferimento completo `claude-code-file-di-configurazione.md`.
> Verificata sulla documentazione ufficiale (code.claude.com/docs) in data **20 ottobre 2026**.

---

## Il modello mentale in una frase

In Claude Code esistono **due famiglie di configurazione**, da non confondere:

- **Impostazioni** (file **JSON** come `settings.json`): regole che il programma **fa rispettare** — permessi, variabili d'ambiente, modello;
- **Istruzioni** (file **Markdown** come `CLAUDE.md`): testo che Claude **legge come guida** — convenzioni, comandi del progetto, stile.

---

## I quattro file da conoscere subito

| File | Dove | A cosa serve |
|---|---|---|
| `CLAUDE.md` | radice del progetto | Le istruzioni del progetto, caricate a ogni sessione: comandi di build/test, convenzioni, architettura. Tenerlo sotto ~200 righe; si modifica con `/memory`. Si committa in git. |
| `~/.claude/settings.json` | cartella home (su Windows: `%USERPROFILE%\.claude\`) | Le impostazioni personali valide in **tutti** i progetti (tema, modello, permessi che si concedono sempre). |
| `.claude/settings.json` | dentro il progetto | Le impostazioni condivise col **team**: si committa, così chi clona il repository le riceve. |
| `.claude/settings.local.json` | dentro il progetto | Gli override **personali** per quel progetto, fuori da git. È il file dove Claude Code salva da solo le approvazioni quando si risponde "Sì, e non chiedere più" a un permesso. |

Dettaglio da sapere: **l'installazione non crea nessun file**. Compaiono la prima volta che si cambia qualcosa da `/config` o si approva un permesso in modo permanente — quindi non allarmarsi se all'inizio le cartelle sono vuote.

---

## La regola d'oro della precedenza

Quando la stessa chiave è impostata in più punti, vince il livello più alto:

**impostazioni aziendali → riga di comando (`--settings`, solo per quella sessione) → locale di progetto → progetto condiviso → utente**

Con una sfumatura: le chiavi *a lista* (come i permessi `allow`) **si sommano** tra i livelli; le chiavi *a valore singolo* (come `model`) vengono sovrascritte.

---

## I permessi, la parte più usata

Nella chiave `permissions` si scrivono regole `allow` / `ask` / `deny` con pattern sugli strumenti. Esempio minimo, da mettere in `~/.claude/settings.json`:

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "permissions": {
    "allow": ["Bash(npm test *)", "Bash(git diff *)"],
    "deny": ["Read(./.env)", "Read(./.env.*)"]
  }
}
```

Significato: eseguire test e `git diff` senza chiedere ogni volta; vietare la lettura dei file `.env` (dove stanno i segreti). La riga `$schema` dà autocompletamento e validazione in VS Code.

---

## Quattro trappole comuni

1. **JSON stretto**: niente commenti `//` né virgole finali — un refuso rende il file "rotto" e Claude Code lo segnala all'avvio.
2. **`~/.claude.json` ≠ `~/.claude/settings.json`**: il primo (nella home, fuori dalla cartella `.claude/`) è lo *stato interno* dell'app (login, fiducia dei progetti, server MCP personali) e **non va modificato a mano**.
3. **`.claudeignore` non esiste**: per nascondere file sensibili si usano le regole `deny` su `Read`, come nell'esempio sopra.
4. **Privacy**: le trascrizioni delle sessioni vengono salvate in chiaro sotto `~/.claude/` — se un comando stampa una credenziale, quella finisce su disco.

---

## I comandi da ricordare

- `/config` — cambiare le opzioni personali da dentro la sessione;
- `/status` — vedere quali file di impostazioni sono stati caricati;
- `/memory` — aprire e modificare CLAUDE.md;
- `claude doctor` — diagnosticare un file di impostazioni che non funziona.

---

## E poi?

Questo è il nucleo per partire. Tutto il resto — regole (`rules/`), skill, subagenti, server MCP, stili di output, livello enterprise — si può introdurre in un secondo momento ed è documentato nel riferimento completo `claude-code-file-di-configurazione.md`.

**Fonti principali:**

- Settings files and precedence — <https://code.claude.com/docs/en/settings>
- Explore the .claude directory — <https://code.claude.com/docs/en/claude-directory>
- Configure permissions — <https://code.claude.com/docs/en/permissions>
- Manage Claude's memory — <https://code.claude.com/docs/en/memory>
