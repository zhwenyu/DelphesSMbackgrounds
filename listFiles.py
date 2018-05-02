import os,sys

samplelist = [
    ## GEN samples as of May 2, 2018 (starting from creation date 2018-04-04                                                                                                                                       
    '/SUSYGluGluToHToTauTau_M-1600_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-350_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-2000_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-3200_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-250_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-600_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-450_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-2600_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-2300_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-900_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-2900_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-500_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-1800_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-1400_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-400_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-700_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-1000_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-1200_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-200_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-800_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/WW_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Mdijet-1000toInf_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Pt-15to7000_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Pt-15to7000_bcToE_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Pt-20to7000_EMEnriched_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUEP8M2T4_14TeV_Pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCDBBbar_Pt-15to7000_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUEP8M2T4_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DiPhotonJetsBox_MGG-40to80_14TeV-Sherpa/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    ]

if not os.path.exists(os.getcwd()+'/fileLists'): os.system('mkdir fileLists')

for sample in samplelist:
    print '------------------------------------------'
    print 'Listing',sample

    # print file list to a .txt                                                                              
    if '_ext' not in sample:
	      os.system('/cvmfs/cms.cern.ch/common/dasgoclient --limit=0 --query="file dataset = '+sample+'" > fileLists/'+sample.split('/')[1]+'.txt')
    else:
        os.system('/cvmfs/cms.cern.ch/common/dasgoclient --limit=0 --query="file dataset = '+sample+'" >> fileLists/'+sample.split('/')[1]+'.txt')

    # check if this sample is on a T2...                                                                     
    #os.system('/cvmfs/cms.cern.ch/common/dasgoclient --limit=0 --query="site dataset = '+sample+'"')        

    # print number of events                                                                                 
    #os.system('/cvmfs/cms.cern.ch/common/dasgoclient --limit=0 --query="dataset = '+sample+' | grep dataset.nevents" ')                       
