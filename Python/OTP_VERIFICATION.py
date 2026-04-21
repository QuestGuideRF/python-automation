import os
import math
import random
digits ="0123456789"
OTP =""
for i in range (6 ):
    OTP +=digits [math .floor (random .random ()*10 )]
otp =OTP +" твой OTP"
msg =otp
print (msg )