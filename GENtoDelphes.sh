#!/bin/bash

#################################### Wrapper submit script for Upgrade production 
#Written by Alexis Kalogeropoulos - July 2014
#Adapted by Julie Hogan - summer 2016, jmhogan@fnal.gov

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc530

startTime=`date +%s`

# Condor arguments
# Arguments = %(FILEIN)s %(OUTPUTDIR)s/%(RELPATH)s_%(PILEUP)s %(FILEOUT)s.root %(PILEUP)s
FILEIN=$1
OUTPUT=$2
FILEOUT=$3
PILEUP=$4

echo "Starting job on " `date`
echo "Running on " `uname -a`
echo "System release " `cat /etc/redhat-release`

# Set variables
runEvents=-1
skipEvents=0
detCard=CMS_PhaseII_${PILEUP}_v02.tcl
energy=14
DelphesVersion=tags/3.4.2pre07
nPU=`echo $detCard | cut -d '_' -f 2 | cut -d '.' -f 1`
process=`echo $FILEIN | cut -d '_' -f 1-2`
configuration=`echo $detCard | cut -d '_' -f 1-2`
DelphesOutput=CMSP2_${nPU}_`echo $FILEIN`.root

# make the CMSSW release, compile, and copy
scram project CMSSW_9_1_0_pre3
cd CMSSW_9_1_0_pre3/src
eval `scram runtime -sh`
cd -

echo "xrdcp source tarball and pileup file"
xrdcp -f root://cmseos.fnal.gov//store/user/snowmass/DelphesSubmissionLPCcondor/Delphes342pre07.tar . #CHECK ME!
XRDEXIT=$?
if [[ $XRDEXIT -ne 0 ]]; then
    echo "exit code $XRDEXIT, failure in xrdcp of Delphes.tar"
    exit $XRDEXIT
fi

tar -xf Delphes342pre07.tar
cd delphes
#./configure
#make -j 4

xrdcp -f root://cmseos.fnal.gov//store/user/snowmass/DelphesSubmissionLPCcondor/MinBias_100k.pileup .
XRDEXIT=$?
if [[ $XRDEXIT -ne 0 ]]; then
    echo "exit code $XRDEXIT, failure in xrdcp of MinBias_100k.pileup"
    exit $XRDEXIT
fi

echo "xrdcp input miniAOD"
# filein should already be in root://eoscms.cern.ch//store/mc/... format
xrdcp -f ${FILEIN} delphesinput.root
XRDEXIT=$?
if [[ $XRDEXIT -ne 0 ]]; then
    echo "exit code $XRDEXIT, failure in xrdcp of LHE file"
    exit $XRDEXIT
fi

setupTime=`date +%s`

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#run MiniAOD through Delphes

./DelphesCMSFWLite cards/CMS_PhaseII/$detCard ${FILEOUT} delphesinput.root
if [ $? -ne 0 ]; then
    exit 16
fi

DelphesTime=`date +%s`

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#metadata

echo "User: " `eval whoami`
echo "Date: " `date` 
echo 

echo "Process: " $process 
echo "Pileup Conditions: " $nPU 
echo "Configuration: " $configuration 
echo "Energy: " $energy 
echo 

echo "Input MiniAOD: " $FILEIN 
echo "Input Events: " $nEventsIn 
echo 

echo "Delphes Output: " $FILEOUT
echo "Delphes Version: " $DelphesVersion 
echo "Detector Card: " $detCard 
echo 

echo "Minutes spent setting up job: " `expr $setupTime / 60 - $startTime / 60` 
echo "Minutes spent running Delphes: " `expr $DelphesTime / 60 - $setupTime / 60` 
echo 

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# copy output to eos
echo "xrdcp -f ${DelphesOutput} ${eosOutDir}/${DelphesOutput}"
xrdcp -f ${FILEOUT} root://cmseos.fnal.gov/${OUTPUT}/${FILEOUT} 2>&1
XRDEXIT=$?
if [[ $XRDEXIT -ne 0 ]]; then
    echo "exit code $XRDEXIT, failure in xrdcp of ROOT"
    exit $XRDEXIT
fi

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
endTime=`date +%s`
echo "Time spent copying output (s): " `expr $endTime - $DelphesTime`
echo "Total runtime (m): " `expr $endTime / 60 - $startTime / 60`

echo "removing inputs from condor"
rm -f ${FILEOUT}
rm -f ../Delphes342pre07.tar *.root MinBias_100k.pileup
