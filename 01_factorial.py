import logging
import time 

logging.basicConfig(filename="./log/01.log", level=logging.DEBUG)
logger = logging.getLogger()

def factorial_recursive(n):
    if n > -1:
        if n == 0 :
            return 1
        else:
            return n * factorial_recursive(n-1)
    else:
        return "Negative"
        

def factorial_iterate(n):
    input_val = n
    tot = 1
    while n >= 1:
        tot = n * tot
        n -= 1
    logger.info(f"iterator: {input_val}: {tot}")



tests = range(70)

start_time = time.time()
for test in tests:
    logger.info(f"recursive: {test}: {factorial_recursive(test)}")
end_time = time.time()
print(f"recursive use time {end_time-start_time}")

print("*"*10)
start_time = time.time()
for test in tests:
    factorial_iterate(test)
end_time = time.time()
print(f"iteration use time {end_time-start_time}")
