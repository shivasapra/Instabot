# importing library
import requests
# importing constants
from constants import BASE_URL, Access_Token
# importing a function from a file
from get_post_id import get_post_id


# function is defined to like a recent post of a user
def like_user_post(insta_username):
    media_id = get_post_id(insta_username)
    request_url = BASE_URL + 'media/%s/likes' % media_id
    payload = {"access_token": Access_Token}
    like_a_post = requests.post(request_url, payload).json()     # post request to like a media
    if like_a_post['meta']== 200:
        print "\npost liked successfully"
    else:
        print "\nunable to like post"
