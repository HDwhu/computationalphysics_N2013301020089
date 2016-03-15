def judge(a):
    A=['    #    ','   # #   ','  #####  ',' #     # ','#       #']
    D=['####  ','#   # ','#    #','#   # ','####  ']
    H=['#   #','#   #','#####','#   #','#   #']
    O=[' ### ','#   #','#   #','#   #',' ### ']
    U=['#   #','#   #','#   #','#   #',' ### ']
    t=['','','','','']
    for i in a :
        if(i=='A'):
            for j in range(len(t)):
                t[j]=t[j]+'  '+A[j]
        elif(i=='D'):
            for j in range(len(t)):
                t[j]=t[j]+'  '+D[j]
        elif(i=='H'):
            for j in range(len(t)):
                t[j]=t[j]+'  '+H[j]
        elif(i=='O'):
            for j in range(len(t)):
                t[j]=t[j]+'  '+O[j]
        elif(i=='U'):
            for j in range(len(t)):
                t[j]=t[j]+'  '+U[j]
    for i in t:
        print i+'\n'
x=raw_input("Input:")
judge(x)
