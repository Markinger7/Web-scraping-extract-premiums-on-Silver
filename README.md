# Web-scraping-to-extract-premiums-on-Silver
There are always premiums attached to buying precious metals physically. Generally, it is closer to the spot price for gold than for silver. During the corona crisis the premiums for silver have increased a lot. So, it would be interesting to see how the premiums of silver are changing over time.

I’ve been manually downloading the html of a website (<a href='https://www.gold.de/aufgeldtabelle/silber/'>Gold.de</a>), where the premiums of silver are shown for different products.

## files
This repo contains a python script (<b>get_silver_premiums.py</b>) that downloads the data from the website, transforms it into a pandas DataFrame and gives you a csv file with the cleaned data.
The script needs to be activated from an environment which has python, pandas and numpy installed.
The goal is that the script runs each day automatically.

<b>'silver premiums from the folder.ipynb'</b> is a jupyter notebook that transforms the manually downloaded html files into cleaned csv files.

In the repo there is also another jupyter notebook (<b>silver premiums.ipynb</b>) which I used to create the the script and currently is used for applying regular expressions to extract more informations from the product column, like product name, weight of coin/bar and retailer.
