# importing constants
from constants import Access_Token, BASE_URL
# importing library
import requests
# importing a function from a file
from get_user_id import get_user_id


# a function is defined to get user_info
def user_info(insta_username):
    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'user does not exist'
        exit()
    request_url = BASE_URL + 'users/%s?access_token=%s' % (user_id, Access_Token)
    print '\nGET request_url : ' + request_url
    user_info = requests.get(request_url).json()            # get request to get json object
    if user_info['meta']['code'] == 200:
        if len(user_info['data']) > 0:
            print '\nusername : ' + user_info['data']['username']
            print 'no. of followers : ' + user_info['data']['counts']['followed_by']        # printing user details
            print 'no. of followings : ' + user_info['data']['counts']['follows']
            print 'no. of posts : ' + user_info['data']['counts']['media']
        else:
            print '\nNo data for this user'
    else:
        print 'code other than 200'
