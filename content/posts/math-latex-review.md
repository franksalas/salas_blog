---
title: Math latex review
date: 2017-09-01
draft: True
---

# Math latext

## Greek letters
```markdown
\alpha, \Alpha, \beta, \Beta, \gamma, \Gamma, \pi, \Pi, \phi, \varphi, \mu, \Phi
```

$$
\alpha, \Alpha, \beta, \Beta, \gamma, \Gamma, \pi, \Pi, \phi, \varphi, \mu, \Phi
$$

## Operators
```md
$\cos (2\theta) = \cos^2 \theta - \sin^2 \theta$
```
$\cos (2\theta) = \cos^2 \theta - \sin^2 \theta$

```md
$\lim_{x \to \infty} \exp(-x) = 0$
```

$\lim_{x \to \infty} \exp(-x) = 0$

For the modular operator there are two commands `\bmod` and `\pmod`:
```md
$a \bmod b$
```
$a \bmod b$

```md
$x \equiv a \pmod{b}$
```

$x \equiv a \pmod{b}$

## Powers and indices

```md
$k_{n+1} = n^2 + k_n^2 - k_{n-1}$
```

$k_{n+1}= n^2 + k^{2}_n -k_{n+1}$


```md
$n^{22}$
```

$n^{22}$

An underscore (_) can be used with a vertical bar ( {\displaystyle |} |) to denote evaluation using subscript notation in mathematics:



```md
$f(n) = n^5 + 4n^2 + 2 |_{n=17}$
```
$f(n) = n^5 + 4n^2 + 2 |_{n=17}$



## fractions and binomials


```md
$\frac{n!}{k!(n-k)!} = \binom{n}{k}$
```

$\frac{n!}{k!(n-k)!} = \binom{n}{k}$

```md
$\frac{\frac{1}{x}+\frac{1}{y}}{y-z}$
```


$\frac{\frac{1}{x}+\frac{1}{y}}{y-z}$

```md
$^3/_7$

```

$^3/_7$


```md
$x^\frac{1}{2}$ % no error
```

$x^\frac{1}{2}$

## Continued fracton
```md
$$
\begin{equation}
  x = a_0 + \cfrac{12356616316}{a_3 
          + \cfrac{16565}{a_3 
          + \cfrac{165465465}{a_9 + \cfrac{1131321}{a_7} } } }
\end{equation}
$$
```


$$
\begin{equation}
  x = a_0 + \cfrac{12356616316}{a_3 
          + \cfrac{16565}{a_3 
          + \cfrac{165465465}{a_9 + \cfrac{1131321}{a_7} } } }
\end{equation}
$$


## multifplication of two numbers
```md

$$
\begin{equation}
\frac{
    \begin{array}[b]{r}
      \left( x_1 x_2 \right)\\
      \times \left( x'_1 x'_2 \right)
    \end{array}
  }{
    \left( y_1y_2y_3y_4 \right)
  }
\end{equation}
$$
```

## Root
```md
$\sqrt{\frac{a}{b}}$
```

$\sqrt{\frac{a}{b}}$


$$
\begin{equation}
\frac{
    \begin{array}[b]{r}
      \left( x_1 x_2 \right)\\
      \times \left( x'_1 x'_2 \right)
    \end{array}
  }{
    \left( y_1y_2y_3y_4 \right)
  }
\end{equation}
$$



## sum and integrals
```md
$\sum_{i=1}^{10} t_i$
```

$\sum_{i=1}^{10} t_i$

or..

```md
$\displaystyle\sum_{i=1}^{10} t_i$
```

$\displaystyle\sum_{i=1}^{10} t_i$


```md
$\int_0^\infty \mathrm{e}^{-x}\,\mathrm{d}x$
```

$\int_0^\infty \mathrm{e}^{-x}\,\mathrm{d}x$

---


|  	|  	|  	|  	|  	|  	|
|---	|---	|---	|---	|---	|---	|
|`\sum`  	|$\sum$  	|`\prod`  	| $\prod$ 	|`\coprod`  	|$\coprod$  	|
| `\bigoplus` 	|$\bigoplus$  	| `\bigotimes` 	| $\bigotimes$ 	|`\bigdot`  	| $\bigodot$ 	|
| `\bigcup` 	|$\bigcup$  	| `\bigcap` 	| $\bigcap$ 	|`\biguplus`  	| $\biguplus$ 	|
| `\bigsqcup` 	|$\bigsqcup$  	| `\bigvee` 	| $\bigvee$ 	|`\bigwedge`  	| $\bigwedge$ 	|
| `\int` 	|$\int$  	| `\oint` 	| $\oint$ 	|`\iint`  	| $\iint$ 	|
| `\iiint` 	|$\iiint$  	| `\iiiint` 	| $\iiiint$ 	|`\idotsint`  	| $\idotsint$ 	|

---
```md
$$
\sum_{\substack{
   0<i<m \\
   0<j<n
  }} 
 P(i,j)
$$
```

$$
\sum_{\substack{
   0<i<m \\
   0<j<n
  }} 
 P(i,j)
$$


If you want the limits of an integral to be specified above and below the symbol (like the sum), use the \limits command

```md
$\int\limits_a^b$
```

$\int\limits_a^b$

## Brackets, braces and delimeters
```md
$$
( a ), [ b ], \{ c \}, | d |, \| e \|,
\langle f \rangle, \lfloor g \rfloor,
\lceil h \rceil, \ulcorner i \urcorner
$$
```

$$
( a ), [ b ], \{ c \}, | d |, \| e \|,
\langle f \rangle, \lfloor g \rfloor,
\lceil h \rceil, \ulcorner i \urcorner
$$

## Automatic sizing

```md
$\left(\frac{x^2}{y^3}\right)$
```
$\left(\frac{x^2}{y^3}\right)$


```md
$P\left(A=2\middle|\frac{A^2}{B}>4\right)$
```

$P\left(A=2\middle|\frac{A^2}{B}>4\right)$


```md
$\left.\frac{x^3}{3}\right|_0^1$
```

$\left.\frac{x^3}{3}\right|_0^1$

### Manual sizing


```md
$( \big( \Big( \bigg( \Bigg($
```
$( \big( \Big( \bigg( \Bigg($


```md
$\frac{\mathrm d}{\mathrm d x} \left( k g(x) \right)$
```
$\frac{\mathrm d}{\mathrm d x} \left( k g(x) \right)$

```md
$x \in [-1,1]$

```
$x \in [-1,1]$

```md
$x \in {[-1,1]}$
```
$x \in {[-1,1]}$

```md
$x \in {[{-1},1]}$
```
$x \in {[{-1},1]}$

## MAtrices and arrays
Does not work yet with mathjax


## Accents


```md

```



```md

```


```md

```


```md

```


```md

```


```md

```