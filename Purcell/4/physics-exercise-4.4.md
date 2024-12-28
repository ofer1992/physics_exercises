---
description: Calculate resistance between concentric spherical shells
topics:
  - resistivity
  - spherical symmetry
  - dimensional analysis
difficulty: medium
status: solved
interested: false
book: Electricity and Magnetism
chapter: Electric currents
---

## Problem Statement
(a) The region between two concentric spherical shells is filled with a material with resistivity ρ. The inner radius is $r_1$, and the outer radius $r_2$ is many times larger (essentially infinite). Show that the resistance between the shells is essentially equal to $\rho/4\pi r_1$.

(b) Without doing any calculations, dimensional analysis suggests that the above resistance should be proportional to $\rho/r_1$, because ρ has units of ohm-meters and $r_1$ has units of meters. But is this reasoning rigorous?

## Solution

(a) We use the same process used in the book for resistance in rod. We can consider the larger sphere as one terminal and the inner one as another.

For a sphere we can relate the field at the point to the potential at a point by $V=E\frac{r^2}{r_1}$.

The current in this scenario is the flux of the density through an enclosing surface which we might take to be a sphere at radius r $I=JA(S_r)=\sigma EA(S_r)$

Then $R=V/I=E\frac{r^2}{r_1}/\sigma EA(S_r)=\frac{\rho}{4\pi r_1}$.

(b) I would say no, since it could also depend on $r_2$ and then we could have area divided by distance etc.

## Notes
so answers are not wrong, but could be better.

In (a), the solution uses the differential resistance through a shell
$$dR=\frac{\rho dr}{4 \pi r^2}$$
and then integrates that from $r_1$ to $r_2$. Actually there is some error in my reasoning because $r_2$ only disappears when it goes to infinity. Perhaps because V is the voltage, ie potential difference from outer to inner sphere, so theres another term there.