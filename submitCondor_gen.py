#### python -u submitCondor_gen.py 200PU >& submit.log &

import os,datetime,time,subprocess
runDir=os.getcwd()

os.system('xrdcp -f root://cmseos.fnal.gov//store/user/snowmass/DelphesSubmissionLPCcondor/scripts/EOSSafeUtils.py '+runDir)
execfile(runDir+'/EOSSafeUtils.py')

start_time = time.time()

#IO directories must be full paths
pileup = str(sys.argv[1])
outputDir='/store/user/snowmass/noreplica/YR_Delphes_prod-luca-split/Delphes342pre14_split/' # CHANGE ME
## outputDir='/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre14/'  ## For CERN condor
## outputDir='/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre14/' ## For DESY (gfal prefix??? See line 52)
condorDir='/uscms/home/lcadamur/nobackup/Delphes342pre14_split_logs/' # Change username, helps to match log directory to the ROOT file directory, adding "_logs" (for compatibility with error checker)

cTime=datetime.datetime.now()

#outDir=outputDir[10:]

maxEvtsPerJob = 20000 ## -1 --> do not make splitting (1 job per file)
# maxEvtsPerJob = -1 ## -1 --> do not make splitting (1 job per file)

print 'Getting proxy'
proxyPath=os.popen('voms-proxy-info -path')
proxyPath=proxyPath.readline().strip()

print 'Starting submission'
count=0

