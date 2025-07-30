# API de Predição de Churn com FastAPI e Docker 🚀

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Python Version](https://img.shields.io/badge/python-3.9-blue)
![Framework](https://img.shields.io/badge/framework-FastAPI-0.95.0)
![Dockerized](https://img.shields.io/badge/docker-ready-blue?logo=docker)
![License](https://img.shields.io/badge/license-MIT-yellow)

## 📋 Visão Geral do Projeto

Este projeto implementa uma solução de Machine Learning de ponta a ponta para prever o **churn de clientes** (probabilidade de cancelamento de serviço). O modelo treinado é exposto através de uma API RESTful robusta, construída com **FastAPI** e totalmente containerizada com **Docker** para garantir portabilidade e facilidade de implantação.

O fluxo de trabalho abrange desde a análise e preparação dos dados em notebooks Jupyter até a criação de um serviço de predição pronto para produção.

## ✨ Features Principais

-   **Modelo Preditivo:** Utiliza um pipeline do Scikit-Learn que inclui pré-processamento de dados (scaling e one-hot encoding) e um modelo de classificação (Regressão Logística).
-   **API de Alta Performance:** Construída com FastAPI, oferecendo validação de dados automática com Pydantic e alta velocidade.
-   **Documentação Interativa:** Geração automática de documentação com Swagger UI (`/docs`) e ReDoc (`/redoc`), permitindo testes de API diretamente no navegador.
-   **Containerização Completa:** O `Dockerfile` otimizado cria uma imagem leve e eficiente, tornando a aplicação independente do ambiente.
-   **Estrutura Organizada:** O código é separado em diretórios lógicos (`notebooks` para exploração e `src` para a aplicação), seguindo as melhores práticas de engenharia de software.

## 🛠️ Tecnologias Utilizadas

-   **Linguagem:** Python 3.9
-   **Análise e Modelagem:** Pandas, NumPy, Scikit-Learn
-   **API Framework:** FastAPI, Uvicorn
-   **Validação de Dados:** Pydantic
-   **Containerização:** Docker

## 📂 Estrutura de Arquivos

```
churn-project/
├── Dockerfile                # Define o ambiente da aplicação para o Docker
├── README.md                 # Esta documentação
├── requirements.txt          # Lista de dependências Python
├── .dockerignore             # Especifica arquivos a serem ignorados pelo Docker
├── .gitignore                # Especifica arquivos a serem ignorados pelo Git
├── notebooks/
│   ├── 01_data_generation.ipynb  # Geração e análise exploratória dos dados
│   └── 02_model_training.ipynb   # Treinamento, avaliação e salvamento do modelo
└── src/
    ├── __init__.py
    ├── main.py               # Lógica principal da API FastAPI
    └── churn_model.joblib    # Artefato do modelo de ML treinado
```

## 🚀 Como Executar o Projeto

Existem duas maneiras de executar a aplicação: localmente com um ambiente virtual ou via Docker (método recomendado).

### Pré-requisitos

-   [Git](https://git-scm.com/)
-   [Python 3.9+](https://www.python.org/)
-   [Docker](https://www.docker.com/get-started)

---

### Método 1: Executando com Docker (Recomendado)

Este método garante um ambiente consistente e isolado.

```bash
# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO

# 2. Construa a imagem Docker
# O comando lê o Dockerfile e monta a imagem com todas as dependências.
docker build -t churn-api .

# 3. Inicie o contêiner a partir da imagem
# -d: Roda em modo detached (segundo plano)
# -p 8000:8000: Mapeia a porta 8000 do seu computador para a porta 8000 do contêiner
docker run -d -p 8000:8000 --name churn-container churn-api
```

A API estará disponível em `http://localhost:8000`.

---

### Método 2: Executando Localmente

Este método é útil para desenvolvimento e depuração rápida.

```bash
# 1. Clone o repositório
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd SEU_REPOSITORIO

# 2. Crie e ative um ambiente virtual
python3 -m venv venv
source venv/bin/activate  # No Windows: .\venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Inicie o servidor da API
# A flag --reload reinicia o servidor automaticamente após alterações no código.
uvicorn src.main:app --reload
```

A API estará disponível em `http://127.0.0.1:8000`.

## 💡 Uso da API

Após iniciar a aplicação, você pode interagir com a API de duas formas:

### 1. Via Documentação Interativa (Swagger UI)

Abra seu navegador e acesse:
[**http://localhost:8000/docs**](http://localhost:8000/docs)

Você encontrará o endpoint `/predict`, onde poderá preencher os dados do cliente em um formulário JSON e clicar em "Execute" para ver a predição em tempo real.

### 2. Via `curl` (Linha de Comando)

Você também pode fazer uma requisição POST usando uma ferramenta como `curl`:

```bash
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "TenureMonths": 2,
    "ContractType": "Month-to-month",
    "MonthlyCharges": 53.85,
    "SupportTickets": 0,
    "FeatureUsageScore": 30,
    "TotalCharges": 108.15
  }'
```

**Resposta Esperada:**

```json
{
  "prediction": "Não Churn",
  "probability": 0.4123
}
```

## 👨‍💻 Autor

-   **Pietro Medeiros**
-   **LinkedIn:** [Meu Linkedin](https://www.linkedin.com/in/pietro-medeiros-770bba162/)
