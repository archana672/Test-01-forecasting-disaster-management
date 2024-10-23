echo import pandas as pd > src\model_evaluation.py
echo from sklearn.metrics import mean_squared_error >> src\model_evaluation.py
echo import joblib >> src\model_evaluation.py
echo. >> src\model_evaluation.py
echo def evaluate_model(model, test_data): >> src\model_evaluation.py
echo     predictions = model.forecast(len(test_data)) >> src\model_evaluation.py
echo     mse = mean_squared_error(test_data, predictions) >> src\model_evaluation.py
echo     return mse >> src\model_evaluation.py
echo. >> src\model_evaluation.py
echo if __name__ == "__main__": >> src\model_evaluation.py
echo     model = joblib.load('model.pkl') >> src\model_evaluation.py
echo     test_data = pd.read_csv('data/test/test_data.csv') >> src\model_evaluation.py
echo     mse = evaluate_model(model, test_data['value']) >> src\model_evaluation.py
echo     print(f'Mean Squared Error: {mse}') >> src\model_evaluation.py
