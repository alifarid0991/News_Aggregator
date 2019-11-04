import praw
reddit = praw.Reddit(
        'user',  # user defined in praw.ini
        user_agent='hadi user agent'
    )

def get_api_reddit(query):

    if query:
        params = {
            'q': query
        }
        news = reddit.get('/search', params)
    else:
        news = reddit.get('/new')

    response_list = []
    for article in news.children:
        response_list.append(
            {
                "headline": article.title,
                "link": article.url,
                "source": 'reddit'
            }
        )
    return response_list
