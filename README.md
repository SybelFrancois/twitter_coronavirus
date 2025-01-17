# Coronavirus twitter analysis


**Introdution**

The project involves analyzing the spread of COVID-19 on social media using geotagged tweets sent in 2020. The dataset contains approximately 1.1 billion tweets stored in zip files, with each file containing tweets for a single day in JSON format. The project follows a MapReduce procedure, where the map step is modified to track the usage of hashtags on both a language and country level, and the reduce step merges the output from map.py to visualize the combined results. The project requires working with large-scale multilingual datasets and using the MapReduce divide-and-conquer paradigm to create parallel code.

**Learning Objectives:**

1. work with large scale datasets
1. work with multilingual text
1. use the MapReduce divide-and-conquer paradigm to create parallel code


**The results:**

![bargraph_for#coronavirus_tweets_by_Country](https://user-images.githubusercontent.com/123044356/223394004-16b8da51-a1b3-4987-a509-962cebd64bf6.png)

The barplot representing the coronavirus hashtag tweets on a country level shows that the top 10 countries with the highest tweets sent with the coronavirus hashtag were the United States, India, Great Britain, Spain, Italy, Brazil, Argentina, Mexico, France, and Turkey. As expected, the United States had the highest number of tweets sent with the #coronavirus hashtag in 2020, exceeding 200,000 tweets. India and Great Britain follow with fewer than 100,000 tweets each.


![bargraph_for#coronavirus_tweets_by_Language](https://user-images.githubusercontent.com/123044356/223394085-f06f6078-24d7-4f22-b570-1177c3b5a60e.png)

According to the barplot illustrating coronavirus hashtag tweets on a language level, English, Spanish, undetermined languages, Italian, and Portuguese were the top five languages with the highest number of tweets sent. It was anticipated that English would be at the top, and not surprising to see Spanish among the top five languages since three Hispanic countries were among the highest countries to send tweets with coronavirus hashtags in the previous bar graph. In 2020, English had the highest number of tweets sent with the #coronavirus hashtag, with over 400,000 tweets.


![bargraph_for#코로나바이러스_tweets_by_Country](https://user-images.githubusercontent.com/123044356/223394228-f9935495-c3b0-43d0-a3ed-f3970bacfb3f.png)

The barplot by country for the Korean coronavirus translation hashtag (#코로나바이러스) shows that Korea had the highest number of tweets sent, with over 250 tweets. This result was expected, as it is the native language of the country. Hong Kong followed in second place, with Spain coming in third.


![bargraph_for#코로나바이러스_tweets_by_Language](https://user-images.githubusercontent.com/123044356/223394282-1222b13c-c41d-4ac5-b796-de0c8edc3c94.png)

The barplot by language for the Korean coronavirus translation hashtag (#코로나바이러스) shows that Korean had the highest number of tweets sent, with again over 250 tweets, English followed in second place, with Undetermined Languages coming in third.

## Computation
To handle the computation, I created a parallel code using the MapReduce divide-and-conquer paradigm, and successfully ran the map.py file on all the tweets in the /data/Twitter\ dataset folder from 2020, generating output files in both .lang and .country format. I developed a shell script, run_maps.sh, that loops over each file in the dataset and runs map.py on that file.

To merge the outputs generated by the map.py file, I utilized reduce.py, and generated the output file named reduced.lang, which contains the combined results. Finally, I accomplished the objective of monitoring the spread of the coronavirus on social media by visualizing the total number of times the hashtag #coronavirus was used on a language and country level, using the visualize.py file.
You will scan all geotagged tweets sent in 2020 to monitor for the spread of the coronavirus on social media.


This project required LOTs of computation time. I was working on it for over one week. Most the reason why it requied that much time it is because we, all students, in the class, for the class (Big Data) use the CMC-lambda server for the class. When many students are connected and trying the run some commands at the same time, it makes it take longer.


**Conclusion and skills squired:**

In this project, I developed skills in working with large-scale datasets and multilingual text by analyzing 1.1 billion tweets sent in 2020. I used Python to process and extract valuable information from big data, specifically by creating a modified map.py file that tracks the usage of hashtags on both a language and country level. This project helped me practice my ability to write a shell script and use `nohup`, `&`, and other process control tools effectively.


## Background

Approximately 500 million tweets are sent everyday.
Of those tweets, about 1% are *geotagged*.
That is, the user's device includes location information about where the tweets were sent from.
The lambda server's `/data-fast/twitter\ 2020` folder contains all geotagged tweets that were sent in 2020.
In total, there are about 1.1 billion tweets in this dataset.


The tweets are stored as follows.
The tweets for each day are stored in a zip file `geoTwitterYY-MM-DD.zip`,
and inside this zip file are 24 text files, one for each hour of the day.
Each text file contains a single tweet per line in JSON format, a popular format for storing data that is closely related to python dictionaries.

For the project I used Vim, which is able to open compressed zip files and explore the dataset.


I used [MapReduce](https://en.wikipedia.org/wiki/MapReduce) procedure to analyze these tweets.
in order to be able to process large scale parallel processing that project required. I followed three steps to do it:

<img src=mapreduce.png width=100% />



## Tasks

I mostly had to work on the map and reduce steps since the partition (splitting up the tweets into one file per day) was done for us already.

**Runtime:**

The simplest and most common scenario is that the map procedure takes time O(n) and the reduce procedure takes time O(1).
If having p<<n processors, then the overall runtime will be O(n/p).

I completed the following tasks:

1.   After forking the [twitter\_coronavirus](https://github.com/mikeizbicki/twitter_coronavirus) repo and clone my fork onto the lambda server.
   Given a `map.py` file, I modified it so that it tracks the usage of the hashtags on both a language and country level by creating a variable `counter_country` and      modifying this variable in the `#search hashtags` section of the code appropriately. The `map.py` file processes a single zip file of tweets.
   Running `map.py` resulted in two files: one that ends with `.lang` for the lanuage dictionary,
   and one that ends in `.country` for the country dictionary. I used the `place` key, which contains a dictionary with the `country_code` key that most countries have    lookup the country that a tweet was sent from, and made the appropriate changes in case of edge cases.

2. My `map.py` file being ready to track results for each country, I theb run the map file on all the tweets in the `/data-fast/twitter\ 2020` folder.
   by creating a shell script `run_maps.sh` that loops over each file in the dataset and runs `map.py` on that file.
   Each call to `map.py` can took some time to finish since the exact runtime depended on the server's load due to fellow classmates.)
   I also used the `nohup` command to ensure the program continues to run after idsconnecting and the `&` operator to ensure that all `map.py` commands run in 
   parallel.

3. After my modified `map.py` has run on all the files, I had a lorge number of files `outputs` folder.
   I then used the `reduce.py` file to combine all of the `.lang` files into a single file,
   and all of the `.country` files into a different file.

4. Lastly, I used the `visualize.py` file to count the total number of occurrences of each of the hashtags.

  



