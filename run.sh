#!/bin/bash

#If editing this file on Windows, please run this command afer every save:
#   sed -i -e 's/\r$//' run.sh
#This command removes ^M characters

export FLASK_APP=app.py
export FLASK_DEBUG=1

flask run --host=0.0.0.0
