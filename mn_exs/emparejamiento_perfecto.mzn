% Perfect Match minimum cost

include "globals.mzn";

int: n;
set of int: VERTEX = 1..n;

array[VERTEX, VERTEX] of int: weights;

array[VERTEX] of var VERTEX: edge;

% Escribir el código a partir de aquí ---------
var int : total_weight;
constraint forall(v in VERTEX)(edge[edge[v]] == v);
constraint alldifferent(edge);
constraint total_weight = sum(v in VERTEX)(weights[v, edge[v]]) / 2;
solve minimize total_weight;

output [
  "\(total_weight) -> \(edge)"
];
