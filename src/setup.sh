#!/bin/bash
if ![ -d venv ]; then
	echo "Start of creating venv\n"
	python -m venv ./venv
	echo "venv created\nStart of installing python packages\n"
	source ./venv/bin/activate
	pip install -r requirements.txt
	deactivate
	echo "End of installing python packages"
else
	echo "venv already installed!"
fi