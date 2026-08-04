# Likelihood Ratio Test (Why Bother?)

Even though we already know the $z$ and $t$ tests...

------------------------------------------------------------------------

## Big Idea

$$
\Lambda(x)
=
\frac{\sup_{\theta \in \Theta_0} L(\theta)}
{\sup_{\theta \in \Theta} L(\theta)}
$$

Reject when $\Lambda$ is small.

------------------------------------------------------------------------

## Why It Matters

• Handles composite hypotheses\
• Reproduces $z$, $t$, $\chi^2$, $F$ tests\
• Scales to multi-parameter models\
• Has large-sample theory (Wilks)

------------------------------------------------------------------------

# One-Sided Normal LRT (σ Known)

Assume

$$
X_1,\dots,X_n \sim \Norm(\mu,\sigma^2)
$$

Test

$$
H_0: \mu = \mu_0
\qquad
H_1: \mu > \mu_0
$$

------------------------------------------------------------------------

## Likelihood

$$
L(\mu)
\propto
\exp\!\left(
-\frac{1}{2\sigma^2}
\sum (x_i - \mu)^2
\right)
$$

Unrestricted MLE:

$$
\hat\mu = \bar X
$$

------------------------------------------------------------------------

## Likelihood Ratio

$$
\Lambda
=
\frac{L(\mu_0)}{L(\bar X)}
=
\exp\!\left(
-\frac{n}{2\sigma^2}
(\bar X - \mu_0)^2
\right)
$$

(using\
$\sum (x_i - \mu_0)^2 = \sum (x_i - \bar X)^2 + n(\bar X - \mu_0)^2$)

------------------------------------------------------------------------

## Rejection Region

Reject when $\Lambda$ is small\
⇔ $(\bar X - \mu_0)^2$ large

Because alternative is one-sided:

$$
\bar X \text{ large}
$$

Equivalently,

$$
\frac{\bar X - \mu_0}{\sigma/\sqrt n}
>
z_\alpha
$$

The LRT reproduces the classical $z$-test.

------------------------------------------------------------------------

# Wilks' Theorem

Under regularity conditions,

$$
-2 \log \Lambda
\overset{d}{\to}
\chi^2_{df}
$$

$$
df
=
\dim(\Theta)
-
\dim(\Theta_0)
$$

------------------------------------------------------------------------

## Example: Normal with Unknown σ

Full model:

$$
(\mu, \sigma^2)
$$

Dimension = 2.

Testing $H_0: \mu = \mu_0$\
Null dimension = 1.

$$
df = 2 - 1 = 1
$$

Interpretation: number of independent restrictions imposed by $H_0$.
