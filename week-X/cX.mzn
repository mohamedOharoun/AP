int:n; 
int: capacity; 
set of int: ITEMS = 1..n; 
array[ITEMS] of int: value; 
array[ITEMS] of int: weight;
array[ITEMS] of var 0..2 : taken;
%Escribir el código a partir de aquí
array[ITEMS] of var int : temp_w;
array[ITEMS] of var int : temp_v;
constraint forall(i in ITEMS) (temp_w[i] = weight[i] * taken[i]);
constraint forall(i in ITEMS) (temp_v[i] = value[i] * taken[i]);
constraint sum(temp_w) <= capacity;
solve maximize sum(temp_v);
output[ "taken = \(taken)\nTotal Value = \(sum(temp_v))" ];