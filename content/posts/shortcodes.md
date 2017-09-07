---
title: "Shortcodes"
date: 2017-09-03T16:54:46Z
tags : [ "shortcodes", "hugo"]
draft: true
---

# Hugo's built in shortcodes 
## figure

{{< figure src="/img/sup-globe/dogo.jpg" title="Doggo" >}}


## gist

{{< gist spf13 7896402 "img.html" >}}


## highlight

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


## tweet

{{< tweet 877500564405444608 >}}


# vimeo

{{< vimeo 146022717 >}}


## youtube

{{< youtube w7Ft2ymGmfc >}}

## higlights


{{< highlight python >}}
print("helllo world")
{{< /highlight >}}


# Addons

## expand

{{%expand%}}Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
proident, sunt in culpa qui officia deserunt mollit anim id est laborum.{{% /expand%}}



## mermaid

### Example 1
{{<mermaid align="left">}}

graph LR;
    A[Hard edge] -->|Link text| B(Round edge)
    B --> C{Decision}
    C -->|One| D[Result one]
    C -->|Two| E[Result two]
{{< /mermaid >}}


### Example 2
{{<mermaid>}}
sequenceDiagram
    participant Alice
    participant Bob
    Alice->>John: Hello John, how are you?
    loop Healthcheck
        John->John: Fight against hypochondria
    end
    Note right of John: Rational thoughts <br/>prevail...
    John-->Alice: Great!
    John->Bob: How about you?
    Bob-->John: Jolly good!
{{< /mermaid >}}

### Example 3
{{<mermaid>}}
gantt
        dateFormat  YYYY-MM-DD
        title Adding GANTT diagram functionality to mermaid
        section A section
        Completed task            :done,    des1, 2014-01-06,2014-01-08
        Active task               :active,  des2, 2014-01-09, 3d
        Future task               :         des3, after des2, 5d
        Future task2               :         des4, after des3, 5d
        section Critical tasks
        Completed task in the critical line :crit, done, 2014-01-06,24h
        Implement parser and jison          :crit, done, after des1, 2d
        Create tests for parser             :crit, active, 3d
        Future task in critical line        :crit, 5d
        Create tests for renderer           :2d
        Add to mermaid                      :1d
{{< /mermaid >}}


## notice

{{% notice note    %}}
This is a note.
{{% /notice %}} 

{{% notice  warning   %}}
this is a warning.
{{% /notice %}}

{{% notice   info  %}}
this is an info.
{{% /notice %}}

{{% notice    tip %}}
this is a tip.
{{% /notice %}} 


## icon
 <i class="fab fa-github fa-10x"></i>
### Web Application Icons

- {{< icon fa-address-book >}} fa-address-book
- {{< icon fa-address-book-o >}} fa-address-book-o
- {{< icon fa-address-card >}} fa-address-card
- {{< icon fa-address-card-o >}} fa-address-card-o
- {{< icon fa-adjust >}} fa-adjust
- {{< icon fa-american-sign-language-interpreting >}} fa-american-sign-language-interpreting
- {{< icon fa-anchor >}} fa-anchor
- {{< icon fa-archive >}} fa-archive
- {{< icon fa-area-chart >}} fa-area-chart
- {{< icon fa-arrows >}} fa-arrows
- {{< icon fa-arrows-h >}} fa-arrows-h
- {{< icon fa-arrows-v >}} fa-arrows-v
- {{< icon fa-asl-interpreting >}} fa-asl-interpreting (alias)
- {{< icon fa-assistive-listening-systems >}} fa-assistive-listening-systems



