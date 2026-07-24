# Model and notation

This document records the main notation used in the mobility-informed SIR model.

## Compartments

| Symbol | Meaning |
|---|---|
| \(S(t)\) | susceptible population |
| \(I(t)\) | infectious population |
| \(R(t)\) | recovered population |
| \(N\) | total population |

## Parameters and time-varying quantities

| Symbol | Meaning |
|---|---|
| \(\xi(t)\) | mobility coefficient constructed from subway boarding counts |
| \(\beta(t)\) | time-varying transmission rate estimated in the model |
| \(\gamma\) | recovery rate |
| \(\gamma^{-1}\) | mean infectious period, fixed at 4.1 days |
| \(R(t)\) | mobility-weighted instantaneous reproduction number |

## Mobility-informed SIR equations

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
R(t) = \frac{\xi(t)\beta(t)}{\gamma}\frac{S(t)}{N}
```

## Important terminology

The mobility coefficient is denoted by \(\xi(t)\). The recovery rate is denoted by \(\gamma\). These two quantities should not be mixed.

If older local files use names such as `*_gamma.csv` for mobility outputs, those files should be interpreted as legacy mobility-coefficient files. New outputs should use `*_xi.csv` or equivalent `xi` terminology.
