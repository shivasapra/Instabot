# importing functions from another file
from own_data import own_data
from user_data import user_data


# program starts
print 'welcome!!!!'
while 1:
    print '\nwhat do you want to do\n'
    print '1. get own data'
    print "2. get other user's data"
    print '3. close application'
    choice = int(raw_input('\nenter your choice'))
    if choice == 1:
        own_data()
    elif choice == 2:
        user_data()
    elif choice == 3:
        exit()
    else:
        print '\n***************' \
              '\nenter correctly' \
              '\n***************'
# program ends :) :) :)
