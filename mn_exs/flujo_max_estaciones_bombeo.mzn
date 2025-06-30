% Problema del Flujo de Agua en un Sistema de Tuberías con Estaciones de Bombeo

% Número de puntos de conexión en el sistema
int: num_nodes;

% Número de tuberías en el sistema
int: num_edges;

% Fuente principal
int: source;

% Contenedor o depósito final
int: sink;

% Definición de las tuberías: [punto de entrada, punto de salida]
array[1..num_edges, 1..2] of int: edges;

% Capacidad de cada tubería en litros/segundo
array[1..num_edges] of int: capacity;

% Capacidad de manejo de las estaciones de bombeo. Usamos -1 para los puntos que no son estaciones.
array[1..num_nodes] of int: node_capacity;

% Salida
output
[
"max flow =" ++ show(max_flow)
];

% Variable de decisión que representa el flujo máximo que llega al contenedor
var int: max_flow;

% Variable de decisión que indica el volumen de agua en cada tubería
array[1..num_edges] of var int : flow;

% ------------------------------------ Resuelve el ejercicio a partir de aqui
constraint forall(eb in 1..num_nodes where eb != source /\ eb != sink) (
    sum(i in 1..num_edges where edges[i, 1] == eb) (flow[i]) ==
    sum(j in 1..num_edges where edges[j, 2] == eb) (flow[j])
);

constraint forall(t in 1..num_edges) (
    flow[t] >= 0 /\
    flow[t] <= capacity[t]
);

constraint forall(n in 1..num_nodes where node_capacity[n] != -1) (
    sum(i in 1..num_edges where edges[i, 2] == n) (flow[i]) <= node_capacity[n]
);

constraint max_flow = sum(i in 1..num_edges where edges[i, 2] == sink) (flow[i]);

solve maximize max_flow;
