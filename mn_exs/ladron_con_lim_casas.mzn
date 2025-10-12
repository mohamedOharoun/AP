int: n;
int: x;
array[1..n] of int: value;

% Introduce tu código a partir de esta línea -------------------------
output[ "taken = \(taken)" ];
output[ "\ntotal_value = \(total_value)" ];

array[1..n] of var 0..1 : taken;
var 0..sum(value) : total_value;

constraint forall(i in 2..n) (
    taken[i] + taken[i-1] <= 1
);

constraint sum(taken) <= x;

constraint total_value = sum(i in 1..n) (taken[i] * value[i]);

solve maximize total_value;