# Hello World Project - CI Pipeline

## Descrição
Este projeto é uma implementação básica de um sistema "Hello World" em Python, configurado com um pipeline de Integração Contínua (CI) usando GitHub Actions. A implementação inclui uma função adicional chamada `hello_universe` e um teste automatizado para garantir a integridade do código.

## Pré-requisitos
* Python 3.11
* Poetry para gerenciamento de dependências

## Como Executar o Projeto

### Instalação
1. Clone o repositório:
```bash
git clone https://github.com/arduinitavares/hello_world_project.git
cd hello_world_project
```

2. Instale as dependências usando o Poetry:
```bash
poetry install
```

### Execução dos Testes
Para garantir que tudo está funcionando corretamente, você pode rodar os testes com o comando:
```bash
poetry run pytest
```

## Pipeline de Integração Contínua

### Etapas do Pipeline
Este projeto utiliza o GitHub Actions para CI. Abaixo estão as etapas configuradas no pipeline:

1. **Checkout do Código**: Faz o checkout do código-fonte do repositório.
2. **Configuração do Ambiente Python**: Configura o ambiente com Python 3.11 e instala dependências usando Poetry.
3. **Instalação de Dependências**: Instala as dependências definidas no `pyproject.toml`.
4. **Execução dos Testes Automatizados**: Executa testes usando o `pytest` para garantir que o código está funcionando como esperado.
5. **Análise de Código (Opcional)**: Configurado para usar o Flake8 para análise estática de código e verificar a conformidade com padrões de estilo e qualidade.
6. **(Opcional) Deploy Automatizado**: Etapa para deploy automatizado pode ser adicionada se desejado.

### Ferramentas Utilizadas
* **Controle de Versão**: Git
* **Hospedagem do Repositório**: GitHub
* **CI/CD**: GitHub Actions
* **Gerenciador de Dependências**: Poetry
* **Testes**: pytest
* **Análise de Código (Opcional)**: Flake8

### Diagrama do Pipeline
*Insira uma imagem do diagrama de fluxo do pipeline que mostre as etapas desde o commit até a execução dos testes.*

## Contribuição
Para contribuir com este projeto:

1. Faça um fork do projeto.
2. Crie uma nova branch para sua funcionalidade ou correção:
```bash
git checkout -b feature/nova-funcionalidade
```

3. Faça commit das suas alterações:
```bash
git commit -m "Descrição da alteração"
```

4. Envie para o repositório remoto:
```bash
git push origin feature/nova-funcionalidade
```

5. Abra um Pull Request no GitHub.

## Licença
Este projeto está licenciado sob a licença MIT.


## Diagrama do Pipeline

```mermaid
graph TD
    A[Commit no GitHub] --> B[GitHub Actions - CI/CD]
    B --> C[Checkout do Código]
    C --> D[Configuração do Ambiente Python]
    D --> E[Instalação de Dependências]
    E --> F[Execução dos Testes]
    F --> G[Análise de Código]
    G --> |Passou| H[Deploy Opcional]
    G --> |Falhou| I[Correção Necessária]
    H --> J[Pipeline Concluído]
    I --> C
