# Modelo de Scouting Personalizable: 
### El modelo busca ofrecer a los clubes una manera sencilla de buscar jugadores de un determinado perfil filtrando por sus necesidades. 

## Filtros
#### Los filtros incluídos son: 

Valor de mercado,
Nacionalidad,
Liga,
Edad y
Minutos disputados.
Los mismos pueden variar según la liga, en el ejemplo básico el filtro de nacionalidad no se aplica a la LPF 2024 ya que es la liga en la que se encuentra el club desde el que realizamos la búsqueda. Se intuye que no habría inconvenientes relacionados con la nacionalidad en ese caso.

## Rosario Central y un caso ficticio
Suponiendo que Rosario Central quiere determinar una posición en la cual reforzarse, establece para cada perfil de jugador una serie de métricas que considera óptimas para evaluar su rendimiento. Entendiendo que no todas tienen la misma relevancia, asigna un peso particular para cada una. Entonces, luego de aplicar el modelo que será explicado luego recibe un mensaje como este:

### Percentiles de los mejores jugadores de mi equipo por posición (comparando con jugadores de la misma liga):
#### En la posición Defensa Central, el mejor jugador está en el percentil: 96.45%
#### En la posición Laterales, el mejor jugador está en el percentil: 84.71%
#### En la posición Volante Central, el mejor jugador está en el percentil: 89.29%
#### En la posición Volante Interior, el mejor jugador está en el percentil: 97.46%
#### En la posición Extremo, el mejor jugador está en el percentil: 73.64%
#### En la posición Delantero Centro, el mejor jugador está en el percentil: 74.29%

#### La posición donde el percentil del mejor jugador es más bajo es: Extremo (percentil 73.64%) POTENCIAL POSICIÓN A REFORZAR

De lo que se encarga esta parte del algoritmo, es determinar en que perfil o posición según los parámetros establecidos para cada una,, nuestro mejor jugador en dicha posición se encuentra más bajo en comparación con el resto. Para esto utilizamos percentiles en lugar de posiciones en un ranking ya que el número de jugadores por posición cambia notablemente.

Teniendo en cuenta los mismos parámetros para la evaluación de jugadores por perfil o puesto utilizados anteriormente y la aplicación de filtros según las necesidades del club, el algoritmo crea una lista con los cinco jugadores mejor rankeados por posición. 
