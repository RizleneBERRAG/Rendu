def fib(limit, cur=0, prev=1):
    if cur > limit :
        return
    print(cur)
    fib(limit, cur + prev, cur)
    

fib(5000)    