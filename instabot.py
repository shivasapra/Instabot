from self_info import self_info
from get_own_post import get_own_post
from user_info import user_info
from get_users_post import get_users_post
from like_user_post import like_user_post
from post_a_comment import post_a_comment

print 'welcome!!!!'
print 'what do you want to do'

temp = 1
while temp:
    choice = int(raw_input("\n1. Get your own info"
                           "\n2. Download your own post" 
                           "\n3. Get information of any user" 
                           "\n4. Get user's recent post" 
                           "\n5. like user's recent media" 
                           "\n6. post a comment on user's post" 
                           "\n7. close application"))

    if choice == 1:
        a = self_info()
    elif choice == 2:
        get_own_post()
    elif choice == 3:
        username = raw_input("enter user's username")
        user_info(username)
    elif choice == 4:
        username = raw_input("enter user's username")
        get_users_post(username)
    elif choice == 5:
        username = raw_input("enter user's username")
        like_user_post(username)
    elif choice == 6:
        username = raw_input("enter user's username")
        post_a_comment(username)
    elif choice == 7:
        temp = 0
    else:
        print 'invalid choice please try again'
        exit()
