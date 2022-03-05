# miscellaneous python code just for me

## perf_timer.py

timer class with perf_counter


## rand_tri.py

 *rand_tri* function returns a tensor filled with random numbers from a triangular distribution with lower limit *a*, upper limit *b* and mode *c*, where a < b and a  <= c <= b.

[wikipedia:Triangular distribution](https://wikipedia.org/wiki/Triangular_distribution)

## rand_dist.py

It provides classes to generate random numbers with an approximated inverse cumulative function.
The approximation function is constructed by piecewise linear interpolation with sampled points.

### RandDistGamma

It generates random numbers from a gamma distribution with shape *a* and scale *b*.

*step* : sample step in the input domain

*eps* : criterion to stop sampling. The sampling is stopped when the cdf is over 1-*eps*

*n_max* : maximum number of sampling iteration. It is to avoid the infinit loop.

[wikipedia: Gamma distribution](https://wikipedia.org/wiki/Gamma_distribution)

[docs.scipy: scipy.special.gammainc](https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.gammainc.html)


### RandDistTruncatedGaussian

It generates random numbers from a truncated gaussian distribution with *mean*, standard deviation *sigma*, lower bound *a*, and upper bound *b*.

*step*: sample step in \[0,1\].

[Qiita: Truncated Distributionからのサンプリング](https://qiita.com/9_ties/items/c593daab8b3f71638edd)
