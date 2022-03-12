# https://discuss.pytorch.org/t/random-number-on-gpu/9649

import torch

class RandNormal():
    def __init__(self, shape=(1,), device=None, dtype=torch.float):
        self.__rand = None
        self.set( shape, device, dtype )

    def set( self, shape=None, device=None, dtype=None ):
        if( shape is None ):
            shape = self.__rand.shape
        if( device is None ):
            device = self.__rand.device
        if( dtype is None ):
            dtype = self.__rand.dtype

        if( self.__rand is None or
            self.__rand.shape != shape or
            self.__rand.device != device or
            self.__rand.dtype != dtype ):
            self.__rand = torch.randn(shape).to(device=device,dtype=dtype)

    def sample( self ):
        return self.__rand.normal_()

    @property
    def shape( self ):
        return self.__rand.shape

    @property
    def dtype( self ):
        return self.__rand.dtype

    @property
    def device( self ):
        return self.__rand.device

if( __name__ == '__main__' ):
    from perf_timer import *

    pt = PerfTimer()

    n = 10000

    x = RandNormal( (n,), 'cuda' )
    print( x.sample()[:2] )
    print( x.sample()[:2] )

    print( 'GPU' )
    pt.start()
    for i in range(n):
        x.set( x.shape, x.device, x.dtype )
        x.sample()
    pt.stop()
    print( pt.get_time() )

    print( 'CPU' )
    print( torch.randn( (n,) )[:2] )
    print( torch.randn( (n,) )[:2] )
    pt.start()
    for i in range(n):
        x = torch.randn( (n,) )
    pt.stop()
    print( pt.get_time() )

    print( 'CPU->GPU' )
    print( torch.randn( (n,) ).to('cuda')[:2] )
    print( torch.randn( (n,) ).to('cuda')[:2] )
    pt.start()
    for i in range(n):
        x = torch.randn( (n,) ).to('cuda')
    pt.stop()
    print( pt.get_time() )

