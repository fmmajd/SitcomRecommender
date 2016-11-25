# TV Show Recommender
we have all been there. wanna watch a tv show? YEEEEEAH. but which episode? 

you choose an episode, and when starting to watch, you realize you have watched it recently. OUCH

so I wrote this command line tool to help us decide which episode to watch next. it keeps track of episodes you have watched, and every time suggests a new one. when you have watched all, it resets the data and starts over.


## requirements

to use this tool, you need python3 and sqlalchemy.


## what shows are included?
currently, these shows are included:

- Friends
- Two and a Half Men
- How I Met Your Mother

feel free to add json file of any show you want, or you can send your requests to me


## how to install
these steps should be done once:


```git clone https://github.com/fmmajd/SitcomRecommender.git```

```cd SitcomRecommender```

```pip3 install sqlalchemy```

```python3 init.py```

after the last command, you would have to choose which shows to add. choose anumer in the list, and that show would be added to the database. you only need to add shows that you are gonna use. you can add additional shows in future(in that case, you only need to run the last command).



## how to use
every time you need a suggestion, cd to the directory containg the script, and run:

```python3 main.py```

choose which show you wanna watch, and enjoy it!


## how to add more shows
if you wanna add a show to this list, it's very easy. follow these steps:

- add a json file to 'shows' folder containing a list of episodes, in the same style as the other shows.
- add the show title and name of the json of file in the file 'shows/shows_list.json'
- init the db for the show by command: python3 init.py and choosing the show from list.

that's it. Enjoy!
