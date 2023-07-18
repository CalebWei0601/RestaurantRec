# RestaurantRec

When I go out with my family, they always don't know what to eat so usually I am the one left with the painful task of deciding the spot.

By the time I finally propose something like Korean BBQ, they may reject and say they now want sushi and don't know where to go.

This is what inspired me to try and build this project - a restaurant recommender that takes a message describing what people would like to eat today and output a few recommendations (in the ideal case).

Currently with the Google Places API I have obtained information and reviews on more than 1500 restaurants in Singapore.  I have also used the SBERT model avaialble on sbert.net to reliably predict a user input query and come up with top comments that associate with the input.

I've also wrapped the tool into a Flask app with a simple UI to make it more user-friendly.

I'll also do some more work on the Flask end, make the site look nicer and maybe add some filter options based on distance, method of commute, etc, as well as update this file with instructions on how to run the project locally.

I may also consider hosting the app on a web server soon.
