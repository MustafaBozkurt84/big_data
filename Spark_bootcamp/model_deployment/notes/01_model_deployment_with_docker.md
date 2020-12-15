1. We will use iris data, build a ML model then deploy it with docker. After deployment we will do some predictions with Postman from host machine.

2. On Virtualbox forward 8082 port from host to guest machine.  

3. in play folder   
    - train.py is for model training.  
    - app.py is for model deployment.  
    - requirements.txt will be used by docker   
    - Dockerfile is to build docker image of our application  
    - saved_models foler for to save models (both classifier and preprocess models)

4. Overview train.py and app.py then execute instructions in README.md  

```
(venvspark) [train@localhost play]$ docker build -t erkansirin78/iris_classifier:1.0 .



5. Once docker container is up and runnning make predictions with Postman and curl.  

6. On Postman  
create a new GET request `http://127.0.0.1:8082/iris`  
Headers Key -> Content-Type and value -> application/json  
Body -> raw and JSON  
Content of Body:   
`{"SepalLengthCm":5.1, "SepalWidthCm":3.5, "PetalLengthCm":1.4 , "PetalWidthCm": 0.2}`  

Send request 

Expected result:  
```
{
    "result": "[{\"label\":\"Iris-setosa\"}]"
}
```

7. Try different numbers.

8. Prediction with curl
```
[train@localhost ~]$ curl http://127.0.0.1:8082/iris -XGET -H 'Content-Type: application/json' -d '{"SepalLengthCm":5.1, "SepalWidthCm":3.5, "PetalLengthCm":1.4 , "PetalWidthCm": 1.2}'
```
Expected output: `{"result":"[{\"label\":\"Iris-setosa\"}]"}`  


