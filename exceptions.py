import time

try:
    for i in range(5):
        print('hej')
        time.sleep(1)
except KeyboardInterrupt:
    print('hej då!')
else:
    print('hej då! - Inga exceptions kastade')
