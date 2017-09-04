'''
---
title: "My First Post"
date: 2017-09-01T02:21:14-05:00
draft: true
---
'''


import sys
import os
from datetime import datetime

today = datetime.today()

TEMPLATE = """
---
title: {title}
date: {year}-{month}-{day}
draft: True
---





![][img1]
![][img2]
![][img3]

[img1]: /img/{slug}/
[img2]: /img/{slug}/
[img3]: /img/{slug}/
"""


def make_entry(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    f_create = "content/posts/{}.md".format(slug)
    # directory = "content/images/{}-{:0>2}-{:0>2}-{}".format(
    # today.year, today.month, today.day, slug)
    t = TEMPLATE.strip().format(title=title,
                                year=today.year,
                                #month=today.month,
                                month = '{:02d}'.format(today.month),
                                day = '{:02d}'.format(today.day),
                                #day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    with open(f_create, 'w') as w:
        w.write(t)
    print("File created -> " + f_create)


if __name__ == '__main__':

    if len(sys.argv) > 1:
        title = sys.argv[1]
        make_entry(title)  # create File
        slug = title.lower().strip().replace(' ', '-')
        directory = 'static/img/{}'.format(slug)

        os.makedirs(directory)
        print(directory)
        # os.mkdir( directory, 0777 );
        # if not os.path.exists(directory):
        #     os.makedirs(directory)
    else:
        print("No title given")        