docker exec -it $(docker ps -lq) mongoimport --collection ingredients --type json --file ingredients.json --jsonArray
