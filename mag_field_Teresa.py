# Cylindrical coordinates, with Br = 0, and Btheta, Bz depending only on r. This guarantees div(B) = 0.
# B0 is the max magnetic field, expressed in Teslas.
# r is the normalized distance to the axis (divided by R).

B0 = 1
R = 1

def TBz(r, n, m, Cnm, tau):
    '''Axial component of the magnetic field.'''
    return B0*(1 - r**(n+1)/tau)

def TdBz(r, n, m, Cnm, tau):
    '''Derivative of the axial component of the magnetic field.'''
    return -(n+1)*r**n*B0/(tau*R)

def TBtheta(r, n, m, Cnm, tau):
    '''Azimuthal component of the magnetic field.'''
    return B0*r**(m+1)/(tau*Cnm)

def TdBtheta(r, n, m, Cnm, tau):
    '''Derivative of the azimuthal component of the magnetic field.'''
    return (m+1)*B0*r**m/(tau*Cnm*R)