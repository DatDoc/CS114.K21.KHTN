# Dataset
foody-dataset is scraped from foody.vn using the Web Scraper - a web scraping extension on Chrome. (https://webscraper.io/) <br/>
foody-dataset contains over 30000 comments and ratings of each comment. <br/>
Duplicate comments or spam comments have been removed by the author. <br/>
# Preprocessing the dataset
Convert the document to lowercase <br/>
Remove duplicate letters in a word (Example: Món này ngon quáaaaaaaa -> Món này ngon quá) <br/>
Normalize the accent structure (Example: hoà -> hòa) <br/>
Normalize sentiment words (Example: okie, okê, oke, okela -> ok) <br/>
Normalize emojis to 2 types: positive and negative <br/>
(Example: positive emojis: :), :v, :-], etc | negative emojis: :(, :-(, etc) <br/>
Remove punctuations and noise characters
# Code 
https://colab.research.google.com/drive/1BqcF6hyMT2QmFW_sfN--56Xl9XygM1hC?usp=sharing
Updating...
