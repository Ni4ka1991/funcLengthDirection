#!/usr/bin/env python3

from os import system
from sys import argv 

length = int( argv[1] )
direction = argv[2]

system( "clear" )

def drawLine( length, direction ):
    if( direction == "h"):
     print( "-" * length )
    elif( direction == "v" ):
     for i in range( length ):
      print( "|\n" )
    else:
     print( "Be careful! Enter h or v to choose a direction." )


#drawLine( 7, "h" )

drawLine( length, direction )
