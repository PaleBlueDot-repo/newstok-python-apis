## RUN
<h2>Active vertual env install folling package. Requred python version<b>3.12<b</h2>

pip install --user Flask

pip install selenium

pip install webdriver_manager

pip install google

pip install google-generative

pip install Pillow

pip install transformers

pip install tensorflow

python app.py

# newstok-python-apis [all are post api]

## Test to image generator api
end point:  http://127.0.0.1:5000/ml/generate-image
body:
{
  "prompt": "a man walking in the fire animated"
}


## classifying fake or real news
end-point: http://127.0.0.1:5000/ml/classify
body: 
{
  "text": "In 2016, a story circulated that Pope Francis made an unprecedented and shocking endorsement of Donald Trump for president"
}

## Summarization News test 

end-point: http://127.0.0.1:5000/ml/process-data
body:
{
    "input_text": "He downplayed. He denied. He dismissed.President Biden’s first television interview since his poor debate performance last week was billed as a prime-time opportunity to reassure the American people that he still has what it takes to run for, win and hold the nation’s highest office.But Mr. Biden, with more than a hint of hoarseness in his voice, spent much of the 22 minutes resisting a range of questions that George Stephanopoulos of ABC News had posed — about his competence, about taking a cognitive test, about his standing in the polls.The president on Friday did not struggle to complete his thoughts the way he did at the debate. But at the same time he was not the smooth-talking senator of his youth, or even the same elder statesman whom the party entrusted four years ago to defeat former President Donald J. Trump.Instead, it was a high-stakes interview with an 81-year-old president whose own party is increasingly doubting him yet who sounded little like a man with any doubts about himself."
}

## news scrapper api

# bangla-news-scrapper
http://127.0.0.1:5000/scraping/scrape_bangla_news?topic=science-technology
# english-news-scrapper
http://127.0.0.1:5000/scraping/scrape_english_news?topic=business-economy


