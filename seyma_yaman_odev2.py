def elmas(N):
    if N%2==1:
        for i in range(1,N+1):
            if i%2==1:
                print ' '*(N-i)+'* '*i
        for i in range(1,N+1):
            if i%2==0:
                print ' '*i +'* '*(N-i)
    else:
        for i in range(1,N+1):
            if i%2==0:
                print ' '*(N-i)+'* '*i
        for i in range(1,N+1):
            if i%2==0:
                print ' '*i +'* '*(N-i)

a=elmas(9)








