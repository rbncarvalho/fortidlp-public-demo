# Troubleshooting e lições aprendidas

## 1. Eventos OneDrive aparecem, mas sem Detection

**Sintoma:** a partilha aparece em `Activity Feed → SharePoint / OneDrive` mas a Cloud Drive Policy não dispara.

**Causa observada no laboratório:** a etiqueta de policy estava aplicada **apenas ao endpoint**. A avaliação cloud precisava do **utilizador** no scope.

**Correção validada:** adicionar a etiqueta de demonstração ao utilizador e confirmar em `View scope` / `Configured Policies`; repetir com evento novo. A deteção passou a surgir.

**Antes de alterar os filtros:** conferir identidade de quem criou a partilha, estado da policy, sync e scope.

## 2. Teams Integration Healthy, mas `HTTP 403`

**Sintoma observado:**

```text
failed to send message: failed to get conversation id
(with guessed service url): HTTP error 403: invalid response
```

**Causa provável e resolução observada:** a app FortiDLP ainda não estava instalada no Teams do utilizador. Depois da instalação, chegou a mensagem interativa e o botão permitiu remediar.

**Não confundir:** credenciais do conector saudáveis com capacidade do bot iniciar conversação.

## 3. `Kill process` falha com PID inválido

**Sintoma observado no ChatGPT Desktop:**

```text
Failed to kill process: failed to get start time for pid ...
gowin32: OpenProcess failed: The parameter is incorrect.
```

**Hipótese:** app multiprocesso e PID transitório. A hipótese não foi comprovada como causa única.

**Validação diferencial:** `Kill process` funcionou com Notepad empacotado em WindowsApps, demonstrando que a ação geral funcionava. ChatGPT Desktop passou a terminar **depois de fechar todas as instâncias e lançar a app novamente**.

**Diagnóstico em Windows PowerShell:**

```powershell
Get-CimInstance Win32_Process |
  Where-Object { $_.Name -eq 'ChatGPT.exe' } |
  Select-Object Name, ProcessId, ParentProcessId, CreationDate
```

**Preparação segura para a demo:** fechar ChatGPT e confirmar ausência de processos antigos antes de abrir. Não depender de PID ou caminho versionado, e evitar filtros sobre processos pai (o Windows Shell pode usar `sihost.exe`).

## 4. Novo Outlook: MPIP em anexo não gerou deteção

**Observado:** email **com classificação MPIP** foi bloqueado. Documento **não encriptado** com label MPIP, anexado a email **sem classificação**, passou sem match.

**Estado:** **pendente de análise**, não alegar suporte testado para anexo-only neste ambiente. Testes com padrões de PII em anexos funcionaram.

## 5. GenAI Web bloqueado, mas conta desconhecida

`Block browser request`, `Capture input evidence` e `Display message` sucederam; `website_user` foi apresentado como `unknown user`.

**Interpretação:** a inspeção/bloqueio do prompt está confirmada, mas a identificação de conta pessoal/corporativa **não está validada por esse evento**. Investigar login, suporte da app e parâmetros de User Account Type.

## 6. Screenshot Evidence `Not Found`

Em UC06, `Capture screenshot evidence` não estava disponível no evento analisado; UC01 teve screenshot evidence com sucesso.

A documentação avisa que a captura/evidência pode levar tempo a concluir; consultar novamente o Action Log. Se persistir, manter como não validada nesse cenário.

## 7. Eventos cloud chegam com atraso

Num teste, houve aproximadamente **3 minutos** entre a partilha e a sua apresentação no FortiDLP.

Em demonstrações, preparar o evento antecipadamente; não repetir várias vezes a mesma partilha à espera de instantaneidade.

## 8. Domínios e convidados B2B

Um destinatário externo pode surgir como UPN Guest com a estrutura `utilizador_dominio#EXT#@<TENANT>.onmicrosoft.com`.

A representação técnica **não altera necessariamente o endereço de email original**. Testar filtros de domínio e email separadamente. Não confundir UPN de convidado com uma licença ou conta Microsoft 365 completa.

## 9. Nmap não gera deteção em todos os scans

A policy `Outgoing port scan performed` avalia atividade de portas num intervalo, **não execuções do executável**. Scans limitados não dispararam; scan abrangente gerou deteção.

A documentação não justifica prometer número exato de execuções toleradas. Validação depende das ligações/portas efetivamente observadas pelo Agent. **Não executar scans fora do âmbito autorizado.**
