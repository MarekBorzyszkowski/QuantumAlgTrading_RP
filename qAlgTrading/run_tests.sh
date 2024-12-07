#!/bin/bash
if [ ! -d src/venv ]; then
  echo "venv hasn't been initialized. Running setup.sh"
  ./setup.sh
fi
source src/venv/bin/activate
pwd

echo "Start of tests"
(src/venv/bin/python3 src/main.py)
echo "End of tests"