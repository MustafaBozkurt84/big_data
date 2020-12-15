1. Create a now experiment from terminal
```
(venvspark) [train@localhost ~]$ mlflow experiments create -n keras_heart_classification -l s3://train-mlflow
Created experiment 'keras_heart_classification' with id 1
```

2. Train model  
`(venvspark) [train@localhost keras_heart_churn_classification]$ python3 train.py`  
