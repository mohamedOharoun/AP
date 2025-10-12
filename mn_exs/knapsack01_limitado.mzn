int:n;                    % numero maximo de items
int: capacity;            % capacidad de la mochila

set of int: ITEMS = 1..n; 
array[ITEMS] of int: value; 
array[ITEMS] of int: weight;

set of ITEMS: limitation;
int:m;                    % Numero maximo de items a elegir dentro del 
                          % conjunto limitation

% Escribe el código a partir de aquí ----------------------------------
var set of 1..n : taken;
var 0..sum(value) : total_value;

constraint total_value = sum(i in taken) (value[i]);

constraint sum(i in taken where i in limitation)(1) <= m;

constraint sum(i in taken)(weight[i]) <= capacity;

solve maximize total_value;

output[ "\(taken)" ];
output[ "\n\(total_value)" ];
