#!/bin/bash
set -e
mkdir -p dados/brutos
for i in {1..30}; do mbw 16 | tee -a dados/brutos/mbw16.txt; done
for i in {1..30}; do mbw 128 | tee -a dados/brutos/mbw128.txt; done
for i in {1..30}; do mbw 1024 | tee -a dados/brutos/mbw1024.txt; done
