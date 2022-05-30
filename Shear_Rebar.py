import math

lightcon=1
fck=24

Vc=(1/6)*lightcon*math.sqrt(fck)
print(Vc)

# Vs=Vu/pi - Vc
Av=71.3*2
fy=300
d=580
s=300
Vc=(1/6)*lightcon*math.sqrt(fck)*350*580/1000
Vs=Av*fy*d/s/1000
print(Vc, '\n', Vs)
print((Vc+Vs)*0.75)

# compressive_shear_supported_column
Nu=1500*1000
Ag=400*400
Vc=(1/6)*(1+(Nu/(14*Ag)))*lightcon*math.sqrt(fck)*400*400/1000
Vs=2*71.3*300*400/300/1000
Vn=Vc+Vs
print(Vc)
print(Vs)
print(0.75*Vn)
