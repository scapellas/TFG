# Cylindrical coordinates, with Br = 0, and Btheta, Bz depending only on r. This guarantees div(B) = 0.
# q and alpha are adimensional parameters for the magnetic field profile.
# For alpha = 1, we obtain the Force-Free Gold-Hoyle model.
# B0 is the max magnetic field, expressed in Teslas.
# r is the normalized distance to the axis (divided by R).

B0 = 1

def Bz(r, q, alpha):
    return B0/(1+(q*r)**2)

def Btheta(r, q, alpha):
    return q*(r**alpha)*Bz(r, q, alpha)

def dBz(r, q, alpha):
    return -(2*q**2*r)/(q**2*r**2 + 1)**2

def dBtheta(r, q, alpha):
    return (alpha*q*r**(alpha - 1))/(q**2*r**2 + 1) - (2*q**3*r**(alpha + 1))/(q**2*r**2 + 1)**2