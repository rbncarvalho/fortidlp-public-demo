# Pré-flight — checklist de 5 minutos

> Abrir esta página antes de entrar em reunião. Cada use case também tem um fluxograma e preparação própria no topo do ficheiro.

- [ ] **Agent Healthy:** Windows 11, FortiDLP **12.8.1**, sincronizado.
- [ ] **Policies/Templates 8.7.0**, `PG-FortiDLP-Demo` Enabled e publicado.
- [ ] **Scope:** label **`dlp_rc_demos` tanto na máquina como no utilizador**.
- [ ] **Edge:** extensão FortiDLP ativa e browser monitoring ON.
- [ ] **Word:** `source.docx` no OneDrive, `classified.docx` com MPIP, DOCX com dados **sintéticos**.
- [ ] **UC05:** New Outlook, Email Add-in e email monitoring prontos.
- [ ] **UC08:** M365 Cloud Connector + Teams saudáveis e app FortiDLP instalada no Teams; partilha de teste pronta.
- [ ] **UC09:** fechar ChatGPT Desktop e subprocessos antes do teste de Kill.
- [ ] **UC10:** Thunderbird instalado; `Start-Process 'ms-outlook:'` abre Outlook nativo.
- [ ] **UC11:** destino **autorizado**, preferencialmente apresentar deteção prévia em vez de scan longo.
- [ ] Deteções confirmadas para UC01, UC05, UC06, UC08, UC09, UC10 e UC11 abertas em separadores de backup.
- [ ] Policies de debug antigas desativadas para evitar duplos popups.

## Falhas a antecipar

| UC | Falha típica | Verificação rápida |
|---|---|---|
| 01 | Origem corporativa não preservada | Data Lineage / File Origin |
| 02 | Clipboard não limpo | `Empty Clipboard — Succeeded` |
| 03 | Label ausente | Word + Content Inspection |
| 04 | Paste em app não abrangida | Application name na Detection |
| 05 | Add-in ausente | New Outlook + Email Monitoring |
| 06 | Prompt não bloqueado | Browser extension + `Block browser request` |
| 07 | Conta `unknown` | Validar conta e policy específica; UC pendente |
| **08** | **Label só no endpoint** | **View scope do utilizador + FortiDLP Teams App** |
| 09 | PID transitório | Fechar todos `ChatGPT.exe` e relançar |
| 10 | Outlook não abre | Testar `ms-outlook:` |
| 11 | Sem conexões observáveis | Destino autorizado e `num_ports` |

**Atalhos:** [Preparação](../setup/README.md) · [Scope](../setup/policy-scope.md) · [Apps Windows](../setup/windows-11.md) · [Guião](../demo-script.md).
