def valint(*args):
    if len(args)==1:
      if type(args[0]) == int:
        return False
      else:
        return False
    if len(args)==2:
        if not type(args[1]) == list:
            raise TypeError("El segundo argumento no es una lista", type(args))
        else:
            for i in range(len(args[1])-1):
                if args[1][i]>=args[1][i+1]:
                    raise ValueError("El segundo argumento de la lista no es de forma creciente")
                else:
                    return True
    if len(args)==0:
      print("no hay ningun valor")
    if len(args)>2:
      raise TypeError("No se puede colocar mas de dos argumento")
  
  
def valfloat(*args):
    if len(args)==1:
      if type(args[0]) == int:
        return True
      else:
          return False
    if len(args)==2:
        if not type(args[1]) == list:
            raise TypeError("El segundo argumento no es una lista", type(args))
        else:
            for i in range(len(args[1])-1):
                if args[1][i]>=args[1][i+1]:
                    raise ValueError("El segundo argumento de la lista no es de forma creciente")
                else:
                    return True
    if len(args)==0:
      print("no hay ningun valor")
    if len(args)>2:
      raise TypeError("No se puede colocar mas de dos argumento")
  
def valcomplex(*args):
    if len(args)==1:
      if type(args[0]) == int:
        return True
      else:
          return False
    if len(args)==2:
        if not type(args[1]) == list:
            raise TypeError("El segundo argumento no es una lista", type(args))
        else:
            for i in range(len(args[1])-1):
                if args[1][i]>=args[1][i+1]:
                    raise ValueError("El segundo argumento de la lista no es de forma creciente")
                else:
                    return True
    if len(args)==0:
      print("no hay ningun valor")
    if len(args)>2:
      raise TypeError("No se puede colocar mas de dos argumento")
  
   
def valList(*args):
    if len(args[0]) == 1:
        if type(args[0])==list:
            return True
        else:
            return False
    elif len(args)==3:
        if  (len(args[1])==list and type(args[2])=='values') or (len(args[1])==int  and type(args[2])==str):
            if not (args[2])==['value', 'len']:
                       raise ValueError("El tercer argumento no son los str('len', 'values')")
        
            if  args[2]=='len':
                if not len(args[0])==list:
                   return  False
                return len(args[0])==(args[1])
        
            elif args[2]=='values':
                if not len(args[0])==list and not len(args[1])==list :
                    return False
                return (args[0])==(args[1])
                  
            else:
                return False
            
        else:
            raise TypeError("son diferentes combinaciones")
    else:
        raise TypeError("solo se pueden resivir 1 o 3 argumentos")
    