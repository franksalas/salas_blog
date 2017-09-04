---
title: "Codeblocks"
date: 2017-09-03T17:43:15Z
draft: true
---

# Codeblocks

#JS test
<iframe width="400" height="400" frameborder="0" scrolling="no" src="//plot.ly/~samsung.staines/21.embed"></iframe>



## viz

```viz-dot
digraph g { a -> b; }
```


```viz-dot
digraph G {

	subgraph cluster_0 {
		style=filled;
		color=lightgrey;
		node [style=filled,color=white];
		a0 -> a1 -> a2 -> a3;
		label = "process #1";
	}

	subgraph cluster_1 {
		node [style=filled];
		b0 -> b1 -> b2 -> b3;
		label = "process #2";
		color=blue
	}
	start -> a0;
	start -> b0;
	a1 -> b3;
	b2 -> a3;
	a3 -> a0;
	a3 -> end;
	b3 -> end;

	start [shape=Mdiamond];
	end [shape=Msquare];
}

```

```viz-dot
graph G {
  e
  subgraph clusterA {
    a -- b;
    subgraph clusterC {
      C -- D;
    }
  }
  subgraph clusterB {
    d -- f
  }
  d -- D
  e -- clusterB
  clusterC -- clusterB
}
```

```viz-dot
digraph TrafficLights {
node [shape=box];  gy2; yr2; rg2; gy1; yr1; rg1;
node [shape=circle,fixedsize=true,width=0.9];  green2; yellow2; red2; safe2; safe1; green1; yellow1; red1;
gy2->yellow2;
rg2->green2;
yr2->safe1;
yr2->red2;
safe2->rg2;
green2->gy2;
yellow2->yr2;
red2->rg2;
gy1->yellow1;
rg1->green1;
yr1->safe2;
yr1->red1;
safe1->rg1;
green1->gy1;
yellow1->yr1;
red1->rg1;

overlap=false
label="PetriNet Model TrafficLights\nExtracted from ConceptBase and layed out by Graphviz"
fontsize=12;
}

```


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




