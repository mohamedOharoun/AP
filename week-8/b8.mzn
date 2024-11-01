var 0..10 : x;
var int : obj;

constraint x mod 4 == 0;
constraint obj == (x-7)*(x-7);

solve minimize (x-7)*(x-7);

output[ "x=\(x)\nobj=\(obj)" ]