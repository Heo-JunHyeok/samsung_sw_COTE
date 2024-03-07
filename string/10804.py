T=int(input())

for test_case in range(1,T+1):
    string=input()
    result=''
    
    for i in string[::-1]:
        if i =='b':
            result+='d'
        elif i=='d':
            result+='b'
        elif i=='p':
            result+='q'
        elif i=='q':
            result+='p'
    
    print(f'#{test_case} {result}')