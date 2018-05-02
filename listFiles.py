import os,sys

samplelist = [
    '/DMScalar_top_tWChan_Mchi1_Mphi500_14TeV_madgraph/PhaseIISpr18AODMiniAOD-PU200_93X_upgrade2023_realistic_v5-v1/MINIAODSIM',
    '/DMScalar_top_tChan_Mchi1_Mphi10_14TeV_madgraph/PhaseIISpr18AODMiniAOD-noPU_93X_upgrade2023_realistic_v5-v1/MINIAODSIM',
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
