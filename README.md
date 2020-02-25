## Twitter Mappep and JSON Navigator

## General info
This project works as a web app that generates a map of users in Twitter friendlist of entered person
* twitter_api directory - additional module that works with Twitter to get info
* flask_app.py + templates directory - the module for running web aplication
* task3.py - main algoritm of starting api and building map

## General info - JSON Navigator
This is an additional module that can navigate through a JSON file. Mainly, it goes through JSON objects keys and advise you to choose next key
If it finds an object (dict) or a list on the key you entered, it ask you gi go on the next level

## Usage
Firstly, yuo should install some packages

```
$ pip install folium
$ pip install geopy
$ pip install flask
```

To use JSON Navigator:

```
$ python3 json_navigator.py
```

To use Twitter Mapper:

```
$ python3 flask_app.py
```
