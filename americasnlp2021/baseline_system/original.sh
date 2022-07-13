#!/bin/bash -l
#SBATCH -o std_out
#SBATCH -e std_err
#SBATCH --gpus=8  
conda activate translator
./run_baseline_system.sh gn ../../original-dataset baseline-results 100 -CLI
