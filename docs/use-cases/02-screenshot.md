# UC02 — Screenshot e limpeza do clipboard

**Estado:** **Validado** (deteção e `Empty Clipboard`).

## Política e condições
`Screenshot taken`, monitorização de captura e aplicação protegida em ecrã.

## Ações
`Display message` e `Empty Clipboard`; não duplicar alertas ao ativar simultaneamente monitorização de capture e save.

## Reproduzir no laboratório
1. Abrir um documento sintético num editor Office.
2. Iniciar uma captura com a ferramenta de screenshots do Windows.
3. Observar a notificação; tentar colar a captura.
4. Consultar deteção e processos associados.

## Resultado observado
Evento de screenshot gerado; processo da ferramenta e aplicação capturada identificados; clipboard limpo com sucesso.

## Limitações e notas
Screenshot como **evento** não é a mesma coisa que `Capture screenshot evidence` como ação forense. Reduzir popups duplicados.

## Evidências a recolher (privadamente)
- Policy / template e versão, com scope aplicável.
- Timestamp, endpoint/utilizador fictício e evento que originou a deteção.
- `Associated actions`, respetivos estados e `Action log`.
- Apenas prints **redigidos/anonimizados**, sem emails reais, URL com tokens, paths de perfil, IDs de tenant ou conteúdo pessoal.
