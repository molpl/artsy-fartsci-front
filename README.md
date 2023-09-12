# Artsy-Fartsci


Artscy-Fartsci is an educational tool designed to introduce users of all artistic persuasions to fine art, using Deep Learning and the Artsy.net API data set.

* Choose an image - use your imagination! A piece of art you saw in a gallery, your toddler's first crayon drawing, a picture of your neighbour's chinchilla - upload directly into Artsy-Fartsci
* Our custom build auto-encoder will reduce the image to its component features, picking out elements such as colour, texture, form and even things the human eye can't pick up.
* Your image will be compared to our dataset of over 10,000 images and the five most similar images will be returned and displayed.
* Then - its up to you. Find the name of the artwork you loved, or similar art and where to find it. Show your toddler which great artists they're similar to - maybe they can have a go at drawing something new. Find the fine art version of your beloved pet.

Behind the scenes

* The image is passed to a custom built API which returns the indexes of the five most similar images.
* These indexes are then used to retrieve the artwork title from a BQ table, and the original image from a Google Bucket. This is displayed to the user.
* The front end is powered by Streamlit, and currently hosted in the cloud.

Future development

* Add more information about the results - artist, movement, genre, medium, where you can see it. Once it is completed, display in the frontend, with links to relevant gallery pages and more information.
* Expand the educational page - add a blurb about each movement, specific info about the artists displayed.
