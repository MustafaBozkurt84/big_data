1. In play folder create 
```
mkdir model-kara-murat
```

2. Copy all files into model-kara-murat (all except model-kara-murat)
`rsync -av --progress * model-kara-murat --exclude model-kara-murat`  

3. into model-kara-murat
```
cd model-kara-murat/

[train@localhost model-kara-murat]$ ll
total 20
-rw-rw-r--. 1 train train 2125 Nov 19 16:50 app.py
-rw-rw-r--. 1 train train  176 Nov 19 16:50 Dockerfile
-rw-rw-r--. 1 train train  766 Nov 24 18:59 README.md
-rw-rw-r--. 1 train train   44 Nov 19 16:50 requirements.txt
drwxrwxr-x. 2 train train   84 Nov 19 16:50 saved_models
-rw-rw-r--. 1 train train 1560 Nov 19 16:50 train.py
```

4. Start gitea `sudo systemctl start gitea`  

5. Create git project
```
# Init git project
[train@localhost model-kara-murat]$ git init

# Add gitea repo
[train@localhost model-kara-murat]$ git remote add origin http://localhost:3000/jenkins/model-kara-murat.git

# Add existing files
[train@localhost model-kara-murat]$ git add . --all

# Commit and push
[train@localhost model-kara-murat]$ git commit -m "First commit from cid/cd jenkins project"

[train@localhost model-kara-murat]$ git push origin master --force
Username for 'http://localhost:3000': jenkins
Password for 'http://jenkins@localhost:3000': Ankara_06
```

6. Start Jenkins

7. Gor oo Jenkins `gitea-kara-murat`project
- Configure
- Execute shell
```
docker build -t erkansirin78/iris_classifier:1.0 .
docker stop iris_classifier || true && docker rm iris_classifier || true
docker run --name iris_classifier -v $(pwd)/saved_models:/app/saved_models -p 8082:8082 -d erkansirin78/iris_classifier:1.0
```

8. Do some change and push it to gitea


9. Check result with curl
```
[train@localhost model-kara-murat]$ curl http://127.0.0.1:8082/iris -XGET -H 'Content-Type: application/json' -d '{"SepalLengthCm":5.1, "SepalWidthCm":3.5, "PetalLengthCm":1.4 , "PetalWidthCm": 1.2}'
{"result":"[{\"label\":\"Iris-setosa\"}]"}
```