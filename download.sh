#!/usr/bin/env bash                                                         #
#                                                                           #
# Author: John Sigmon                                                       #
# Created: 6/22/2018                                                        #
# Last modified: 6/25/2018                                                  #
#                                                                           #
#############################################################################
# Description                                                               #
############################################################################# 
# This script creates directories and downloads word embedding tests        #
# into these directories. There is not much logic, it checks if a           #
# directory is present, and if not it downloads the file, cleans up,        #
# and moves on to the next one. You must create or delete the appropriate   #
# directories to modify this process for your own purposes or to correct    #
# any errors.                                                               #
#############################################################################

# WS-353 Finkelstein et al 2002
DIR="WS-353"
if [ ! -d $DIR ]; then
    mkdir $DIR
    cd $DIR
    FILE="wordsim353"
    curl -o ${FILE}.zip "http://www.cs.technion.ac.il/~gabr/resources/data/wordsim353/wordsim353.zip"
    unzip ${FILE}.zip -d .
    rm -f ${FILE}.zip
    cd ../
fi

# Rare-Word Luong et al 2013
# https://nlp.stanford.edu/~lmthang/morphoNLM/
#DIR="Rare-Word"
#if [ ! -d $DIR ]; then
#    mkdir $DIR
#    cd $DIR
#    FILE="rw"
#    curl -o ${FILE}.zip "http://www-nlp.stanford.edu/~lmthang/morphoNLM/rw.zip"
#    unzip ${FILE}.zip -d .
#    rm -f ${FILE}.zip
#    cd ../
#fi

# MEN Test Collection Elia Bruni 2012
# http://clic.cimec.unitn.it/~elia.bruni/MEN.html
DIR="MEN"
if [ ! -d $DIR ]; then
    mkdir $DIR
    cd $DIR
    FILE="MEN"
    curl -o ${FILE}.tar.gz "http://clic.cimec.unitn.it/~elia.bruni/resources/MEN.tar.gz"
    tar -xf ${FILE}.tar.gz
    rm -f ${FILE}.zip
    cd ../
fi

# MTurk 771 Word Relatedness Halawi, Dror 2012
# http://www2.mta.ac.il/~gideon/mturk771.html 
DIR="MTurk"
if [ ! -d $DIR ]; then
    mkdir $DIR
    cd $DIR
    FILE_1="MTURK"
    FILE_2="MTURK_RAW"
    curl -o ${FILE_1}.csv "http://www2.mta.ac.il/~gideon/datasets/MTURK-771.csv"
    curl -o ${FILE_2}.csv "http://www2.mta.ac.il/~gideon/datasets/MTURK-771-RAW.csv" 
    cd ../
fi

# SimLex-999
# http://www.cl.cam.ac.uk/~fh295/simlex.html# 
DIR="SimLex"
if [ ! -d $DIR ]; then
    mkdir $DIR
    cd $DIR
    FILE="simlex"
    curl -o ${FILE}.zip "http://www.cl.cam.ac.uk/~fh295/SimLex-999.zip"
    unzip ${FILE}.zip -d .
    rm -f ${FILE}.zip
    cd ../
fi

