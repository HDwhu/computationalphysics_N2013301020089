def judge(a):
    for i in a :
        if(i=='A'):
            print '    #\n   # #\n  #####\n #     #\n#       #'
        elif(i=='D'):
            print '####\n#   #\n#    #\n#   #\n####'
        elif(i=='H'):
            print '#   #\n#   #\n#####\n#   #\n#   #'
        elif(i=='O'):
            print ' ###\n#   #\n#   #\n#   #\n ###'
        elif(i=='U'):
            print '#   #\n#   #\n#   #\n#   #\n ###'
x=raw_input("Input:")
judge(x)
