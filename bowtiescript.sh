#!/bin/bash

for x in ./*.txt
do
bowtie2 -a --norc -x Human_GeCKOv2_Library_A_09Mar2015 -r $x -S ${x/.txt/.wDups.sam}
done