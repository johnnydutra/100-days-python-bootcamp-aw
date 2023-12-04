music_dictionary = {
  "Guitar": "Six strings, can be acoustic or electric",
  "Drums": "Make some noise",
}

print(music_dictionary["Guitar"])

music_dictionary["Bass"] = "Nobody remembers it exists"
print(music_dictionary)

# music_dictionary = {}

music_dictionary["Drums"] = "Acoustic, electric or even virtual"

for key in music_dictionary:
  print(key)
  print(music_dictionary[key])

#####################

capitals = {
  "France": "Paris",
  "Germany": "Berlin"
}

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
  },
  "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

travel_log_list = [
  {
    "country": "France", 
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
  },
  {
    "country": "Germany", 
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
    "total_visits": 5
  }
]