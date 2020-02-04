# Nostrock

This repository is a more deeper version of https://github.com/jg-fisher/googleSentiment with it being able to scrap the
news sites of the google news results given and searching for the subjectivity and sentimental value of the paragraphs of these 
and give an 'Idea' of the perception a stock has in the most recent news articles.

Simply run Analysis.py in the terminal followed by the stock you want to search:

> python Analysis.py tsla

The command will show you the stock current value and will read the give you the sentimental value of the latest two news articles in google news by scrapping the paragraphs of these sites. You can read the article yourself without navigating to google news, just by adding 'print(blob)' at the end of the for loop inside the function called pages.

If the input given is not a stock it will still give you the sentimental and subjectivity value of the search query.

