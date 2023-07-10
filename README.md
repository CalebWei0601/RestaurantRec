# RestaurantRec

When I go out with my family, they always don't know what to eat so usually I am the one left with the painful task of deciding the spot.

By the time I finally propose something like Korean BBQ, they may reject and say they now want sushi and don't know where to go.

This is what inspired me to try and build this project - a restaurant recommender that takes a moody message describing what the gang would like to eat today (in the ideal case).

Currently with the help of Google API I have obtained information and reviews on more than 1300 restaurants in Singapore.  I have also used the SBERT model avaialble on sbert.net to reliably predict a user input query and come up with top comments that associate with the input.

The next step is to wrap it up into an application.  The current plan is Flask.

I'll update this as I go.
