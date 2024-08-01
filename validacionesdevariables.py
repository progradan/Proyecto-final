def valint(*args):
    if len(args)==1:
      if type(args[0]) == int:
        return True
      else:
          return False
    if len(args)==2:
        if type(args[0]) == int and type(args[1]) == list:
            for i in range(len(args[1])-1):
                if args[1][i]>=args[1][i+1]:
                    raise ValueError("El segundo argumento de la lista no es de forma creciente")
                else:
                    return True
            return True
        if  type(args[1])== list or type(args[0]) != int:
            return False
        if not type(args[1])== list:  
            raise TypeError("El segundo argumento no es una lista", type(args))
    if len(args)==0:
      print("no hay ningun valor")
    if len(args)>2:
      raise TypeError("No se puede colocar mas de dos argumento")
  
  
def valfloat(*args):
    if len(args)==1:
      if type(args[0])==float:
        return True
      else:
          return False
    if len(args)==2:
        if type(args[0]) ==float and type(args[1]) == list:
            for i in range(len(args[1])-1):
                if args[1][i]>=args[1][i+1]:
                    raise ValueError("El segundo argumento de la lista no es de forma creciente")
                else:
                    return True
            return True
        if  type(args[1])== list or type(args[0]) != float:
            return False
        if not type(args[1])== list:  
            raise TypeError("El segundo argumento no es una lista", type(args))
        
    if len(args)==0:
      print("no hay ningun valor")
    if len(args)>2:
      raise TypeError("No se puede colocar mas de dos argumento")
  
def valcomplex(*args):
    if len(args)==1:
      if type(args[0]) ==complex:
        return True
      else:
          return False
    if len(args)==2:
        if type(args[0]) ==complex and type(args[1]) == list:
            for i in range(len(args[1])-1):
                if args[1][i]>=args[1][i+1]:
                    raise ValueError("El segundo argumento de la lista no es de forma creciente")
                else:
                    return True
            return True
        if  type(args[1])== list or type(args[0]) != complex:
            return False
        if not type(args[1])== list:  
            raise TypeError("El segundo argumento no es una lista", type(args))
    if len(args)==0:
      print("no hay ningun valor")
    if len(args)>2:
      raise TypeError("No se puede colocar mas de dos argumento")
  
   
def valList(*args):
    if len(args) == 1:
        if type(args[0])==list:
            return True
    if len(args) == 3: 
        if (type(args[0])==list and type(args[1])==list and type(args[2])==str) or (type(args[0])==list and type(args[1])==int and type(args[2])==str):
            if args[2]=='value' and type(args[0])==list and type(args[1])==list and args[0]==args[1]:
                return True
            elif args[2] == 'value' and (type(args[0]) != list or type(args[1]) != list or args[0] != args[1]):
                return False
            elif args[2]=='len' and type(args[0]) == list and type(args[1]) == int and len(args[0]) == args[1]:
                return True
            elif args[2] == 'len' and (type(args[0]) != list or len(args[0]) != args[1]):
                return False
            elif (args[2] != 'len' or args[2] != 'value'):
                raise ValueError('El ultimo argumento es diferente de len o value.')
        elif (type(args[0])==list and (type(args[1])!=int or type(args[2])!=str)) or (type(args[0])==list and (type(args[1])!=list or type(args[2])!=str)):
            raise TypeError('Los argumentos son diferentes.')     
    else:
        raise TypeError("solo se pueden resivir 1 o 3 argumentos")
    
    
