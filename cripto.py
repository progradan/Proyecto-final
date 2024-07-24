abc='ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234!#$%&¡?56789'
abc_total=''

def user_cod(palabra_1):
        abc_inicial=abc[:len(abc)-7]
        abc_final=abc[len(abc)-7:]
        abc_total=abc_final+abc_inicial
        
        dict_1={}
        for i in range(len(abc)):
            dict_1[abc[i]]=abc_total[i]
            
        
        palabra_1_lista=list(palabra_1)
        palabra_cifrada_1=''
        
        for letra_1 in palabra_1_lista:
            palabra_cifrada_1+=dict_1[letra_1]
        return palabra_cifrada_1
        

def user_dec(palabra_2):
        abc_inicial=abc[:len(abc)-7]
        abc_final=abc[len(abc)-7:]
        abc_total=abc_final+abc_inicial
        
        dict_2={}
        for k in range(len(abc)):
            dict_2[abc_total[k]]=abc[k]
            
            
        palabra_2_lista=list(palabra_2)
        palabra_descifrada_1=''
        
        for letra_2 in palabra_2_lista:
            palabra_descifrada_1+=dict_2[letra_2]
        return (palabra_descifrada_1)

