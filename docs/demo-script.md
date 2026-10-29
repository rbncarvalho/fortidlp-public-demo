# Guião para apresentação — FortiDLP

**Público:** equipas técnicas, segurança, IT e governação de dados.  
**Duração recomendada:** 35–45 minutos.  
**Linguagem:** portuguesa, com nomes de produtos e operações na designação original.  
**Regra de ouro:** não executar funcionalidades não validadas como se estivessem garantidas.

## Sequência recomendada — dry run das 11 policies

Na apresentação, usar as cenas com melhor impacto e reduzir as opcionais conforme o tempo disponível. A **história GenAI é contínua: UC04 → UC06 → UC09**, sem trocar os dados de teste.

| Ordem | Use case | Mensagem / ação |
|---|---|---|
| 1 | UC01 | OneDrive → rename → upload → override auditável |
| 2 | UC02 | Screenshot → Empty Clipboard |
| 3 | UC03 | MPIP label → deteção browser |
| 4 | UC04 | PII → paste em Claude Desktop: **deteção, não bloqueio** |
| 5 | UC06 | **A mesma PII** → ChatGPT Web: **Block browser request** |
| 6 | UC09 | ChatGPT Desktop não autorizado: **Kill process** |
| 7 | UC05 | New Outlook: bloqueio de email com PII |
| 8 | UC10 | Thunderbird: Kill + abrir Outlook nativo |
| 9 | UC08 | OneDrive: partilha externa → Teams → Reader |
| 10 | UC11 | Nmap autorizado: deteção de recon mais intenso |

**UC07:** utilizar como teste opcional/pendente de SaaS pessoal; não anunciar um bloqueio específico ainda não validado.

### Discurso de transição GenAI

> “Na aplicação nativa conseguimos identificar a tentativa de partilha e alertar, mas este controlo não bloqueia o conteúdo. Ao efetuar a mesma ação no browser, conseguimos impedir a submissão do prompt. E para reduzir a hipótese de contorno pelo cliente ChatGPT Desktop não autorizado, aplicamos Application Control e terminamos o processo.”

**Nota:** os mecanismos são *channel-specific*. A demo comprova bloqueio do pedido ChatGPT **Web** e término da aplicação **ChatGPT Desktop**; não comprova o bloqueio de todas as aplicações GenAI nativas.

## Abertura

**Dizer:** “Esta demonstração acompanha a informação através de vários canais: ficheiros locais e corporativos, email, aplicações desktop, GenAI e cloud. Vamos distinguir deteção, bloqueio, exceção e remediação, mostrando as ações efetivamente observadas.”

**Mostrar:** lista de policies ativas, endpoint saudável e conector cloud configurado, sem expor identidades reais.

## Cena 1 — A origem continua a importar (UC01)

**Preparação:** DOCX de laboratório no OneDrive; acesso ao destino cloud externo; política com override.

**Dizer:** “O utilizador descarrega um documento de um repositório corporativo, move-o e até altera a extensão. Será que a plataforma se lembra de onde veio?”

**Ao vivo:** download → rename `.docx` para `.jpg` → tentativa de upload → popup → escolher motivo e comentário → continuar.

**Mostrar SOC:** Detecção → Origin/Data Lineage → operações rename/move/copy; `Associated Actions`; motivo e screenshot.

**Mensagem:** “Não estamos dependentes da extensão. A ação pode ser bloqueada ou permitida por exceção auditável.”

**Plano B:** deteção previamente gerada e print anonimizado da lineage.


## Cena 2 — Captura de ecrã (UC02)

**Dizer:** “E quando alguém tenta contornar a transferência de ficheiro fazendo uma captura de ecrã?”

**Ao vivo:** abrir documento sintético → Snipping Tool → tentar colar após `Empty Clipboard`.

**Mostrar SOC:** Screenshot event e ação de limpeza.

**Mensagem:** “Visibilidade sobre operações do utilizador, não apenas uploads.”


## Cena 3 — Sensitivity Labels MPIP (UC03)

**Preparação:** documento sintético com label de laboratório aplicada no Word e policy `DEMO-03` ativa.

**Dizer:** “Além de padrões de dados pessoais, o endpoint reconhece classificações Microsoft Purview no documento.”

**Ao vivo:** confirmar a label no Word → guardar e fechar → upload no Edge → abrir Detection e verificar o match da label.

**Mensagem:** “Deteção e coaching confirmados; bloqueio do upload específico desta UC ainda não demonstrado.”


## Cena 4 — GenAI Desktop: visibilidade sem bloqueio de paste (UC04)

**Preparação:** texto PII sintético em Word; Claude Desktop aberto; policy `DEMO-04B` ativa.

**Dizer:** “Ao colar informação sensível numa aplicação GenAI nativa, conseguimos detetar e alertar. Porém, este template não impede o envio do conteúdo. E se o colaborador fizer o mesmo no browser?”

**Ao vivo:** copiar PII sintética de Word → colar em Claude Desktop **sem submeter** → confirmar popup e deteção da aplicação nativa.

