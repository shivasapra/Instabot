from constants import Access_Token, BASE_URL
import requests
from get_user_id import get_user_id


# a function is defined to get user_info
def user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'user does not exist'
        exit()
    request_url = BASE_URL + 'users/%s?access_token=%s' % (user_id, Access_Token)
    print 'GET request_url : ' + request_url
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        if len(user_info['data']) > 0:
            print 'username : ' + user_info['data']['username']
            print 'no. of followers : ' + user_info['data']['counts']['followed_by']
            print 'no. of followings : ' + user_info['data']['counts']['follows']
            print 'no. of posts : ' + user_info['data']['counts']['media']
        else:
            print 'No data for this user'
    else:
        print 'request not completed'