# OtusHomeWork3 - Kubernetes base
Commands to apply:
```
git clone https://github.com/RomashkoRomanV/otus_home_work_2.git  
cd otus_home_work_2  
minikube addons enable ingress  
kubectl apply -f postgres.yaml
kubectl apply -f initdb.yaml
helm install myapp ./otus-chart
```
Tesing:
```
curl http://arch.homework/otusapp
curl http://arch.homework/otusapp/health
curl http://arch.homework/otusapp/config
curl http://arch.homework/otusapp/db
curl http://arch.homework/otusapp/user/1
curl -X 'POST' -H 'Content-Type: application/json' \
'http://arch.homework/otusapp/user' \
--data-raw '{
    "userName": "TestUser",
    "firstName": "FirstName",
    "lastName": "LastName",
    "email": "user2@domain.root",
    "phone": "+11231231212"
}'
curl http://arch.homework/otusapp/user/2
curl -X 'PUT' -H 'Content-Type: application/json' \
'http://arch.homework/otusapp/user/2' \
--data-raw '{
    "firstName": "FirstName1",
    "lastName": "LastName1",
    "email": "user21@domain.root",
    "phone": "+11111111111"
}'
curl -X 'DELETE' http://arch.homework/otusapp/user/2
curl http://arch.homework/otusapp/db
```
Postman collection url:
  https://web.postman.co/workspace/My-Workspace~37b48d30-c657-4222-8584-21093bf5181b/request/24396906-6b377e42-5da4-41af-a98d-e1ee66141cbf