fileList = [  # CHOOSE SAMPLES, you MUST have listed the file names with listFiles.py
    'GluGluToHHTo2B2G_node_2_14TeV-madgraph.txt',
    'GluGluToHHTo2B2G_node_SM_14TeV-madgraph.txt',
    'GluGluToHHTo2B2Tau_node_2_14TeV-madgraph.txt',
    'GluGluToHHTo2B2VTo2L2Nu_node_2_14TeV-madgraph.txt',
    'GluGluToHHTo2B2VTo2L2Nu_node_SM_14TeV-madgraph.txt',
    'GluGluToHHTo4B_node_2_14TeV-madgraph.txt',
    'GluGluToHHTo4B_node_SM_14TeV-madgraph.txt',
    ######
    # 'RSGluonToTTbar_M3000_TuneCUEP8M1_14TeV_pythia8.txt',
    # 'RSGluonToTTbar_M4000_TuneCUEP8M1_14TeV_pythia8.txt',
    # 'ST_FCNC-TA_Tleptonic_kappa_act-Madgraph5-pythia8.txt',
    # 'ST_FCNC-TA_Tleptonic_kappa_aut-Madgraph5-pythia8.txt',
    # 'ST_FCNC-TH_Thadronic_HToaa_eta_hct-MadGraph5-pythia8.txt',
    # 'ST_FCNC-TH_Thadronic_HToaa_eta_hut-MadGraph5-pythia8.txt',
    # 'ST_FCNC-TH_Tleptonic_HToWWZZtautau_eta_hct-MadGraph5-pythia8.txt',
    # 'ST_FCNC-TH_Tleptonic_HToWWZZtautau_eta_hut-MadGraph5-pythia8.txt',
    # 'ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8.txt',
    # 'ST_FCNC-TH_Tleptonic_HToaa_eta_hut-MadGraph5-pythia8.txt',
    # 'ST_FCNC-TH_Tleptonic_HTobb_eta_hct-MadGraph5-pythia8.txt',
    # 'ST_FCNC-TH_Tleptonic_HTobb_eta_hut-MadGraph5-pythia8.txt',
    # 'ST_FCNC-T_Tleptonic_kappa_gct-MadGraph5-pythia8.txt',
    # 'ST_FCNC-T_Tleptonic_kappa_gut-MadGraph5-pythia8.txt',
    # 'SingleLQ3ToTauB_5f_madgraph_LO_pair-M500.txt',
    # 'SingleLQ3ToTauB_5f_madgraph_LO_pair-M1000.txt',
    # 'SingleLQ3ToTauB_5f_madgraph_LO_pair-M1500.txt',
    # 'SingleLQ3ToTauB_5f_madgraph_LO_pair-M2000.txt',
    # 'SingleLQ3ToTauB_5f_madgraph_LO_pair-M2500.txt',
    ###
    # 'SingleLQ3ToTauB_5f_madgraph_LO_s-channel-M500.txt',
    # 'SingleLQ3ToTauB_5f_madgraph_LO_s-channel-M1000.txt',
    # 'SingleLQ3ToTauB_5f_madgraph_LO_s-channel-M1500.txt',
    # 'SingleLQ3ToTauB_5f_madgraph_LO_s-channel-M2000.txt',
    # 'SingleLQ3ToTauB_5f_madgraph_LO_s-channel-M2500.txt',
    # 'SingleLQ3ToTauB_5f_madgraph_LO_t-channel-M500.txt',
    # 'SingleLQ3ToTauB_5f_madgraph_LO_t-channel-M1000.txt',
    # 'SingleLQ3ToTauB_5f_madgraph_LO_t-channel-M1500.txt',
    # 'SingleLQ3ToTauB_5f_madgraph_LO_t-channel-M2000.txt',
    # 'SingleLQ3ToTauB_5f_madgraph_LO_t-channel-M2500.txt',
    # 'TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-10_TuneCUETP8M1_14TeV-madgraph-pythia8.txt',
    # 'TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-20_TuneCUETP8M1_14TeV-madgraph-pythia8.txt',
    # 'TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-50_TuneCUETP8M1_14TeV-madgraph-pythia8.txt',
    # 'TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-100_TuneCUETP8M1_14TeV-madgraph-pythia8.txt',
    # 'TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-200_TuneCUETP8M1_14TeV-madgraph-pythia8.txt',
    # 'TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-300_TuneCUETP8M1_14TeV-madgraph-pythia8.txt',
    # 'TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-500_TuneCUETP8M1_14TeV-madgraph-pythia8.txt',
    # 'TTbarDMJets_DiLept_scalar_NLO_Mchi-1_Mphi-10_TuneCUETP8M1_14TeV-madgraph-pythia8.txt',
    # 'TTbarDMJets_DiLept_scalar_NLO_Mchi-1_Mphi-20_TuneCUETP8M1_14TeV-madgraph-pythia8.txt',
    # 'TTbarDMJets_DiLept_scalar_NLO_Mchi-1_Mphi-50_TuneCUETP8M1_14TeV-madgraph-pythia8.txt',
    # 'TTbarDMJets_DiLept_scalar_NLO_Mchi-1_Mphi-100_TuneCUETP8M1_14TeV-madgraph-pythia8.txt',
    # 'TTbarDMJets_DiLept_scalar_NLO_Mchi-1_Mphi-200_TuneCUETP8M1_14TeV-madgraph-pythia8.txt',
    # 'TTbarDMJets_DiLept_scalar_NLO_Mchi-1_Mphi-300_TuneCUETP8M1_14TeV-madgraph-pythia8.txt',
    # 'TTbarDMJets_DiLept_scalar_NLO_Mchi-1_Mphi-500_TuneCUETP8M1_14TeV-madgraph-pythia8.txt',
    ]

