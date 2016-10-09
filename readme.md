# TV Show Recommender
we have all been there. wanna watch a tv show? YEEEEEAH. but which episode? 

you choose an episode, and when starting to watch, you realize you have watched it recently. OUCH

so I wrote this command line tool to help us decide which episode to watch next. it keeps track of episodes you have watched, and every time suggests a new one. when you have watched all, it resets the data and starts over.


##requirements
to use this tool, you need python3 and sqlalchemy.


##what shows are included?
currently, these shows are included:

- Friends

feel free to add json file of any show you want, or you can send you requests to me


##how to install
these steps should be done once:


```git clone https://github.com/fmmajd/SitcomRecommender.git```

```cd SitcomRecommender```

```pip3 install sqlalchemy```

if you want to add all the shows, for example it's the first time initializing, use this command(this does not work yet):

```python3 init.py```

but if you are already set and have data and just want to add an extra show, say Friends, you can use this command:

```python3 init Friends```



##how to use
every time you need a suggestion, cd to the directory containg the script, and run:

```python3 main.py```
