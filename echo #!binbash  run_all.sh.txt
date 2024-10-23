echo #!/bin/bash > run_all.sh
echo python src\data_preprocessing.py >> run_all.sh
echo python src\model_training.py >> run_all.sh
echo python src\model_evaluation.py >> run_all.sh
