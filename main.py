# ASSIGNMENT 05

# Web scraping
# For web scraping i've used some common libraries/modules or pakages(Like: bs4, BeautifulSoup, requests, pandas)
# these are builtin libraries

from bs4 import BeautifulSoup
import requests
import pandas as pd

# This is the url of the given link(Assignment 05) of islamqa.info
url = "https://islamqa.info/en/answers/128927/it-is-essential-to-acquire-and-take-possession-of-items-before-selling-them"

# requests.get(url) is used to send a GET request to the specified url(like i've given above)
# and return the response to object
r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

# This method is provided by BeautifulSoup, which is used to parse the HTML docs.
# .text is an attribute and used for retrieving textual content of an element
title = soup.find(class_="title is-4 is-size-5-touch").text

questionNum = soup.find(class_="level-item has-separator").text

question = soup.find(class_="single_fatwa__question text-justified").text

answer = soup.find(class_="single_fatwa__answer__body text-justified _pa--0").text

# Double square brackets "[[]]" is used to create a list inside a list
data = [[title, questionNum, question, answer]]
df = pd.DataFrame(data, columns=["title", "questionNum", "questions", "answer"])     # DataFrame is basically used in analysis, cleaning, visualization of data
print(df)

# .to_csv() is a method and used to write contents of DataFrame to CSV file
# CSV stands for Comma Separated Values
df.to_csv("islamqa.csv")
print("CSV file successfully created!!")
