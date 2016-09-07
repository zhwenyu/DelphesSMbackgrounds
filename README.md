# DelphesSMbackgrounds

----------------------------------------------------------

To SUBMIT condor jobs at the LPC:

voms-proxy-init -voms cms
python -u submitCondor.py <0,200>PU >& submit.log &

In this file, set output directories and choose samples

---------------------------------------------------------

EXECUTABLE: LHEtoDelphes.sh

No need to change this file! Can control card, number of events, etc, from here.
This script does xrdcp from EOS, runs Pythia, and runs Delphes. 

---------------------------------------------------------

To check output of jobs, edit CheckErrorsDelphes.py (check ROOT file directory path & month for zero size test)

python -u CheckErrorsDelphes.py /path/to/logs/ --pileup <0,200>PU --verbose <0,1> --resubmit <0,1> --resub_num <-1,0,1,2>

This will check for three types of failures (give as resub_num argument)

0. Explicit failure of xrdcp, printed in the log file

1. ROOT file in EOS with zero size. NOTE: have to hardcode the month expected in ls -l

2. No ROOT file with the expected name in EOS. NOTE: hardcode the path if its name differs from the log directory

-1 will resubmit all types of failures.

Logs can be deleted after jobs are successful.

--------------------------------------------------------

Post-processing scripts are available to hadd and xrdcp files

python -u haddOnCondor.py <0,200>PU

Set up to hadd files and copy to another LPC EOS directory. 

python -u xrdcpOnCondor.py <0,200>PU

Set up to xrdcp files from LPC EOS to CERN EOS.

