# importing functions from another files
from self_info import self_info
from get_own_post import get_own_post
from recent_media_liked import recent_media_liked


def own_data():
    while 1:
        print '\nwhat do you want to do\n'
        print 'enter 1 to get your own information'
        print 'enter 2 to get your own post'
        print 'enter 3 to get recent media you liked'
        print 'enter 4 to close application'
        choice = int(raw_input('\nplease enter'))

        if choice == 1:
            self_info()
        elif choice == 2:
            get_own_post()
        elif choice == 3:
            recent_media_liked()
        elif choice == 4:
            exit()
        else:
            print '\n*************************' \
                  '\nplease enter valid option' \
                  '\n*************************'
