# importing constants
from constants import Access_Token, BASE_URL
# importing library
import requests


# function is defined to get user id
def get_user_id(insta_username):
    request_url = BASE_URL + 'users/search?q=' + insta_username + '&access_token=' + Access_Token
    print '\nGET request_url : ' + request_url
    user_info = requests.get(request_url).json()         # get request to get json object
    if user_info['meta']['code'] == 200:
        if len(user_info['data']) > 0:
            return user_info['data'][0]['id']     # returning user id
        else:
            print '\nuser does not exist'
    else:
        print '\ncode other than 200'
        exit()
