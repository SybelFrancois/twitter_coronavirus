#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--type',choices=['Country', 'Language'], required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
# items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
# for k,v in items:
# print(k,':',v)


# sort the count values
data_sorted = sorted(counts[args.key].items(), key=lambda item: (item[1], item[0]))

# retrieve the top 10 data
top_data = data_sorted[-10:]


# generate the bar graph
plt.figure(figsize=(8,6))
plt.subplots_adjust(bottom=0.25)
plt.bar([i[0] for i in top_data], [i[1] for i in top_data])


# create the titles and labels
plt.xlabel('Countries' if args.type == 'Country' else 'Languages')
plt.ylabel('The number of Tweets (2020)')
plt.title(f'The TOP 10 {args.key} counts tweets by {args.type} in the Twitter Dataset in 2020 ')


# store the bar graph as a png file
plt.savefig('count_bar_graph_for' + args.key + 'tweets_by_' + args.type)


#close the plot
plt.close()
