# importing constants
from constants import Access_Token, BASE_URL
# impoting libraries
import requests
import urllib # library for downloading images


# function is defined to get own post
def get_own_post():
    request_url = BASE_URL + 'users/self/media/recent/?access_token=' + Access_Token
    print '\nGET request_url : ' + request_url
    own_media = requests.get(request_url).json()     # get request to get json object
    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name) # downloading imagee
            print '\n******************************' \
                  '\nyour image has been downloaded' \
                  '\n******************************'
            return own_media['data'][0]['id']
        else:
            print 'post does not exist'
    else:
        print "code other than 200"
