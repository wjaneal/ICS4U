#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 19:50:37 2018

@author: chenquancheng
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 17:36:20 2018

@author: chenquancheng
"""
import math
pi=4*math.atan(1)
gears=[3,5,7,10]
torqueRequired=0.5*120/2.2*9.8*0.025
print(torqueRequired)
RPM=3562.12
torqueM=0.5495
speed=RPM/60*2*pi*0.025
for i in gears:
    for j in gears:
        if torqueM*i*j>=1*torqueRequired:
            t=1.03/(speed/i/j)
            if t<5:
                print("Torque:",torqueM*i*j,"speed:",speed/i/j,"Time",t,"Gears:",i,j)