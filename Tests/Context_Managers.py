file = open('new.txt', 'w') 
file.write('hello')
file.close() #vai fechar o arquivo ('isso poupa memória, caso vc abra outros arquivos')

# a questão acima pode ser claramente refeita com o ContextManager:
with open('new.txt', 'w') as file:
        file.write('hello')


##Outras formas de fazer:
# ContextManager 
class ContextManager():
    def __init__(self):
        print('init method called')
         
    def __enter__(self):
        print('enter method called')
        return self
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
       # print(f"{exc_type},{exc_value},{exc_traceback}")
        print('exit method called')

with ContextManager() as manager:
    print('with statement block')
#  ===============================================================
## OPEN FILE WITH ContextManager

class Open_File():
    
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        print('init method called')
         
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print('enter method called')
        return self.file
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close() #vai esperar todo o programa terminar para ser executado
        print('exit method called')


with Open_File('new.txt', 'w') as f:
    f.write('Testing')
    print('with statement block')

print(f.closed)  #após todo o programa ter sido executado, esse comando vai fechar o programa

#  ===============================================================