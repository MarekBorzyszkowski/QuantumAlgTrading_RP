#!/bin/bash
if [ ! -d src/venv ]; then
  echo "venv hasn't been initialized. Running setup.sh"
  ./setup.sh
fi
source src/venv/bin/activate

echo "Start of tests"
src/venv/bin/python3 src/main.py example.json
echo "End of tests"
echo "Start of tests"
src/venv/bin/python3 src/main.py example_2.json
echo "End of tests"
deactivate