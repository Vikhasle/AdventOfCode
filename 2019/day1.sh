#!/bin/bash
part_one(){
    fuel=0
    while read p; do
        ((fuel +=  p/3 - 2))
    done < input1.txt
    echo $fuel
}

fuel(){
    mass=$1
    ((f=mass/3-2))
    if [ $f -le 0 ]; then
        echo 0
        return 1
    fi
    r=$(fuel $f)
    echo $((f+r))
}
part_two(){
    total_fuel=0
    while read p; do
        t=$(fuel p)
        ((total_fuel+= t))
    done < input1.txt
    echo $total_fuel
}
part_one
part_two