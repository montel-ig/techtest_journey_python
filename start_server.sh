#!/bin/bash

echo "starting the service"
FLASK_APP=server.py flask run -p 7890 -h 0.0.0.0
