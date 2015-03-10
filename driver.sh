clear
echo "##pypy"
time pypy speedtest.py

echo
echo -e "----\n"
echo "##pypy3"
time pypy3 speedtest.py


echo
echo -e "----\n"
echo "##python3"
time python3 speedtest.py

echo
echo -e "----\n"
echo "##python2"
time python2.7 speedtest.py

echo
echo -e "----\n"
echo "##python3 Ofast"
time ./Python-3.5.0a2/python.exe speedtest.py

echo
echo -e "----\n"
echo "build cython extension"

echo
echo -e "----\n"
echo "##run cython build extension python"
rm -f *.so
rm -f *.c
python3 setup.py build_ext --inplace > /dev/null 2> /dev/null
time python3 speedtestcython.py

echo
echo -e "----\n"
echo "##go run"
time go run speedtest.go

echo
echo -e "----\n"
echo "##go run compiled speedtest"
go build speedtest.go
time ./speedtest
