include "globals.mzn";

% Número de parcelas
int: N;

% Rango de las dosis permitidas
int: min_dosis = 1;
int: max_dosis = 30;

% Salida
output ["Dosis para cada parcela: \(dosis) suma =\(sum(dosis))"];

% ---------------------- Resuelve el ejercicio a partir de aqui
array[1..N] of var min_dosis..max_dosis : dosis;

constraint alldifferent(dosis);

constraint forall(i in 2..N-1) (
    dosis[i] != (dosis[i-1] + dosis[i+1]) div 2
);

var int : first_half = N div 2;
constraint forall(i in 1..first_half, j in (first_half + 1)..N) (
    dosis[i] < dosis[j]
);

solve minimize sum(dosis);
