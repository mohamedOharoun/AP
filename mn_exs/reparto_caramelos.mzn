int: n;
array[1..n] of int: nota;
int: max_caramelos = 100000;
array[1..n] of var 1..max_caramelos: x;
var int: total_caramelos = sum(x);

constraint forall(i in 1..n, j in 1..n)(x[i] < 2*x[j]);
constraint forall(i in 2..n)(
    (nota[i] == nota[i-1] -> x[i] == x[i-1]) /\
    (nota[i] > nota[i-1] -> x[i] > x[i-1]) /\
    (nota[i] < nota[i-1] -> x[i] < x[i-1])
);

solve minimize total_caramelos;
output [show(total_caramelos)];
