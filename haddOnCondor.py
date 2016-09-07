import os,sys,datetime,time
from ROOT import *
execfile("/uscms_data/d3/jmanagan/EOSSafeUtils.py")
runDir=os.getcwd()

start_time = time.time()

pileup = sys.argv[1]

#IO directories must be full paths
inputDir='/eos/uscms/store/user/snowmass/noreplica/DelphesFromLHE_333pre16_2016Aug/'
outputDir='/eos/uscms/store/user/snowmass/noreplica/DelphesFromLHE_333pre16hadd_2016Aug/'
condorDir='/uscms_data/d3/jmanagan/test/'

cTime=datetime.datetime.now()

inDir=inputDir[10:]
outDir=outputDir[10:]

print 'Getting proxy'
proxyPath=os.popen('voms-proxy-info -path')
proxyPath=proxyPath.readline().strip()

dirList = [
    'B-4p-0-1-v1510_14TEV',
    'BB-4p-0-300-v1510_14TEV',
    'BB-4p-1300-2100-v1510_14TEV',
    'BB-4p-2100-100000-v1510_14TEV',
    'BB-4p-300-700-v1510_14TEV',
    'BB-4p-700-1300-v1510_14TEV',
    'BBB-4p-0-600-v1510_14TEV',
    'BBB-4p-1300-100000-v1510_14TEV',
    'BBB-4p-600-1300-v1510_14TEV',
    'Bj-4p-0-300-v1510_14TEV',
    'Bj-4p-1100-1800-v1510_14TEV',
    'Bj-4p-1800-2700-v1510_14TEV',
    'Bj-4p-2700-3700-v1510_14TEV',
    'Bj-4p-300-600-v1510_14TEV',
    'Bj-4p-3700-100000-v1510_14TEV',
    'Bj-4p-600-1100-v1510_14TEV',
    'Bjj-vbf-4p-0-700-v1510_14TEV',
    'Bjj-vbf-4p-1400-2300-v1510_14TEV',
    'Bjj-vbf-4p-2300-3400-v1510_14TEV',
    'Bjj-vbf-4p-700-1400-v1510_14TEV',
    'H-4p-0-300-v1510_14TEV',
    'H-4p-1500-100000-v1510_14TEV',
    'H-4p-300-800-v1510_14TEV',
    'H-4p-800-1500-v1510_14TEV',
    'LL-4p-0-100-v1510_14TEV',
    'LL-4p-100-200-v1510_14TEV',
    'LL-4p-1400-100000-v1510_14TEV',
    'LL-4p-200-500-v1510_14TEV',
    'LL-4p-500-900-v1510_14TEV',
    'LL-4p-900-1400-v1510_14TEV',
    'LLB-4p-0-400-v1510_14TEV',
    'LLB-4p-400-900-v1510_14TEV',
    'LLB-4p-900-100000-v1510_14TEV',
    'tB-4p-0-500-v1510_14TEV',
    'tB-4p-1500-2200-v1510_14TEV',
    'tB-4p-2200-100000-v1510_14TEV',
    'tB-4p-500-900-v1510_14TEV',
    'tB-4p-900-1500-v1510_14TEV',
    'tj-4p-0-500-v1510_14TEV',
    'tj-4p-1000-1600-v1510_14TEV',
    'tj-4p-1600-2400-v1510_14TEV',
    'tj-4p-2400-100000-v1510_14TEV',
    'tj-4p-500-1000-v1510_14TEV',
    'tt-4p-0-600-v1510_14TEV',
    'tt-4p-1100-1700-v1510_14TEV',
    'tt-4p-1700-2500-v1510_14TEV',
    'tt-4p-2500-100000-v1510_14TEV',
    'tt-4p-600-1100-v1510_14TEV',
    'ttB-4p-0-900-v1510_14TEV',
    'ttB-4p-1600-2500-v1510_14TEV',
    'ttB-4p-2500-100000-v1510_14TEV',
    'ttB-4p-900-1600-v1510_14TEV',
    ]

