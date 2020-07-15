import requests

a = list(input().split('\n'))
count = 0
for elem in a:
    r = requests.get('https://' + str(elem))
    if r.status_code != 200:
        print(elem)
        count += 1
print('Failed:', count)