# Install mongodb
brew update
brew install mongodb
mkdir -p /data/db
sudo chown -R `id -un` /data/db

# Get a sample databaes
wget http://media.mongodb.org/zips.json
mongoimport -v --file=zips.json #loads into test.zips
# if you want to specify a database and collection
# mongoimport --db scratch --collection zips --file zips.json
