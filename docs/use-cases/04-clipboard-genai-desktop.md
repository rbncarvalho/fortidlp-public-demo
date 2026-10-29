# UC04 — Clipboard para aplicações GenAI desktop

**Estado:** **Validado para deteção/coaching**.

## Política e condições
`Sensitive content pasted to desktop application`; padrões portugueses de identificação, telemóveis e telefones; aplicações desktop selecionadas.

## Ações
Display/coaching, evidência de clipboard se disponível; **não implica Block Paste**.

## Reproduzir no laboratório
1. Copiar de Word um texto sintético com identificadores portugueses.
2. Colar em Claude Desktop ou ChatGPT Desktop.
3. Opcional: repetir em VS Code com assistente.
4. Abrir deteção e inspecionar aplicação de destino, padrão e evidência.

## Resultado observado
Deteção confirmada para várias aplicações nativas, incluindo Claude, ChatGPT e VS Code.

## Limitações e notas
Evitar policy duplicada `Sensitive content copied and pasted to desktop application` em paralelo, que produziu ruído; este teste não prova inspeção de calls MCP nem bloqueio nativo de prompt.

## Evidências a recolher (privadamente)
- Policy / template e versão, com scope aplicável.
- Timestamp, endpoint/utilizador fictício e evento que originou a deteção.
- `Associated actions`, respetivos estados e `Action log`.
- Apenas prints **redigidos/anonimizados**, sem emails reais, URL com tokens, paths de perfil, IDs de tenant ou conteúdo pessoal.
