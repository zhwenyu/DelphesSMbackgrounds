import os,datetime,time
runDir=os.getcwd()

os.system('xrdcp -f root://cmseos.fnal.gov//store/user/snowmass/DelphesSubmissionLPCcondor/scripts/EOSSafeUtils.py '+runDir)
execfile(runDir+'/EOSSafeUtils.py')

start_time = time.time()

#IO directories must be full paths
pileup = str(sys.argv[1])
outputDir='/store/user/snowmass/noreplica/YR_Delphes/Delphes342pre13/' # CHANGE ME
## outputDir='/store/group/upgrade/delphes_output/YR_Delphes/Delphes342pre13/'  ## For CERN condor
condorDir='/uscms_data/d3/jmanagan/YR_Delphes/Delphes342pre13_logs/' # Change username, helps to match log directory to the ROOT file directory, adding "_logs" (for compatibility with error checker)

cTime=datetime.datetime.now()

#outDir=outputDir[10:]

print 'Getting proxy'
proxyPath=os.popen('voms-proxy-info -path')
proxyPath=proxyPath.readline().strip()

print 'Starting submission'
count=0

fileList = [  # CHOOSE SAMPLES, you MUST have listed the file names with listFiles.py
    'DMScalar_top_tChan_Mchi1_Mphi100_14TeV_madgraph.txt',                                                  
    'DMScalar_top_tChan_Mchi1_Mphi10_14TeV_madgraph.txt',
    'DMScalar_top_tChan_Mchi1_Mphi500_14TeV_madgraph.txt',                                                  
    'DMScalar_top_tWChan_Mchi1_Mphi100_14TeV_madgraph.txt',                                                 
    'DMScalar_top_tWChan_Mchi1_Mphi10_14TeV_madgraph.txt',                                                  
    'DMScalar_top_tWChan_Mchi1_Mphi500_14TeV_madgraph.txt',
    ]

for sample in fileList:

    rootlist = open('fileLists/'+sample)
    rootfiles = []
    for line in rootlist:
        rootfiles.append('root://cmsxrootd.fnal.gov/'+line.strip())  ## Can change to whatever is normal for running @ CERN
        # OPTIONAL: use a more exact accessor for certain samples at CERN:
        #if(sample != 'WprimeToWZToWhadZinv_narrow_M-600_13TeV-madgraph.txt'): rootfiles.append('root://eoscms.cern.ch/'+line.strip())
        #else: rootfiles.append('root://cmsxrootd.fnal.gov/'+line.strip())
    rootlist.close()

    relPath = sample.replace('.txt','')
    #print 'relPath =',relPath

    os.system('eos root://cmseos.fnal.gov/ mkdir -p '+outputDir+relPath+'_'+pileup)
    ## os.system('eos root://eoscms.cern.ch/ mkdir -p '+outputDir+relPath+'_'+pileup) # For running @ CERN
    os.system('mkdir -p '+condorDir+relPath+'_'+pileup)
    
    tempcount = 0;
    for file in rootfiles:
        infile = file

        count+=1
        tempcount+=1
        if tempcount > 1: continue   # OPTIONAL to submit a test job

        outfile = relPath+'_'+str(tempcount)

        dict={'RUNDIR':runDir, 'RELPATH':relPath, 'PILEUP':pileup, 'FILEIN':infile, 'FILEOUT':outfile, 'PROXY':proxyPath, 'OUTPUTDIR':outputDir}
        jdfName=condorDir+'/%(RELPATH)s_%(PILEUP)s/%(FILEOUT)s.jdl'%dict
        print jdfName
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
        jdf.close()
        os.chdir('%s/%s_%s'%(condorDir,relPath,pileup))
        os.system('condor_submit %(FILEOUT)s.jdl'%dict)
        os.system('sleep 0.5')                                
        os.chdir('%s'%(runDir))
        print str(count), "jobs submitted!!!"

print("--- %s minutes ---" % (round(time.time() - start_time, 2)/60))

