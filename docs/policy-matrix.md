# Matriz de policies

> Os valores são uma referência para reconstrução. **Não** são um export direto da consola e não devem ser importados automaticamente. Verificar os nomes dos campos na versão instalada e ativar regras de impacto apenas após testes.

| UC | Policy de referência | Template | Filtro base | Ações comprovadas / pretendidas |
|---|---|---|---|---|
| 01 | `DEMO-01 | Corporate Source Protection` | `Sensitive file uploaded` | Origem OneDrive/SharePoint corporativo | Block browser upload + override; file/screenshot evidence |
| 02 | `DEMO-02 | Corporate Screenshot Protection` | `Screenshot taken` | Aplicação em foco e captura | Display message; Empty Clipboard |
| 03 | `DEMO-03 | MPIP Confidential Protection` | `Sensitive file uploaded` | Label MPIP em ficheiro | Deteção; coaching; block ainda não validado |
| 04 | `DEMO-04B | Sensitive Data Pasted to GenAI` | `Sensitive content pasted to desktop application` | Padrões PII PT + destinos desktop | Deteção; coaching |
| 05 | `DEMO-05A | Personal Data Email Protection` | `Unauthorized email sent` | Destinatário externo + padrões PII / MPIP | Block outbound email; evidence; message |
| 06 | `DEMO-06 | GenAI Prompt Protection` | `Sensitive content sent to GenAI web app` | GenAI apps + padrões PII PT | Block browser request; capture input; message |
| 07 | `DEMO-07 | Personal Cloud Protection` | `Sensitive file uploaded` | Google Drive/Dropbox/OneDrive + Non-corporate | Ainda não validado neste filtro |
| 08 | `DEMO-08 | Cloud Sharing Remediation` | `Sensitive file or folder shared with user on SharePoint or OneDrive` | Destinatário externo, scope no utilizador | `Change shared file access permission` → Reader via Teams |
| 09 | `DEMO-09 | Unauthorized GenAI Desktop` | `Unauthorized application used` | `ChatGPT.exe` | Kill process + display message |
| 10 | `DEMO-10 | Unauthorized Email Client` | `Unauthorized email tool used` | Outlook permitido / Thunderbird não autorizado | Kill process + message com URI `ms-outlook:` |
| 11 | `DEMO-11 | Excessive Network Reconnaissance` | `Outgoing port scan performed` | Portas distintas por destino / janela | Deteção e coaching; sem kill |

## Regras de interpretação

- `Capture screenshot evidence: Not Found` pode ser transitório se a ação ainda estiver em processamento. Se persistir, não marcar como validada.
- `Block browser upload` com override pode registar `blocked` na fase inicial, **mas a transferência acaba permitida** se o utilizador escolher continuar.
- Ações e filtros mudam entre releases. A versão registada é a do laboratório em outubro de 2026.
- Nos filtros por regex, `^arquivo\.docx$` corresponde exatamente a `arquivo.docx`; `arquivo.docx` não faz o mesmo isolamento.
- Para Cloud Drive, **validar primeiro a identidade abrangida por View scope**. O conector pode recolher eventos sem que a policy gere deteções.
