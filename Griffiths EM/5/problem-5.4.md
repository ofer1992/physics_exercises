---
description: Find magnetic field for a square loop with uniform current
topics:
  - magnetostatics
  - Biot-Savart law
  - current loops
difficulty: medium
status: solved
interested: false
book: Introduction to Electrodynamics
chapter: 5 Magnetostatics
---

## Problem Statement
Suppose that the magnetic field in some region has the form $$B = kz\hat{x}$$ (where $k$ is a constant). Find the force on a square loop (side $a$), lying in the yz plane and centered at the origin, if it carries a current $I$, flowing counterclockwise, when you look down the x axis.

## Solution

$\vec{B} = kz\hat{x}$

Force felt by a line segment is:

$I\int d\vec{l} \times \vec{B}$

How do I know that?

$d\vec{q}\vec{v} \times \vec{B}$
$\lambda dl\vec{v} \times \vec{B}$
$\lambda v\int dt \times \vec{B}$
$I = \lambda v$

We have four different segments, and at all times $\vec{B} \perp d\vec{l}$.

Upper = $I\int d\vec{l} \times \vec{B}$
$$\begin{align*}
&= I\int(dl\hat{y})(k\frac{a}{2}\hat{x}) \\
&= Ik\frac{a}{2}\int-dl\hat{z} \\
&= -Ika\frac{a}{2}\hat{z}
\end{align*}$$

Lower is the same since both $\vec{B}$ and $d\vec{l}$ flip.

Left = $I\int d\vec{l} \times \vec{B} = I\int dl\hat{z} \times kz\hat{x}$

$$\begin{align*}
&= Ik\int dz\hat{z} \times kz\hat{x} \\
&= Ik\int_{-a/2}^{a/2} dz\cdot z\hat{y} \\
&= Ik[\frac{z^2}{2}]_{-a/2}^{a/2}\hat{y} = 0
\end{align*}$$

Right is similar, just $dl = -dl\hat{z}$, so also contributes 0.

In total, the force is $-Ika^2\hat{z}$