---
title: python test
date: 2002-09-01
draft: True
---


# image show
### first image
![][img1]

### image two
![][img2]

## shortcodes

{{% notice note %}}
A notice disclaimer
{{% /notice %}}


### info

{{% notice info %}}
An information disclaimer
{{% /notice %}}


### tip

{{% notice tip %}}
A tip disclaimer
{{% /notice %}}

### warning
{{% notice warning %}}
An warning disclaimer
{{% /notice %}}


## mermaid

{{<mermaid align="left">}}
graph LR;
    A[Hard edge] -->|Link text| B(Round edge)
    B --> C{Decision}
    C -->|One| D[Result one]
    C -->|Two| E[Result two]
{{< /mermaid >}}



[img1]: /img/python-test/image1.jpg
[img2]: /img/python-test/giphy.gif