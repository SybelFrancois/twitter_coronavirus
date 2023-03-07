#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser() # Create the ArgumentParser object
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--type',choices=['Country', 'Language'], required=True) # Type of analysis: for country or language
parser.add_argument('--percent',action='store_true') 
args = parser.parse_args() # Parse the arguments

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg') # set the backend for Matplotlib to "Agg" to create figures without display
import matplotlib.font_manager as fm # to manage fonts for Matplotlib
import matplotlib.pyplot as plt # interface to create plots in Matplotlib

# define the path to the Korean font file
pathfonts = 'fonts/NotoSansKR-Bold.otf' 

# Load the Korean font to display Korean characters
display_korean = matplotlib.font_manager.FontProperties(fname=pathfonts) 

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# sort the count values
data_sorted = sorted(counts[args.key].items(), key=lambda item: (item[1], item[0]), reverse=False)


# retrieve the top 10 data
top_data = data_sorted[-10:]

# determines the range of x values to use in the plot based on the length of top_data
if len(top_data) < 10:
    x_range = len(top_data)
else:
    x_range = 10

# Initialize empty lists for x, y, z
x ,y, z  = [],[],[]

# Loop over the range of the x_range variable and append each value to x
for i in range(x_range):
    x.append(i)

# Loop over the top_data items and append the values to y and z
for k,v in top_data:
    y.append(v)
    z.append(k)

# generate the bar graph and specs
plt.figure(figsize=(8,8))
plt.subplots_adjust(bottom=0.33)
plt.bar(x,y)

# create the titles and labels
plt.xlabel( "The different Country ISO Codes" if args.type == "Country" else "The different Languages")
plt.ylabel('The number of Tweets (2020)')
plt.title(f'Total {args.key} Hashtag Tweets Usage by TOP 10-{args.type} in the Twitter Dataset in 2020', fontproperties=display_korean)
plt.xticks(x, z)

# store the bar graph as a png file
plt.savefig('bargraph_for' + args.key + '_tweets_by_' + args.type, fontproperties=display_korean)

#close the plot
plt.close()
