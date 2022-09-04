#!/usr/bin/env python3
import json
import numpy as np
import sys
x2=float(sys.argv[2])
y2=float(sys.argv[3])
d=float(sys.argv[1])
for i in sys.stdin:
    j = json.loads(i.strip())
    distance=np.sqrt((x2-j['lat'])**2+(y2-j['lon'])**2)
    
    if(  distance<d and ((j['humidity']>48) and (j['humidity']<54) ) and ((j['temperature']>20) and (j['temperature']<24))):
        print(j['timestamp'],1)           
