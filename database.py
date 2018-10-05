import os
import json

data_file = os.environ.get('DATA_FILE', 'planets.json')
PLANETS = json.load(open(data_file, 'rt'))


def planets():
    return PLANETS


def planet(planet_id):
    return PLANETS.get(planet_id)
