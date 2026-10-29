# Arquitetura e pré-requisitos

## Topologia lógica

- **Windows 11** de laboratório, com FortiDLP Agent **12.8.1**, Edge e aplicações Office.
- **FortiDLP Console**, Policy Templates **8.7.0**, grupos de policies associados a identidades e/ou endpoints.
- **Microsoft 365 de laboratório** com New Outlook, OneDrive, SharePoint e Microsoft Teams.
- **FortiDLP Email Add-in** para New Outlook.
- **SharePoint/OneDrive Cloud Connector** com eventos de auditoria, ações de partilha e remediação.
- **Teams integration** e app FortiDLP instalada para o utilizador de teste.
- **Browser monitoring, clipboard monitoring, screenshot monitoring, email monitoring** ativos conforme o use case.
- **Aplicações de demonstração:** ChatGPT Web/Desktop, Claude Desktop, VS Code, Thunderbird, Nmap e ferramentas de screenshot.

## Separação dos contextos

| Contexto | Fonte de telemetria | Exemplos |
|---|---|---|
| Endpoint | Agent | clipboard, processos, screenshot, email, browser |
| SaaS por browser | Agent + contexto de conta | upload para armazenamento pessoal, prompt Web |
| Cloud-native | Connector Microsoft 365 | partilha no OneDrive, remediação via Teams |

**Atenção ao scope:** uma etiqueta aplicada **apenas ao computador** não implica que uma *cloud drive policy* fique associada ao **utilizador** que partilha. O laboratório só começou a gerar deteções UC08 após aplicar a label de demonstração diretamente ao utilizador.

## Controlo de acesso e impacto

Usar um tenant, utilizador, documentos e destinatários exclusivos de laboratório. Não ativar remediação por domínio em toda a organização sem primeiro validar detecções com escopo restrito.

Os identificadores de domínio usados na documentação são **exemplos** (por exemplo, `corp.example` e `example.invalid`); devem ser substituídos pelos domínios reais *apenas na consola privada*, nunca nos commits públicos.

### Requisitos específicos

| Função | Condições |
|---|---|
| GenAI Web request blocking | Agent **12.8.1+** e Policy Templates **8.7.0+** |
| Cloud remediation (Preview) | Cloud Connector e Policies **8.6.0+**; permissões de escrita |
| Teams remediation | Integração Teams saudável + app FortiDLP instalada para o utilizador |
| New Outlook DLP | Email Add-in e email monitoring |
| SaaS account matching | Domínios de **login** corporativo configurados, não apenas URLs `sharepoint.com` |
| Testes Nmap | Apenas hosts/rede sob controlo ou autorizados; sem `Isolate` na VM remota |

## Estados de observação

- **Validated:** confirmado em detecção e/ou Action Log no laboratório.
- **Partial:** há deteção, mas a ação de bloqueio não foi demonstrada.
- **Pending:** policy existe ou foi planeada, mas ainda faltam evidências.
- **Not supported/unknown:** não presumir capacidade por existirem funcionalidades próximas noutro produto.
