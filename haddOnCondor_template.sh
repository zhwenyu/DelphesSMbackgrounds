#!/bin/bash

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530

# Condor arguments
SAMPLE=$1
FILENAME=$2
OUTPUTDIR=$3

echo "Starting job on " `date`
echo "Running on " `uname -a`
echo "System release " `cat /etc/redhat-release`

scram project CMSSW_8_0_4
cd CMSSW_8_0_4/src
eval `scram runtime -sh`
cd -

hadd -f ${FILENAME} INSERTFILES 

HADDEXIT=$?
if [[ $HADDEXIT -ne 0 ]]; then
    echo "exit code $HADDEXIT, failure in hadding input files"
    exit $HADDEXIT
fi

xrdcp -f ${FILENAME} ${OUTPUTDIR}/${SAMPLE}/${FILENAME}

XRDCPEXIT=$?
if [[ $XRDCPEXIT -ne 0 ]]; then
    echo "exit code $XRDCPEXIT, failure in xrdcp of output file"
    rm *.root
    exit $XRDCPEXIT
fi

rm *.root