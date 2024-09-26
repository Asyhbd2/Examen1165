print("Examen 1165")
print("Angel Tadeo De Leon Ceniceros Matricula: 22308051281165")
# Zona de clases
class Inventario1165:
    # Zona de funciones
    # El constructor Inventario
    def __init__(self,InventarioID,ProductoID,Cantidadinicial,Cantidadactual,Fechaactualizacion,Ubicacion,Notas):
     self.InventarioID1165=InventarioID
     self.ProductoID1165=ProductoID
     self.Cantidadinicial1165=Cantidadinicial
     self.Cantidadactual1165=Cantidadactual
     self.Fechaactualizacion1165=Fechaactualizacion
     self.Ubicacion1165=Ubicacion
     self.Notas1165=Notas
    # Mostrar datos
    def Datos1165(self):
       print(f"ID: {self.ProductoID1165} ProductoID: {self.ProductoID1165} ")
       print(f"Cantidad inicial: {self.Cantidadinicial1165} Cantidad actual: {self.Cantidadactual1165}")
       print(f"Fecha: {self.Fechaactualizacion1165} Notas: {self.Notas1165}")
    # Tupla   
    def Tupla_Inventario1165(self):
       Inventario=("Harina","Leche","Betun","Moldes","Huevos","Bandejas","Frutas")
       print(Inventario)
       for x in Inventario:
          print(x)
    # Lista
    def Lista_Ubicaciones1165(self):
       Ubicacion = ["Calle piña","Avenida raton","Avenida catabum","Calle torres","Calle epicon","Avenida casahouse","Avenida fresa"]
       print(Ubicacion)
       for x in Ubicacion:
          print(x)
    # Diccionario
    def Diccionario_Almacen_Condicion1165(self):
        Almacenycondicion={
            "Almacen A":"Bueno",
            "Almacen B":"Bueno",
            "Almacen C":"Bueno",
            "Almacen D":"Fuera de servicio",
            "Almacen E":"Bueno",
            "Almacen F":"Bueno",
            "Almacen G":"Fuera de servicio"
        }
        print(Almacenycondicion)
        for x,y in Almacenycondicion.items():
            print(x,y)                
# Zona de creacion del objeto
ObjetoInventario=Inventario1165(1,1,35,10,"10/5/24","Almacen C","Todo en orden")
# Zona de uso de objetos
print("Lista de atributos:")
ObjetoInventario.Datos1165()
print("Tupla de cosas en inventario:")
ObjetoInventario.Tupla_Inventario1165()
print("Lista de Ubicaciones:")
ObjetoInventario.Lista_Ubicaciones1165()
print("Diccionarios de almacenes y condicion:")
ObjetoInventario.Diccionario_Almacen_Condicion1165()