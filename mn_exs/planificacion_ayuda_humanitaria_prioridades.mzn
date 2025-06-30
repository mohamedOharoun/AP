nclude "globals.mzn";

int: n;  % Número de envíos
int: k;  % Número de transportistas disponibles
int: t;  % Número de camiones disponibles

array[1..n] of int: durations;      % Duración de cada envío
array[1..n] of int: transportistas; % Transportistas necesarios para cada envío
array[1..n] of int: camiones;       % Camiones necesarios para cada envío
array[1..n] of int: priorities;     % Prioridad de cada envío

% Salida
output [
    "Tiempo total: \(show(total_time))\n",
    "\(show([start_times[i] | i in 1..n]))"
];

% ----------------------- Resuelve el ejercicio a partir de aqui
array[1..n] of var 0..sum(durations) : start_times;
var int : total_time;

constraint alldifferent(start_times);

constraint cumulative(start_times, durations, camiones, t);
constraint cumulative(start_times, durations, transportistas, k);

constraint forall(e in 1..n where priorities[e] == 1) (
    forall(e2 in 1..n where priorities[e2] == 2) (
        start_times[e] < start_times[e2]
    )
);

constraint total_time = max([start_times[i] + durations[i] | i in 1..n]);

solve minimize total_time;