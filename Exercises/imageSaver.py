# going to make a program that saves a image from the internet
# By Levance Wamley jr

import urllib.request

# Created a function to gather the link, file path and set a name


def img_saver(url, file_path, filename):
    # here we are telling the program where to save and name the file and what type of extension we want
    full_path = file_path + filename + ".jpeg"
    # we go to grab the image from the link and then save it.
    urllib.request.urlretrieve(url, full_path)


# link to file and name
link = "https://image.shutterstock.com/image-photo/ripe-red-apples-wooden-box-600w-1115705399.jpg"
filename = "apple"


img_saver(link, "images/", filename)
