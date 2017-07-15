# importing constants
from constants import Access_Token, BASE_URL
# importing library
import requests


# a function to get own info
def self_info():
    request_url = BASE_URL + 'users/self/?access_token=' + Access_Token
    print '\nGET request url : %s' % request_url
    user_info = requests.get(request_url).json()   # get request to get json object
    if user_info['meta']['code'] == 200:
        if len(user_info['data']) > 0:
            print '\nusername : ' + user_info['data']['username']
            print 'no. of followers : ' + str(user_info['data']['counts']['followed_by'])
            print 'no. of followings : ' + str(user_info['data']['counts']['follows'])             # printing details
            print 'no. of posts : ' + str(user_info['data']['counts']['media'])
        else:
            print 'user does not exist'
    else:
        print 'code other than 200'
