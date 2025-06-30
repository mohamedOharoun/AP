include "globals.mzn";

% Número de donantes/receptores
int: n;
set of int: PARTICIPANTS = 1..n;

% Enumerado para las categorías (colores)
enum COLOR = {Azul, Naranja, Verde, Rojo};

% Matriz fija de compatibilidad (4x4) para los colores
array[COLOR, COLOR] of int: compatibility = [|
    100,  50,  20,   0 | % Azul
     50, 100,   0,  70 | % Naranja
     20,   0, 100,  60 | % Verde
      0,  70,  60, 100 | % Rojo
|];

% Categorías de los donantes y receptores
array[PARTICIPANTS] of COLOR: donor_categories;
array[PARTICIPANTS] of COLOR: recipient_categories;

% ------------------------------------ Resuelve el ejercicio a partir de aqui
% Variable de decisión: asignación de donantes a receptores
array[PARTICIPANTS] of var PARTICIPANTS : assignments;

constraint alldifferent(assignments);

var int : total_compatibility = sum(p in PARTICIPANTS) (
    compatibility[donor_categories[p],  recipient_categories[assignments[p]]]
);

solve maximize total_compatibility;

% Salida
output [
    "Compatibilidad total: \(total_compatibility)\n",
    "Emparejamiento: \(assignments)"
];