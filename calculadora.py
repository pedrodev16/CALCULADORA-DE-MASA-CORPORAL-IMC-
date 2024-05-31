# Diccionarios
#autor del software
autor = {
    'nombre': 'Laura',
    'apellido': 'Laura',
    'email':'Laura@gmail.com'
    
}

data_autor= autor['nombre']+" Email:"+autor['email']


#lista TABLAS O ARREGLO  DE DIAGNOSTICOS 
data_diagnostico=[
'Criterio de ingreso en hospital',
'Infrapeso',
'Bajo peso',
'Peso normal (saludable)',
'Sobrepeso (obesidad de grado I)',
'Sobrepeso crónico (obesidad de grado II)',
'Obesidad premórbida (obesidad de grado III)',
'Obesidad mórbida (obesidad de grado IV)'
]






      #aqui creamos una FUNCION para calcular el indice de masa corporal 
def calcular_imc(p,a):
        return p / (a * a)


#CREAMOS UNA FUNCION PARA CATEGORIZAR EL DIAGNOSTICO SEGUN EL RESULTADO IMC
   
def categorizar_peso(p,a):
      # Crear una tupla [DATOS DE CONDICION IMC]
      mi_tupla_IMC = (16,17,18,25,30,35,40)
      
       # Ejemplo de llamada a la función carcular_imc()
      imc = calcular_imc(p,a)

      if imc < mi_tupla_IMC[0]:  
              return data_diagnostico[0]
      
      elif mi_tupla_IMC[0] <= imc < mi_tupla_IMC[1]:
              return data_diagnostico[1]
      
      elif mi_tupla_IMC[1] <= imc < mi_tupla_IMC[2]:        
              return data_diagnostico[2]
      
      elif mi_tupla_IMC[2] <= imc < mi_tupla_IMC[3]: 
               return data_diagnostico[3]
      
      elif mi_tupla_IMC[3] <= imc < mi_tupla_IMC[4]: 
                return data_diagnostico[4]
      
      elif mi_tupla_IMC[4] <= imc < mi_tupla_IMC[5]:  
              return data_diagnostico[5]
      
      elif mi_tupla_IMC[5] <= imc < mi_tupla_IMC[6]:      
               return data_diagnostico[6]
      else:
              return data_diagnostico[7]
      

print("############## CALCULADORA DE MASA CORPORAL (IMC) ##############") 
print("autor:",data_autor)
print()

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# creamos un objeto de la clase Persona


# llamada a metodo o funcion, retorna el imc y lo concatena acontinuacion.
print("#######################################") 
print("-->Su índice de masa corporal (IMC) es:", calcular_imc(peso,altura))
print("-->Categoría de peso:", categorizar_peso(peso,altura))
