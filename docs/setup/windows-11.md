# Preparar a máquina Windows 11

## Base obrigatória

| Componente | UC | Como validar |
|---|---|---|
| **FortiDLP Agent 12.8.1** | Todas as UC de endpoint | Online/Healthy e sincronizado no FortiDLP Console |
| **Microsoft Edge + extensão FortiDLP** | 01,03,06,07 | Browser monitoring ativo + extensão instalada |
| Chrome + extensão FortiDLP | Opcional | Repetir validação de Edge |
| **Microsoft Word / M365 Apps** | 01–05 | Criar DOCX e aplicar label MPIP de laboratório |
| **OneDrive e SharePoint Web** | 01,08 | Ficheiro DOCX em repositório corporativo de laboratório |
| **New Outlook** | 05,10 | Mailbox de teste e envio para destinatário controlado |
| **FortiDLP Email Add-in do New Outlook** | 05 | Add-in visível, certificado configurado e Email Monitoring ON |
| **Microsoft Teams** | 08 | Mesma identidade do utilizador abrangido pela cloud policy |
| **App FortiDLP no Teams** | 08 | Instalada/desbloqueada; recebe ação de remediação |
| **Snipping Tool** (Windows) | 02 | Captura de ecrã e prova de Empty Clipboard |

## Aplicações de teste

| Aplicação | UC | Nota |
|---|---|---|
| **ChatGPT Desktop para Windows** | 04,09 | Processo **`ChatGPT.exe`**; antes da UC09 fechar todas as instâncias |
| **Claude Desktop** | 04 | Processo típico `claude.exe`; validar na VM |
| Visual Studio Code / Copilot | 04 opcional | Só se o assistente estiver instalado e configurado |
| **Mozilla Thunderbird** | 10 | Deve estar instalado; não configurar com email real |
| **Nmap CLI** | 11 | Usar apenas destino autorizado |
| Zenmap | 11 opcional | GUI para Nmap; pode lançar `nmap.exe` via `pythonw.exe` |

**Não necessário:** Wireshark (backlog, não testado), ferramentas OCR, Docker ou MCP.

## New Outlook: Add-in ≠ Agent ≠ Browser Extension

O **FortiDLP Email Add-in** para New Outlook/OWA é diferente do **Email Plugin Legacy** para Classic Outlook. Em `FortiDLP → Integrations → Microsoft → New Outlook add-in → Setup`, obter manifest/URL e configurar certificado de comunicação com o Agent. Ativar também **Email Monitoring** no Agent configuration group.

Referências: [Instalar Email Add-in Windows](https://docs.fortinet.com/document/fortidlp/1.0.0/fortidlp-agent-deployment-guide/875510/deploying-the-fortidlp-email-add-in-to-windows) · [Requisitos opcionais do Agent](https://docs.fortinet.com/document/fortidlp/latest/fortidlp-agent-deployment-guide/088312/fortidlp-agent-optional-requirements).

## Dados e contas a preparar

- `source.docx`: colocar no OneDrive corporativo do lab e descarregar via Edge (UC01).
- `classified.docx`: aplicar label MPIP de laboratório no Word (UC03).
- `pii-test.docx`: conteúdo **sintético** que faz match com padrões PII portugueses (UC04–06).
- Conta de cloud pessoal **de teste** e conta corporativa **de teste**, separadas (UC07).
- Mailbox corporativa + caixa externa controlada, não dados de pessoas reais (UC05).
- Documento OneDrive partilhável + destinatário externo controlado (UC08).

## Diagnóstico rápido no Windows

```powershell
# Confirmar instâncias de apps que possam interferir na demo
Get-CimInstance Win32_Process |
  Where-Object { $_.Name -in @('ChatGPT.exe','thunderbird.exe','nmap.exe') } |
  Select-Object Name, ProcessId, ParentProcessId

# Confirmar que o protocolo abre o New Outlook nativo
Start-Process 'ms-outlook:'

# Confirmar Nmap no PATH, se aplicável
Get-Command nmap.exe -ErrorAction SilentlyContinue
```

Não fixar PID nem caminho versionado do ChatGPT Desktop: são variáveis. Se o `Kill process` falhar num PID transitório, fechar a app totalmente e relançar.
