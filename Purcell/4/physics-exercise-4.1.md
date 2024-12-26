---
description: Calculate current in Van de Graaff generator from belt parameters
topics:
  - electrostatics
  - current
difficulty: easy
status: solved
interested: false
book: Electricity and Magnetism
chapter: Electric currents
---

## Problem Statement
In a Van de Graaff electrostatic generator, a rubberized belt 0.3 m wide travels at a velocity of 20 m/s. The belt is given a surface charge at the lower roller, the surface charge density being high enough to cause a field of $10^6$ V/m on each side of the belt. What is the current in milliamps?

## Solution

Given:
- $w = 0.3\text{ m}$
- $v = 20\text{ m/s}$
- $E = 10^6\text{ V/m}$

Regarding units
- $V = \frac{N}{c}\cdot m$
- $\frac{V}{m} = \frac{N}{c}$ which is field units

Tasks:
- Figure out the charge density σ
- Calculate $\sigma\cdot w\cdot v = I$

From symmetry, at least if the field doesn't depend on the currents, then it should be horizontal near the middle, and from Gauss with a box:

$$2whE = \int_S E\cdot da = \frac{1}{\epsilon_0}\int_V dq = 2\sigma wh$$

$$\sigma = \epsilon_0E = \epsilon_0\cdot 10^6\frac{V}{m} = 10^{-2}\frac{C}{m^2}$$

where:
$\epsilon_0 = \frac{1}{4\pi K} = \frac{1}{4\pi\cdot 9\cdot 10^9} = \frac{1}{10^{12}}10^{-9}$

Current calculation:
$$
\begin{align*}
I &= \frac{4}{9}\pi\cdot 10^{-3}\cdot 0.3\cdot 20 \\
&= \frac{4}{15}\pi\cdot 10^{-2}\text{ A} \\
&= \frac{4}{15}\pi\cdot 10\text{ mA} \\
&= \frac{8}{3}\pi\text{ mA}
\end{align*}
$$

where $\text{mA} = 10^{-3}\text{ A}$

Mistakes according to solution noted:
- $k = \frac{1}{4\pi\epsilon_0}$, not $\frac{4\pi}{\epsilon_0}$. Consider switching to numerical eventually.
- says $E = \frac{\sigma}{2\epsilon_0}?$ but why?