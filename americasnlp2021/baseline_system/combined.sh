#!/bin/bash -l
#SBATCH -o std_out3
#SBATCH -e std_err3
#SBATCH -p Quick 
#SBATCH --gpus=8  
conda activate translator
./run_baseline_system.sh gn ../../combined-dataset translations/combined-dataset-results 100 -CLI
