
[Source](https://algoritmos-rw.github.io/tda/tp1/ "Permalink to Teoría de Algoritmos I")

# Teoría de Algoritmos I

El trabajo práctico consiste en las tres partes que se listan a continuación.

Lineamientos básicos:

* el trabajo se realizará en grupos de tres personas.
* la fecha de entrega es el **lunes 24 de abril de 2017**. Se debe entregar en el horario de clase en papel (informe + `código en monoespacio`), más una entrega en digital de código (.zip) e informe (.pdf) al correo de entregas del curso: `tps.7529rw@gmail.com`.
* el lenguaje de implementación es libre, pero se debe comunicar por correo en caso de _no_ ser uno de: C, Python, Java, JavaScript, Ruby.

## Contenidos

### Asignación de residencias

El 5 de abril, miles de estudiantes de medicina rendirán el Examen de Concurso de la Ciudad de Buenos Aires para llevar a cabo residencias y concurrencias durante los próximos años. En este contexto, decenas de hospitales publican un número de vacantes por especialidad en las que admiten residentes.

Definimos el problema de asignación genérico de residencias de la siguiente manera: sean _n_ estudiantes que desean llevar a cabo sus residencias en alguna de las _l_ especialidades dictadas por los _m_ hospitales públicos de una determinada ciudad. Cada hospital para cada especialidad posee una cantidad _q~ij~_ de vacantes.

Suponer que cada uno de los estudiantes tiene un listado de preferencias de tamaño _l*m_ en donde se contemplan todas las especialidades de todos los hospitales, y que a su vez los resultados del examen permiten a cada hospital establecer una orden de mérito para cada especialidad.

Se pide:

1. Considerando la simplificación de que no existan especialidades, implementar un programa que genere instancias aleatorias del problema dados los parámetros _n_ (cantidad de aplicantes) y _m_ (cantidad de hospitales). Este deberá generar: 
    * Un arreglo E de _n_ listas de tamaño _m_ que representan las preferencias de cada estudiante.
    * Un arreglo H de _m_ listas de tamaño _n_ que representan el orden de mérito para cada hospital.
    * Un arreglo Q de tamaño _m_ que modele la cantidad de vacantes de cada hospital. Los problemas deben ser exportados a un archivo cuya estructura está descripta al final de la presente consigna.
2. Reducir el problema simplificado de la asignación genérica de residencias al problema de los matrimonios estables descriptos en la bibliografía.
3. Implementar un algoritmo que resuelva el problema simplificado.
4. Simular la ejecución del algoritmo ante entradas generadas aleatoriamente con 
    1. _n_ = _m_ = 100
    2. _n_ = _m_ = 1000
    3. _n_ = _m_ = 10000
    4. _n_ = _m_ = 100000
5. Extraer breves conclusiones (máximo dos párrafos) sobre el rendimiento del algoritmo ante diferentes tamaños de la entrada comparándolo con su complejidad computacional.

### Puntos de falla

En un intento para mejorar el servicio de luz para el verano del año 2018, se quiere proteger el servicio eléctrico. Para ello, se notó que existen ciertos generadores que son muy importantes para la red y muy propensos a fallas.

Dado un modelo de la red como un grafo no dirigido, se propone aplicar los conocimientos adquiridos en la materia para identificar aquéllos nodos que son más frágiles, debido a que su baja generaría la desconexión del circuito.

Se pide:

1. Implementar el algoritmo de Hopcroft y Tarjan para encontrar puntos de articulación en grafos.
2. Importar los [archivos provistos por el curso][1] y ejecutar el algoritmo para encontrar la cantidad de nodos frágiles de la red.
3. Escribir un breve informe (máximo tres párrafos) comentando el funcionamiento del algoritmo.
4. Extraer breves conclusiones (máximo dos párrafos) sobre el rendimiento del algoritmo ante diferentes tamaños de la entrada comparándolo con su complejidad computacional.

### Comunidades en redes

Un grupo de científicos de datos propuso estudiar el comportamiento de los usuarios de una dada red social en la que no todas las relaciones son simétricas (es decir, el usuario _a_ no necesariamente es amigo del _b_ cuando _b_ es amigo de _a_).

Se sospecha que las relaciones entre las comunidades es tan fuerte que se pueden identificar usando un simple algoritmo de componentes fuertemente conexas.

Se pide:

1. Implementar el algoritmo de Kosaraju para encontrar las componentes fuertemente conexas en grafos dirigidos.
2. Importar los [archivos provistos por el curso][2] y ejecutar el algoritmo para encontrar la cantidad de componentes fuertemente conexas en la red.
3. Escribir un breve informe (máximo tres párrafos) comentando el funcionamiento del algoritmo.
4. Extraer breves conclusiones (máximo dos párrafos) sobre el rendimiento del algoritmo ante diferentes tamaños de la entrada comparándolo con su complejidad computacional.

## Aclaraciones generales

1. El informe de todo el trabajo no debe superar dos carillas de extensión, y deberá incluir las instrucciones para ejecutar todos los programas desarrollados.
2. Para la implementación de los algoritmos se podrán usar todo tipo de bibliotecas, excepto de grafos.
3. El archivo que describe la instancia del problema de la asignación de residencias deberá tener el siguiente formato: 
    * Una línea con el número _n_ de estudiantes.
    * _n_ líneas consecutivas que expresen las preferencias de cada estudiante, separados por espacios.
    * Una línea con el número _m_ de hospitales.
    * _m_ líneas consecutivas que expresen el orden de mérito de cada hospital, separados por espacios.
    * Una línea que contenga la cantidad de vacantes de cada uno de los _m_ hospitales, separados por espacios.
4. Los grafos serán provistos en el formato propuesto por Sedgewick, en donde los vértices estarán nombrados según indentificadores desde 0 hasta _V-1_, y los archivos de entrada están armados según: 
    * Una primera línea indicando la cantidad de vértices _V_.
    * Una segunda línea indicando la cantidad de aristas _A_.
    * Sucesivas líneas representando cada arista, en dónde se indican los vértices de origen y destino, separados por espacios. Sólo se listará una de las direcciones si el grafo es no dirigido.

### Implementación de los grafos

En general, recomendamos seguir un patrón de diseño parecido al de Robert Sedgewick en _Algorithms_ (2011, 4.ª ed.).

Se recomienda implementar un TAD Grafo inmutable de funcionalidad mínima, y en segundo lugar dos clientes para los algoritmos correspondientes.

El TAD Grafo mantendrá la mínima representación necesaria del grafo. En cuanto a los algoritmos, se recomienda realizar todo el trabajo de cada algoritmo en su propio constructor (así, una vez inicializado, es inmutable y se convierte en un objeto de solo-consulta).

Como ejemplo en Python, el TAD Grafo podría plantearse así:
    
    
    class Digraph:
      """Grafo dirigido con un número fijo de vértices.
    
      Los vértices son siempre números enteros no negativos. El primer vértice
      es 0.
    
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
    

Como ejemplo en Java, los algoritmos podrían representarse así:
    
    
    public class Kosaraju {
    
        private List> stronglyConnectedComponents;
    
        public Kosaraju(Digraph d) { /* ... */ }
    
        /**
         * Devuelve el número de componentes fuertemente conexas del grafo.
         * @return  El número de componentes fuertemente conexas.
         */
        public int getSCCNumber() { /* ... */ }
    
        /**
         * Devuelve un conjunto de vértices que pertenecen a la componente fuertemente
         *     conexa cuyo número es pasado por parámetro.
         * @param sccId   El número de componente fuertemente conexa.
         * @return        El conjunto de vértices que forman parte de la componente.
         * @throws IllegalArgumentException si no se cumple que {@code 0 <= sccId < getSCCNumber()}
         */
        public Set getMembersOfSCC(int sccId) { /* ... */ }
    
    }
    
    public class Tarjan {
    
        private Set articulationPoints;
    
        public Tarjan(Graph g) { /* ... */ }
    
        /**
         * Devuelve el conjunto de vértices que son puntos de articulación del grafo.
         * @return   El conjunto de vértices que son puntos de articulación.
         */
        public Set getArticulationPoints()  { /* ... */ }
    }
    

[1]: https://drive.google.com/drive/folders/0B0x0VPz_v-f_ZWJTdmVZcG9vY0k
[2]: https://drive.google.com/drive/folders/0B0x0VPz_v-f_MDdldkduZ3BwSDA
