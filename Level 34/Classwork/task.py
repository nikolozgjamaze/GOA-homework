def multiply(n1=0, n2=0):
    result = n1 * n2
    
    print(result)
    return  result













def greet(name):
    return "Hello", name
greeting, person = greet("Giorgi")


    

def sum_upto(n=10):
    total = 0
    for i in range(1, n + 1):
        total += i
        print(f"Sum up to {i}: {total}")







def check_length(s):
    if len(s) > 10:
        return s
    else:
        return "Too short"

