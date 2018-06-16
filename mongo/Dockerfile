From mongo:3.6.5
COPY pokemon.json /pokemon.json
CMD mongoimport --host database --collection pokemon --type json --file pokemon.json --jsonArray
