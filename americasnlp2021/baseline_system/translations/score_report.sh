#!/bin/bash
lang_name=../../data/guarani-spanish
lang=gn
echo $lang_name
python ../../evaluate.py --system_output ${lang}_es/${lang}_es.hyp --gold_reference ${lang_name}/dev.${lang}
echo -----------------------------------
