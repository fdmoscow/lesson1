stroka1 = input()
stroka2 = input()


def compare(stroka1, stroka2): 
    if type(stroka1)  or type(stroka2) is not str:
        return(0)
    
    elif len(stroka1) == len(stroka2):
        return(1)
    
    elif len(stroka1) > len(stroka2):
        return(2)
    
    elif len(stroka1) != len(stroka2) and stroka2 =='learn':
        return(3)
    else:
        return('Хрень какая-то')
    
sravnenie = compare(stroka1, stroka2)    #нужно ли вводить здесь еще одну переменную sravnenie или правильно сразу выводить на печать print(compare(str1, str2))?
print(sravnenie) 
        
