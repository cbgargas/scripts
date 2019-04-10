#!/bin/bash

for i in {1..100}; do
    echo "cd \$PBS_O_WORKDIR; ./iqtree -s decu-almt05.afa -spp decu-almt05-part.nex -o Eunotia_pectinalis_HK153 -nt 3 -pre iqtree_opt_${i} " > iq.script;
    # echo "cd \$PBS_O_WORKDIR; ./raxml --all --msa decussata_almt04.phy --threads 6 --model decu_almt03_partition.txt --prefix raxml_opt_${i} " > rax.script;
#    qsub -j oe -V -q debug16core -l nodes=1:ppn=3 -l walltime=1:00 iq.script;
    qsub -j oe -V -q tiny16core -l nodes=1:ppn=3 -l walltime=4:00:00 iq.script;
    # qsub -j oe -V -q med12core -l nodes=1:ppn=6 -l walltime=24:00:00 rax.script;
done


