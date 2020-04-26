import time
# This gives us a timestamp


def send_emails():
    for i in range(10000):
        pass


# start the timer
start = time.time()
# execute code
send_emails()
# end the timer
end = time.time()
duration = end - start
print(duration)
