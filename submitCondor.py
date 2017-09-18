import os,datetime,time
runDir=os.getcwd()

os.system('xrdcp -f root://cmseos.fnal.gov//store/user/snowmass/DelphesSubmissionLPCcondor/scripts/EOSSafeUtils.py '+runDir)
execfile(runDir+'/EOSSafeUtils.py')

start_time = time.time()

#IO directories must be full paths
pileup = str(sys.argv[1])
inputDir='/eos/uscms/store/user/snowmass/HTBinned_LHEfiles/14TEV/' 
outputDir='/eos/uscms/store/user/snowmass/noreplica/DelphesFromLHE_342pre05_2017July/' # CHANGEME
condorDir='/uscms_data/d3/jmanagan/DelphesFromLHE_342pre05_2017July_logs/' # Change username, match log directory to the ROOT file directory

cTime=datetime.datetime.now()

inDir=inputDir[10:]
outDir=outputDir[10:]

print 'Getting proxy'
proxyPath=os.popen('voms-proxy-info -path')
proxyPath=proxyPath.readline().strip()

print 'Starting submission'
count=0

dirList = [  # CHOOSE SAMPLES
    'B-4p-0-1-v1510_14TEV',
    # 'BB-4p-0-300-v1510_14TEV',
    # 'BB-4p-1300-2100-v1510_14TEV',
    # 'BB-4p-2100-100000-v1510_14TEV',
    # 'BB-4p-300-700-v1510_14TEV',
    # 'BB-4p-700-1300-v1510_14TEV',
    # 'Bj-4p-0-300-v1510_14TEV',
    # 'Bj-4p-1100-1800-v1510_14TEV',
    # 'Bj-4p-1800-2700-v1510_14TEV',
    # 'Bj-4p-2700-3700-v1510_14TEV',
    # 'Bj-4p-300-600-v1510_14TEV',
    # 'Bj-4p-3700-100000-v1510_14TEV',
    # 'Bj-4p-600-1100-v1510_14TEV',
    # 'BBB-4p-0-600-v1510_14TEV',
    # 'BBB-4p-1300-100000-v1510_14TEV',
    # 'BBB-4p-600-1300-v1510_14TEV',
    # 'Bjj-vbf-4p-0-700-v1510_14TEV',
    # 'Bjj-vbf-4p-1400-2300-v1510_14TEV',
    # 'Bjj-vbf-4p-2300-3400-v1510_14TEV',
    # 'Bjj-vbf-4p-700-1400-v1510_14TEV',
    # 'H-4p-0-300-v1510_14TEV',
    # 'H-4p-1500-100000-v1510_14TEV',
    # 'H-4p-300-800-v1510_14TEV',
    # 'H-4p-800-1500-v1510_14TEV',
    # 'LL-4p-0-100-v1510_14TEV',
    # 'LL-4p-100-200-v1510_14TEV',
    # 'LL-4p-1400-100000-v1510_14TEV',
    # 'LL-4p-200-500-v1510_14TEV',
    # 'LL-4p-500-900-v1510_14TEV',
    # 'LL-4p-900-1400-v1510_14TEV',
    # 'LLB-4p-0-400-v1510_14TEV',
    # 'LLB-4p-400-900-v1510_14TEV',
    # 'LLB-4p-900-100000-v1510_14TEV',
    # 'tB-4p-0-500-v1510_14TEV',
    # 'tB-4p-1500-2200-v1510_14TEV',
    # 'tB-4p-2200-100000-v1510_14TEV',
    # 'tB-4p-500-900-v1510_14TEV',
    # 'tB-4p-900-1500-v1510_14TEV',
    # 'tj-4p-0-500-v1510_14TEV',
    # 'tj-4p-1000-1600-v1510_14TEV',
    # 'tj-4p-1600-2400-v1510_14TEV',
    # 'tj-4p-2400-100000-v1510_14TEV',
    # 'tj-4p-500-1000-v1510_14TEV',
    # 'tt-4p-0-600-v1510_14TEV',
    # 'tt-4p-1100-1700-v1510_14TEV',
    # 'tt-4p-1700-2500-v1510_14TEV',
    # 'tt-4p-2500-100000-v1510_14TEV',
    # 'tt-4p-600-1100-v1510_14TEV',
    # 'ttB-4p-0-900-v1510_14TEV',
    # 'ttB-4p-1600-2500-v1510_14TEV',
    # 'ttB-4p-2500-100000-v1510_14TEV',
    # 'ttB-4p-900-1600-v1510_14TEV',    
    ]

for sample in dirList:
    os.system('eos root://cmseos.fnal.gov/ mkdir -p '+outDir+sample+'_'+pileup)
    os.system('eos root://cmseos.fnal.gov/ mkdir -p '+outDir+sample+'_'+pileup+'/metaData')
    os.system('mkdir -p '+condorDir+sample+'_'+pileup)
    relPath = sample
    process = sample.split('-')[0]
    if process == 'Bjj': process = 'Bjj-vbf'    

    xqcut = 40
    if 't' in process: xqcut = 60
    if 'tt' in process: xqcut = 80
    maxjets = 2
    if process == 'BBB' or process == 'LLB' or process == 'ttB': maxjets = 1
    if process == 'Bj' or process == 'Bjj-vbf' or process == 'H' or process =='tj': maxjets = 3

    qcut = xqcut*1.75 #guidance is between 1.5 and 2. Previously sliding scale 1.5 to 1.75, now use 1.75.

    print 'Process '+process+', using xqcut '+str(xqcut)+' and max jets '+str(maxjets)

    lhefiles = EOSlist_lhe_files(inputDir+sample)
    if count+len(lhefiles) > 4000: 
        print 'SKIPPING '+sample+', more than 4K jobs'  # OPTIONAL TO SUBMIT IN CHUNKS. LPC queues can run 2k.
        continue

    tempcount = 0;
    for file in lhefiles:
        rawfile = file[:-7]

        count+=1
        tempcount+=1
        if tempcount > 1: continue   # OPTIONAL: RUN A 1 JOB TEST

        dict={'RUNDIR':runDir, 'RELPATH':relPath, 'PILEUP':pileup, 'QCUT':str(qcut), 'JETS':str(maxjets), 'INPUTDIR':inDir, 'FILENAME':rawfile, 'PROXY':proxyPath, 'OUTPUTDIR':outDir}
        jdfName=condorDir+'/%(RELPATH)s_%(PILEUP)s/%(FILENAME)s.jdl'%dict
        print jdfName
        jdf=open(jdfName,'w')
        jdf.write(
            """x509userproxy = %(PROXY)s
universe = vanilla
Executable = %(RUNDIR)s/LHEtoDelphes.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
Output = %(FILENAME)s.out
Error = %(FILENAME)s.err
Log = %(FILENAME)s.log
Notification = Never
Arguments = %(INPUTDIR)s/%(RELPATH)s %(OUTPUTDIR)s/%(RELPATH)s_%(PILEUP)s %(FILENAME)s.lhe.gz %(QCUT)s %(JETS)s %(PILEUP)s

Queue 1"""%dict)
        jdf.close()
        os.chdir('%s/%s_%s'%(condorDir,relPath,pileup))
        os.system('condor_submit %(FILENAME)s.jdl'%dict)
        os.system('sleep 0.5')                                
        os.chdir('%s'%(runDir))
        print count, "jobs submitted!!!"

print("--- %s minutes ---" % (round(time.time() - start_time, 2)/60))
