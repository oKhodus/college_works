def cache_results(func):
    """ Decorator that caches result of a function to avoid unnecessary calculation

    - Uses a dictionary to store previously computed results.
    - Prints "Cache hit for {args}: returning cached result" if the result is already stored.
    - Prints "Calculating result for {args}" if the function is executed.
    - Returns the cached result when available, otherwise, it computes and stores the new result.

    Args:
        func (function): Function which will be wrapped and cached

    Returns:
        function: Wrapper function that checks the cache before calling original function
    """
    store = {}

    def wrapper(*args):
        """Checks if result for given arguments is already cached - 
        if yes -> returns cached result
        else -> calls the original function and caches result
        
        Args:
            *args: arguments which gived to the decorated function

        Returns:
            Cached result of decorated function, else calls original function and caches result 
        """
        n = args[0]
        if n in store:
            print(f"\nCache hit for {n}: returning cached result")
            return store[n]
        else:
            print(f"Calculating result for {n}")
            res = func(*args)
            store[n] = res
            return res
    return wrapper

@cache_results
def fibo(n):
    """ Recursive function that calculate the n'th fibonacci number 

    Args:
        n (int): pos of the fibonacci number to calculate

    Returns:
        int: n'th fibonacci number
    """
    if n <= 1:
        return n
    return fibo(n-1) + fibo(n-2)

users_num = int(input("Enter a number: "))

print(fibo(users_num))

for num in range(users_num +1):
    print(fibo(num))
