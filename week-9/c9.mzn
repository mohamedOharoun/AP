par int : n = 5;
array[1..n] of var 0..3 : seq;

constraint seq[1] = 0;
constraint seq[n] = 3;
constraint forall(i in 1..n-1)
    (seq[i] + seq[i+1] <= 3);
constraint forall(i in 1..n where i mod 3 == 0)
    (seq[i] >= 2);
solve maximize sum(seq);

output[ "x = \(seq)" ];
