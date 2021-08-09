## HoloLinks

**get_yt_data.py** - handles all yt request, save it in an json that acts as the db.
the rest of the site is static and only displays the data from the json db file.

the site will be regenerated when there is a change in the json db file.
this can be done by **entr** or **get_yt_data.py**

___

TODO:
- See who is live and upcoming videos!

#### See who is live and upcoming videos!
- Get The data (Search.list) (100 Quota)
- Save it in a Object

## Build

[Install](https://jekyllrb.com/docs/installation/) ruby and gem.
install projects gem dependencies with bundler
	
	gem install bundler
	bundle install

jekyll should now be installed to build run:

	bundle exec jekyll build