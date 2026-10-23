# Piani di abbonamento Claude (ottobre 2026)

Oct 19, 2026 · @Antonio

I prezzi sono pubblicati in dollari USA (la pagina ufficiale non riporta prezzi in euro), valgono per la sottoscrizione via web — sugli store mobili possono variare — e sono dichiarati soggetti a modifica a discrezione di Anthropic.

## Tabella riassuntiva

| Piano | Prezzo | Limiti d'uso | Claude Code |
| --- | --- | --- | --- |
| **Free** | 0 $ | Uso base, finestra che si azzera ogni 5 ore | No |
| **Pro** | 17 $/mese con fatturazione annuale (200 $ anticipati) · 20 $/mese mensile | Almeno 5× il Free per sessione, più limiti settimanali | Sì |
| **Max 5x** | 100 $/mese (solo mensile) | 5× il Pro per sessione | Sì |
| **Max 20x** | 200 $/mese (solo mensile) | 20× il Pro per sessione | Sì |
| **Team** | Posto Standard: 20 $/posto/mese annuale (25 $ mensile) · Posto Premium: 100 $ annuale (125 $ mensile) | Standard: superiore al Pro · Premium: 5× lo Standard | Sì |
| **Enterprise** | 20 $/posto/mese (annuale, minimo 20 posti) + consumo fatturato a tariffe API | Scala col consumo; gli admin impostano tetti di spesa per utente e organizzazione | Sì |

Team è pensato per gruppi da 2 a 150 posti, con posti Standard e Premium mescolabili.

## Piani individuali: offerta tecnica incrementale

**Free** — Modelli Sonnet e Haiku; fino a 5 Projects; memoria, connettori, ricerca web, creazione file ed esecuzione codice, Artifacts (Design, Slides, Docs), voice mode, skills; contesto fino a 1M di token (varia per modello, come su tutti i piani). Niente Claude Code né Research.

**Pro** (aggiunge al Free) — Opus incluso; Fable accessibile tramite *crediti d'uso* (consumo extra fatturato a tariffe API quando si esauriscono i limiti); **Claude Code** su tutte le superfici; Research; pianificazione e handoff dei task; Claude in Chrome, Claude per Microsoft 365/Outlook, Claude Science, Dashboards (beta). Nessun controllo amministrativo; training sui dati disattivabile (opt-out).

**Max 5x / 20x** (aggiunge al Pro) — Limiti 5× o 20×; **Fable incluso fino al 50% dei limiti settimanali**; crediti API inclusi: 100 $/mese (5x) o 200 $/mese (20x); accesso prioritario nelle ore di punta e accesso anticipato alle funzioni nuove. È il piano tipico per chi usa Claude Code in modo intensivo dalla CLI.

## Piani per organizzazioni: Team ed Enterprise

**Team** (2–150 posti, Standard e Premium mescolabili) — Tutto quanto sopra più: condivisione di Projects, enterprise search nei connettori, Motion (beta), fino a 500 $/mese di crediti API *condivisi* dal team; Fable al 50% dei limiti settimanali sui posti Premium. Lato amministrazione: SSO, verifica del dominio, fatturazione centralizzata, controlli admin sui connettori, analytics d'uso, skills a livello di organizzazione; **nessun training sui dati per impostazione predefinita**. Non include: SCIM, audit log, Compliance API, retention personalizzata, offerta HIPAA. Pagamento con carta, mensile o annuale (niente bonifico/fattura).

**Enterprise** — Modello nuovo: quota posto bassa (20 $) ma **consumo fatturato a tariffe API**, con tetti di spesa impostabili dagli admin. Tutti i modelli inclusa Fable; tutto il Team più Claude Security (beta) e il pacchetto completo di governance: SSO, permessi granulari (RBAC), SCIM, audit log, Compliance API, retention personalizzata, controlli di rete e IP allowlisting, offerta HIPAA-ready, inference hooks. Fatturazione annuale (carta o ACH in self-serve; con il sales anche fattura con termini di pagamento).

## Note pratiche per Claude Code

- Per usare Claude Code individualmente il **Pro** è il punto d'ingresso; **Max** è il piano tipico per l'uso intensivo dalla CLI.
- In alternativa all'abbonamento, Claude Code (CLI, VS Code, JetBrains) funziona anche con un account **Console/API a consumo**: si paga per token, senza canone mensile.

## Fonti

Verificate il 19 ottobre 2026:

- [Pricing — claude.com](https://claude.com/pricing)
- [Che cos'è il piano Max — Supporto Claude](https://support.claude.com/it/articles/11049741-che-cos-e-il-piano-max)
- [Che cos'è il piano Pro — Supporto Claude](https://support.claude.com/it/articles/8325606-che-cos-e-il-piano-pro)