for sample in fileList:

    rootlist = open('fileLists/'+sample)
    rootfiles = []
    rootfiles_bare = []
    for line in rootlist:
        rootfiles.append('root://cmsxrootd.fnal.gov/'+line.strip())  ## Can change to whatever is normal for running @ CERN
        rootfiles_bare.append(line.strip())
        # OPTIONAL: use a more exact accessor for certain samples at CERN:
        #if(sample != 'WprimeToWZToWhadZinv_narrow_M-600_13TeV-madgraph.txt'): rootfiles.append('root://eoscms.cern.ch/'+line.strip())
        #else: rootfiles.append('root://cmsxrootd.fnal.gov/'+line.strip())
    rootlist.close()

    relPath = sample.replace('.txt','')
    #print 'relPath =',relPath

    os.system('eos root://cmseos.fnal.gov/ mkdir -p '+outputDir+relPath+'_'+pileup)
    ## os.system('eos root://eoscms.cern.ch/ mkdir -p '+outputDir+relPath+'_'+pileup) # For running @ CERN
    ## os.system('gfal-mkdir -p srm://dcache-se-cms.desy.de/pnfs/desy.de/cms/tier2'+outputDir+relPath+'_'+pileup) ## DESY???
    os.system('mkdir -p '+condorDir+relPath+'_'+pileup)
    
    tempcount = 0;
    for ifile, file in enumerate(rootfiles):
        infile = file

        tempcount+=1

        # print file
        # print rootfiles_bare[ifile]
        fname_bare = rootfiles_bare[ifile]
        n_jobs = 1
        if maxEvtsPerJob > -1: ## just query DAS if necessary
            command = '/cvmfs/cms.cern.ch/common/dasgoclient --query="file='+fname_bare+' | grep file.nevents" '
            proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
            (out, err) = proc.communicate()
            try: nevents = int(out.split('\n')[0])
            except:
                try: nevents = int(out.split('\n')[1])
                except: print 'ERROR: couldnt isolate the number of events'
            # print fname_bare
            # print "num files: ", nevents
            # print ""
            # if tempcount > 1: continue   # OPTIONAL to submit a test job
            n_jobs = int(nevents) / int(maxEvtsPerJob)
            if int(nevents) % int(maxEvtsPerJob) > 0:
                n_jobs += 1 ## and extra one to account for the remainder

        ### split based on the number of events
        for i_split in range(n_jobs):
            
            count+=1
            ### usual submitter if no splitting
            if not maxEvtsPerJob > -1:
                outfile = relPath+'_'+str(tempcount)

                dict={'RUNDIR':runDir, 'RELPATH':relPath, 'PILEUP':pileup, 'FILEIN':infile, 'FILEOUT':outfile, 'PROXY':proxyPath, 'OUTPUTDIR':outputDir}
                jdfName=condorDir+'/%(RELPATH)s_%(PILEUP)s/%(FILEOUT)s.jdl'%dict
                # print jdfName
                jdf=open(jdfName,'w')
                jdf.write(
                    """x509userproxy = %(PROXY)s
universe = vanilla
Executable = %(RUNDIR)s/GENtoDelphes.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
Output = %(FILEOUT)s.out
Error = %(FILEOUT)s.err
Log = %(FILEOUT)s.log
Notification = Never
Arguments = %(FILEIN)s %(OUTPUTDIR)s/%(RELPATH)s_%(PILEUP)s %(FILEOUT)s.root %(PILEUP)s

Queue 1"""%dict)
            else:
                outfile = relPath+'_'+str(tempcount)+'_'+str(i_split)
                maxEvents = int(maxEvtsPerJob)
                skipEvents = int(maxEvtsPerJob*i_split)
                if i_split == n_jobs-1:
                   maxEvents = nevents - maxEvtsPerJob*(n_jobs-1) ## up to the last event

                # print i_split, nevents, skipEvents, maxEvents
                dict={'RUNDIR':runDir, 'RELPATH':relPath, 'PILEUP':pileup, 'FILEIN':infile, 'FILEOUT':outfile, 'PROXY':proxyPath, 'OUTPUTDIR':outputDir, 'SKIPEVENTS':str(skipEvents), 'MAXEVENTS':str(maxEvents), 'ISPLIT':str(i_split)}
                jdfName=condorDir+'/%(RELPATH)s_%(PILEUP)s/%(FILEOUT)s.jdl'%dict ## note: i_split is contained in FILEOUT
                # print dict
                # print 'AA:', jdfName
                jdf=open(jdfName,'w')
                jdf.write(
                    """x509userproxy = %(PROXY)s
universe = vanilla
Executable = %(RUNDIR)s/GENtoDelphes.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
Output = %(FILEOUT)s.out
Error = %(FILEOUT)s.err
Log = %(FILEOUT)s.log
Notification = Never
Arguments = %(FILEIN)s %(OUTPUTDIR)s/%(RELPATH)s_%(PILEUP)s %(FILEOUT)s.root %(PILEUP)s %(SKIPEVENTS)s %(MAXEVENTS)s

Queue 1"""%dict)

            jdf.close()
            os.chdir('%s/%s_%s'%(condorDir,relPath,pileup))
            os.system('condor_submit %(FILEOUT)s.jdl'%dict)
            os.system('sleep 0.5')                                
            os.chdir('%s'%(runDir))
            print str(count), "jobs submitted!!!"

print("--- %s minutes ---" % (round(time.time() - start_time, 2)/60))

