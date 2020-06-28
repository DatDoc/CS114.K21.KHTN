# Dataset
foody-dataset is scraped from foody.vn using the Web Scraper - a web scraping extension on Chrome. (https://webscraper.io/) <br/>
foody-dataset contains over 30000 comments and ratings of each comment. <br/>
Duplicate comments or spam comments have been removed by the author. <br/>
# Preprocessing the dataset
Convert the document to lowercase
Remove duplicate letters in a word (Example: Món này ngon quassaaaaaa -> Món này ngon quá)
Normalize the accent structure (Example: hoà -> hòa)
Normalize sentiment words (Example: okie, okê, oke, okela -> ok)
Normalize emojis to 2 types: positive and negative 
(Example: positive emojis: :), :v, :-], etc | negative emojis: :(, :-(, etc)
Remove punctuations and noise characters
