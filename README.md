# Pipeline-Path-Finder
This Application finds the shortest Route using Dijkstra Algorithm for Laying the pipeline By considering all industrial and residential Place's between the path
To run the application:

step 1) clone this repository

step 2) create your own google maps api

step 3) in the maps.py file you can see i have created a environment variable called googleapikey so you can either create a environment variable too or hardcode the key

step 4) next in the index.html file u have to copy paste ur own api key inside the "{insert your apikey here}" that i have specified inside src. there are two instances where you have to change

it looks like:

<script src="https://maps.googleapis.com/maps/api/js?key={insertyourapikeyhere}&libraries=places&callback=initAutocomplete" async defer></script>
(note that u can use environment variables for this too and i will soon update the code using environment variables so that no hard coding is needed)

step5) now the code is ready to run. you can run the app.py file
