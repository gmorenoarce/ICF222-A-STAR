## HAY UN PSEUDOCODIGO ABAJO EXPLICANDO COMO FUNCIONA ESTO ##

class Nodo: #Creamos una clase Nodos 
    def __init__(self, Padre=None, Ubicacion=None):
        self.Padre = Padre
        self.Ubicacion = Ubicacion
        self.g = 0
        self.h = 0
        self.f = 0
        
def AgregarListaAbiertos(ListaAbiertos, Hijo):
    for node in open:
        if (Hijo == Nodo and Hijo.f >= Nodo.f):
            return False
    return True

def AEstrella(Mapa, Inicial, Meta):
    ListaAbiertos = []
    ListaCerrados = []
    NodoInicial = Nodo(Inicial, None)
    NodoMeta = Nodo(Meta, None)
    ListaAbiertos.append(NodoInicial)
    
    while len(ListaAbiertos) > 0:
        ListaAbiertos.sort()
        NodoActual = ListaAbiertos.pop(0)
        ListaCerrados.append(NodoActual)
        
        if NodoActual == NodoMeta:
            Camino = []
            while NodoActual != NodoInicial:
                Camino.append(NodoActual.Ubicacion)
                NodoActual = NodoActual.Padre
            return Camino[::-1]
        (x, y) = NodoActual.Ubicacion
        Hijos = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for next in Hijos:
            ValorEnMapa = Mapa.get(next)
            # Revisar los mapas para cambiar ESTO
            if(ValorEnMapa == '#' or ValorEnMapa == '@'):
                continue
            # Revisar si hay que cambiar condicionales para paredes y obstaculos
            Hijo = Nodo(next, NodoActual)
            if(Hijo in ListaCerrados):
                continue
            Hijo.g = (Hijo.Ubicacion[0] - NodoInicial.Ubicacion[0]) + (Hijo.Ubicacion[1] - NodoInicial.Ubicacion[1])
            Hijo.h = (Hijo.Ubicacion[0] - NodoInicial.Ubicacion[0]) + (Hijo.Ubicacion[1] - NodoInicial.Ubicacion[1])
            Hijo.f = Hijo.g + Hijo.h
            if(AgregarListaAbiertos(open, Hijo) == True):
                ListaAbiertos.append(Hijo)
    return None
    
def main():
  Mapa = {}
  Almacenados = []
  NodoInicial = None
  NodoMeta = None
    
  Archivo = input('Ingrese el nombre del archivo .map extension incluida')
  with open(Archivo,'r') as openfileobject:
    for line in openfileobject:
      entrada = line
      temp = len(entrada)
      salida = entrada[:temp - 1] # Escribimos las lineas del archivo eliminando el \n
      Almacenados.append(salida)

  Archivo.close()
  Camino = AEstrella(Mapa, NodoInicial, NodoMeta)
  print(Camino)

# REVISAR CAMBIOS PARA MAPAS
# PUEDE SER NECESARIO UNA HEURISTICA GLOBAL def 
# COMPARAR MAPAS CON LA PAGINA DEL PROFE PARA VER SI LOS RESUELVE IGUAL

########################################################################################
# A* Pseudocodigo
# Inicializar la lista de nodos disponibles y nodos usados
#ListaAbiertos = ListaVacia # La lista abierta es igual a la lista con los nodos vacios
#ListaCerrados= ListaVacia # La lista cerrada es igual a la lista con los nodos vacios

# Agregamos el nodo Inicial
#Agregamos el NodoInicial a la ListaAbiertos (dejamos f con valor 0)

# Loop hasta encontrar la salida osea
#while ListaAbiertos != void
    # Obtener el nodo actual
    #NodoActual = (Nodo con el menor valor de f)
    #Remover el NodoActual de ListaAbiertos
    #Agregar el NodoActual a ListaCerrados
    # Encontrar la meta
    #if NodoActual = Meta
        #MetaLograda, asi que, break:
    # Generar Vecinos del Nodo Seleccionado
   #Hijos = Nodos Adyacentes del NodoActual
    
    #for each Hijo in Hijos
        # Si el hijo esta en ListaCerrados
        #if Hijo exist in ListaCerrados
            #continuamos el loop

        # Creamos los valores f,g,h para el hijo
       # Hijo.g = NodoActual.g + DistanciaEntreHijoYActual
       # Hijo.h = DistanciaEntreHijoYMeta
        #Hijo.f = Hijo.g + Hijo.h

        # Si el hijo esta en ListaAbiertos
        #if Hijo.Ubicacion esta en ListaAbierta.NodoActual.Ubicacion
            #if Hijo.g > ListaAbierta.NodoActual.g
                #continuamos el loop
        # Agregamos el hijo a ListaAbiertos
        #ListaAbiertos.Append(Hijo)
  #TRANSFORMAR EL MAPA INGRESADO CON LOS CARACTERES A 0 Y 1
  #
########################################################################################
