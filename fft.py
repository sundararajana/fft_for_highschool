import cmath

two_pi_i = 2*cmath.pi*(1j)

def FFT(poly):
    n = len(poly)
    if n == 1:
        return poly

    poly_even = poly[0:(n - 1):2]
    poly_odd = poly[1:n:2]
    y_even = FFT(poly_even)
    y_odd = FFT(poly_odd)

    y = [0]*n
    omega = cmath.exp(two_pi_i / n)
    for j in range(n//2):
        omega_pow_j = omega ** j
        y[j] = y_even[j] + omega_pow_j * y_odd[j]
        y[j + n//2] = y_even[j] - omega_pow_j * y_odd[j]
    return y

def IFFT(poly):
    def ifft_helper(poly):
        n = len(poly)
        if n == 1:
            return poly

        poly_even = poly[0:(n - 1):2]
        poly_odd = poly[1:n:2]
        y_even = ifft_helper(poly_even)
        y_odd = ifft_helper(poly_odd)

        y = [0]*n
        omega = cmath.exp(-two_pi_i / n)
        for j in range(n//2):
            omega_pow_j = omega ** j
            y[j] = y_even[j] + omega_pow_j * y_odd[j]
            y[j + n//2] = y_even[j] - omega_pow_j * y_odd[j]
        return y

    # normalization step
    n = len(poly)
    res = ifft_helper(poly)
    return [ i/n for i in res ]

x = [ 3, 4, 4, 6, 2, 1, 3, 4]
print(FFT(x))

# small imaginary parts result due to floating point
# computation. Just ignore imaginary parts as we know our 
# polynomial has only real coefficients

print([i.real for i in IFFT(FFT(x))])
