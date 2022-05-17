#!/bin/bash

module load cuda/11.4
module load anaconda/2020.11
source activate d2l
export PYTHONUNBUFFERED=1

/data/home/scv6728/run/FashionMMT/driver/run.sh