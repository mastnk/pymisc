from calc import *

def exec_test( cmd ):
    line = '{}(3)'.format(cmd)
    print('x=', line)
    try:
        x = eval(line)
        print( 'OK:', x)
    except:
        print( 'ERROR' )
    print()


exec_test( 'square' )
exec_test( '_square' )

exec_test( 'calc.square' )
exec_test( 'calc._square' )

import calc
exec_test( 'calc.square' )
exec_test( 'calc._square' )


