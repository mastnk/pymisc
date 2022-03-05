import time

__all__ = ['PerfTimer']

class PerfTimer:
    def __init__( self ):
        self.reset()

    def start( self ):
        self.__start_time = time.perf_counter()

    def stop( self ):
        self.__sec += time.perf_counter() - self.__start_time
        self.__start_time = None
        return self.get_time()

    def reset( self ):
        self.__start_time = None
        self.__sec = 0

    def restart( self ):
        self.reset()
        self.start()

    def get_time( self ):
        s = self.__sec
        if( self.__start_time is not None ):
            s += time.perf_counter() - self.__start_time
        return s

if( __name__ == '__main__' ):
    pt = PerfTimer()

    pt.start()
    time.sleep(1)
    pt.stop()

    print( pt.get_time() )
