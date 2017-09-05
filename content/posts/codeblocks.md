---
title: "Codeblocks"
date: 2017-09-03T17:43:15Z
draft: true  
---

# Codeblocks


<iframe width="700" height="400" frameborder="0" scrolling="yes" src="//plot.ly/~samsung.staines/21.embed"></iframe>



## viz

```viz-dot
digraph g { a -> b; }
```

{{< highlight html >}}
<section id="main">
  <div>
   <h1 id="title">{{ .Title }}</h1>
    {{ range .Data.Pages }}
        {{ .Render "summary"}}
    {{ end }}
  </div>
</section>
{{< /highlight >}}



### html

```html
<section id="main">
  <div>
   <h1 id="title">{{ .Title }}</h1>
    {{ range .Data.Pages }}
        {{ .Render "summary"}}
    {{ end }}
  </div>
</section>
```

### python

```python
def my_func(name):
    out = "Hello {}".format(name)
    return out
```

## other stuff

### mathjax

$e=mc^2$




