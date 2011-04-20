from collections import deque
import re
from time import sleep
from urllib2 import urlopen


def follow_the_chain(base_url, nothing):
    urlq = deque([nothing])
    nothings = []

    for _ in range(400):
        if not urlq:
            break

        next_nothing = urlq.popleft()
        next_url = ''.join([base_url, next_nothing])

        print "requesting({0})".format(next_url)

        response = urlopen(next_url)

        if not response:
            print "No response"
            continue

        text = response.read()
        match = re.search(r'next nothing is (\d+)', text)

        if not match:
            match = re.search(r'[Dd]ivide by two', text)
            if match:
                nothing = str(int(next_nothing) / 2)
            else:
                print "No match"
                print text
                continue
        else:
            nothing = match.group(1)

        nothings.append(nothing)
        urlq.append(nothing)

        sleep(0.5)

    return urlq, nothings


if __name__ == '__main__':
    base_url = ("http://www.pythonchallenge.com/pc/def/linkedlist.php"
                "?nothing=")
    follow_the_chain(base_url, "12345")
