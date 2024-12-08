#!/bin/bash
if [ ! -d src/venv ]; then
  echo "venv hasn't been initialized. Running setup.sh"
  ./setup.sh
fi
source src/venv/bin/activate

echo "Start of tests S&P"
src/venv/bin/python3 src/main.py jsons/S\&P.json
echo "End of tests"
echo "Start of tests wig_20"
src/venv/bin/python3 src/main.py jsons/wig_20.json
echo "End of tests"
echo "Start of tests CDR"
src/venv/bin/python3 src/main.py jsons/CDR.json
echo "End of tests"
echo "Start of tests META"
src/venv/bin/python3 src/main.py jsons/META.json
echo "End of tests"
echo "Start of tests NFLX"
src/venv/bin/python3 src/main.py jsons/NFLX.json
echo "End of tests"
echo "Start of tests PKO"
src/venv/bin/python3 src/main.py jsons/PKO.json
echo "End of tests"
echo "Start of tests TSLA"
src/venv/bin/python3 src/main.py jsons/TSLA.json
echo "End of tests"
deactivate