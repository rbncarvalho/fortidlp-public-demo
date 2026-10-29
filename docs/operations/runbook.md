# Runbook de execução

## Preparação (antes de abrir o laboratório)

1. Confirmar **Agent 12.8.1+** e Policy Templates **8.7.0+** no endpoint/testes GenAI.
2. Garantir que o endpoint está online e a etiqueta/grupo da demo está distribuído.
3. Garantir `Browser`, `Clipboard`, `Screenshot` e `Email` monitoring para as políticas relevantes.
4. Validar o **FortiDLP Email Add-in** no New Outlook.
5. Confirmar ligações SaaS corporativa e pessoal com contas fictícias.
6. Confirmar **Cloud Connector SharePoint/OneDrive** e integração Microsoft Teams `Healthy`.
7. **Instalar a aplicação FortiDLP no Teams** na conta que vai receber a remediação.
8. Confirmar que a **label de scope está aplicada ao utilizador cloud**, não apenas ao computador.
9. Confirmar que a policy `DEMO-08` aparece na lista de *Configured Policies* desse utilizador.
10. Usar uma pasta de demonstração e arquivos de teste; nunca dados reais.

## Check de estado em 30 segundos

| O que validar | Sinal de sucesso |
|---|---|
| Política distribuída | `Enable policy` ativo + endpoint/grupo sincronizado |
| Cloud event ingestion | Evento OneDrive/SharePoint aparece no Activity Feed |
| Policy evaluation | A **mesma** policy gera Detection |
| Action | `Associated Actions` com `Succeeded` |
| Teams | Mensagem entregue ao utilizador e botão funcional |
| Remediação | Permissão alterada no OneDrive; Action Log confirma |

## Sequência por ordem de robustez

UC01 → UC02 → UC05 → UC06 → UC09 → UC10 → UC08 → UC11.  
Fazer UC08 com a partilha preparada em paralelo; não depender de latência previsível.

## Não confundir

- **Evento Activity Feed** ≠ **Detection**. Um conector pode estar saudável sem que os filtros da policy façam match.
- **Screenshot event** ≠ **Screenshot evidence**.
- **Remediation request submitted** ≠ **Permission change succeeded**.
- **Initial block / override** ≠ **transferência efetivamente impedida**.
- **App sancionada** ≠ **conta corporativa**.

## Quando há problemas

Consultar o [Troubleshooting](troubleshooting.md); mudar **um filtro de cada vez**, guardar, publicar e produzir um **novo evento** com ficheiro de teste para evitar deduplicações.

## Recolha de evidências

Registar numa folha privada: use case, UTC timestamp, versão da policy, versão do Agent, scope, ação, estado, evidência na consola, comentário. Evitar exportar eventos integrais para GitHub.
