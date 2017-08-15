         
def _primality(num):
    """check is the number is prime and return True"""

    mylist = list(range(1, num + 1))
    newlist = []
    for i in mylist:
        if num % i == 0:
            newlist.append(i)
    if len(newlist) == 2:
        return True
    else:
        return False    

def gen_prime(n):
    """
    Test if prime then add to a list   
    
    """
    prime_list = []
    my_list = list(range(1,n+1))
    for i in my_list:
        if _primality(i) == True:
            prime_list.append(i)
    return prime_list                

print(_primality(7))
print(gen_prime(7))    

