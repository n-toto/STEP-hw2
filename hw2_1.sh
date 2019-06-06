chmod u+x hw2_1.sh
#!/bin/sh
for i in `seq 1 $1`
do
    python3 hw2_1.py $(($i*10))
done