# I mode di Claude Code (ottobre 2026)

Oct 19, 2026 · @Antonio

## Premessa: cosa indica «mode»

In Claude Code la parola *mode* indica soprattutto i **permission mode**: le modalità che stabiliscono quali azioni Claude può eseguire da solo e per quali deve invece chiederci conferma. La documentazione chiama però «mode» anche altre cose — modalità di avvio, di editing del prompt, di rendering — raccolte più avanti. La novità principale: i permission mode sono passati da quattro a **sei** e il nuovo `auto` è diventato la modalità di partenza predefinita.

## I sei permission mode

Ogni modalità definisce il perimetro di ciò che viene eseguito senza richiesta di conferma.

| Valore di configurazione | Etichetta nell'interfaccia | Cosa esegue senza chiedere conferma |
| --- | --- | --- |
| `default` (alias `manual`) | Manual | Solo letture |
| `acceptEdits` | Edit automatically | Letture, modifiche ai file nelle directory di lavoro e comandi filesystem comuni (`mkdir`, `touch`, `rm`, `mv`, `cp`, `sed`) |
| `plan` | Plan | Letture più alcuni comandi shell; nessuna modifica al codice finché il piano non viene approvato |
| `auto` | Auto | Tutto, ma un *classificatore* (un secondo modello che valuta ogni azione prima di eseguirla) blocca quelle rischiose; le regole «ask» esplicite continuano a chiedere conferma |
| `dontAsk` | — | Solo strumenti pre-approvati e azioni di sola lettura; ciò che chiederebbe conferma viene negato (pensato per gli script) |
| `bypassPermissions` | Bypass permissions | Tutto; da usare solo in container o VM |

L'Agent SDK usa gli stessi valori: `permission_mode` in Python, `permissionMode` in TypeScript.

## Come si cambia modalità

La precedenza è: flag di lancio, poi file di settings, poi default incorporato.

- **Shift+Tab** cicla Manual → acceptEdits → Plan, più bypass se abilitato al lancio e auto quando disponibile; `dontAsk` non compare mai nel ciclo.
- **Flag di avvio**: `claude --permission-mode <valore>`.
- **Settings**: `"permissions": { "defaultMode": "<valore>" }`. Attenzione: `auto` e `bypassPermissions` nei file di progetto (`.claude/settings.json`) vengono ignorati e vanno in `~/.claude/settings.json` o nei managed settings.
- **VS Code**: clic sull'indicatore di modalità in basso nel riquadro del prompt; la modalità iniziale si imposta con `claudeCode.initialPermissionMode` (accetta tutti i valori tranne `auto`).

## Novità rispetto al vecchio elenco

- `auto` è la modalità nuova: dalla v2.1.283 è quella di partenza predefinita per terminale e VS Code (prima lo era solo sui piani Pro, Max e Team); gli amministratori possono disabilitarla con `disableAutoMode` nei managed settings.
- Il flag `--enable-auto-mode` è stato rimosso nella v2.1.111: si usa `--permission-mode auto`.
- `manual` è accettato come alias di `default` dalla v2.1.200.
- `--dangerously-skip-permissions` equivale a `--permission-mode bypassPermissions`; `--allow-dangerously-skip-permissions` aggiunge bypass al ciclo Shift+Tab senza partirci.
- Anche in bypass restano attive le deny rule, le ask rule esplicite e la protezione di `rm`/`rmdir` sui percorsi critici; il flag è rifiutato se lanciato come root o con sudo.

## Plan mode: comportamento attuale

In Plan mode Claude legge i file, esplora con comandi shell e scrive un piano, ma non modifica il codice finché il piano non viene approvato (strumento `ExitPlanMode`).

- **Attivazione**: Shift+Tab, `/plan` davanti a un singolo prompt, `--permission-mode plan` oppure `permissions.defaultMode: "plan"`; un altro Shift+Tab esce senza approvare.
- **Menu di approvazione**: «Yes, and use auto mode», «Yes, manually approve edits», «No, keep planning»; Ctrl+G apre il piano nell'editor.
- **Avvertenza documentata**: nel terminale interattivo con bypass disponibile il blocco delle modifiche non è imposto tecnicamente; vale invece in `-p`, nell'Agent SDK e nel pannello VS Code.
- **Correlato**: `/model opusplan` usa Opus per pianificare e Sonnet per eseguire.

## Altre cose chiamate «mode» nella documentazione

| Nome | Cos'è | Come si attiva |
| --- | --- | --- |
| Interactive mode | La sessione live predefinita in cui si digitano i prompt | `claude` |
| Print mode (non-interactive) | Un prompt, una risposta, poi esce; per script e CI | `claude -p "..."` |
| Bare mode | Avvio in print mode che salta hook, skill, plugin, server MCP e CLAUDE.md; diventerà il default di `-p` | `--bare` |
| Safe mode | Disattiva tutte le personalizzazioni per diagnosticare un setup rotto | `--safe-mode` |
| Restricted mode | Blocca esecuzione comandi e accesso ai file, per macchine condivise | `--restricted` |
| Vim editor mode | Tasti vim nel prompt (NORMAL/INSERT/VISUAL) | `/config` → Editor mode, o `"editorMode": "vim"` |
| Shell mode | Esegue direttamente un comando shell digitato | Prompt che inizia con `!` |
| Extended thinking | Ragionamento esteso prima della risposta; non disattivabile su Opus/Sonnet/Haiku 5.5 e sui modelli Fable | Alt+T (Option+T su macOS); default in `/config` |
| Effort level | Quanto sforzo di ragionamento spende il modello: `low`, `medium`, `high`, `xhigh`, `max`, `ultracode` | `/effort`, `--effort` o il setting `effortLevel` |
| Fast mode | Risposte Opus più veloci a prezzo maggiore (research preview); non cambia i permessi | `/fast`, Alt+O (Option+O su macOS) |
| Output styles | Istruzioni che cambiano tono e formato: Default, Proactive, Concise, Explanatory, Learning — ancora supportati | `/output-style <stile>` |
| Sandbox modes | Auto-allow vs regular permissions per il sandbox a livello di sistema operativo dei comandi Bash; cosa diversa dai permission mode | `/sandbox`, scheda Mode |
| Screen reader mode | Output lineare per lettori di schermo | `--ax-screen-reader` |
| Ultracode | Claude scrive script che orchestrano molti subagent (agenti ausiliari) per ogni compito | `/effort ultracode` |

Il Background Bash (Ctrl+B per mandare un comando in background, `/tasks` per elencarli) non è formalmente un «mode», ma viene spesso cercato come tale.

## Avvertenze e fonti

Per le sessioni `claude -p` e Agent SDK la documentazione è in conflitto sulla modalità di partenza (auto vs Manual dalla v2.1.302): con `claude --version` si verifica quale build è in uso.

Fonti ufficiali (code.claude.com, consultate il 19 ottobre 2026):

- [Permission modes](https://code.claude.com/docs/en/permission-modes)
- [Permissions](https://code.claude.com/docs/en/permissions)
- [Interactive mode](https://code.claude.com/docs/en/interactive-mode)
- [Headless / print mode](https://code.claude.com/docs/en/headless)
- [CLI reference](https://code.claude.com/docs/en/cli-reference)
- [Output styles](https://code.claude.com/docs/en/output-styles)
- [Sandboxing](https://code.claude.com/docs/en/sandboxing)
- [Fast mode](https://code.claude.com/docs/en/fast-mode)
