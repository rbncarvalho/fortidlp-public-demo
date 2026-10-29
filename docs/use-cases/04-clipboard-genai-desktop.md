# UC04 — Clipboard para aplicações GenAI desktop

> **GUIÃO RÁPIDO:** preparação + fluxograma + resultado. [Setup completo](../setup/README.md) · [Checklist 5 min](../operations/preflight.md)

## 0. Preparação rápida

| Item | Verificar |
|---|---|
| Aplicações | Word, Claude Desktop ou ChatGPT Desktop; VS Code opcional |
| Label / scope | Endpoint `dlp_rc_demos` |
| Policy Enabled | `DEMO-04B | Sensitive Data Pasted to GenAI` |

- [ ] Texto fictício com PII portuguesa no Word
- [ ] Clipboard Monitoring ON
- [ ] App de destino aberta; regra antiga DEMO-04 desativada

## 1. Fluxograma — executar pela ordem indicada

```mermaid
flowchart TD
  A["Abrir texto PII no Word"]
  B["Copiar texto"]
  C["Abrir app GenAI desktop"]
  D["Colar texto"]
  E["FortiDLP deteta paste"]
  F["Popup de coaching"]
  G["Validar app e padrões"]
  A --> B
  B --> C
  C --> D
  D --> E
  E --> F
  F --> G
```

## 2. O que comprovar na consola

Deteção do paste e destino; **sem bloqueio de colagem demonstrado**.

## 3. Plano B

Abrir Detection anterior de ChatGPT/Claude/VS Code.

---

## Detalhe técnico e evidências

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
