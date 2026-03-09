def formating(n):
     s = format(n, '.3f')
     intpart, ostpart = s.split('.')

     intval = int(intpart)

     intzapyat = format(intval, ',')
     intspaces = intzapyat.replace(',', ' ')
     result = intspaces + ' .' + ostpart 
     
     return result.center(30, '*')
print(formating(123488482390.28174))



