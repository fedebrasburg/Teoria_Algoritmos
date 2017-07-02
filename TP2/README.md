[Source](https://algoritmos-rw.github.io/tda/tp2/ "Permalink to Teoría de Algoritmos I")

# Teoría de Algoritmos I

El trabajo práctico consiste en las dos partes que se listan a continuación.

Lineamientos básicos:

* el trabajo se realizará en grupos de tres personas.
* la fecha de entrega es el **lunes 5 de junio de 2017**. Se debe entregar en el horario de clase en papel (informe + `código en monoespacio`), más una entrega en digital de código (.zip) e informe (.pdf) al correo de entregas del curso: `tps.7529rw@gmail.com`.
* el lenguaje de implementación es libre, pero se debe comunicar por correo en caso de _no_ ser uno de: C, Python, Java, JavaScript, Ruby.

## Contenidos

### Clases de complejidad

Escribir el pseudocódigo de un algoritmo que resuelva cada uno de los siguientes problemas en tiempo polinomial, o bien demostrar que son NP-Completos.

1. Se tiene un conjunto de _n_ actividades para seleccionar. Cada actividad tiene asociados un tiempo de inicio y tiempo de fin. Se dice que un conjunto de actividades es compatible si no hay dos que se superpongan en un tiempo. Se pide un algoritmo que devuelva verdadero o falso de acuerdo a si se puede encontrar un subconjunto compatible de tamaño _k_ o superior.

2. Se tiene un conjunto de _n_ actividades para seleccionar. Cada actividad tiene asociados un conjunto de tiempos de inicio y fin. Se dice que un conjunto de actividades es compatible si no hay dos que se superpongan en un tiempo. Se pide un algoritmo que devuelva verdadero o falso de acuerdo a si se puede encontrar un subconjunto compatible de tamaño _k_ o superior.

3. En teoría de grafos, un camino hamiltoniano es un camino que visita cada vértice del grafo exactamente una vez. Se pide un algoritmo que indique si un grafo G tiene un camino hamiltoniano o no.

4. En teoría de grafos, un camino hamiltoniano es un camino que visita cada vértice del grafo exactamente una vez. Se pide un algoritmo que indique si un digrafo acíclico D tiene un camino hamiltoniano o no.

5. Se tiene un grafo dirigido y pesado G, cuyas aristas tienen pesos que pueden ser negativos. Se pide devolver verdadero o falso de acuerdo a si el grafo tiene algún ciclo con peso negativo.

6. Se tiene un grafo dirigido y pesado G, cuyas aristas tienen pesos que pueden ser negativos. Se pide devolver verdadero o falso de acuerdo a si el grafo tiene algún ciclo con exactamente igual a cero.

### Algoritmos de camino mínimo

Un grupo de conocidos inversores ha logrado modelar un dinámico sistema financiero usando un grafo dirigido. En este los vértices son modelados como monedas y sus aristas por unos valores relacionados a las tasas de cambio entre ellas, de manera tal que el camino mínimo entre dos monedas represente la manera óptima de cambiar dinero de una en otra.[1][1]

Dado que el conocimiento de estos financistas sobre algoritmia es limitado, acuden a estudiantes de Teoría de Algoritmos I para asesoramiento.

Se pide, entonces:

1. Escribir un breve informe (máximo cinco párrafos), explicando las ventajas y desventajas de los tres algoritmos de camino mínimo vistos en el curso (Dijkstra, Bellman-Ford y Floyd-Warshall). Explicar el principio de funcionamiento de cada uno y a qué técnica de programación responde.
2. El hecho de encontrar ciclos negativos en este problema significa que podríamos explotar el tipo de cambio para potencialmente ganar dinero infinito. Explicar cómo se identificaría esta situación usando los algoritmos descriptos.
3. Escribir un programa que dado un número _n_ genere un digrafo completo de _n_ vértices (y por lo tanto aristas _n*(n-1)_), con todos pesos positivos.
4. Implementar los algoritmos de Dijkstra, Bellman-Ford y Floyd-Warshall para encontrar caminos mínimos en grafos.
5. Extraer breves conclusiones (máximo dos párrafos) sobre el rendimiento de cada algoritmo ante diferentes tamaños de la entrada comparándolo con su complejidad computacional teórica.

[1]: Para analizar más en detalle este modelo, consultar "Algorithms", R. Sedgewick, K. Wayne, (cuarta edición), cap. 4.4 "Arbitrage", pp: 679-681.

## Aclaraciones generales

1. El informe de todo el trabajo no debe superar las cuatro carillas de extensión, y deberá incluir las instrucciones para ejecutar todos los programas desarrollados.
2. Para la implementación de los algoritmos se podrán usar todo tipo de bibliotecas, excepto de grafos.
3. Los grafos deberán ser generados en el formato propuesto por Sedgewick, en donde los vértices estarán nombrados según indentificadores desde 0 hasta _V-1_, y los archivos de están confeccionados según: 
    * Una primera línea indicando la cantidad de vértices _V_.
    * Una segunda línea indicando la cantidad de aristas _A_.
    * Sucesivas líneas representando cada arista, en dónde se indican los vértices de origen y destino, separados por espacios. Sólo se listará una de las direcciones si el grafo es no dirigido.

### Implementación de los grafos

En general, recomendamos seguir un patrón de diseño parecido al de Robert Sedgewick en _Algorithms_ (2011, 4.ª ed.).

Se recomienda implementar un TAD Grafo inmutable de funcionalidad mínima, y en segundo lugar tres clientes para los algoritmos correspondientes.

El TAD Grafo mantendrá la mínima representación necesaria del grafo. En cuanto a los algoritmos, se recomienda realizar todo el trabajo de cada algoritmo en su propio constructor cuando corresponda (así, una vez inicializado, es inmutable y se convierte en un objeto de solo-consulta).

Como ejemplo en Python, el TAD Grafo podría plantearse así:
```python
class Digraph:
  """Grafo dirigido con un número fijo de vértices.
    
  Los vértices son siempre números enteros no negativos. El primer vértice es 0.
    
  El grafo se crea vacío, se añaden las aristas con add_edge(). Una vez
  creadas, las aristas no se pueden eliminar, pero siempre se pueden añadir
  nuevas aristas.
  """
  def __init__(g, V):
    """Construye un grafo sin aristas de V vértices.
    """
    
  def V(g):
    """Número de vértices en el grafo.
    """
    
  def E(g):
    """Número de aristas en el grafo.
    """
    
  def adj_e(g, v):
    """Itera sobre los aristas incidentes _desde_ v.
    """
    
  def adj(g, v):
    """Itera sobre los vértices adyacentes a 'v'.
    """
    
  def add_edge(g, u, v):
    """Añade una arista al grafo.
    """
    
  def __iter__(g):
    """Itera de 0 a V."""
    return iter(range(g.V()))
    
  def iter_edges(g):
    """Itera sobre todas las aristas del grafo.
    
    Las aristas devueltas tienen los siguientes atributos de solo lectura:
    
        • e.src
        • e.dst
    """
    
class Edge:
  """Arista de un grafo.
  """
  def __init__(self, src, dst):
    ...
```    

Como ejemplo en Java, los algoritmos podrían representarse así:
    
```java    
public interface ShortestPathAlgorithm {

    /**
     * Devuelve el camino mínimo entre dos vértices del grafo.
     *
     * @param   srcId   el id del vértice de origen.
     * @param   destId  el id del vértice de destino.
     * @return  una lista con los vértices que conforman el camino, incluyendo
     *          el origen y el destino.
     * @throws IllegalArgumentException si algún id de vértice es inválido.
     */
    public List getShortestPath(int src, int dest);
    
}

public class Dijkstra implements ShortestPathAlgorithm {

    public Dijkstra(Digraph d) { /* ... */ }
    
    /**
     * Aplica el algoritmo de Dijkstra para obtener el camino mínimo entre dos
     * vértices del grafo.
     *
     * @param   srcId   el id del vértice de origen.
     * @param   destId  el id del vértice de destino.
     * @return  una lista con los vértices que conforman el camino, incluyendo
     *          el origen y el destino.
     * @throws IllegalArgumentException si algún id de vértice es inválido.
     */
    @Override
    public List getShortestPath(int src, int dest) { /* ... */ }

}
```
