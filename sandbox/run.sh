#!/bin/sh

cd /home/ywatanabe/Devel/github/asset-parser/

source ./.secrets
source /home/ywatanabe/Devel/env/bin/activate

echo 'Scraping nomura securities'
python3 sandbox/parse-nomura-securities.py

echo 'Scraping mufg'
python3 sandbox/parse-mufg.py
