#Definimos la clase persona

class Persona:
	#Definir sus atributos
	nombre = ' '
	apellidos = ' '
	edad = 0
	poblacion= ' '

	#Definición de métodos


	#Definir el contructor
	def __init__(self, nombre):
		self.nombre = nombre

	def setApellidos(self, apellidos):
		self.apellidos = apellidos

	def setEdad(self, edad):
		self.edad = edad 

	def setPoblacion(self, poblacion):
		self.poblacion = poblacion 

	#Metodos
	def getNombre(self):
		return self.nombre
	def getApellidos(self):
		return self.apellidos
	def getEdad(self):
		return self.edad
	def getPoblacion(self):
		return self.poblacion

	#Mostrar datos
	def mostrarDatos(self):
		print('Todos los datos de la persona: ' + self.nombre +"  "+ self.apellidos +"  "+ str(self.edad) +"  "+ self.poblacion)
		print('El apellidos de la persona es: ' + self.apellidos)
		print('El edad de la persona es: ' + str(self.edad))
		print('El poblacion de la persona es: ' + self.poblacion)

	def mostrarDatosGet(self):
		print

#----Programa Principal

ciudadano = Persona("Ana")
ciudadano.setApellidos("Romero Torres")
ciudadano.setEdad(25)
ciudadano.setPoblacion("PA BAHALO TO")
ciudadano.mostrarDatos()

