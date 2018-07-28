# DONT DO THIS IN PRODUCTION - you should seed your data from another container (or in any other way :) )
mongod --fork --logpath database.log

mongoimport --collection ingredients --type json --file ingredients.json --jsonArray

mongo --eval "db.getSiblingDB('admin').shutdownServer()"
mongod --bind_ip_all
