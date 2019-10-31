# NewsAggregator

This Project contain two main part; Reddit and News. As it was suggested in assignment description, URL, r/news was exploited to collect the news around reddit and /news was utilized to gather news around News Api. I used rest-framework-django to build APIs. 

I would clarify the two app as below.

  ##  1- Reddit
Firstly, for testing the Reddit APIs, I made a Script app in [Reddit](https://www.reddit.com/prefs/apps). Also, for using Reddit APIs, I used [Praw](https://praw.readthedocs.io) Package. Necessary Username, ClientID and Passwords for authorization is included in Praw.ini.
Request method of r/news is “get” and based on query parameter presence on request parameters or APIs of search, would be called or APIs of recent news, would be called.

  ##  2- News API
For testing the News API, [NewsAPIClient](https://newsapi.org/docs/client-libraries/python) have been used which necessary Secret Key for authorization is included in venv/bin/activate which after activation of Virtual Environment would be exported as Environment Variable and we would obtain this secret key in setting.py file. 
Request method is “get”.  News API is only following one function for calling and collecting news. If this function is out of query, would return all the news, but if there was a query, would search and collect all the news tagged as that query.

In both app, there are several Unit Test, examines situations such as redirect or assess the response. 
For documentation of APIs, [django-rest-swagger](https://django-rest-swagger.readthedocs.io/en/latest/) has been used that could be looked at /docs.

  ##  Follow these instructions for running application
  ##### 1- run below command in your terminal (with python3.6)
    pip install -r requirements.txt
  ##### 2-copy below lines at the end of praw.ini, in praw packages that installed in $VIRTUALENV/lib/python3.6/site-packages
  
    [user]
    client_id=zmHMvdl7_V6jOg
    client_secret=_-lUyJsY3c9Op0s-l_Ox2-DLz4o
    password=asddsahadiz
    username=hadizamani77
  
  ##### 3-run below command in your terminal
  
    export NEWS_API_SECRET_KEY="d282e470f89243e68406e0ecc21f39ea"
    
  ##### 4-run below command in your terminal
    python manage.py runserver
  
  
