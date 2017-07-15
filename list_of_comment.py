# importing library
import requests
# importing constants
from constants import BASE_URL, Access_Token
# importing a function from a file
from get_post_id import get_post_id
comment = []   # a list to store comments


# function is defined to like a recent post of a user
def list_of_comments(username):
    media_id = get_post_id(username)
    request_url = BASE_URL + 'media/%s/comments?access_token=%s' % (media_id,Access_Token)
    print '\nGET request_url : ' + request_url
    list_of_comment = requests.get(request_url).json()     # get request to get json object
    if list_of_comment['meta']['code'] == 200:
        temp = 0
        while len(list_of_comment['data']) > temp:
            comment.append(list_of_comment['data'][temp]['text'])    # appending comments in a list
            temp = temp + 1
        print "comments are"
        for a in comment:            # printing comments
            print a + "\n"
    else:
        print 'code other than 200'
#list_of_comments()