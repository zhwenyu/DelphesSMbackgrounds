import os, sys, getopt
execfile("/uscms_data/d3/jmanagan/EOSSafeUtils.py")
dir = sys.argv[1]

print; print 'Checking', dir

try:
    opts, args = getopt.getopt(sys.argv[2:], "", ["verbose=", "resubmit=", "resub_num=", "pileup="])
except getopt.GetoptError as err:
    print str(err)
    sys.exit(1)
    
verbose_level = 0
resubmit = '0'
resub_num = -2
doNoLog = False
pileup = '0PU'

for o, a in opts:
	print o, a
	if o == '--verbose': verbose_level = int(a)
	if o == '--resubmit': resubmit = a
	if o == '--resub_num': resub_num = int(a)
        if o == '--pileup': pileup = str(a)

print 'Pileup setting:',pileup
rootdir = '/eos/uscms/store/user/snowmass/noreplica/'+dir.split('/')[-2]+'/'
rootdir = rootdir.replace('_logs','')
print 'checking ROOT files in:',rootdir
folders = [x for x in os.walk(dir).next()[1]]

total_total = 0
total_succeeded = 0
total_error = 0
total_running = 0
total_roots = 0

no_roots = 0
size_fail = 0
copy_fail = 0

for folder in folders:

        #to exclude one or more processes:
        #if 'LL-4p-0-100' not in folder: continue

        if pileup == '200PU' and '_0PU' in folder: 
            print 'skipping',folder,', pileup was',pileup
            continue
        if pileup == '0PU' and '_200PU' in folder: 
            print 'skipping',folder,', pileup was', pileup
            continue

	if verbose_level > 0:  print; print folder

        rootfiles = EOSlist_root_files(rootdir+folder)
        total_roots += len(rootfiles)

	files = [x for x in os.listdir(dir+'/'+folder) if '.jdl' in x]
	
	os.listdir(dir+'/'+folder)
	
	resub_index = []
	count_total = 0
	for file in files:
		total_total+=1
		index = file[file.find('_')+1:file.find('.')]
		if '_' in index: index = index.split('_')[-1]
		count_total += 1

		try:
			current = open(dir + '/'+folder+'/'+file.replace('.jdl','.out'),'r')
			copyfail = False
			for line in current:                                
                                if 'failure in xrdcp' in line: copyfail = True
                        if not nofail:
                                if verbose_level > 0:
                                    print '\tXRDCP FAIL:',file,' and JobIndex:',index
                                copy_fail+=1
                                if resub_num == -1 or resub_num == 2: resub_index.append(index)
                                continue
		except:
			pass

                thisroot = ''
                for rootfile in rootfiles:
                    if '_'+index+'_' in rootfile: thisroot = rootfile
	
                if thisroot != '':
                    zerosize = EOSisZeroSizefile(rootdir+folder+'/'+thisroot,'Aug')
                    if zerosize:
                        if verbose_level > 0:
                            print '\tZERO SIZE:',file,' and JobIndex:',index
                        size_fail+=1
                        if resub_num == -1 or resub_num == 0: resub_index.append(index)
                        continue
                else: 
                        if verbose_level > 0:
                            print '\tNO ROOT:',file,' and JobIndex:',index
                        no_roots+=1
                        if resub_num == -1 or resub_num == 1: resub_index.append(index)
                        continue
                    

	if resub_index != []: print 'RESUBS:', resub_index
	if resubmit != '1': continue

	indexind = 0
        savedir = os.getcwd()
	for index in resub_index:
		os.chdir(dir + '/' + folder)
		os.system('rm ' + dir + '/' + folder + '/' + folder.replace('_'+pileup,'') + '_' + index + '.out')
		os.system('condor_submit ' + dir + '/' + folder + '/' + folder.replace('_'+pileup,'') + '_' + index + '.jdl')
		indexind+=1
                os.chdir(savedir)
	
	

print
print 'TOTAL JOBS: ', total_total
print 'ZERO SIZE:', size_fail
print 'COPY FAIL:', copy_fail
print 'NO ROOTS:', no_roots
print 'ROOT files:', total_roots
print 'DONE:', total_total - no_roots - size_fail - copy_fail
