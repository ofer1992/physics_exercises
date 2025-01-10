---
description: "Complete proof of vector potential theorem and analyze examples"
topics: ["magnetostatics", "vector potential", "mathematical theorems"]
difficulty: "hard"
status: "unsolved"
interested: false
book: "Introduction to Electrodynamics"
chapter: "5 Magnetostatics"
---

## Problem Statement
a. Complete the proof of Theorem 2, Sect. 1.6.2. That is, show that any divergenceless vector field $F$ can be written as the curl of a vector potential $A$. What you have to do is find $A_x$, $A_y$, and $A_z$ such that:
   (i) $\partial A_z/\partial y - \partial A_y/\partial z = F_x$
   (ii) $\partial A_x/\partial z - \partial A_z/\partial x = F_y$
   (iii) $\partial A_y/\partial x - \partial A_x/\partial y = F_z$
Here's one way to do it: Pick $A_x = 0$, and solve (ii) and (iii) for $A_y$ and $A_z$. Note that the "constants of integration" are themselves functions of y and z—they're constant only with respect to x. Now plug these expressions into (i), and use the fact that $\nabla \cdot F = 0$ to obtain

$$A_y = \int_0^x F_z(x', y, z) dx'$$
$$A_z = \int_0^y F_x(0, y', z) dy' - \int_0^x F_y(x', y, z) dx'$$

b. By direct differentiation, check that the $A$ you obtained in part (a) satisfies $\nabla \times A = F$. Is $A$ divergenceless?

c. As an example, let $F = y\hat{x} + z\hat{y} + x\hat{z}$. Calculate $A$, and confirm that $\nabla \times A = F$.