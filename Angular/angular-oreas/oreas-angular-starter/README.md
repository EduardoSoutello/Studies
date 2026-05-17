# Oreas • Angular Starter

Projeto Angular (standalone, Angular 18) para a marca **Oreas** com:
- Página inicial com resumo de pacotes e bloco "Sobre a Oreas"
- Página de login
- Página de compra/listagem de pacotes
- Header fixo com link para o **Podcast** (canto superior direito)

## Como usar

1. Instale as dependências:
   ```bash
   npm install
   ```
2. Rode em desenvolvimento:
   ```bash
   npm start
   ```
3. Build de produção:
   ```bash
   npm run build
   ```

> O link do podcast está como `https://podcast.oreas.example` no header. Substitua pelo URL real.

Estrutura principal:
```
src/
  app/
    components/header
    pages/{home,login,packages}
    services/{package,auth}
    models/package.model.ts
```
