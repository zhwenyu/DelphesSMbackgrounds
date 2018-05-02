# DelphesSMbackgrounds

These scripts facilitate submitting HTCondor jobs that process a defined set of LHE or GEN input files through Delphes tag 3.4.2pre05 on the FNAL LPC cluster. Changes to the input file name structure, Delphes tag, or cluster will require edits.

To create a new Delphes area: https://twiki.cern.ch/twiki/bin/view/CMS/DelphesUPG
If running on LHE: compile DelphesPythia8 and copy configLHE_jetmatchning.cmnd into the delphes directory before creating a tarball.

LHE-input scripts: submitCondor.py, LHEtoDelphes.sh

GEN-input scripts: submitCondor_gen.py, GENtoDelphes.sh

CHECK ALL YOUR SCRIPTS BEFORE RUNNING, MAKE NO ASSUMPTIONS!

----------------------------------------------------------

To SUBMIT condor jobs at the LPC:

voms-proxy-init -voms cms
python -u submitCondor_gen.py <0,200>PU >& submit.log &

*In this file, set output directories and choose samples*

---------------------------------------------------------

EXECUTABLE: LHEtoDelphes.sh, GENtoDelphes.sh

Check CMSSW releases and locations of tarball and minBias file, they are not arguments.
Can control card, number of events, etc, from here.
This script does xrdcp from EOS, runs Pythia, and runs Delphes. 

*NOTE: check which minBias file your delphes card is set to use!! Re-tar after any card edits.*

---------------------------------------------------------

To check output of jobs, edit CheckErrorsDelphesGEN.py (check ROOT file directory path & month for zero size test)

python -u CheckErrorsDelphes.py /path/to/logs/ --pileup <0,200>PU --verbose <0,1> --resubmit <0,1> --resub_num <-1,0,1,2,3>

*Note: the final slash on the log file directory path is important*

This will check for four types of failures (give as resub_num argument)

0. Explicit failure of xrdcp, printed in the log file

1. Job went over the 2-day walltime limit on the LPC cluster

1. ROOT file in EOS with zero size. NOTE: have to hardcode the month expected in ls -l

2. No ROOT file with the expected name in EOS. NOTE: hardcode the path if its name differs from the log directory

-1 will resubmit all types of failures.

Logs can be deleted after jobs are successful.

--------------------------------------------------------

Post-processing scripts are available to hadd and xrdcp files

*CAUTION, as of May 2018 there is trouble copying to CERN, check with Julie for updates*

python -u haddOnCondor.py <0,200>PU

Set up to hadd files and copy to another LPC EOS directory. 

python -u xrdcpOnCondor.py <0,200>PU

Set up to xrdcp files from LPC EOS to CERN EOS.

