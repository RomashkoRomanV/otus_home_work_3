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
kubectl get ing
curl -H 'Host: arch.homework' http://<IP_ADDRESS>/otusapp
curl -H 'Host: arch.homework' http://<IP_ADDRESS>/otusapp/health
curl -H 'Host: arch.homework' http://<IP_ADDRESS>/otusapp/config
curl -H 'Host: arch.homework' http://<IP_ADDRESS>/otusapp/db
curl -H 'Host: arch.homework' http://<IP_ADDRESS>/otusapp/user/1
curl -X 'POST' -H 'Host: arch.homework' -H 'Content-Type: application/json' \
'http://<IP_ADDRESS>/otusapp/user' \
--data-raw '{
    "userName": "TestUser",
    "firstName": "FirstName",
    "lastName": "LastName",
    "email": "user2@domain.root",
    "phone": "+11231231212"
}'
curl -H 'Host: arch.homework' http://<IP_ADDRESS>/otusapp/user/2
curl -X 'PUT' -H 'Host: arch.homework' -H 'Content-Type: application/json' \
'http://<IP_ADDRESS>/otusapp/user/2' \
--data-raw '{
    "firstName": "FirstName1",
    "lastName": "LastName1",
    "email": "user21@domain.root",
    "phone": "+11111111111"
}'
curl -X 'DELETE' -H 'Host: arch.homework' http://<IP_ADDRESS>/otusapp/user/2
curl -H 'Host: arch.homework' http://<IP_ADDRESS>/otusapp/db
```
Postman collection url:
  https://web.postman.co/workspace/My-Workspace~37b48d30-c657-4222-8584-21093bf5181b/request/24396906-6b377e42-5da4-41af-a98d-e1ee66141cbf

