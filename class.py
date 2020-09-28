# words = set(shakespeare.read().decode().split())
  #max (7.5, 9.5)
  #max(min(1, -2), min(pow(3, 5), -4))
  #pow(100, 2)
  #from math import sqrt, exp
#sqrt(256)
#two = print(2)


#def sum_squares(x, y):
     #   return add(square(x), square(y
#sum_squares(3, 4)
#def pressure(v, t, n):
      #  """Compute the pressure in pascals of an ideal gas.

    #     def percent_difference(x, y):
     #       difference = abs(x-y)
   #     return 100 * difference / x
#>>> percent_difference(40, 50)

       # Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law

     #   v -- volume of gas, in cubic meters
       ##  n -- particles of gas
         #k = 1.38e-23  # Boltzmann's constant
     #   return n * k * t / v

 #def percent_difference(x, y):
 #       difference = abs(x-y)
    #    return 100 * difference / x
#percent_difference(40, 50)
phi = 1/2 + pow(5, 1/2)/2
>>> def near_test():
        assert near(phi, square, successor), 'phi * phi is not near phi + 1'

def iter_improve_test():
        approx_phi = iter_improve(golden_update, golden_test)
        assert approx_eq(phi, approx_phi), 'phi differs from its approximation'