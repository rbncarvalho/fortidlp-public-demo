# UC03 — Microsoft Purview / label no browser

**Estado:** **Parcial** (deteção e coaching).

## Política e condições
`Sensitive file uploaded` com Microsoft Sensitivity Label de teste, por exemplo `Lab-Confidential` (substituir pela etiqueta real de laboratório).

## Ações
`Display message` confirmado; `Block browser upload` **não confirmado** nesta UC.

## Reproduzir no laboratório
1. Aplicar uma label MPIP a um DOCX de laboratório.
2. Guardar, reabrir e verificar a classificação.
3. Tentar upload através do Edge.
4. Inspecionar `Content Inspection` na deteção.

## Resultado observado
A classificação MPIP foi reconhecida em upload de DOCX via browser. Deteção e coaching observados.

## Limitações e notas
Não inferir que a inspeção de anexo etiquetado no New Outlook tem cobertura igual; há um teste negativo não resolvido descrito em UC05.

## Evidências a recolher (privadamente)
- Policy / template e versão, com scope aplicável.
- Timestamp, endpoint/utilizador fictício e evento que originou a deteção.
- `Associated actions`, respetivos estados e `Action log`.
- Apenas prints **redigidos/anonimizados**, sem emails reais, URL com tokens, paths de perfil, IDs de tenant ou conteúdo pessoal.
