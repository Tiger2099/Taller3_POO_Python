# ******** zona de clase ************
#se crea la clase
class cliente:
    #se crea el modelo constructor
    def __init__(self):
        #se crean atributos de clase
        self.nombre_cliente = ""
        self.apellido_cliente = ""
   #crear metodos get y set por atributos
def get_nombre(self):
    return self.nombre_cliente

def get_apellido(self):
    return self.apellido_cliente

def set_nombre(self, dato_nombre):
   self.nombre_cliente = dato_nombre

def set_apellido(self, dato_apellido):
   self.apellido_cliente = dato_apellido
   
   


def get_nombre(self):
    pass

def get_apellido(self):
    pass

def set_nombre(self, dato_nombre):
   pass

def set_apellido(self, dato_apellido):
   pass
   
   
   
   
   
   
    #se crean metodos normales de la clase
def tomar_datos(self):
    self.nombre_cliente = input("Ingrese su nombre: ")
    self.apellido_cliente = input("Ingrese su apellido: ")
    
def procesar_datos (self):
    print(f"El nombre del cliente es: {self.nombre_cliente}")
    print(f"El apellido del cliente es: {self.apellido_cliente}")