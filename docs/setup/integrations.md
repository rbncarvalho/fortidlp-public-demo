# Integrações e contas SaaS

## Microsoft 365 e OneDrive/SharePoint (UC01, UC08)

- [ ] Tenant **exclusivamente laboratorial**; utilizador Entra/M365 com licença e OneDrive/SharePoint.
- [ ] Ficheiro DOCX de teste no OneDrive; utilizador autorizado a partilhá-lo.
- [ ] Cloud Connector FortiDLP Microsoft 365 **Healthy**, a recolher eventos.
- [ ] Permissões necessárias para **Change shared file access permission** disponíveis.
- [ ] UC08 com filtro de destinatário externo controlado e **scope aplicado ao utilizador**.
- [ ] Partilha de laboratório `Can edit / Contribute` → ação **user-triggered** de mudar para `Reader / Can view`.
- [ ] Verificar **Action Log Succeeded** e a permissão final no **OneDrive**.

## Microsoft Teams (UC08)

- [ ] Integração `FortiDLP → Integrations → Messaging → Microsoft Teams` ativa.
- [ ] Credenciais adequadas ao tenant de laboratório, estado Healthy.
- [ ] App **FortiDLP** permitida no Teams Admin Center e **instalada para o utilizador**.
- [ ] Utilizador de teste com sessão Teams e capaz de receber mensagem interativa.
- [ ] Criar a partilha com antecedência: houve cerca de **3 minutos** de atraso entre evento e deteção.

**Problema observado:** `HTTP 403 / failed to get conversation id` mesmo com integração Healthy. Instalar a **app FortiDLP no Teams do utilizador** permitiu receber a mensagem e executar a ação.

Referências: [Integração Teams (Preview)](https://docs.fortinet.com/document/fortidlp/1.0.0/fortidlp-administration-guide/802536/adding-a-teams-integration-preview) · [Mensagens e remediação Teams (Preview)](https://docs.fortinet.com/document/fortidlp/latest/fortidlp-console-user-guide/361558/send-message-to-slack-or-teams-preview).

## Outlook e Purview (UC03, UC05, UC10)

- [ ] **New Outlook** ligado a mailbox Exchange Online/Microsoft 365 de teste.
- [ ] **FortiDLP Email Add-in** instalado (não o plugin do Classic Outlook).
- [ ] Certificado/trust do add-in configurados e **Email Monitoring ON**.
- [ ] Label Microsoft Purview de teste publicada para o utilizador Word/Outlook.
- [ ] Destinatário externo controlado pelo tester (não contas pessoais de terceiros).
- [ ] URI `ms-outlook:` registada e testada na VM para UC10.

**Limitação real:** etiqueta MPIP no **próprio email** bloqueou; etiqueta só no **anexo**, sem classificação da mensagem, não bloqueou no teste observado.

## SaaS pessoal e GenAI (UC01, UC06, UC07)

- [ ] Sessão cloud corporativa e sessão pessoal **de laboratório** separadas.
- [ ] Configurar **domínio de login corporativo** para classificação de contas SaaS, não apenas hostname SharePoint.
- [ ] Testar prompt ChatGPT Web através de browser com extensão FortiDLP ativa.
- [ ] Verificar a **policy que disparou**: matching de app não comprova matching de **tipo de conta**.

**UC07 pendente:** havia deteções de uploads por outras policies, mas não foi validado o match de conta `Non-corporate` nem o bloqueio próprio da UC07. **UC06 validado:** `Block browser request — Succeeded`, mesmo com conta SaaS apresentada como `unknown user`.

## Regra de segurança

Não colocar neste repositório exports de conectores, UPNs reais, passwords, tokens, URLs de evidências ou IDs de tenant. Usar apenas dados sintéticos e prints anonimizados.
