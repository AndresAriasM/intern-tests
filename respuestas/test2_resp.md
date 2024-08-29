# Función de web-scrapping

### Lógica de la función

Se crea una función scrape_url para extraer datos de páginas web. 

Primero se hace una solicitud HTTP de tipo GET para solicitar la extracción de datos del sitio. Si la solicitud es exitosa (code 200), se procede a analizar el contenido de la página con BeautifulSoup para su estructuración y extracción. Si la solicitud falla se lanzará una excepción indicando el error.

Para la extracción se busca el primer div en el HTML que tenga la clase example-class. Si se encuentra, se extrae el texto de ese div. En caso de encontrarse la información la función devuelve ese texto y en el caso contrario devolverá un mensaje de error especificado en la función junto con un None como retorno.

Finalmente se encuentra un bucle for que recorre un arreglo con direcciones URL para aplicar la función previamente explicada e imprimir los resultados del web-scrapping para cada una de ellas.

Como extra se importa la libreria multiprocessing que en caso de implementarse sería de gran ayuda para reducir tiempos de ejecución puesto que podría distirbuirse la carga de trabajo paralelamente.

### Web-scraping secuencial y concurrente.

El secuencial es ideal cuando se aplica sobre un número reducido de páginas web, siendo la latencia y el tiempo de espera no tan esenciales. Es fácil de implementar y depurar, además de ser mas discreto.

El concurrente es mas óptimo para grandes volúmenes de datos o cuando se requiere extraer información de muchas páginas rápidamente. Se reducen los tiempos de espera al realizar solicitudes en paralelo pero cuenta con un riesgo mayor de ser detectado y bloqueado por firewalls por exceso de solicitudes. 
