import json


jsonFileHandler = open('config/config.json', 'r')
parking_data = json.load(jsonFileHandler)


# hierarchical structure of parking
'''
LOT
 |__LANES
      |__SPOTS
'''


# searching the location of sensor and returning the tuple
def locate(sensor_id):
    for lotKey, lotValue in parking_data.items():
        for laneKey, laneValue in lotValue.items():
            for spotKey, spotValue in laneValue.items():
                if spotValue['sensor_id'] == sensor_id:
                    sensor_location = (lotKey, laneKey, spotKey)
                    return sensor_location

    # if the given sensor_id is invalid
    return None


# Closing file
jsonFileHandler.close()
