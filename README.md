## HoloLinks

<<<<<<< HEAD
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
=======
A static site with links to holomembers channels, also shows the latest videos.

---

TODO:
1. Show who is live, and show the upcoming videos
	- The youtube API does not make this easy...
2. Add a nijisanji page or create a fork for with nijisanji.
3. Activate github pages, and host it on github.
4. Create instructions for how to build and generate a local version.

---

**get_yt_data.py** - currently gets the 3 latest videos.

To regenerate the site when .json is updated we can use **entr** or do it in **get_yt_data.py**.
See if github pages has the ability to run scripts.

#### To Get Upcoming and Live status 
- Get The data (Search.list) (Cost: 100)
- Save it in a Object
>>>>>>> c2e65f6fd88b3a5ce67e3743677785232f679b7c
