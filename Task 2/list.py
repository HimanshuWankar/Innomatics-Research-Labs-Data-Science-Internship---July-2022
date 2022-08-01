if __name__ == '__main__':
    N = int(input())
    
    lists = []
    
    for i in range(N):
        a = list(map(str,input().split( )))
        lists.append(a)
    
    arr = []
    
    for x in lists:
        if x[0] == "insert":
            i = int(x[1])
            e = int(x[2])
            arr.insert(i,e)
        
        elif x[0] == "print":
            print(arr)
             
        elif x[0] == "remove":
            e = int(x[1])
            arr.remove(e)
             
        elif x[0] == "append":
            e = int(x[1])
            arr.append(e)
            
        elif x[0] == "sort":
            arr.sort()
            
        elif x[0] == "pop":
            arr.pop()
            
        elif x[0] == "reverse":
            arr.reverse() 
        