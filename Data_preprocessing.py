echo import pandas as pd > src\data_preprocessing.py
echo. >> src\data_preprocessing.py
echo def load_data(filepath): >> src\data_preprocessing.py
echo     data = pd.read_csv(filepath) >> src\data_preprocessing.py
echo     return data >> src\data_preprocessing.py
echo. >> src\data_preprocessing.py
echo def clean_data(data): >> src\data_preprocessing.py
echo     data.dropna(inplace=True) >> src\data_preprocessing.py
echo     return data >> src\data_preprocessing.py
echo. >> src\data_preprocessing.py
echo if __name__ == "__main__": >> src\data_preprocessing.py
echo     raw_data = load_data('data/raw/example_data.csv') >> src\data_preprocessing.py
echo     cleaned_data = clean_data(raw_data) >> src\data_preprocessing.py
echo     cleaned_data.to_csv('data/processed/cleaned_data.csv', index=False) >> src\data_preprocessing.py
