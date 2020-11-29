# CODECHELLA 2020

## TWEELP - Twitter for Help



See installation [here](#how-to-install)

## What is this?
TWEELP is an AI based SaaS web data integration (WDI) platform which send alerts for Disaster/Crime to the twitter user as well as local agency for them to investigate/help. It converts the unstructered web data into structured format by extracting, preparing and integrating web data in areas of crime, natural disasters, etc for consumption in criminal and GEO helping investigation agencies. It takes full ability of Twitter API to fulfill its job.

TWEELP also provides a visual environment for automating the workflow of extracting and transforming web data using the twitter api. After gaining insights from  the tweets of people from a particular location where disaster, crimes etc started to gain interest, the web data extraction module provides a visual environment for designing automated workflows for harvesting data, going beyond HTML/XML parsing of static content to automate end user interactions yielding data that would otherwise not be immediately visible.

Once extracted, the software provides full data preparation capabilities that are used for harmonizing and cleansing the web data. 

For consuming the results, TWEELP provides several options. It has its own visualization and dashboarding module( which includes filtering & AI processing of media) to help criminal investigators gain the insights that they need. It also provides REST APIs that offer full access to everything that can be done on our platform, allowing web data to be integrated directly. 

TWEELP uses NLP to cleanse the data. The AI Model is capable of geolocating the probable crimes, natural disasters etc.

Scheduler is a sub application developed for TWEELP  to automatically recheck  the authenticity of existing disasters or crime so that if any new report is found, it checks whether the old report was correct or not. By default scheduler runs after every 3 days which can otherwise be set to the user's choice.


## Deployed on Pythonanywhere
The first version of TWEELP (only a demo version) is deployed, it is limited to threaded few results. AI tasks and CELERY workers are disabled due to free hosting service provider. To experience TWEELP to its full capability please [install](#how-to-install) it and use.

Deployed [here](https://tweelp.pythonanywhere.com/ "here").


### Test User
username - codechella
password - Codechella#2020


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



### Efficient
TWEELP uses the celery worker feature to take up multiple tasks from the user and perform it in a queue.
We can have upto 10 celery workers at a time. This feature allows us to use the twitter api capabilities to fetch around thousands of tweets for all TWEELP users parallely.


## How to Install
- Create virtual enviorement, then activate it.
- Create ```.env``` file and add 
  ```python
    export SOCIAL_AUTH_TWITTER_KEY=your_twitter_key
    export SOCIAL_AUTH_TWITTER_SECRET=your_twitter_secret
    export ACCESS_KEY=your_twitter_access_key
    export ACCESS_SECRET=your_twitter_access_secret
    export ACCOUNT_SID=your_twilio_account_sid
    export AUTH_TOKEN=your_twilio_auth_token```
    
- Install all the requirements file, ``` pip install -r requirements.txt```
- Run TWEELP, ```python manage.py runserver``` after migrating ```python manage.py migrate```

### Follow below steps to setup celery worker
- Setup RabbitMQ server for broker service, ``` docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management```
- start your rabbitmq broker service.
- In falcon setting change ```CELERY_BROKER_URL = 'your_rabbitmq_address'```, if your not using the default port for RabbitMQ.
- Run celery worker, ```celery -A falcon worker -l info```
- For first time usage, ```python manage.py migrate``` and create admin ```python manage.py createsuperuser```
- Run TWEELP, ```python manage.py runserver```





