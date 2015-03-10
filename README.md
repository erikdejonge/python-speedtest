# python-speedtest
Python vs Golang vs Pypy vs Cython



pypy
1 2 3 4 5 6 7 8 9 10 ()

real	0m0.407s
user	0m0.160s
sys	0m0.046s

----
pypy3
1 2 3 4 5 6 7 8 9 10 

real	0m0.482s
user	0m0.190s
sys	0m0.066s

----
python3
1 2 3 4 5 6 7 8 9 10 

real	0m1.829s
user	0m1.757s
sys	0m0.025s

----
python2
1 2 3 4 5 6 7 8 9 10 ()

real	0m0.916s
user	0m0.867s
sys	0m0.019s

----
python3 Ofast
1 2 3 4 5 6 7 8 9 10 

real	0m1.698s
user	0m1.661s
sys	0m0.012s

----
build cython extension

----
run cython build extension python
1 2 3 4 5 6 7 8 9 10 

real	0m0.065s
user	0m0.054s
sys	0m0.009s

----
go run
0 1 2 3 4 5 6 7 8 9 

real	0m0.370s
user	0m0.125s
sys	0m0.078s

----
Go run builded speedtest
0 1 2 3 4 5 6 7 8 9 

real	0m0.015s
user	0m0.013s
sys	0m0.002s
