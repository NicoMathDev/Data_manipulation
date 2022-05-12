# Returns the Fibonacci sequence number for the desired index
def fb_order(indice): 
    if indice <= 0:
        return print('Insira um valor inteiro positivo diferente de zero')
    before = 0
    after = 0
    for i in range(0, indice):
        after = after + before
        before = after - before
        if after == 0:
            after = after + 1

    return after    
    
result = fb_order(13)
print(result)


# Return to list with Fibbonaci sequence until index
def fb_matriz(index):
    if index <= 0:
        return print('Insira um valor inteiro positivo diferente de zero')
    fib = []
    before = 0
    after = 0
    for i in range(0, index):
        after += before
        before = after - before
        if after == 0:
            after =+ 1
        fib.append(after)

    return fib

result = fb_matriz(10)
print(result)
