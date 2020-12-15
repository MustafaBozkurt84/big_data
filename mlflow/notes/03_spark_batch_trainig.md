## Before start, be sure mlflow server is running.

1. Train and register your model

- Do the first training  
`/home/train/advanced_ds_bigdata/mlflow/play/spark_advertsing_regression/train.py`

```
(venvspark) [train@localhost spark_advertsing_regression]$ spark-submit --master yarn train.py
```

- Once your train is over open browser http://localhost:5000/#/experiments/1 see the experiment.

- Second training with different model, log params and different run name
```
(venvspark) [train@localhost spark_advertsing_regression]$ spark-submit --master yarn train_gbt_.py
```

2. Make Batch predictions

- You can get the registered model name and version from training logs on screen or mlflow web ui.
An example of train logs on screen:  
```
Model name: spark-gbt-regressor, version 1
```
`/home/train/advanced_ds_bigdata/mlflow/play/batch_prediction/batch_prediction.py `

- Make batch predictions
```
(venvspark) [train@localhost spark_advertsing_regression]$ spark-submit --master yarn batch_prediction.py
```
Expected output:  
` [20.945943568858045, 10.664813501556925, 10.069087121212121, 20.29233789018, 14.147560744810743] ` 

