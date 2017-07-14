from self_info import self_info
from get_own_post import get_own_post
from user_info import user_info
from get_users_post import get_users_post
from like_user_post import like_user_post
from post_a_comment import post_a_comment

print 'welcome!!!!'



print 'what do you want to do'
while 1:
    print '1. get own data'
    print "2. get other user's data"
    print '3. close application'
    choice = raw_input('\nenter your choice')
    if choice == 1:
        own_data()
    elif choice == 2:
        user_data()
    elif choice == 3:
        exit()
    else:
        print 'enter correctly'
