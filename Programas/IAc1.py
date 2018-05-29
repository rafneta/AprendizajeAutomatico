
# coding: utf-8

# In[46]:


def IAc1():
    
    def imprime():
        print "Para las siguientes enunciados contesta:"
        print "1 si representa una aplicación de IA"
        print "2 si no representa una aplicación de IA"
        print "3 si el ejemplo puede o no ser una aplicación de IA "        "dependiendo del punto de vista \n"
        a=raw_input("Escribe tu nombre: ")
    
    imprime()
    
    def preguntas():
        
        # Pregunta 1
        print "\n Hoja de cálculo que calcula sumas y otras funciones"        " predefinidas en datos dados"
        a=input("Opción: ")
        print "El resultado está determinado por la fórmula especificada"        " por el usuario, no se necesita AI"
            
        # Pregunta 2
        print "\n Predecir el mercado bursátil ajustando una curva a datos "        " anteriores sobre precios de acciones"
        a=input("Opción: ")
        print "Ajustar una curva simple no es realmente AI, pero hay tantas"        " curvas diferentes para elegir, incluso si hay una gran cantidad de"        " datos para restringirlas, que se necesita aprendizaje-automático/IA"        " para obtener resultados útiles."
        
        # Pregunta 3
        print "\n Un sistema de navegación GPS para encontrar la ruta "        "  más rápida"
        a=input("Opción: ")
        print "El procesamiento de señal y la geometría utilizados para"        " determinar las coordenadas no son AI, pero proporcionan buenas"        " sugerencias para la navegación (las rutas más cortas / más rápidas)"        " es AI, especialmente si se tienen en cuenta variables tales como las"        " condiciones del tráfico"
            
        # Pregunta 4
        print "\n Un sistema de recomendación de música como Spotify"        "que sugiere música"        "  en función del comportamiento de escucha del usuario"
        a=input("Opción: ")
        print "El sistema aprende del comportamiento de los usuarios"        " (no solo de usted)"
            
        
        # Pregunta 5
        print "\n Sistema de datos (como imágenes o videos) que puede"        "almacenar grandes"        " cantidades de datos y transmitirlos a muchos usuarios al mismo tiempo"
        a=input("Opción: ")
        print "Almacenar y recuperar elementos específicos de una recopilación"        " de datos no es adaptativo ni autónomo"
            
         # Pregunta 6
        print "\n Filtros de imágenes en aplicaciones como Photoshop"
        a=input("Opción: ")
        print "Los filtros suelen ser transformaciones sencillas, como el ajuste"        " del equilibrio de color, el contraste, etc., y por lo tanto, no son"        " adaptativos ni autónomos, pero los desarrolladores de la aplicación pueden"        " usar algunos algortimos de AI para ajustar automáticamente los filtros."
            
        # Pregunta 7
        print "\n Filtros de transferencia de estilo en aplicaciones como Prisma"        " que toman una foto y la transforman en diferentes estilos de arte"        "(impresionista, cubista, ...)"
        a=input("Opción: ")
        print "Tales métodos generalmente aprenden las estadísticas de la imagen"        " (características de un estilo de imagen)"        " y transforman la foto de entrada para que sus estadísticas coincidan"        " con el estilo, por lo que el sistema es adaptativo"
    preguntas()

