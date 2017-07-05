from constants import Access_Token, BASE_URL
import requests

from get_user_id import get_user_id


# function is defined to get another user's post
def get_users_post(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'user does not exist'
        exit()
    request_url = BASE_URL + 'users/%s/media/recent/?access_token=%s' % (user_id, Access_Token)
    print 'GET request_url : ' + request_url
    user_media = requests.get(request_url).json()
    if user_media['meta']['code'] == 200:
        if len(user_media['data']) > 0:
            return user_media['data'][0]['id']
        else:
            print 'there is no recent post'
    else:
        print 'request not completed'
    return None