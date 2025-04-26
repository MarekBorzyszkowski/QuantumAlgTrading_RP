#!/bin/bash
if [ ! -d venv ]; then
  echo "venv hasn't been initialized. Running setup.sh"
  ./setup.sh
fi
source venv/bin/activate

echo "Start of tests S&P"
venv/bin/python3 src/main.py jsons/S\&P.json
#echo "Start of tests wig_20"
#src/venv/bin/python3 src/main.py jsons/wig_20.json
#echo "Start of tests NVDA"
#src/venv/bin/python3 src/main.py jsons/NVDA.json
#echo "Start of tests CDR"
#src/venv/bin/python3 src/main.py jsons/CDR.json
#echo "Start of tests NFLX"
#src/venv/bin/python3 src/main.py jsons/NFLX.json
#echo "Start of tests PKO"
#src/venv/bin/python3 src/main.py jsons/PKO.json
#echo "Start of tests TSLA"
#src/venv/bin/python3 src/main.py jsons/TSLA.json
#echo "Start of tests MSFT"
#src/venv/bin/python3 src/main.py jsons/MSFT.json
#echo "Start of tests META"
#src/venv/bin/python3 src/main.py jsons/META.json
#echo "Start of tests AAPL"
#src/venv/bin/python3 src/main.py jsons/AAPL.json
#echo "Start of tests ADBE"
#src/venv/bin/python3 src/main.py jsons/ADBE.json
#echo "Start of tests AMZN"
#src/venv/bin/python3 src/main.py jsons/AMZN.json
#echo "Start of tests BAC"
#src/venv/bin/python3 src/main.py jsons/BAC.json
#echo "Start of tests BRK-B"
#src/venv/bin/python3 src/main.py jsons/BRK-B.json
#echo "Start of tests COST"
#src/venv/bin/python3 src/main.py jsons/COST.json
#echo "Start of tests CVX"
#src/venv/bin/python3 src/main.py jsons/CVX.json
#echo "Start of tests HD"
#src/venv/bin/python3 src/main.py jsons/HD.json
echo "End of tests"
deactivate
