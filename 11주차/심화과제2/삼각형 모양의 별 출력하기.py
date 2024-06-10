for line in range(1, 11, 1):
    for blank in range(10 - line):
        print(' ', end='')
        
    
    for star in range(line * 2 - 1):
        print('*', end='')
    
    print()