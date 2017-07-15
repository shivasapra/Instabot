# importing functions from another files
from user_info import user_info
from get_user_id import get_user_id
from get_post_id import get_post_id
from get_users_post import get_users_post
from like_user_post import like_user_post
from post_a_comment import post_a_comment


def user_data():
    username = raw_input('\nplease enter username')
    while 1:
        print '\nwhat do you want to do\n'
        print 'enter 1 to get user information'
        print 'enter 2 to get user id '
        print 'enter 3 to get user\'s post id'
        print 'enter 4 to get user\'s post'
        print 'enter 5 to like user\'s recent post'
        print 'enter 6 to post a comment on user\'s recent media'
        print 'enter 7 to close application'
        choice = int(raw_input('\nplease enter'))

        if choice == 1:
            user_info(username)
        elif choice == 2:
            id = get_user_id(username)
            print id
        elif choice == 3:
            id = get_post_id(username)
            print id
        elif choice == 4:
            get_users_post(username)
        elif choice == 5:
            like_user_post(username)
        elif choice == 6:
            post_a_comment(username)
        elif choice == 7:
            exit()
        else:
            print '\n*************************' \
                  '\nplease enter valid option' \
                  '\n*************************'
