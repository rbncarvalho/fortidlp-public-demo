# Guião para apresentação — FortiDLP

**Público:** equipas técnicas, segurança, IT e governação de dados.  
**Duração recomendada:** 35–45 minutos.  
**Linguagem:** portuguesa, com nomes de produtos e operações na designação original.  
**Regra de ouro:** não executar funcionalidades não validadas como se estivessem garantidas.

## Sequência principal (8 momentos)

| Momento | Duração | Use case | Interação visível |
|---|---:|---|---|
| Abertura | 2 min | Arquitetura | Endpoint + cloud connector |
| 1 | 6 min | UC01 | OneDrive → rename → browser upload → override |
| 2 | 3 min | UC02 | Screenshot + Empty Clipboard |
| 3 | 4 min | UC05 | New Outlook: email externo bloqueado |
| 4 | 5 min | UC06 | ChatGPT Web: prompt com PII bloqueado |
| 5 | 3 min | UC09 | ChatGPT Desktop: Kill + popup |
| 6 | 3 min | UC10 | Thunderbird: Kill + abrir Outlook nativo |
| 7 | 7 min | UC08 | Partilha OneDrive → Teams → Reader |
| 8 | 3 min | UC11 | Nmap: deteção comportamental + logs |
| Encerramento | 4 min | Investigate | Evidências, Data Lineage, feedback e ações |

UC03, UC04 e UC07 servem de módulos opcionais ou transições técnicas.

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

## Cena 3 — Email não autorizado (UC05)

**Dizer:** “Uma mensagem enviada pelo cliente corporativo pode conter dados pessoais ou estar classificada. O destino também importa.”

**Ao vivo:** New Outlook → destinatário externo de teste → documento sintético com padrões de conteúdo → Send.

**Mostrar SOC:** `Block outbound email — Succeeded`. Se relevante, repetir com classificação no **email**, não apenas no ficheiro.

**Mensagem:** “Combinação de destinatário, conteúdo e classificação.”

## Cena 4 — Dados pessoais para GenAI Web (UC06)

**Dizer:** “E se o colaborador tentar enviar os mesmos dados diretamente num prompt?”

**Ao vivo:** prompt neutro (passa) → prompt com telefones fictícios (bloqueado) → popup → deteção com `Capture input evidence`.

**Mostrar SOC:** `Block browser request — Succeeded`, `Capture input evidence — Succeeded`.  
**Não mostrar:** conteúdo original de evidência se incluir identidades ou dados reais.

**Mensagem:** “O controlo atua na submissão do pedido Web, não só no clipboard.”

## Cena 5 — Aplicação GenAI não autorizada (UC09)

**Dizer:** “O canal Web pode estar protegido, mas a app desktop tem outra superfície de controlo. Quando a política não permite essa aplicação, podemos terminá-la.”

**Ao vivo:** arranque **limpo** de ChatGPT Desktop; popup e término automático.

**Mostrar SOC:** `Kill process — Succeeded`.

**Mensagem:** “Controlar a utilização da app complementa a inspeção do conteúdo.”

## Cena 6 — Cliente de email alternativo (UC10)

**Dizer:** “Não basta controlar mensagens no Outlook se o colaborador instalar um cliente de email fora dos mecanismos aprovados.”

**Ao vivo:** lançar Thunderbird → popup → Kill → clicar `Abrir Outlook corporativo` → abre New Outlook nativo.

**Mensagem:** “Prevenção com uma alternativa imediatamente acessível.”

## Cena 7 — Partilha cloud e remediação no Teams (UC08)

**Preparação crítica:** criar a partilha com **antecedência**, por causa da latência de ingestão (cerca de 3 minutos num teste). Confirmar que o utilizador recebeu a mensagem.

**Dizer:** “A informação pode ficar exposta sem sair do Microsoft 365. Vamos corrigir uma permissão excessiva no serviço cloud.”

**Ao vivo:** consultar partilha `Can edit` → mensagem FortiDLP no Teams → clicar botão de alteração → OneDrive `Manage access` → confirmar `Can view`.

**Mostrar SOC:** `Cloud change permission — Succeeded`, destino `READER`.

**Mensagem:** “Detetar na cloud, envolver o utilizador e corrigir na própria fonte, sem depender da máquina usada para criar a partilha.”

**Plano B:** detecção e Action Log já gerados, com prints devidamente anonimizados.

## Cena 8 — Reconhecimento excessivo de rede (UC11)

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
