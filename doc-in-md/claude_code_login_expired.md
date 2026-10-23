# Claude Code — "Login expired · Please run /login"

## Cosa significa

Claude Code si autentica tramite OAuth: al login riceve un **access token** (un "pass" di breve durata) e un **refresh token** (che serve a rinnovare il pass automaticamente). Il messaggio "Login expired" indica che il token è scaduto e il rinnovo automatico non è più possibile.

## Durate tipiche

Non documentate ufficialmente, ma osservate dagli utenti:

- **Access token**: circa 8 ore (talvolta 12–24 ore). Viene rinnovato in automatico in background mentre si usa Claude Code — normalmente non ci si accorge di nulla.
- **Refresh token**: scade lato server dopo circa 24 ore di inattività su quella macchina. A quel punto il rinnovo automatico fallisce e serve riautenticarsi.

## In pratica

- **Uso quotidiano** → login quasi mai richiesto.
- **Un giorno o più senza usare Claude Code** → al rientro chiede `/login`. È un comportamento normale, non un errore del PC.

## Soluzione

1. Nel prompt di Claude Code digitare `/login`.
2. Completare l'autenticazione nel browser (se non si apre da solo, copiare e incollare il link mostrato nel terminale).
3. Nulla va perso: impostazioni, progetti e cronologia restano intatti.

## Fonti

- GitHub issue [#72017](https://github.com/anthropics/claude-code/issues/72017) — access token ~8h, refresh non automatico in alcuni casi
- GitHub issue [#35221](https://github.com/anthropics/claude-code/issues/35221) — refresh token scade dopo ~24h di inattività
- [InventiveHQ — Fix OAuth token expired](https://inventivehq.com/knowledge-base/claude/how-to-fix-oauth-token-has-expired)
