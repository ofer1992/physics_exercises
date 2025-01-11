---
description: Analyze J.J. Thomson's electron charge-to-mass ratio experiment
topics:
  - magnetostatics
  - electron properties
  - historical experiments
difficulty: hard
status: solved
interested: false
book: Introduction to Electrodynamics
chapter: 5 Magnetostatics
---

## Problem Statement
In 1897, J. J. Thomson "discovered" the electron by measuring the charge-to-mass ratio of "cathode rays" (actually, streams of electrons, with charge $q$ and mass $m$) as follows:

a. First he passed the beam through uniform crossed electric and magnetic fields $E$ and $B$ (mutually perpendicular, and both of them perpendicular to the beam), and adjusted the electric field until he got zero deflection. What, then, was the speed of the particles (in terms of $E$ and $B$)?

b. Then he turned off the electric field, and measured the radius of curvature, $R$, of the beam, as deflected by the magnetic field alone. In terms of $E$, $B$, and $R$, what is the charge-to-mass ratio $(q/m)$ of the particles?

## Solution 
(a) $$qE = qvB \implies v = \frac{E}{B}$$

(b) $$F_B = q\vec{v}\times\vec{B}$$

Since $\vec{v}$ under the radial magnetic force is always $\perp$ to $\vec{B}$ and $F_B$ is always radial $|F_B|$ is constant, hence the particle's trajectory is part of UCM.

UCM formulas
$$\begin{align*}
\vec{r} &= R\hat{r}(\omega t) \\
\vec{v} &= R\omega\hat{\theta}(\omega r) \\
\vec{a} &= -R\omega^2\hat{r}(\omega t) \\
v &= R\omega \\
\omega^2 &= \frac{v^2}{R^2}
\end{align*}$$

$$mR\omega^2 = F_B = qvB$$

$$\frac{q}{m} = \frac{R\omega^2}{vB} = \frac{Rv^2}{R^2B} = \frac{v}{RB} = \frac{E}{RB^2}$$