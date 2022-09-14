'''
X = coluna
Y = linha

Como se fosse uma planilha eletrônica
'''

x = 0           
while x < 10:   #  começo do loop maior
    y = 0
    
    while y < 5:    #  loop dentro de outro loop
        print(f'({x}, {y})')
        y +=1
        
    x +=1
    
print('FIM')
