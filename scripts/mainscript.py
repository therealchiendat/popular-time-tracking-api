import json
import populartimes


def app():
    api_key = 'API KEY HERE'
    top_left_coor = (46.063567, -66.739405)
    bottom_right_coor = (45.822528, -66.640126)
    types = ["food","grocery_or_supermarket"]
    data = populartimes.get(api_key, types, top_left_coor,
                            bottom_right_coor, 20, 1000)
    return data