**Ponte:** “Vamos usar exatamente os mesmos dados no ChatGPT Web e verificar se conseguimos impedir o pedido.”


## Cena 5 — Dados pessoais para GenAI Web (UC06)

**Dizer:** “Vimos que no cliente nativo este template deteta mas não bloqueia o paste. No browser, com uma policy específica de GenAI, podemos impedir o envio do mesmo conteúdo.”

**Ao vivo:** prompt neutro (passa) → prompt com telefones fictícios (bloqueado) → popup → deteção com `Capture input evidence`.

**Mostrar SOC:** `Block browser request — Succeeded`, `Capture input evidence — Succeeded`.  
**Não mostrar:** conteúdo original de evidência se incluir identidades ou dados reais.

**Mensagem:** “`Block browser request — Succeeded` prova que este pedido Web foi impedido. Segue-se a demonstração de como podemos limitar o acesso pela app nativa.”


## Cena 6 — Aplicação GenAI não autorizada (UC09)

**Dizer:** “O canal Web pode estar protegido, mas a app desktop tem outra superfície de controlo. Quando a política não permite essa aplicação, podemos terminá-la.”

**Ao vivo:** arranque **limpo** de ChatGPT Desktop; popup e término automático.

**Mostrar SOC:** `Kill process — Succeeded`.

**Mensagem:** “A prevenção de exfiltração aqui resulta da combinação dos controlos: pedido bloqueado no browser e ChatGPT Desktop não autorizado terminado no endpoint. Isto não significa cobertura universal de todas as apps GenAI (por exemplo, Claude Desktop apenas gerou deteção de paste neste laboratório).”


## Cena 7 — Email não autorizado (UC05)

**Dizer:** “Uma mensagem enviada pelo cliente corporativo pode conter dados pessoais ou estar classificada. O destino também importa.”

**Ao vivo:** New Outlook → destinatário externo de teste → documento sintético com padrões de conteúdo → Send.

**Mostrar SOC:** `Block outbound email — Succeeded`. Se relevante, repetir com classificação no **email**, não apenas no ficheiro.

**Mensagem:** “Combinação de destinatário, conteúdo e classificação.”


## Cena 8 — Cliente de email alternativo (UC10)

**Dizer:** “Não basta controlar mensagens no Outlook se o colaborador instalar um cliente de email fora dos mecanismos aprovados.”

**Ao vivo:** lançar Thunderbird → popup → Kill → clicar `Abrir Outlook corporativo` → abre New Outlook nativo.

**Mensagem:** “Prevenção com uma alternativa imediatamente acessível.”


## Cena 9 — Partilha cloud e remediação no Teams (UC08)

**Preparação crítica:** criar a partilha com **antecedência**, por causa da latência de ingestão (cerca de 3 minutos num teste). Confirmar que o utilizador recebeu a mensagem.

**Dizer:** “A informação pode ficar exposta sem sair do Microsoft 365. Vamos corrigir uma permissão excessiva no serviço cloud.”

**Ao vivo:** consultar partilha `Can edit` → mensagem FortiDLP no Teams → clicar botão de alteração → OneDrive `Manage access` → confirmar `Can view`.

**Mostrar SOC:** `Cloud change permission — Succeeded`, destino `READER`.

**Mensagem:** “Detetar na cloud, envolver o utilizador e corrigir na própria fonte, sem depender da máquina usada para criar a partilha.”

**Plano B:** detecção e Action Log já gerados, com prints devidamente anonimizados.


## Cena 10 — Reconhecimento excessivo de rede (UC11)

**Dizer:** “Nem toda a utilização de ferramentas técnicas é maliciosa. A política permite identificar excesso de atividade, mas não contamos simplesmente quantas vezes alguém executou o Nmap.”

**Ao vivo:** de preferência **não** efetuar scan intensivo durante a apresentação; mostrar os eventos preparados com o alvo autorizado. Se optar por scan, respeitar o âmbito escrito de autorização.

**Mostrar SOC:** `num_ports`, endereço de destino de laboratório e janela de avaliação.

**Mensagem:** “Análise de comportamento e limites definidos por política; não foi demonstrado Kill nem isolamento.”

## Encerramento — Investigate / Forensics

Revisitar UC01, UC06 e UC08. Mostrar separadamente:
- **Data Lineage** (a origem e operações);
- **Associated Actions** (concluídas, falhadas e pendentes);
- **User feedback / override**;
- **Remediação Teams**, confirmada no serviço cloud.

**Dizer:** “O ponto central não é um popup isolado: é termos rastreabilidade, contexto de risco, ação e evidência de auditoria.”

## Material que deve estar preparado

- Documento com **dados integralmente sintéticos**.
- Contas pessoal/corporativa estritamente de laboratório.
- FortiDLP Agent atualizado, Teams App instalada e âmbito cloud correto.
- Uma deteção **bem-sucedida** pronta para cada passo, caso haja latência ou falha de demo.
- Screenshots anonimizados, verificados segundo [publication-safety](publication-safety.md).
