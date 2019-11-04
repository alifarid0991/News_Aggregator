# NewsAggregator

This Project contain two main part; Reddit and News. I used rest-framework-django to build APIs. 

I would clarify the two part as below.

  ##  1- reddit
Firstly, for testing the Reddit APIs, I made a Script app in [Reddit](https://www.reddit.com/prefs/apps). Also, for using Reddit APIs, I used [Praw](https://praw.readthedocs.io) Package. Necessary Username, ClientID and Passwords for authorization is included in Praw.ini.

  ##  2- newsapi
For testing the News API, [NewsAPIClient](https://newsapi.org/docs/client-libraries/python) have been used which necessary Secret Key for authorization is included in venv/bin/activate which after activation of Virtual Environment would be exported as Environment Variable and I would obtain this secret key in setting.py file. 
Request method is “get”.  News API is only following one function for calling and collecting news. If this function is out of query, would return all the news, but if there was a query, would search and collect all the news tagged as that query.

In this app, there are several Unit Test, examines situations such as redirect or assess the response. 

In this unit test I send 500 requests to the server with diffrent words as parameter. because these apps in [reddit](https://www.reddit.com/prefs/apps) and [newsapi](https://newsapi.org/docs/client-libraries/python) are testing apps it may get some errors such as 
"you are not allowed to send more than 500 in 12 hours". I add handle exception for these cases and also in this unit test I print duration of each request in app.log file for 50 requests.

For documentation of APIs, [django-rest-swagger](https://django-rest-swagger.readthedocs.io/en/latest/) has been used that could be looked at /docs.

  ##  Follow these instructions for running application after cloning project
  ##### 1- run below command (python3.6)
    pip install -r requirements.txt
  ##### 2-copy the below lines at the end of praw.ini, in praw packages that installed in $VIRTUALENV/lib/python3.6/site-packages
  
    [user]
    client_id=zmHMvdl7_V6jOg
    client_secret=_-lUyJsY3c9Op0s-l_Ox2-DLz4o
    password=asddsahadiz
    username=hadizamani77
  
  ##### 3-run below command in your terminal
  
    export NEWS_API_SECRET_KEY="52ec1647432f4428ac6c80f23b1a3513"
    
  ##### 4-run the server by manage.py
  
  