from constants import Access_Token, BASE_URL
import requests
import urllib


# function is defined to get own post
def get_own_post():
    request_url = BASE_URL + 'users/self/media/recent/?access_token=' + Access_Token
    print 'GET request_url : ' + request_url
    own_media = requests.get(request_url).json()
    if own_media['meta']['code'] == 200:
        if len(own_media['data']):
            image_name = own_media['data'][0]['id'] + '.jpeg'
            image_url = own_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'your image has been downloaded'
            return own_media['data'][0]['id']
        else:
            print 'post does not exist'
    else:
        print "request not completed"
