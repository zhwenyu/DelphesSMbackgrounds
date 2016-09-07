#!/bin/bash

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530

# Condor arguments
INPUTDIR=$1
SAMPLE=$2
FILENAME=$3
OUTPUTDIR=$4

echo "Starting job on " `date`
echo "Running on " `uname -a`
echo "System release " `cat /etc/redhat-release`

xrdcp -f ${INPUTDIR}/${SAMPLE}/${FILENAME} ${OUTPUTDIR}/${SAMPLE}/

XRDEXIT=$?
if [[ $XRDEXIT -ne 0 ]]; then
    echo "exit code $XRDEXIT, failure in xrdcp of output file"
    exit $XRDEXIT
fi
