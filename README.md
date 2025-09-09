# Conversor de Moedas - Projeto de Integração Contínua

Este é um mini-projeto que demonstra um pipeline de Integração e Entrega Contínua (CI/CD) para uma simples aplicação web de conversão de moedas (USD-BRL).

A aplicação é construída com Python e Flask, e containerizada com Docker.

## Como Executar Localmente

Para executar a aplicação em seu ambiente de desenvolvimento, você precisará ter o Docker e o Docker Compose instalados.

1.  Clone o repositório e entre no diretório:
    ```bash
    git clone <URL_DO_REPOSITORIO>
    cd Integracao_Continua
    ```

2.  Inicie os serviços com o Docker Compose:
    ```bash
    docker-compose up --build
    ```

3.  Acesse a aplicação em seu navegador no endereço `http://localhost:5000`.

## Pipeline de CI/CD com GitHub Actions

O projeto utiliza GitHub Actions para automatizar o processo de teste, construção da imagem Docker e deploy da aplicação. O pipeline é definido no arquivo `.github/workflows/conversor.yml`.

### Gatilhos (Triggers)

O pipeline é acionado automaticamente nos seguintes eventos:
*   `push` na branch `main`.
*   `pull_request` para a branch `main`.

### Etapas do Pipeline

O pipeline consiste em dois jobs principais que rodam em sequência: `build` e `deploy`.

#### 1. Job: `build`

Este job é responsável por verificar a qualidade do código, testar a aplicação e construir a imagem Docker.
*   **Verificação de Código**: Executa o `flake8` para garantir que o código segue as convenções de estilo.
*   **Testes**: Roda os testes automatizados com `pytest` para verificar a funcionalidade da aplicação.
*   **Build e Push da Imagem Docker**: Faz login no Docker Hub, constrói a imagem Docker da aplicação e a envia (push) para o Docker Hub com duas tags: `latest` e uma tag única baseada no hash do commit (`github.sha`), garantindo o versionamento.

#### 2. Job: `deploy`

Este job só é executado se o job `build` for concluído com sucesso. Ele é responsável por implantar a nova versão da aplicação em um servidor (neste caso, uma instância EC2 da AWS).
*   **Conexão SSH**: Conecta-se ao servidor EC2 de forma segura.
*   **Deploy**: Executa um script no servidor remoto que:
    1.  Para e remove o container da versão antiga.
    2.  Baixa a imagem com a tag `latest` do Docker Hub.
    3.  Inicia um novo container com a imagem atualizada.



### Ferramentas Utilizadas
*   Python + Flask(Aplicação WEB)
*   Flake8 (Teste de qualidade do código Lint)
*   Docker (Cointainerização da Aplicação)
*   GitHubActions(CI/CD)
*   Docker HUB (Repositório de Imagens Docker)
*   Secrets(Segredos do GitHubActions)    
*   AWS EC2(Maquina de Produção)


### Dificuldades encontradas
*   Tempo para desenvolvimento do projeto
*   Configurar o pipeline 
*   Ajustar a aplicação após rodar o teste(encontrou alguns erros de qualdiade de código)

### O que aprendi no processo
*   Aperfeicoamento do conceito de containerização
*   Aperfeicoamento do conceito e Técnicas de CI/CD
*   Utilização de Secrets e Docker HUB
*   Utilização de testes unitários