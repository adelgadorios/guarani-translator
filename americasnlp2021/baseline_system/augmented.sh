#!/bin/bash -l
#SBATCH -o std_out2
#SBATCH -e std_err2
#SBATCH --gpus=8  
conda activate translator
./run_baseline_system.sh gn ../../augmented-dataset augmented-results 100 -CLI
