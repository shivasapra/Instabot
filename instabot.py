from own_data import own_data

print 'welcome!!!!'
while 1:
    print 'what do you want to do'
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
