% Problema de ubicación de instalaciones
%
% Este problema busca determinar en qué ubicaciones abrir instalaciones
% (facilidades) para satisfacer la demanda de un conjunto de clientes, 
% minimizando los costos totales.
%
% Los costos incluyen:
% - Costos de instalación de las facilidades.
% - Costos de transporte desde las facilidades hasta los clientes.
% 
% Dado:
% - Un conjunto de posibles ubicaciones para las facilidades.
% - Costos asociados con abrir cada facilidad.
% - Costos de transporte desde cada facilidad a cada cliente.
%
% Objetivo:
% Minimizar el costo total (instalación + transporte), asegurando que cada 
% cliente esté asignado a exactamente una facilidad abierta.
%
% Ejemplo de entrada:
% - 3 instalaciones posibles con costos de apertura [10000, 15000, 12000].
% - 4 clientes con costos de transporte dados por una matriz 3x4.
% 
% Salida:
% - Costo total mínimo.
% - Instalaciones abiertas.
% - Asignación de clientes a instalaciones.

int: n_facilities;  % Número de instalaciones posibles
int: n_clients;     % Número de clientes

set of int: Facilities = 1..n_facilities;
set of int: Clients = 1..n_clients;

array[Facilities] of int: installation_costs;
array[Facilities, Clients] of float: transportation_costs; 


% Variables
array[Facilities] of var 0..1: open; % 1 si se abre la instalación, 0 si no
array[Facilities, Clients] of var 0..1: assign; % 1 si un cliente es asignado a una instalación, 0 si no

output["total_cost=", show(total_cost), "\n"];
output["open=", show(open), "\n"];
output["assign=", show(assign), "\n"];

% ------------------------------------------- Resuelve el ejercicio aqui
var float: total_cost = sum(f in Facilities)(open[f] * installation_costs[f]) +
    sum(c in Clients, f in Facilities)(transportation_costs[f, c] * assign[f, c]);
solve minimize(total_cost);

constraint forall(c in Clients, f in Facilities where assign[f, c] == 1)(open[f] == 1);

constraint forall(c in Clients)(sum(f in Facilities)(assign[f,c]) == 1);