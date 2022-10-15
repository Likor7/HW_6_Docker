import os

hostname = "api.github.com"
response = os.system("ping -c 1 " + hostname)

while True:
    if response == 0:
        print(hostname, 'is up!')
    else:
        print(hostname, 'is down!')
