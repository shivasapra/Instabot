import requests
from constants import BASE_URL, Access_Token
from get_own_post import get_own_post


# function is defined to like a recent post of a user
def list_of_comments():
    media_id = get_own_post()
    request_url = BASE_URL + 'media/%s/comments?access_token=%s' % (media_id,Access_Token)
    print 'GET request_url : ' + request_url
    list_of_comment = requests.get(request_url).json()
    if list_of_comment['meta']['code'] == 200:
        if len(list_of_comment['data']):
            print list_of_comment['data'][0]['text']
        else:
            print 'no comments'
    else:
        print 'request not completed'
list_of_comments()