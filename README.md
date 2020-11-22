# CODECHELLA 2020

## SK216: Data Crawlers to crawl keywords in area of crime, child abuse, woman abuse etc.

## TWEELP - Twitter for Help



See installation [here](#how-to-install)

## What is this?
TWEELP is an AI based SaaS web data integration (WDI) platform which send alerts for Disaster/Crime to the twitteruser as well as local agency for them to investigate/help. It converts the unstructered web data into structured format by extracting, preparing and integrating web data in areas of crime, natural disasters, etc for consumption in criminal and GEO helping investigation agencies. It takes full ability of Twitter API to fulfill its job.

TWEELP also provides a visual environment for automating the workflow of extracting and transforming web data using the twitter api. After gaining insights from  the tweets of people from a particular location where disaster, crimes etc started to gain interest, the web data extraction module provides a visual environment for designing automated workflows for harvesting data, going beyond HTML/XML parsing of static content to automate end user interactions yielding data that would otherwise not be immediately visible.

Once extracted, the software provides full data preparation capabilities that are used for harmonizing and cleansing the web data. 

For consuming the results, TWEELP provides several options. It has its own visualization and dashboarding module( which includes filtering & AI processing of media) to help criminal investigators gain the insights that they need. It also provides REST APIs that offer full access to everything that can be done on our platform, allowing web data to be integrated directly. 

TWEELP uses NLP to cleanse the data. The AI Model is capable of geolocating the probable crimes, natural disasters etc.

Scheduler is a sub application developed for TWEELP  to automatically recheck  the authenticity of existing disasters or crime so that if any new report is found, it checks whether the old report was correct or not. By default scheduler runs after every 3 days which can otherwise be set to the user's choice.


## Features
- Structured data
- SMS & Email alerts to user of disaster prone location. 
- Email PDF report
- Graphical Data
- Trends and Analytica
- Multiple keywords search
- Multiple filters option
- Schedule the report to verify the authenticity of the disaster.
- User registration and advance admin panel
- AI to search smart
- TWEELP own custom REST API to open source developers to use!
- Multilingual support
- Media data AI Processing
- Scalable to search Thousands of query using Celery Workers!

![collage (1)](https://user-images.githubusercontent.com/28597524/89094557-b4f13e00-d3e2-11ea-8bb6-13c6b3111271.jpg "FALCON Results")





### Efficient
FALCON uses the celery worker feature to take up multiple tasks from the user and perform it in a queue.
We can have upto 10 celery workers at a time. This feature allows us to crawl around ten million links and scrap around one million links.


## How to Install
- Create virtual enviorement, then activate it.
- Create ```.env``` file and add ```export SOCIAL_AUTH_TWITTER_KEY=
export SOCIAL_AUTH_TWITTER_SECRET=
export ACCESS_KEY=
export ACCESS_SECRET=
export ACCOUNT_SID=
export AUTH_TOKEN=```
- Install all the requirements file, ``` pip install -r requirements.txt```
- Setup RabbitMQ server for broker service, ``` docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management```
- start your rabbitmq broker service.
- In falcon setting change ```CELERY_BROKER_URL = 'your_rabbitmq_address'```, if your not using the default port for RabbitMQ.
- Run celery worker, ```celery -A falcon worker -l info```
- For first time usage, ```python manage.py migrate``` and create admin ```python manage.py createsuperuser```
- Run FALCON, ```python manage.py runserver```





