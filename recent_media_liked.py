# importing constants
from constants import Access_Token, BASE_URL
# importing libraries
import requests
import urllib    # library to download image


# function is defined to get another user's post
def recent_media_liked():
    request_url = BASE_URL + 'users/self/media/liked?access_token=' + Access_Token
    print '\nGET request_url : ' + request_url
    liked_media = requests.get(request_url).json()     # get request to get json object
    if liked_media['meta']['code'] == 200:
        if len(liked_media['data']) > 0:
            image_name = liked_media['data'][0]['id'] + '.jpeg'
            image_url = liked_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)     # downloading image
            print '\n******************************' \
                  '\nyour image has been downloaded' \
                  '\n******************************'
        else:
            print 'there is no recent post'
    else:
        print 'code other than 200'
# https://api.instagram.com/v1/users/self/media/liked?access_token=ACCESS-TOKEN
# recent_media_liked()
