# same as loops
# when a function calls itself repeatedlly 

def show(n):
    if(n == 0): # base case
        return
    print(n)
    show(n-1)

show(5)