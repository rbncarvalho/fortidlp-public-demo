# Mensagens de coaching (PT-PT)

> Estes são **exemplos genéricos**, não exports de mensagens da consola. Os placeholders variam conforme o template e só devem ser usados se surgirem na lista do editor correspondente.

## UC01 — Upload com override

**Título:** Transferência de informação corporativa

```text
Foi identificada uma tentativa de transferência de um ficheiro corporativo.

Ficheiro(s): {violating_file_filenames}
Destino: {hostname}

A proteção mantém-se mesmo após cópia, movimentação ou alteração do nome.

A transferência foi interrompida pela política de segurança.
Se tiver um motivo profissional legítimo, utilize a opção de exceção e
registe a justificação. Esta decisão será auditada.
```

**Sugestões de justificação:** necessidade operacional; partilha autorizada; falso positivo; outra situação (com comentário obrigatório). O motivo é uma **declaração do utilizador**, não aprovação externa automaticamente verificada.

## UC06 — GenAI Web

**Título:** Informação sensível bloqueada

```text
Foi detetada uma tentativa de enviar dados sensíveis para uma aplicação de IA.

Aplicação: {genai_app}
Destino: {hostname}
Padrão identificado: {content_info}

O pedido foi bloqueado. Utilize serviços e contas aprovados
para o tratamento de informação corporativa.
```

## UC08 — Cloud sharing via Teams

**Título:** Rever permissões de partilha

```text
Foi identificada uma partilha com permissões que necessitam de revisão.

Documento: {event.file_name}
Destinatário: {resolved_target_name}
Permissões atribuídas: {event.permissions_granted}

Selecione a ação de alteração de permissões apresentada pelo FortiDLP
para reduzir o acesso para leitura (Viewer). A alteração será auditada.
```

O botão de remediação é gerado pelo workflow nativo do FortiDLP, não por um botão HTML adicionado ao texto.

## UC09 — Aplicação GenAI desktop

**Título:** Aplicação de IA não autorizada

```text
Foi detetada uma aplicação de IA não autorizada neste endpoint.

Aplicação: {event.child_process.binary_name}

A aplicação será terminada. Utilize apenas os canais de IA
corporativos aprovados ou contacte a equipa de segurança.
```

## UC10 — Cliente de email

**Título:** Cliente de email não autorizado

```text
Foi identificada uma aplicação de email que não está aprovada.

Aplicação: {event.child_process.binary_name}

A aplicação será terminada. Utilize o Outlook corporativo.
```

**Link da mensagem:** URL `ms-outlook:`; texto `Abrir Outlook corporativo` — validado apenas em Windows com o New Outlook instalado e protocolo registado.

## UC11 — Network reconnaissance

**Título:** Atividade de rede suspeita

```text
Foi identificado um número excessivo de portas remotas contactadas.

Origem: {localAddr}
Destino: {remoteAddr}
Portas contactadas: {num_ports}

Interrompa a atividade e contacte a equipa de segurança caso
se trate de diagnóstico autorizado.
```

`{max_port_number}` representa o limite superior do intervalo observado; **não** o número máximo de portas permitido.
