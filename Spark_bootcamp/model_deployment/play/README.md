This project deploy a classification model on iris data.


## Build
`docker build -t erkansirin78/iris_classifier:1.0 .`

## RUN
```
docker container stop iris_classifier
docker container rm iris_classifier
docker run --name iris_classifier -v $(pwd)/saved_models:/app/saved_models -p 8082:8082 -d erkansirin78/iris_classifier:1.0
```

## API USAGE
## METHOD GET
## url
`http://localhost:8082/iris`  

## sample request on Postman
```
{"SepalLengthCm":5.1, "SepalWidthCm":3.5, "PetalLengthCm":1.4 , "PetalWidthCm": 0.2}

# Expected output
{
    "result": "[{\"label\":\"Iris-setosa\"}]"
}
```

## Request via curl
```
[train@localhost model-kara-murat]$ curl http://127.0.0.1:8082/iris -XGET -H 'Content-Type: application/json' -d '{"SepalLengthCm":5.1, "SepalWidthCm":3.5, "PetalLengthCm":1.4 , "PetalWidthCm": 1.2}'

# Expected output
{"result":"[{\"label\":\"Iris-setosa\"}]"}
```