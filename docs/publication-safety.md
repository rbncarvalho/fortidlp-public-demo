# Checklist de segurança antes de publicar

Este repositório é intencionalmente **público**. Não copiar screenshots, JSONs de eventos, exports de policies ou logs sem revisão.

## Informação proibida em commits públicos

- Nomes de clientes, utilizadores, responsáveis, colegas e endereços de email reais.
- Nomes de tenants Entra ID, domínios internos/organizacionais, UUIDs, IDs de app registration e IDs de subscrições.
- Tokens, chaves, cookies, Authorization headers, links de consola com query string e URLs assinadas.
- Nomes de ficheiros com identificação de cidadãos, conteúdo real de prompts ou evidência forense.
- IPs internos, IPs de gestão, nomes DDNS do laboratório e rotas/topologia de produção.
- Caminhos de ficheiros com perfis de utilizador reais; substituir por `%USERPROFILE%` ou `C:\Users\<LAB_USER>`.
- Imagens originais da consola que revelem outras equipas, labels internas ou nomes de grupos.

## Antes de incluir screenshots

1. Criar uma conta e documentos exclusivamente sintéticos.
2. Esconder identidades, nomes do tenant, endereços, IPs, process UUID e IDs de evento.
3. Remover conteúdo capturado em `Capture Input Evidence` ou `Capture File Evidence`.
4. Rever *toda a imagem*, incluindo breadcrumb, URL, tab title, timestamps e avatars.
5. Guardar apenas a versão anonimizada, de preferência com metadados EXIF removidos.
6. Ter aprovação explícita para qualquer imagem que mostre dados de terceiros.

## Validar texto automaticamente

Executar:

```bash
python scripts/check-public-content.py
```

Este scanner é **heurístico** e não substitui revisão humana. O ZIP fornecido não inclui screenshots, tokens nem exports de produção.

## Confiabilidade das afirmações

Não confundir resultado observado no laboratório com suporte oficial para todos os clientes/versões. Manter as limitações e casos pendentes visíveis.
