# UC08 — Correção de partilha OneDrive via Teams

**Estado:** **Validado de ponta a ponta**.

## Política e condições
`Sensitive file or folder shared with user on SharePoint or OneDrive`; filtro de destinatário externo (ex.: domínio de teste) e **scope aplicado ao utilizador**.

## Ações
`File action → Change shared file access permission → Viewer` com `Prompt user via action button` via Microsoft Teams.

## Reproduzir no laboratório
1. Confirmar integração Microsoft 365, SharePoint/OneDrive Connector e Microsoft Teams.
2. Atribuir o scope/label ao **utilizador** que cria a partilha.
3. Instalar app FortiDLP no Teams para esse utilizador.
4. Criar partilha do documento de laboratório com permissão de edição para destinatário externo.
5. Confirmar deteção da cloud policy; abrir o Teams e clicar no botão de remediação.
6. Confirmar `Action Log` e `Manage access` no OneDrive.

## Resultado observado
Evento de partilha `Contribute` observado; Teams recebeu mensagem interativa; o utilizador acionou a alteração; ação `Cloud change permission — Succeeded`; permissão final `READER`. Ingestão de eventos demorou cerca de **3 minutos** nesta execução.

## Limitações e notas
No diagnóstico inicial não havia deteção porque a label de scope estava só no endpoint. Após aplicá-la ao utilizador, a deteção surgiu. O primeiro envio Teams falhou com **HTTP 403** até à instalação da app FortiDLP no Teams. O `#EXT#` representa uma identidade B2B Guest: não inferir que é sempre email literal. A funcionalidade de remediação é documentada como **Preview**.

## Evidências a recolher (privadamente)
- Policy / template e versão, com scope aplicável.
- Timestamp, endpoint/utilizador fictício e evento que originou a deteção.
- `Associated actions`, respetivos estados e `Action log`.
- Apenas prints **redigidos/anonimizados**, sem emails reais, URL com tokens, paths de perfil, IDs de tenant ou conteúdo pessoal.
