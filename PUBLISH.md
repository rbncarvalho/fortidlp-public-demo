# Publicar no GitHub — novo repositório público

O conteúdo foi preparado para **um repositório separado e público**, para não expor um repositório privado de infraestrutura.

## 1. Criar o repositório

Na tua conta GitHub, cria um novo repositório com o nome sugerido:

`fortidlp-public-demo`

Seleciona **Public**. Não inicializes com README, porque o pacote já tem um.

## 2. Publicar a partir do terminal

Na pasta raiz deste pacote:

```bash
git init -b main
git add .
git commit -m "docs: publish anonymized FortiDLP demo lab"
git remote add origin https://github.com/<YOUR_GITHUB_USER>/fortidlp-public-demo.git
git push -u origin main
```

Terás de autenticar o Git com as credenciais da tua conta (por exemplo, SSH ou GitHub CLI).

## 3. Segurança

Antes do `git add .`:

```bash
python scripts/check-public-content.py
git status --short
```

Não adicionar screenshots de consola sem anonimização manual. O projeto inclui `.gitignore` para reduzir anexos acidentais.

## 4. Atualizações futuras

Validar novamente no laboratório cada ação quando mudarem Agent, templates ou conetores. Atualizar `docs/test-results.md` com a versão e a data de validação.

Este guia **não** altera visibilidade de projetos existentes nem publica credenciais.
