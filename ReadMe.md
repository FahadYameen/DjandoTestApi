# Factor-A
## Prerequisite
- Docker

## Steps to run
```
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose up
```
## Example

POST REQUEST :
- Now send a request at http://0.0.0.0:8000/api/post
- Request Body => {
   "score" : 10,
   "title" : "test data"
}
![image](https://drive.google.com/uc?export=view&id=143KFDKki-uN4PEu3Mv01WRy9p8p67v0t)
GET REQUEST :

- Now send a request at http://0.0.0.0:8000/api/post
- the response will be the top 5 record with highest score value

![image](https://drive.google.com/uc?export=view&id=1M0K1SB4wpfueMbsfT-vOvOao-0oO-kEo)