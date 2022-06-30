#!/bin/bash -l
#SBATCH -o std_out
#SBATCH -e std_err
#SBATCH -p Quick 
#SBATCH --cpus-per-task=32 
#SBATCH --mem=100GB 
#SBATCH --gpus=8  
conda activate translator
./run_baseline_system.sh gn ../data/guarani-spanish augmented-data-set 200 -CLI
