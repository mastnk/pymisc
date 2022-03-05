from scipy.special import gammainc
from scipy.interpolate import interp1d
from scipy.special import erf
from scipy.special import erfinv
from math import sqrt

import numpy as np

__all__ = ['RandDistGamma', 'RandDistTruncatedGaussian']

##### gamma distribution #####
#https://en.wikipedia.org/wiki/Gamma_distribution
#https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.gammainc.html

def sampled_gamma_dist_cdf(a, b, step=0.001, eps=1E-6, n_max=1E6 ):
    cdf = []
    xxx = []
    x = 0
    for i in range(int(n_max)):
        y = gammainc(a,x/b)
        xxx.append(x)
        cdf.append(y)
        x += step
        if( y > 1-eps ):
            break
    xxx.append(x)
    cdf.append(1.0)
    return xxx,cdf

def approximated_gamma_dist_cdf(a, b, step=0.001, eps=1E-6, n_max=1E6 ):
    xxx, cdf = sampled_gamma_dist_cdf(a,b,step, eps, n_max )
    return interp1d( xxx,cdf )

def approximated_gamma_dist_cdf_inv(a, b, step=0.001, eps=1E-6, n_max=1E6 ):
    xxx, cdf = sampled_gamma_dist_cdf(a,b,step, eps, n_max )
    return interp1d( cdf, xxx )

class RandDistGamma():
    '''
        a: shape, b: scale
        https://en.wikipedia.org/wiki/Gamma_distribution

        cdf is scipy.special.gammainc
    '''
    def __init__( self, a, b, step=0.001, eps=1E-6, n_max=1E6 ):
        self.cdf_inv = approximated_gamma_dist_cdf_inv(a,b,step,eps,n_max)

    def __call__(self, shape):
        u = np.random.uniform(size=shape)
        return self.cdf_inv(u)

##### truncated gaussian distribution #####
# https://qiita.com/9_ties/items/c593daab8b3f71638edd
def sampled_t_std_gaussian_dist_cdf_inv( a, b, step=0.001 ):
    n = int(1/step)
    uuu = [step*i for i in range(n)]
    while( uuu[-1] >= 1.0 ):
        uuu.pop(-1)
    uuu.append(1.0)

    Fa = 0.5 * (1 + erf(a/sqrt(2)))
    Fb = 0.5 * (1 + erf(b/sqrt(2)))

    xxx = [sqrt(2)*erfinv(2 *((Fb - Fa) * u + Fa) - 1) for u in uuu]
    return uuu, xxx

def approximated_t_std_gaussian_cdf_inv(a, b, step=0.001 ):
    uuu, xxx = sampled_t_std_gaussian_dist_cdf_inv(a,b,step)
    return interp1d( uuu, xxx )

class RandDistTruncatedGaussian():
    def __init__( self, mean, sigma, a, b, step=0.001 ):
        self.mean = mean
        self.sigma = sigma
        self.a=a
        self.b=b

        aa = (a-self.mean)/self.sigma
        bb = (b-self.mean)/self.sigma
        self.cdf_inv = approximated_t_std_gaussian_cdf_inv( aa, bb, step )

    def __call__(self, shape):
        u = np.random.uniform(size=shape)
        return self.cdf_inv(u)*self.sigma + self.mean

if( __name__ == '__main__' ):
    s2=0.5*0.5
    a=1/s2
    b=s2

    rdg = RandDistGamma(a,b)
    x = rdg([2,8])
    print(x)

    rdtg = RandDistTruncatedGaussian( 1, 1, 0, 2 )
    x = rdtg([2,8])
    print(x)

