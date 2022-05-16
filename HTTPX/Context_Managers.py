 
# ContextManager 
class ContextManager():
    def __init__(self):
        print('init method called')
         
    def __enter__(self):
        print('enter method called')
        return self
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
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

print(f.closed)  #vai motrar que o programa começou, seguiu a sua ordem e por fim chegou no seu fim, que é o exit

#  ===============================================================