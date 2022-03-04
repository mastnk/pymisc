import torch

def rand_tri( shape, a, b, c ):
    def tri_inv_cdf( u, a, b, c ):
        m = (u< (c-a)/(b-a)).float()
        return m*( a + (u* ((b-a)*(c-a))).sqrt() ) + \
              (1-m)*( b - ((1-u)* ((b-a)*(b-c))).sqrt() )

    return tri_inv_cdf( torch.rand( shape ), a, b, c )

if( __name__ == '__main__' ):
    print( rand_tri( (2,4), 0, 10, 3 ) )