count = 0
for sample in dirList:

    if count > 0: continue

    sample = sample+'_'+pileup
    thisoutDir = outDir+sample
    os.system('eos root://cmseos.fnal.gov/ mkdir -p '+thisoutDir)
    os.system('mkdir -p '+condorDir+sample)

    rootfiles = EOSlist_root_files(inputDir+'/'+sample)

    print '##########'*15
    print 'HADDING:', sample
    print '##########'*15
    print
    print 'N root files in',sample,'=',len(rootfiles)

    if pileup == '0PU': nFilesPerHadd = 400
    else: nFilesPerHadd = 100
    print 'Merging '+str(nFilesPerHadd)+' input files: '+str(int(len(rootfiles)/nFilesPerHadd)+1)+' output files'

    if len(rootfiles) < nFilesPerHadd:
        haddcommand = ''
        filename = sample+'_PhaseII_Substructure_PIX4022'
        for file in rootfiles:
            haddcommand+=' root://cmseos.fnal.gov/'+inDir+'/'+sample+'/'+file
        #print haddcommand        

        count+=1

        dict={'RUNDIR':runDir, 'RELPATH':sample, 'INPUTDIR':inDir, 'FILENAME':filename, 'PROXY':proxyPath, 'OUTPUTDIR':outDir}

        os.system('cp haddOnCondor_template.sh '+condorDir+'/'+sample+'/haddOnCondor_'+filename+'.sh')
        os.system('sed -i "s|INSERTFILES|'+haddcommand+'|" '+condorDir+'/'+sample+'/haddOnCondor_'+filename+'.sh')

        jdfName=condorDir+'/%(RELPATH)s/hadd_%(FILENAME)s.jdl'%dict
        print jdfName
        jdf=open(jdfName,'w')
        jdf.write(
            """x509userproxy = %(PROXY)s
universe = vanilla
Executable = haddOnCondor_%(FILENAME)s.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
Output = hadd_%(FILENAME)s.out
Error = hadd_%(FILENAME)s.err
Log = hadd_%(FILENAME)s.log
Notification = Never
Arguments = %(RELPATH)s %(FILENAME)s.root root://cmseos.fnal.gov/%(OUTPUTDIR)s

Queue 1"""%dict)
        jdf.close()
        os.chdir('%s/%s'%(condorDir,sample))
        os.system('condor_submit hadd_%(FILENAME)s.jdl'%dict)
        os.system('sleep 0.5')                                
        os.chdir('%s'%(runDir))
        print count, "jobs submitted!!!"

    else:
        for i in range(int(len(rootfiles)/nFilesPerHadd)+1):
            haddcommand = ''
            filename = sample+'_PhaseII_Substructure_PIX4022_'+str(i+1)
            begin=i*nFilesPerHadd
            end=begin+nFilesPerHadd
            if end > len(rootfiles): end=len(rootfiles)
            for j in range(begin,end):
                haddcommand+=' root://cmseos.fnal.gov/'+inDir+'/'+sample+'/'+rootfiles[j]
            #print haddcommand

            count+=1

            dict={'RUNDIR':runDir, 'RELPATH':sample, 'INPUTDIR':inDir, 'FILENAME':filename, 'PROXY':proxyPath, 'OUTPUTDIR':outDir}

            os.system('cp haddOnCondor_template.sh '+condorDir+'/'+sample+'/haddOnCondor_'+filename+'.sh')
            os.system('sed -i "s|INSERTFILES|'+haddcommand+'|" '+condorDir+'/'+sample+'/haddOnCondor_'+filename+'.sh')                    
            jdfName=condorDir+'/%(RELPATH)s/hadd_%(FILENAME)s.jdl'%dict
            print jdfName
            jdf=open(jdfName,'w')
            jdf.write(
                """x509userproxy = %(PROXY)s
universe = vanilla
Executable = haddOnCondor_%(FILENAME)s.sh
Should_Transfer_Files = YES
WhenToTransferOutput = ON_EXIT
Output = hadd_%(FILENAME)s.out
Error = hadd_%(FILENAME)s.err
Log = hadd_%(FILENAME)s.log
Notification = Never
Arguments = %(RELPATH)s %(FILENAME)s.root root://cmseos.fnal.gov/%(OUTPUTDIR)s

Queue 1"""%dict)
            jdf.close()
            os.chdir('%s/%s'%(condorDir,sample))
            os.system('condor_submit hadd_%(FILENAME)s.jdl'%dict)
            os.system('sleep 0.5')                                
            os.chdir('%s'%(runDir))
            print count, "jobs submitted!!!"
            


print("--- %s minutes ---" % (round(time.time() - start_time, 2)/60))



