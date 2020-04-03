import json as systemjson


##########################################
# creates JSON from an object
#
# Input: o, any object
# Output: a String containing the JSON representation of the input object
#
def json(obj):
    return systemjson.dumps(obj, default=lambda o: o.__dict__, sort_keys=True, indent=4)
