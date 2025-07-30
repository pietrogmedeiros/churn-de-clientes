# -------------------------------------------------------------------
# ARQUIVO: src/main.py
# Copie e cole todo este conteúdo no seu arquivo.
# -------------------------------------------------------------------

from fastapi import FastAPI
from pydantic import BaseModel, Field
import pandas as pd
import joblib
from pathlib import Path # <-- A importação crucial

# 1. Definição da Aplicação FastAPI
app = FastAPI(
    title="API de Predição de Churn",
    description="Uma API para prever a probabilidade de um cliente cancelar o serviço, com base nos dados de treinamento.",
    version="1.0.0"
)

# 2. CARREGAMENTO DO MODELO (A FORMA CORRETA E ROBUSTA)
# Esta seção garante que o modelo seja encontrado, não importa de onde você execute o servidor.
try:
    # Encontra o diretório do arquivo atual (a pasta 'src')
    BASE_DIR = Path(__file__).resolve().parent
    # Cria o caminho completo para o arquivo do modelo
    MODEL_PATH = BASE_DIR / "churn_model.joblib"
    
    print(f"Tentando carregar o modelo de: {MODEL_PATH}")
    model = joblib.load(MODEL_PATH)
    print("Modelo carregado com sucesso!")

except Exception as e:
    print(f"ERRO AO CARREGAR O MODELO: {e}")
    model = None

# 3. Definição dos modelos de dados (Pydantic)
# Este é o formato dos dados que a API espera receber.
# DEVE CORRESPONDER ÀS FEATURES USADAS NO TREINAMENTO!
class CustomerData(BaseModel):
    TenureMonths: int = Field(..., example=43)
    ContractType: str = Field(..., example="One year")
    MonthlyCharges: float = Field(..., example=102.80)
    SupportTickets: int = Field(..., example=3)
    FeatureUsageScore: int = Field(..., example=85)
    TotalCharges: float = Field(..., example=4400.50)

# Este é o formato da resposta da API
class ChurnPrediction(BaseModel):
    prediction: str
    probability: float

# 4. Criação do Endpoint de Predição (/predict)
@app.post("/predict", response_model=ChurnPrediction)
def predict_churn(data: CustomerData):
    if model is None:
        return {"error": "Modelo não foi carregado. Verifique os logs do servidor."}

    # Converte os dados recebidos em um DataFrame do Pandas
    input_df = pd.DataFrame([data.dict()])

    # Faz a predição de probabilidade (o pipeline cuida do pré-processamento)
    # Pegamos a probabilidade da classe '1' (Churn)
    churn_probability = model.predict_proba(input_df)[0][1]

    # Define o rótulo da predição com base em um limiar de 0.5
    prediction_label = 'Churn' if churn_probability > 0.5 else 'Não Churn'

    # Retorna o resultado no formato definido por ChurnPrediction
    return {
        "prediction": prediction_label,
        "probability": churn_probability
    }

# Endpoint raiz para verificar se a API está no ar
@app.get("/")
def read_root():
    return {"message": "API de Churn está no ar. Acesse /docs para testar o endpoint /predict."}