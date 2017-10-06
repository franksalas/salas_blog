---
title: "Basic Tutorial Template"
date: 2017-09-06
tags : [ ]
draft: true
---


# Basic tutorial template
loren5  Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi. Nulla quis sem at nibh elementum imperdiet. Duis sagittis ipsum. Praesent mauris. Fusce nec tellus sed augue semper porta. Mauris massa. Vestibulum lacinia arcu eget nulla. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Curabitur sodales ligula in libero. 

```python
# Function definition is here
def printme( str ):
   "This prints a passed string into this function"
   print str
   return
```

Sed dignissim lacinia nunc. Curabitur tortor. Pellentesque nibh. Aenean quam. In scelerisque sem at dolor. Maecenas mattis. Sed convallis tristique sem. Proin ut ligula vel nunc egestas porttitor. Morbi lectus risus, iaculis vel, suscipit quis, luctus non, massa. Fusce ac turpis quis ligula lacinia aliquet. Mauris ipsum. 

```html
Sed dignissim lacinia nunc. Curabitur tortor. Pellentesque nibh. Aenean quam. In
<------------------this is 80 characters line --------------------------------->1234567
```
Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, nibh. Quisque volutpat condimentum velit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nam nec ante. Sed lacinia, urna non tincidunt mattis, tortor neque adipiscing diam, a cursus ipsum ante quis turpis. Nulla facilisi. Ut fringilla. Suspendisse potenti. Nunc feugiat mi a tellus consequat imperdiet. Vestibulum sapien. Proin quam. Etiam ultrices. Suspendisse in justo eu magna luctus suscipit. 

Sed lectus. Integer euismod lacus luctus magna. Quisque cursus, metus vitae pharetra auctor, sem massa mattis sem, at interdum magna augue eget diam. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Morbi lacinia molestie dui. Praesent blandit dolor. Sed non quam. In vel mi sit amet augue congue elementum. Morbi in ipsum sit amet pede facilisis laoreet. Donec lacus nunc, viverra nec, blandit vel, egestas et, augue. Vestibulum tincidunt malesuada tellus. Ut ultrices ultrices enim. Curabitur sit amet mauris. Morbi in dui quis est pulvinar ullamcorper. Nulla facilisi. 

Integer lacinia sollicitudin massa. Cras metus. Sed aliquet risus a tortor. Integer id quam. Morbi mi. Quisque nisl felis, venenatis tristique, dignissim in, ultrices sit amet, augue. Proin sodales libero eget ante. Nulla quam. Aenean laoreet. Vestibulum nisi lectus, commodo ac, facilisis ac, ultricies eu, pede. Ut orci risus, accumsan porttitor, cursus quis, aliquet eget, justo. Sed pretium blandit orci. 

### Code

```python
def make_entry(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    f_create = "content/posts/{}.md".format(slug)
    # directory = "content/images/{}-{:0>2}-{:0>2}-{}".format(
    # today.year, today.month, today.day, slug)
    t = TEMPLATE.strip().format(title=title.title(),
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
```

{{<highlight python>}}
def make_entry(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    f_create = "content/posts/{}.md".format(slug)
    # directory = "content/images/{}-{:0>2}-{:0>2}-{}".format(
    # today.year, today.month, today.day, slug)
    t = TEMPLATE.strip().format(title=title.title(),
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
{{</highlight>}}



<!-- 1.Write an overview// -->

<!-- 2. Describe your intended audience //-->



<!-- 3. State the Purpose //-->

<!-- 4. List any Preriquisites //-->


<!-- 5. Describe the steps of your how-to //-->


<!-- 6. Extend the learning //-->

<!-- 7. Summarize the Entire Process //-->

<!-- 8. Reference //-->


