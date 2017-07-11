import requests
from constants import BASE_URL, Access_Token
from get_post_id import get_post_id


# function is defined to like a recent post of a user
def post_a_comment(insta_username):
    media_id = get_post_id(insta_username)
    comment = raw_input('enter comment')
    request_url = BASE_URL + 'media/%s/comments' % media_id
    payload = {"access_token": Access_Token, "message": comment}
    post_a_comment = requests.post(request_url,payload).json()
    if post_a_comment['meta']['data'] == 200:
        print "post commented successfully"
    else:
        print "unable to post a comment"
