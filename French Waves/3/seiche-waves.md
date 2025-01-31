---
description: "Analysis of seiche waves in a rectangular lake using energy conservation"
topics:
  - fluid dynamics
  - wave motion
  - energy conservation
  - continuity equation
difficulty: hard
status: unsolved
interested: false
book: "A.P. French - Vibrations and Waves"
chapter: "The Free Vibrations of Physical Systems"
---

## Problem Statement
This problem is much more ambitious than the usual problems, in the sense that it requires putting together a greater number of parts. But if you tackle the various parts as suggested, you should find that they are not, individually, especially difficult, and the problem as a whole exemplifies the power of the energy-conservation method for analyzing oscillation problems.

![Rectangular lake showing tilted water surface with velocity v and displacement y]

You are no doubt familiar with the phenomenon of water sloshing about in the bathtub. The simplest motion is, to some approximation, one in which the water surface just tilts as shown but seems to remain more or less flat. A similar phenomenon occurs in lakes and is called a seiche (pronounced: saysh). Imagine a lake of rectangular cross section, as shown, of length $L$ and with water depth $h$ ($\ll L$). The problem resembles that of the simple pendulum, in that the kinetic energy is almost entirely due to horizontal flow of the water, whereas the potential energy depends on the very small change of vertical level. Here is a program for calculating, approximately, the period of the oscillations:

(a) Imagine that at some instant the water level at the extreme ends is at $\pm y_0$ with respect to the normal level. Show that the increased gravitational potential energy of the whole mass of water is given by
$$U = \frac{1}{6}\rho g L y_0^2$$
where $b$ is the width of the lake. You get this result by finding the increased potential energy of a slice a distance $x$ from the center and integrating.

(b) Assuming that the water flow is predominantly horizontal, its speed $v$ must vary with $x$, being greatest at $x = 0$ and zero at $x = \pm L/2$. Because water is incompressible (more or less) we can relate the difference of flow velocities at $x$ and $x + dx$ to the rate of change $dy/dt$ of the height of the water surface at $x$. This is a continuity condition. Water flows in at $x$ at the rate $vhb$ and flows out at $x + dx$ at the rate $(v + dv)hb$. (We are assuming $y_0 \ll h$.) The difference must be equal to $(b\,dx)(dy/dt)$, which represents the rate of increase of the volume of water contained between $x$ and $x + dx$. Using this condition, show that
$$v(x) = v(0) - \frac{1}{hL}x^2\frac{dy_0}{dt}$$
where
$$v(0) = \frac{L}{4h}\frac{dy_0}{dt}$$

(c) Hence show that at any given instant, the total kinetic energy associated with horizontal motion of the water is given by
$$K = \frac{1}{60}\frac{bpL^3}{h}\left(\frac{dy_0}{dt}\right)^2$$
To get this result, one must take the kinetic energy of the slice of water lying between $x$ and $x + dx$ (with volume equal to $bh\,dx$), which moves with speed $v(x)$, and integrate between the limits $x = \pm L/2$.

(d) Now put
$$K + U = \text{const.}$$
This is an equation of the form
$$A\left(\frac{dy_0}{dt}\right)^2 + By_0^2 = \text{const.}$$
and defines SHM of a certain period. You will find that this period depends only on the length $L$, the depth $h$, and $g$. [Note: This theory is not really correct. The water surface is actually a piece of a sine wave, not a plane surface. But our formula is correct to better than 1%. (The true answer is $T = 2L/\sqrt{gh}$.)]

(e) The Lake of Geneva can be approximated as a rectangular tank of water of length about 70 km and of mean depth about 150 m. The period of its seiche has been observed to be about 73 min. Compare this with your formula.