#!/usr/bin/env python3

import os
import subprocess
import argparse
from nabazpileds import Nabazpileds

# get the command line options
parser = argparse.ArgumentParser()
parser.add_argument("-a", "--animation", help="LED animation (i.e. 'glow')", required=True )
args = parser.parse_args()

# init the leds
leds = Nabazpileds()
#leds.startup()

# fire the animation
if( args.animation == 'startup' ):
	leds.startup()
if( args.animation == 'glow' ):
	leds.glow()
if( args.animation == 'k.i.t.t.' ):
	leds.kitt()
if( args.animation == 'wave' ):
	leds.wave()
if( args.animation == 'cross' ):
	leds.cross()
if( args.animation == 'colorcycle' ):
	leds.colorcycle()
if( args.animation == 'rainbow' ):
	leds.rainbow()
if( args.animation == 'disco' ):
	leds.disco()
if( args.animation == 'police' ):
	leds.police()
if( args.animation == 'traffic' ):
	leds.traffic()
if( args.animation == 'randomglow' ):
	leds.randomglow()
exit(0)
