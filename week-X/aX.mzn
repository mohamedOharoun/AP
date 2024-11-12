int: n = 5;
array[1..n] of int: value = [3,10,3,1,2];

%Introduzca el código a partir de esta línea
array[1..n] of var 0..1 : taken;
array[1..n] of var int : temp;
var int : total_value;

constraint forall(i in 1..n-1) (taken[i] + taken[i+1] <= 1);
constraint taken[n] != taken[n-1];

constraint forall(i in 1..n) (temp[i] = taken[i] * value[i]);

constraint total_value = sum(temp);
solve maximize total_value;

output[ "taken = \(taken)\ntotal_value = \(total_value)" ];