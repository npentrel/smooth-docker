From mongo:3.6.5
COPY ingredients.json /ingredients.json
CMD mongoimport --host database --collection ingredients --type json --file ingredients.json --jsonArray
