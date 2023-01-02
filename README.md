# Guarani Translator
## Independent study performed at the Univeristy of South Florida with the assistance and guidance of Dr. Zacariah Beasley

Guarani is one of the two native languages of Paraguay; it is spoken by over seven million people in Praguay and has a rich history that dates back even before the Spanish Conquistadors landed in South America in the late 1400s. As of now there is no way for someone to translate this language without the help of a native speaker. As of today, there exists no translator that can be used by the public both in Paraguay and the rest of the world. The Paraguayan Government is reluctant towards creating the proper resources for Guarani even though over 90% of the Paraguayan population speaks it.
My project consists on creating an open-source Guarani translator that would be available to the public through both a website and mobile apps. 

## Conda Environment Setup
- conda create --name guarani
- conda activate guarani
- conda install -c conda-forge fairseq 
- conda install -c conda-forge sentencepiece 
- conda install -c anaconda cudatoolkit
- conda install -c conda-forge nvidia-apex
- conda install -c conda-forge tensorflow
- pip install tensorflow-io

## Run Training
- cd guarani-translator/americasnlp2021/baseline_system
- sbatch subset_name.sh

## Data Sources
- Uruguay Team's GitHub: https://github.com/sgongora27/giossa-gongora-guarani-2021
- Guaraní: Chiruzzo, L., Amarilla, P., Ríos, A., & Lugo, G. G. (2020, May). Development of a Guarani-Spanish Parallel Corpus. In Proceedings of The 12th Language Resources and Evaluation Conference (pp. 2629-2633).

- Uruguay Team's Research Document: https://aclanthology.org/2021.americasnlp-1.16/

- Helsinki Team's Github: https://github.com/AmericasNLP/americasnlp2021

- Helsinki Team's Research Document: https://aclanthology.org/2021.americasnlp-1.29.pdf
