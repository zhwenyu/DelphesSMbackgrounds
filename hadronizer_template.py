# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Hadronizer_TuneCUETP8M1_13TeV_generic_LHE_pythia8_cff.py --fileout file:EXO-RunIISummer15GS-01246.root --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --step GEN --conditions auto:mc --datatier GEN-SIM --eventcontent RAWSIM -n 1 --filein=file:tt-4p-600-1100-v1510_14TEV_183994371.lhe --no_exec
import FWCore.ParameterSet.Config as cms

process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.destinations = ['cout','cerr']
process.MessageLogger.cerr.FwkReport.reportEvery = 5000

process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')

###SJ
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
###SJ

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(RUNEVENTS)
)

# Input source
process.source = cms.Source("LHESource",
			    #fileNames = cms.untracked.vstring('file:tt-4p-600-1100-v1510_14TEV_183994371.lhe')
			    skipEvents=cms.untracked.uint32(SKIPEVENTS),
			    fileNames = cms.untracked.vstring('file:SETLHEFILENAME')
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.19 $'),
    annotation = cms.untracked.string('Hadronizer_TuneCUETP8M1_13TeV_generic_LHE_pythia8_cff.py nevts:1'),
    name = cms.untracked.string('Applications')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
					#fileName = cms.untracked.string('file:EXO-RunIISummer15GS-01246.root'),
					fileName = cms.untracked.string('file:file_out.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition
#*********************************************************************
# Matching - Warning! ickkw > 1 is still beta
#*********************************************************************
# 1        = ickkw            ! 0 no matching, 1 MLM, 2 CKKW matching
#*********************************************************************
#*********************************************************************
# maximal pdg code for quark to be considered as a light jet         *
# (otherwise b cuts are applied)                                     *
#*********************************************************************
# 5 = maxjetflavor    ! Maximum jet pdg code
#*********************************************************************
# Jet measure cuts                                                   *
#*********************************************************************
# 40   = xqcut   ! minimum kt jet measure between partons
#*********************************************************************

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:mc', '')

process.generator = cms.EDFilter("Pythia8HadronizerFilter",
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(14000.0),
    maxEventsToPrint = cms.untracked.int32(1),
    PythiaParameters = cms.PSet(
		pythia8CommonSettingsBlock,  ###SJ
		pythia8CUEP8M1SettingsBlock,   ###SJ
		processParameters = cms.vstring(
			'JetMatching:setMad = off',
			'JetMatching:scheme = 1',
			'JetMatching:merge = on',
			'JetMatching:jetAlgorithm = 2',
			'JetMatching:etaJetMax = 5.',
			'JetMatching:coneRadius = 1',
			'JetMatching:slowJetPower = 1',
			'JetMatching:qCut = SETQCUT',
			'JetMatching:nQmatch = 5',
			'JetMatching:nJetMax = SETMAXJETS',
			'JetMatching:doShowerKt = off',
		),
		parameterSets = cms.vstring('pythia8CommonSettings', 
					    'pythia8CUEP8M1Settings',
					    'processParameters',
					    )
    )
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RAWSIMoutput_step)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

# customisation of the process.

# Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.postLS1Customs
from SLHCUpgradeSimulations.Configuration.postLS1Customs import customisePostLS1 

#call to customisation function customisePostLS1 imported from SLHCUpgradeSimulations.Configuration.postLS1Customs
process = customisePostLS1(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

