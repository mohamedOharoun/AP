par int : budget = 10000;
var 0..1000 : F;
var 0..400 : L;
var 0..500 : Z;
var 0..150 : J;
var int : total_force;

constraint 13*F + 21*L + 17*Z + 100*J <= budget;
constraint total_force = 6*F + 10*L + 8*Z + 40*J;

solve maximize total_force;

output [ "F = \(F);\n L = \(L);\n Z = \(Z);\n J = \(J);" ]