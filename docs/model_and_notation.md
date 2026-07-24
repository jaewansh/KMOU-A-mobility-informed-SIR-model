# Model and notation

This document defines the notation used in the manuscript and the corresponding names used in the attached notebooks.

## Manuscript notation

| Symbol | Meaning |
|---|---|
| \(S(t)\) | susceptible population |
| \(I(t)\) | infectious population |
| \(R(t)\) | recovered population |
| \(N\) | total population |
| \(\xi(t)\) | mobility coefficient constructed from subway boarding counts |
| \(\beta(t)\) | time-varying transmission rate |
| \(\gamma\) | recovery rate |
| \(R(t)\) | instantaneous reproduction number |

## Mobility-informed SIR model

```math
\frac{dS}{dt} = -\xi(t)\beta(t)\frac{S(t)I(t)}{N}
```

```math
\frac{dI}{dt} = \xi(t)\beta(t)\frac{S(t)I(t)}{N} - \gamma I(t)
```

```math
\frac{dR}{dt} = \gamma I(t)
```

## Instantaneous reproduction number

```math
R(t)=\frac{\xi(t)\beta(t)}{\gamma}\frac{S(t)}{N}
```

## Mobility factor

```math
m(t)=\frac{X(t)}{Pop}
```

```math
L=\frac{1}{|T|}\sum_{t\in T}m(t)
```

```math
c(t)=\frac{m(t)}{L}
```

```math
b(t)=\frac{1}{|W(t)|}\sum_{\mu\in W(t)}c(\mu),
\quad W(t)=\{\mu\in T: |\mu-t|\leq 3\}
```

```math
\xi(t)=b(t)
```

## Code notation

| Code name | Manuscript notation | Meaning |
|---|---|---|
| `people_in` | \(X(t)\) | daily subway boarding count |
| `pop` | \(Pop\) | population denominator |
| `m` | \(m(t)\) | per-capita mobility intensity |
| `m_7` | implementation variable | centered 7-day moving average of `m` in the uploaded notebook |
| `L` | \(L\) | baseline mobility level |
| `c` | \(c(t)\) | normalized temporal mobility variation |
| `b` | \(b(t)\) | 7-day smoothed normalized mobility |
| `gamma` | \(\xi(t)\) | observed mobility coefficient in the uploaded code |
| `gamma_1` | \(0.9\xi(t)\) | 10% mobility-reduction scenario |
| `gamma_2` | \(0.8\xi(t)\) | 20% mobility-reduction scenario |
| `gamma_3` | \(0.7\xi(t)\) | 30% mobility-reduction scenario |
| `gamma_4` | \(0.6\xi(t)\) | 40% mobility-reduction scenario |
| `gamma_5` | \(0.5\xi(t)\) | 50% mobility-reduction scenario |
| `sigma` | \(\gamma\) | recovery rate in the Rt estimation notebook |

## Uploaded notebook implementation detail

The manuscript defines \(L\) as the temporal mean of \(m(t)\). The uploaded mobility-factor notebook uses the following implementation sequence:

```text
m = people_in / pop
m_7 = centered 7-day moving average of m
L = city-level mean of m_7
c = m / L
b = centered 7-day moving average of c
gamma = b
```

Thus, in the uploaded code, the final mobility coefficient is stored as `gamma`, and the manuscript notation for that final column is \(\xi(t)\).

## Important warning

In the attached code, the name `gamma` is used in the mobility-factor CSV files. This is not the same quantity as the SIR recovery rate \(\gamma\) in the manuscript. The recovery rate in the Rt estimation notebook is represented by:

```python
sigma = 1.0 / 4.1
```

No `theta` parameter is used in the manuscript mobility construction or in the attached notebooks.
