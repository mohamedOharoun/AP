int:n; 
int: capacity; 
set of int: ITEMS = 1..n; 
array[ITEMS] of int: value; 
array[ITEMS] of int: weight;

output[ "taken = {\(taken)}" ];

output[ "\nTotal Value = \(valor)" ];

%Escribir el código a partir de aquí


var set of 1..n : taken;
var int : valor;

constraint capacity >= sum(i in taken)(weight[i]);

constraint valor = sum(i in taken) (value[i]);
solve maximize valor;