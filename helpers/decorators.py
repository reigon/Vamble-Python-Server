from functools import wraps
import time
import helpers.constants as constants

def AsyncWrapper(func):
    @wraps(func)
    async def withAsyncWrapper(*args, **kwargs):
        return await func(*args, **kwargs)
    return withAsyncWrapper
        
        
def PerformaceTester(func): 
    @wraps(func)    
    def withPerformaceTest(*args, **kwargs):
        start = time.time()
        returnedValue = func(*args, **kwargs)
        print("Calling function " + func.__name__ + " took: " + str(time.time() - start) + " seconds")
        return returnedValue
    
    return withPerformaceTest

def AsyncErrorHandler(func):
    @wraps(func)
    async def withErrorHandling(*args, **kwargs): 
        errorCount = 0 
        while errorCount < constants.ERROR_LIMIT:
            try:
                returnedValue = await func(*args, **kwargs)
                return returnedValue
            except Exception as e:
                print("Error is: " + str(e))
                errorCount = errorCount + 1
        return 
    return withErrorHandling

    