## HoloLinks

A static site with links to holomembers channels, also shows the latest videos.

---

TODO:
1. Show who is live, and show the upcoming videos
2. Activate github pages, and host it on github,
3. use a github action to update the latest video part.
4. Create instructions for how to build and generate a local version.

---

**get_yt_data.py** - a scripts that gets the 3 latest videos, uses the youtube api.
need to rebuild the page after the script is run

	bundle exec jekyll build

## Build

[Install](https://jekyllrb.com/docs/installation/)
install the jekyll and bundler gem.

	gem install jekyll bundler

jekyll should now be installed to build run:

	jekyll build

## Memo
To get live status, try to extract it from hololive schedule site.

moved REGloss members to the main page, but currently keeping the html file
if more members join the dev_is branch.

each region has its own json file, but also liquid file, these are
currently identical only change is which json file to loop through.

but currently cannot get it to work with a variable for the region,
I think the problem is how the "offset: continue" works, it seems to
treat "site.data.hololive[region]" as one namespace even if the
region variable changes.

removed the Gemfiles, and now only use the jekyll build command,
after any update can never get bundler to install correctly.
