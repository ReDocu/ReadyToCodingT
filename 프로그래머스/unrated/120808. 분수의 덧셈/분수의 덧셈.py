import math

def solution(numer1, denom1, numer2, denom2):
    numer = denom1 * numer2 + denom2 * numer1   
    denom = denom1 * denom2
    
    return [numer // math.gcd(denom, numer) , denom // math.gcd(denom, numer)]