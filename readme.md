# TV Show Recommender
we have all been there. wanna watch a tv show? YEEEEEAH. but which episode? 

you choose an episode, and when starting to watch, you realize you have watched it recently. OUCH

so I wrote this command line tool to help us decide which episode to watch next. it keeps track of episodes you have watched, and every time suggests a new one. when you have watched all, it resets the data and starts over.

##requirements
to use this tool, you need python3 and sqlalchemy library.

##how to install
these steps should be done once:


```git clone https://github.com/fmmajd/SitcomRecommender.git```

```cd SitcomRecommender```

```pip3 install sqlalchemy```

```python3 init.py```

##how to use
every time you need a suggestion, cd to the directory containg the script, and run:

```python3 main.py```