def judge(a):
    for i in a :
        if(i=='A'):
            print '    #'
            print '   # #'
            print '  #####'
            print ' #     #'
            print '#       #'
        elif(i=='D'):
            print '####'
            print '#   #' 
            print '#    #'
            print '#   #'
            print '####'
        elif(i=='H'):
            print '#   #'
            print '#   #'
            print '#####'
            print '#   #'
            print '#   #'
        elif(i=='O'):
            print ' ###'
            print '#   #'
            print '#   #'
            print '#   #'
            print ' ###'
        elif(i=='U'):
            print '#   #'
            print '#   #'
            print '#   #'
            print '#   #'
            print ' ###'
x=raw_input("Input:")
judge(x)
