"""
Module for generating a map of twitter user`s friendlist
"""

import random
import folium
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim
from twitter_api import twitter2


def get_user_locations(name_of_user, count):
    """
    (str, int) -> dict
    This func uses twitter API to get user friendlist.
    From this list we need user locations and icon url
    """
    location_dict = {}

    data = twitter2.get_data(name_of_user, count)

    print(data)

    for user in data['users']:
        location_dict[user['name']] = (user['location'], user['profile_image_url'])

    return location_dict


def get_coords(location_dict):
    """
    dict -> dict
    This func uses geopy to transform locations to coordinates
    """
    result_dict = {}

    geolocator = Nominatim(user_agent="map_of_films_by_year", timeout=3)
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

    for elem in location_dict:
        try:
            location = geolocator.geocode(location_dict[elem][0])
            coords = (location.latitude, location.longitude)

            if coords in result_dict:
                random_epsilon = random.randint(-10, 10)
                new_coord = (coords[0] + random_epsilon / 100, coords[1] + random_epsilon / 100)
                result_dict[new_coord] = (elem, location_dict[elem][1])

            else:
                result_dict[coords] = (elem, location_dict[elem][1])

        except AttributeError:
            pass

    return result_dict


def build_map(dict_of_locations):
    """
    (tuple(float, float), dict) -> None
    This func generates a map by given coordinates
    2 layers: main map, photo-markers of users
    """
    mapp = folium.Map(zoom_start=2)

    films_layer = folium.FeatureGroup(name="People Map")

    for coord in dict_of_locations:
        icon = folium.features.CustomIcon(dict_of_locations[coord][1],
                                          icon_size=(40, 40))

        films_layer.add_child(folium.Marker(location=coord, popup=dict_of_locations[coord][0],
                                            icon=icon))

    mapp.add_child(films_layer)

    mapp.save('templates/Map_people.html')



def main(name_of_user, count):
    """
    (str, int) -> None
    Main func
    """
    print("Getting info from Tweeter...")

    location_dict = get_user_locations(name_of_user, count)

    print("Getting coords...")

    coords_dict = get_coords(location_dict)

    print("Building map...")

    build_map(coords_dict)

    print("Done")


if __name__ == '__main__':
    main('yewhen2', 20)
