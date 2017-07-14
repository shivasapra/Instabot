import requests
from constants import BASE_URL, Access_Token
from get_own_post import get_own_post
comment = []


# function is defined to like a recent post of a user
def list_of_comments():
    media_id = get_own_post()
    request_url = BASE_URL + 'media/%s/comments?access_token=%s' % (media_id,Access_Token)
    print 'GET request_url : ' + request_url
    list_of_comment = requests.get(request_url).json()
    if list_of_comment['meta']['code'] == 200:
        temp = 0
        while len(list_of_comment['data']) > temp:
            comment.append(list_of_comment['data'][temp]['text'])
            temp = temp + 1
        print "comments are"
        for a in comment:
            print a + "\n"
    else:
        print 'request not completed'
list_of_comments()