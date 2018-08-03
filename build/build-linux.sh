#!/bin/bash
mkdir src
cp ../dr/* ./src/
mv ./src/dr.py ./src/__main__.py
cd src
zip dr *.py
cd ..
mv src/dr.zip ./
cat otherSB.txt dr.zip > dr
curl -X PURGE https://pypi.org/project/devRantSimple/
python3 -m pip install -r ../requirements.txt
chmod +755 ./dr
mv ./dr /usr/local/bin/
rm -rf ./dr ./src ./dr.zip
