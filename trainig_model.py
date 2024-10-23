echo import pandas as pd > src\model_training.py
echo from statsmodels.tsa.arima.model import ARIMA >> src\model_training.py
echo import yaml >> src\model_training.py
echo. >> src\model_training.py
echo def train_model(data): >> src\model_training.py
echo     model = ARIMA(data, order=(1, 1, 1)) >> src\model_training.py
echo     model_fit = model.fit() >> src\model_training.py
echo     return model_fit >> src\model_training.py
echo. >> src\model_training.py
echo if __name__ == "__main__": >> src\model_training.py
echo     data = pd.read_csv('data/processed/cleaned_data.csv') >> src\model_training.py
echo     model_fit = train_model(data['value']) >> src\model_training.py
echo     model_fit.save('model.pkl') >> src\model_training.py
