#!/usr/bin/python
"""
Author: Greyson Paris 

This is the first side project I've ever really worked on. Lets see how it goes 

Premise 
    Duplicate the functionality of https://twitter.com/Dominant_Colors
    learn about and practice interacting with the twitter api, manipulating images, applying classification algorithms, 
     designing solutions, software architecture, soliciting for donations (maybe)

Note that this is a python3 project.
"""
import numpy as np
import os
from   PIL import Image
import random
from   sklearn.cluster import KMeans
import sys ## for argv / params 

## TODO -- add better path handling
## TODO -- refactor things into reusable functions 

IMAGE_BAND = 'RGB'
# SEED = int( random.random() * 100 ) ## for spicing up the run 
SEED_KMEANS = 0 
inputPath = "/Users/tefferon/Documents/Workspace/dominant-colors/assets/nut.png"

def outputPath( inputPath ):
    import datetime
    path, fileExtension = inputPath.split('.')
    nowWithoutMicroseconds = datetime.datetime.now().isoformat().split('.')[0] ## ex, ['2019-07-27T13:49:38', '234493'][0]
    return "{}-{}.{}".format(path, nowWithoutMicroseconds, fileExtension)

## Open the file and settle for only RGB
im = Image.open(inputPath).convert(IMAGE_BAND)

## Get our image data and dimensions
width, height = im.size
pixels = np.array(im.getdata())

## create and run our model 
kmeans = KMeans(n_clusters=5, random_state=SEED_KMEANS).fit(pixels)

## round out and store our centroid values 
dominant_colors = []
for centroid in kmeans.cluster_centers_:
    dominant_colors.append( 
        tuple( int( round( color ) ) for color in list( centroid ) )
    ) 

# figure out the distribution of values in the clusters
labels = kmeans.predict(pixels)
## histogram bucketing is weird
dist, buckets = np.histogram(labels,range(6))
evenDist = dist - (dist % width)
# pmf = dist / len(pixels) ## not used, but interesting 

out = []
for label in sorted(labels):
    out.append( dominant_colors[label] )

outArray = []
for y in range(height):
    line = []
    for x in range(width):
        line.append( out[ width*y ] )
    outArray.append( line )

outImage = Image.fromarray( np.array( outArray , dtype=np.dtype('uint8') ), mode='RGB') 
outImage.save( outputPath( inputPath ) )

