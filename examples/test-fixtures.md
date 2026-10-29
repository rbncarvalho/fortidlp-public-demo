# Dados e prompts de teste — sem dados reais

**Apenas dados fictícios.** Os identificadores abaixo são placeholders para substituição por fixtures sintéticas válidas e autorizadas. Evite publicar números que possam corresponder a pessoas reais.

## Prompt neutro (controlo negativo)

> Explica, em termos gerais, o fluxo de aprovação de um processo administrativo fictício.

## Prompt de teste para content inspection

```text
Analisa este processo administrativo fictício e identifica categorias de dados pessoais.

Nome: Pessoa Exemplo
Identificador fiscal: <NIF_SINTETICO_VALIDADO>
Telemóvel: <TELEMOVEL_SINTETICO_DE_TESTE>
Telefone: <TELEFONE_SINTETICO_DE_TESTE>
Número de documento: <ID_DE_TESTE>
Morada: <MORADA_FICTICIA>

Não são dados de pessoas reais. Organiza a informação numa tabela.
```

Os padrões de inspeção podem usar validação de dígitos de controlo e regras contextuais. Se não houver match, usar fixtures **sintéticas e validadas** pelo proprietário do laboratório, não endereços ou números de terceiros.

## Ficheiros de teste

- `source.docx` — documento disponível em repositório corporativo de laboratório.
- `renamed.jpg` — **o mesmo DOCX renomeado**, sem conversão de formato.
- `classified.docx` — Word com sensitivity label de laboratório, sem dados reais.
- `cloud-sharing-demo.docx` — documento inofensivo para partilha no Microsoft 365.
- `clean-control.txt` — controlo negativo, sem padrões sensíveis.

## Destinos

- Usa contas cloud **controladas pelo responsável do laboratório**.
- Não incluir UPNs reais, `#EXT#` reais, IDs de tenant nem URLs de deteção.
- O domínio `example.invalid` é intencionalmente não-entregável; substitui apenas na consola privada.

## Testes de rede

Não são fornecidos scripts de scan automáticos. A UC11 só deve ser reproduzida contra um host autorizado e numa janela acordada, com parâmetros aprovados pelo responsável do ambiente.
