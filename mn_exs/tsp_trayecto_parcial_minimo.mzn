%TSP trayecto parcial mínimo

include "globals.mzn";
int: numCities;          % número de ciudades
set of int: City = 1..numCities; 
int: maxAllowedEdge;     % máxima distancia permitida de un trayecto del recorrido

% distancia entre ciudades 
% -1 significa que no hay conexión directa
array[City,City] of int: distance; 

% Introducir el codigo a partir de aqui ------------------------------------------
array[City] of var City: succ;
var int : maxEdge;

constraint circuit(succ);

constraint forall(c in City)(
distance[c, succ[c]] != -1 /\
distance[c, succ[c]] <= maxAllowedEdge
);
constraint maxEdge = max(c in City)(distance[c, succ[c]]);

solve minimize maxEdge;

output [
  "succ = \(succ)" ++
  "\nmaxEdge = \(maxEdge)" 
];