#!/bin/bash
mkdir src
cp -r ../dr/* ./src/
mv ./src/dr.py ./src/__main__.py
cd src
zip dr *.py
cd ..
mv src/dr.zip ./
cat chromeosSB.txt dr.zip > dr
curl -X PURGE https://pypi.org/project/classRant
curl -X PURGE https://pypi.org/project/devRantSimple/
python3 -m pip install --no-cache-dir --upgrade -r ../requirements.txt
chmod +755 ./dr
mv ./dr /usr/local/bin/
rm -rf ./dr ./src ./dr.zip
