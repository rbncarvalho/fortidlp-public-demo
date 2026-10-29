# Matriz de resultados observados

> **Dry run 29/10/2026:** todos os 11 percursos foram executados. Ver [relatório](operations/dry-run-2026-10-29.md) e [mapa de apresentação](presentation-flow.md).

| UC | Condição | Observado | Evidência técnica principal | Lacuna |
|---|---|---|---|---|
| 01 | Download de ficheiro corporativo, renomeação e upload | Bloqueio inicial com override permitido | Data Lineage, `Block browser upload... Succeeded`, feedback, screenshot/file evidence | Teste `Cancel` independente desejável |
| 02 | Screenshot de documento | Deteção e Empty Clipboard | Screenshot event, ação de clipboard | Evitar captura+save em simultâneo |
| 03 | Upload DOCX com MPIP | Deteção e coaching | `Content Inspection` com nome da label | Bloqueio não testado |
| 04 | Paste para apps GenAI desktop | Deteção | App destino e padrão português | Sem bloqueio nativo de prompt por este template |
| 05 | Email para destinatário externo com PII | Bloqueado | `Block outbound email — Succeeded` | MPIP de anexo-only não fez match |
| 06 | Prompt ChatGPT Web com telefones PT | Bloqueado | `Block browser request — Succeeded`; input evidence | `website_user=unknown`; screenshot `Not Found` |
| 07 | Google Drive com documento classificado e com documento só PII | Deteções próprias DEMO-07 confirmadas para MPIP e PII; bloqueio configurado e reteste reportado concluído | `Created by DEMO-07`, Content Inspection, ações de browser | Action Log final do bloqueio não partilhado; `Unknown` não prova conta pessoal |
| 08 | Partilha cloud para conta externa com edição | Permissão reduzida via Teams | Contribute → Reader; `Cloud change permission — Succeeded` | Feature Preview e atraso de auditoria |
| 09 | ChatGPT Desktop não aprovado | Terminado após arranque limpo | `Kill process — Succeeded` | Primeira tentativa falhou em PID transitório |
| 10 | Thunderbird não aprovado | Terminado, redirecionado | Kill process + `ms-outlook:` | URI depende da instalação no endpoint |
| 11 | Scan Nmap mais abrangente | Deteção | Evento de scan e coaching | Não houve `Kill`, `Isolate` nem contagem final publicada |

## Capacidades excluídas / futuras

- **FortiDLP OCR para texto dentro de imagens:** sem confirmação no Agent testado.
- **Agentic AI Inventory / MCP tool-call enforcement:** não demonstrados no tenant.
- **Wireshark / sniffing tools:** caso de utilização mencionado, mas não configurado nem validado.
- **USB:** intencionalmente excluído por o endpoint de teste ser uma VM cloud.
- **FortiGate DLP/OCR:** laboratório separado; não é parte dos resultados FortiDLP aqui documentados.

O marcador `✅ Validado` refere-se à **ação descrita**, não a todas as variantes possíveis do produto.
