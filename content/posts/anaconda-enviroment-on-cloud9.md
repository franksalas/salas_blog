---
title: "Anaconda Enviroment On Cloud9"
date: 2017-09-05
tags : ["python", "anaconda","c9" ]
draft: false
---

{{% notice note   %}}
open clould 9
download miniconda for linux
install on cloud 9
profit ?
{{% /notice %}}



- open cloud9
-


## installations
- go to https://conda.io/miniconda.html
- right click on python 3.6 linxu 64-bit (bash installer) and `copy link address`
- get on the terminal and type `wget -c ` and paste the link from before

```$

uhdfrank:~/workspace $ wget -c https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

Your workspace should look like this

```$

uhdfrank:~/workspace $ ls
Miniconda3-latest-Linux-x86_64.sh  README.md
```

now we need to make the file executable


```bash

uhdfrank:~/workspace $ chmod +x Miniconda3-latest-Linux-x86_64.sh 
uhdfrank:~/workspace $ ls
Miniconda3-latest-Linux-x86_64.sh*  README.md
uhdfrank:~/workspace $ 
```


lets execute it 

```#
uhdfrank:~/workspace $ ./Miniconda3-latest-Linux-x86_64.sh

Welcome to Miniconda3 4.3.21 (by Continuum Analytics, Inc.)

In order to continue the installation process, please review the license
agreement.
Please, press ENTER to continue
>>> 
```
keep clicking untill it ask you to say  yes or no

- press enter to confir installation on /home/ubuntu/miniconda3



```$
Do you wish the installer to prepend the Miniconda3 install location
to PATH in your /home/ubuntu/.bashrc ? [yes|no]
[no] >>>  yes

```


restart terminal and type python

```$
uhdfrank:~/workspace $ python
Python 3.6.1 |Continuum Analytics, Inc.| (default, May 11 2017, 13:09:58) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 

```


![][img1]
![][img2]
![][img3]

[img1]: /img/anaconda-enviroment-on-cloud9/
[img2]: /img/anaconda-enviroment-on-cloud9/
[img3]: /img/anaconda-enviroment-on-cloud9/√