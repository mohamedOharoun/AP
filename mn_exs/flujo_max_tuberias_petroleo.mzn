% Parámetros del problema
% Problema de flujo máximo en una red de tuberías de petróleo

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

% Rango de presión operativa seguro: [presión minima, presión máxima]
array[1..num_edges, 1..2] of int: pressure_range;

% Presión base de cada tubería (presión mínima sin flujo)
array[1..num_edges] of int: base_pressure;

% Constante conocida
int: k;

% Variable de decisión que representa el flujo máximo que llega al contenedor
var int: max_flow;

% Variable de decisión que indica el volumen de agua en cada tubería
array[1..num_edges] of var 0..max(capacity): flow;

% Poner el código a partir de aquí ------------------------------------------
constraint forall(n in 1..num_nodes where n != source /\ n != sink) (
    sum(i in 1..num_edges where edges[i, 1] == n) (flow[i]) == 
    sum(j in 1..num_edges where edges[j, 2] == n) (flow[j])
);

constraint forall(t in 1..num_edges) (
    flow[t] <= capacity[t] /\
    flow[t] >= 0
);

constraint forall(t in 1..num_edges) (
    pressure_range[t,1] <= base_pressure[t] + k * flow[t] /\
    pressure_range[t,2] >= base_pressure[t] + k * flow[t]
);

max_flow = sum(t in 1..num_edges where edges[t, 2] == sink) (flow[t]);

solve maximize max_flow;

output[ "max_flow = \(max_flow);\n" ];
output[ "flow = \(flow);" ]
