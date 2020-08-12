def factorial(n):
    if n > -1:
        if n == 0 :
            return 1
        else:
            return n * factorial(n-1)
    else:
        return "Negative"
        
tests = [-2,-1,0,1,2,3,4]
for test in tests:
    print(f"{test}: {factorial(test)}"
