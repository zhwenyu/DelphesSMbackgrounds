import os,sys

samplelist = [

    ## New on 8/31/18
    # Claim on skype chat
    '/GluGluToHHTo2B2ZTo4L_node_SM_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN', # 500k
    '/TTbarDMJets_DiLept_pseudoscalar_2_NLO_Mchi-1_Mphi-10_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN', # 600k
    '/TtbarDMJets_DiLept_pseudoscalar_2_NLO_Mchi-1_Mphi-50_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN', # 600k
    '/TtbarDMJets_DiLept_scalar_2_NLO_Mchi-1_Mphi-10_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN', # 600k
    '/TtbarDMJets_DiLept_scalar_2_NLO_Mchi-1_Mphi-300_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN', # 600k
    '/TtbarDMJets_DiLept_scalar_2_NLO_Mchi-1_Mphi-50_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN', # 600k
    '/VBFHHToHHTo2B2ZTo4L_CV_1_C2V_1_C3_1_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN', # 500k?
    '/ZPrimeToTTJets_M_2000GeV_W20GeV_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v4/GEN', # 400k

    ## New on 8/16/18
    # Claim on skype chat -- Basil
    '/QCD_HT1000to1500_BGenFilter_TuneCUEP8M2T4_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN', # 10M
    '/TTGG_0Jets_TuneCUETP8M1_14TeV_amcatnlo_madspin_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN', # 40M
    '/WJetsToQQ_HT180toInf_14TeV-madgraphMLM-pythia8_GenPt_250GeV/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN', # 10M
    '/ZPrimeToTTJets_M_10000GeV_W3000GeV_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN', # 400k

    # Julie
    '/QCD_Pt-5toInf_EMEnriched_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN', # 120M

    ## New on 8/3/18
    # Juliette
    '/DYJetsToLL_1J_M-10to50_TuneCUEP8M2T4_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN', # 40M
    '/WWWTo3L3Nu_aQGC_TuneCUEP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN', # 1M

    # Luca
    '/DYJetsToLL_M-10to50_TuneCUEP8M2T4_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN', # 100M? Maybe has "ext" sample?

    # Wenyu
    '/ZZTo4L_0Jets_ZZOnShell_14TeV-amcatnloFXFX-madspin-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN', # ? no gdoc?
    '/ZZTo4L_1Jets_ZZOnShell_14TeV-amcatnloFXFX-madspin-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN', # ? no gdoc?
    '/ZPrimeToTTJets_M_4000GeV_W120GeV_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN', # 400k

    # Basil (extension of existing)
    '/QCD_Pt-15to7000_MuEnrichedPt5_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5_ext1-v1/GEN', # 60M
    
    # Julie
    '/TTTT_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN', # < 10M
    '/TGJets_14TeV-amcatnlo-madspin-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN', # 1.5M
    '/VLF_MF_100_MS_95_BRmu50_BRtau50_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN', # 500k
    '/VLF_MF_150_MS_140_BRmu50_BRtau50_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN', # 500k

    ## New on 7/19/18
    # Wenyu
    '/DYJetsToLL_M-100_TuneCUEP8M2T4_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN', # 20M

    # Basil
    '/DYJetsToLL_M-4to10_TuneCUEP8M2T4_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN', # 40M

    # Julie
    '/QCD_Pt-5toInf_MuEnrichedPt5_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN', # 120M
    '/QCD_Pt-800to1000_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN', # 8M, replaces other sample

    # Luca
    '/SMS-TChiWW_mWMin-0p1_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17GenOnly-GridpackScan_93X_upgrade2023_realistic_v5-v2/GEN', # 7.2M
    '/SMS-TChiWZ_ZToLL_mZMin-0p1_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17GenOnly-GridpackScan_93X_upgrade2023_realistic_v5-v2/GEN', # 16M

    # Juliette
    '/VLF_MF_100_MS_80_BRmu100_BRtau0_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_100_MS_80_BRmu50_BRtau50_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_100_MS_90_BRmu50_BRtau50_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_100_MS_95_BRmu100_BRtau0_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/VLF_MF_150_MS_130_BRmu100_BRtau0_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_150_MS_130_BRmu50_BRtau50_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_150_MS_140_BRmu100_BRtau0_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_150_MS_145_BRmu100_BRtau0_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_150_MS_145_BRmu50_BRtau50_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_200_MS_180_BRmu100_BRtau0_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_200_MS_180_BRmu50_BRtau50_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_200_MS_190_BRmu100_BRtau0_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_200_MS_190_BRmu50_BRtau50_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_200_MS_195_BRmu100_BRtau0_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VLF_MF_200_MS_195_BRmu50_BRtau50_TuneCUETP8M1_14TeV_madgraph_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN', # 7.5M total
    '/WWZTo4L2Nu_aQGC_TuneCUEP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v3/GEN',  # 1M


    ## New on 6/27/18
    ## Wenyu 80M
    '/DY2Jets_MLL-50_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',  ## 80M
    
    ## Basil 33M
    '/Estar_EG_L10000_m1000_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',  ## 140k
    '/Estar_EG_L10000_m3500_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m3750_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m4000_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m4250_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m4500_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m4750_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m5000_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m5250_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m5500_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m5750_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m6000_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m6250_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Estar_EG_L10000_m6500_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m1000_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',  ## 140k
    '/Mustar_MuG_L10000_m3500_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m3750_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m4000_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m4250_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m4500_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m4750_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m5000_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m5250_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m5500_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m5750_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m6000_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m6250_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/Mustar_MuG_L10000_m6500_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/GluGluHToGG_M70_14TeV_amcatnloFXFX_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',  ## 500k
    '/GluGluHToWWTo2L2Nu_M125_14TeV_amcatnloFXFX_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',  ## 500k
    '/GluGluHToZZTo4L_M125_14TeV_powheg2_JHUgenV702_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',  ## 1M
    '/GluGluHToZZTo4L_M125_14TeV_powheg2_minloHJJ_JHUGenV7011_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',  ## 1M
    '/GluGlu_LFV_HToETau_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',  ## 500k
    '/GluGluToHHTo2B2Tau_node_SM_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',  ## 500k
    '/SUSYGluGluToBBHToTauTau_M-1400_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',  ## 100k
    '/TGGJets_leptonic_14TeV-amcatnlo-madspin-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v1/GEN',  ## 800k
    '/TGJets_lept_14TeV-amcatnlo-madspin-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',  ## 8M
    '/THW_Hincl_14TeV_TuneCUETP8M1-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',  ## 2M
    '/TT_FCNC-T2HJ_aTleptonic_HToaa_eta_hct-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',  ## 4M
    '/ttHJetToGG_M125_14TeV_amcatnloFXFX_madspin_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',  ## 1M
    '/TTZToLL_M-1to10_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',  ## 1M
    '/TTZToLLNuNu_M-10_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',  ## 10M
    '/VBFHToGG_M70_14TeV_amcatnlo_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',  ## 500k
        
    ## Maria 80M
    '/EWKWPlus2Jets_WToLNu_M-50_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',  ## 80M
    
    ## Juliette 78M
    '/QCDBBar_Pt-15to7000_MuEnriched_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN', ## 4M
    '/QCD_bEnriched_HT1000to1500_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',  ## 10M
    '/QCD_bEnriched_HT700to1000_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',  ## 10M
    '/QCDCCbar_Pt-15to7000_MuEnriched_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',  ## 4M
    '/QCD_Pt-30to40_DoubleEMEnriched_MGG-80toInf_TuneCUEP8M2T4_14TeV_Pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v3/GEN',  ## 20M
    '/WW_DoubleScattering_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',  ## 2M
    '/WWJJTo2L2Nu2J_SS_QCD_TuneCUEP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',  ## 2M
    '/WZTo3LNu_0Jets_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',  ## 20M
    '/ZH_HToBB_ZToQQ_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',  ## 2M
    '/ZJetsToNuNu_HT-1200To2500_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',  ## 2M
    '/ZJetsToNuNu_HT-600To800_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',  ## 2M
    
    ## Julie  290M? (can't be quite this big, already done the non-exts    
    '/ST_tch_14TeV_top_incl-powheg-pythia8-madspin/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v1/GEN',  ## 60M?
    '/ST_tW_antitop_5f_NoFullyHadronicDecays_14TeV-powheg-pythia8_TuneCUETP8M1/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',  ## 8M?
    '/ST_tW_top_5f_NoFUllyHadronicDecays_14TeV-powheg-pythia8_TuneCUETP8M1/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',  ## 8M?
    '/TTGamma_Hadronic_TuneCUETP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',  ## 12M?
    '/TTTJ_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',  ## 400k?
    '/WJetsToLNu_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',  ## 200M
    
    ## Luca 80M
    '/W2JetsToLNu_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',  ## 80M


    ## NEW on 6/1/18
    ## Juliette -------------------
    '/DYJetsToLL_M-50_HT-70to100_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DYJetsToLL_M-50_HT-100to200_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DYJetsToLL_M-50_HT-200to400_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DYJetsToLL_M-50_HT-400to600_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DYJetsToLL_M-50_HT-600to800_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DYJetsToLL_M-50_HT-800to1200_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DYJetsToLL_M-50_HT-1200to2500_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DYJetsToLL_M-50_HT-2500toInf_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DYToLL-M-50_0J_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/DYToLL-M-50_1J_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/DYToLL-M-50_2J_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/DYToLL-M-50_3J_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/QCDBBar_Pt-15to7000_MuEnriched_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/QCDBBbar_Pt-15to7000_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCDCCbar_Pt-15to7000_MuEnriched_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    ## Basil ---------------------
    '/QCD_Flat_Pt-15to7000_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/QCD_Pt-15to7000_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Pt-15to7000_bcToE_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Pt-15to7000_MuEnrichedPt5_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/QCD_Pt-15to7000_MuEnrichedPt5_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-91X_upgrade2023_realistic_v3_ext1-v1/GEN',
    '/QCD_Pt-20to7000_EMEnriched_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCUEP8M2T4_14TeV_Pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUEP8M2T4_14TeV_Pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',    
    '/QCD_Pt-0to300_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Pt-1000_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Mdijet-1000toInf_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_bEnriched_HT200to300_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_bEnriched_HT300to500_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_bEnriched_HT500to700_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_bEnriched_HT1500to2000_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_bEnriched_HT2000toInf_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    ## Maria ---------------------------
    '/VBF_LFV_HToEMu_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v3/GEN',
    '/RSGluonToTTbar_M2000_TuneCUEP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/RSGluonToTTbar_M5000_TuneCUEP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    ## Luca ----------------------------
    '/QCD_Pt-50to80_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/QCD_Pt-80to120_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/QCD_Pt-120to170_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/QCD_Pt-170to300_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/QCD_Pt-300to470_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Pt-470to600_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Pt-600to800_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Pt-800to1000_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/QCD_Pt-1000toInf_TuneCUETP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-91X_upgrade2023_realistic_v3-v1/GEN',



    ## SMP
    ## Wenyu ---------------
    '/DY0Jets_MLL-50_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DY1Jets_MLL-50_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DY3Jets_MLL-50_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DYJets_incl_MLL-50_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DiPhotonJetsBox_MGG-40to80_14TeV-Sherpa/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DiPhotonJetsBox_MGG-80toInf_14TeV-Sherpa/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/EWKWMinus2Jets_WToLNu_M-50_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/EWKZ2Jets_ZToLL_M-50_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/EWKZ2Jets_ZToNuNu_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GJet_Pt-20toInf_DoubleEMEnriched_MGG-40to80_TuneCUEP8M2T4_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/GJet_Pt-40toInf_DoubleEMEnriched_MGG-80toInf_TuneCUEP8M2T4_14TeV_Pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    
    ## Julie ---------------------------
    '/ST_s-channel_4f_InclusiveDecays_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/ST_s-channel_4f_InclusiveDecays_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/ST_s-channel_4f_leptonic_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/ST_s-channel_4f_leptonic_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/ST_tW_antitop_5f_NoFullyHadronicDecays_14TeV-powheg-pythia8_TuneCUETP8M1/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v2/GEN',
    '/ST_tW_antitop_5f_inclusiveDecays_14TeV-powheg-pythia8_TuneCUETP8M1/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v2/GEN',
    '/ST_tW_antitop_5f_inclusiveDecays_14TeV-powheg-pythia8_TuneCUETP8M1/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',
    '/ST_tW_top_5f_NoFUllyHadronicDecays_14TeV-powheg-pythia8_TuneCUETP8M1/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v2/GEN',
    '/ST_tW_top_5f_inclusiveDecays_14TeV-powheg-pythia8_TuneCUETP8M1/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v2/GEN',
    '/ST_tW_top_5f_inclusiveDecays_14TeV-powheg-pythia8_TuneCUETP8M1/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/TGJets_leptonic_14TeV-amcatnlo-madspin-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTGamma_Dilept_TuneCUETP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTGamma_Dilept_TuneCUETP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v4/GEN',
    '/TTGamma_Dilept_TuneCUETP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext2-v3/GEN',
    '/TTGamma_Hadronic_TuneCUETP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTGamma_SingleLeptFromT_TuneCUETP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',
    '/TTGamma_SingleLeptFromTbar_TuneCUETP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTGamma_SingleLeptFromTbar_TuneCUETP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',
    '/TTJets_DiLept_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTJets_DiLept_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',
    '/TTTJ_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTTT_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTTW_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTTW_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v4/GEN',
    '/TTWH_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTWH_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v4/GEN',
    '/TTWJetsToLNu_TuneCUETP8M1_14TeV-amcatnloFXFX-madspin-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTWJetsToLNu_TuneCUETP8M1_14TeV-amcatnloFXFX-madspin-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',
    '/TTWW_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTWW_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/TTWZ_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTWZ_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',
    '/TTZJets_TuneCUETP8M2_14TeV_madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTZJets_TuneCUETP8M2_14TeV_madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',
    '/TTZZ_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTZZ_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',
    '/TT_Mtt1000toInf_TuneCUETP8M1_14TeV-powheg-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_TuneCUETP8M2T4_14TeV-powheg-pythia8-GenJetPt-350GeV/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_TuneCUETP8M2T4_14TeV-powheg-pythia8-GenJetPt-950GeV/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_TuneCUETP8M2T4_14TeV-powheg-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TT_TuneCUETP8M2T4_14TeV-powheg-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',
    '/VVTo2L2Nu_14TeV_amcatnloFXFX_madspin_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/W0JetsToLNu_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/W1JetsToLNu_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/W3JetsToLNu_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/WGToLNuG_PtG-40_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/WToLNu_1J_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/WToLNu_2J_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/WToLNu_3J_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/WTolNu01234Jets_5f_LO_MLM_madgraph_V5_2p4p2/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/WWG_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/WWJJTo2L2Nu2J_SS_EWK_TuneCUEP8M2T4_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/WWW_4F_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/WWZ_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/WW_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/WZG_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/WZZ_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/ZGTo2LG_TuneCUETP8M1_14TeV-amcatnloFXFX-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZJetsToNuNu_HT-100To200_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZJetsToNuNu_HT-200To400_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZJetsToNuNu_HT-400To600_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZJetsToNuNu_HT-800To1200_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZZTo2L2Q_14TeV_amcatnloFXFX_madspin_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZZTo4L_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZZZ_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/tZq_ll_4f_14TeV-amcatnlo-madspin-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/tZq_nunu_4f_14TeV-amcatnlo-madspin-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/ttHTobb_M125_TuneCUETP8M2_14TeV-powheg-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',

    ## SUSY
    ## Juliette ------------
    '/DisplacedSUSY_stopToBottom_M_200_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_200_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_200_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_200_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_200_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_250_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_250_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_250_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_250_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_250_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_300_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_300_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_300_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_300_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_300_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_350_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_350_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_350_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_350_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_350_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_400_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_400_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_400_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_400_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_400_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_450_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_450_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_450_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_450_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_450_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_500_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_500_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_500_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_500_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_500_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_550_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_550_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_550_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_550_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_550_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_600_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_600_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_600_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_600_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_600_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_650_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_650_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_650_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_650_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_650_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_700_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_700_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_700_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_700_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToBottom_M_700_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_200_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_200_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_200_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_200_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_200_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_250_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_250_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_250_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_250_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_250_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_300_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_300_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_300_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_300_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_300_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_350_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_350_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_350_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_350_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_350_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_400_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_400_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_400_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_400_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_400_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_450_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_450_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_450_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_450_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_450_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_500_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_500_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_500_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_500_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_500_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_550_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_550_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_550_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_550_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_550_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_600_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_600_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_600_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_600_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_600_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_650_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_650_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_650_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_650_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_650_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_700_10000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_700_1000mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_700_100mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_700_10mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/DisplacedSUSY_stopToTopChi_M_700_1mm_TuneCP5_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    ## Basil ------------------
    '/SMS-TStauStau_mStau-100_mLSP-1_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-100_mLSP-25_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-100_mLSP-50_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-100_mLSP-75_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-200_mLSP-100_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-200_mLSP-150_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-200_mLSP-1_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-300_mLSP-100_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-300_mLSP-1_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-300_mLSP-200_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-300_mLSP-250_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-400_mLSP-100_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-400_mLSP-1_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-400_mLSP-200_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-400_mLSP-300_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-500_mLSP-100_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-500_mLSP-1_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-500_mLSP-200_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-500_mLSP-300_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-600_mLSP-100_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-600_mLSP-1_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-600_mLSP-200_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-600_mLSP-300_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-700_mLSP-100_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-700_mLSP-1_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-700_mLSP-200_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-700_mLSP-300_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-800_mLSP-100_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-800_mLSP-1_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-800_mLSP-200_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SMS-TStauStau_mStau-800_mLSP-300_TuneCUETP8M1_14TeV-madgraphMLM-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-1000_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-1200_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-1600_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-1800_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-2000_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-200_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-2300_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-250_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-2600_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-2900_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-3200_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-350_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-400_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-450_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-500_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-600_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-700_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-800_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToBBHToTauTau_M-900_TuneCUETP8M1_14TeV-amcatnlo-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SUSYGluGluToHToTauTau_M-1000_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-1200_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-1400_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-1600_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-1800_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-2000_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-200_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-2300_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-250_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-2600_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-2900_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-3200_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-350_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-400_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-450_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-500_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-600_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-700_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-800_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/SUSYGluGluToHToTauTau_M-900_TuneCUETP8M1_14TeV-pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',

    ## Higgs
    ## Maria ----------------
    '/GluGluHToBB_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGluHToGG_M125_14TeV_amcatnloFXFX_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGluHToMuMu_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGluHToTauTau_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGlu_LFV_HToEMu_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGlu_LFV_HToMuTau_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/THQ_Hincl_14TeV-TuneCUETP8M1-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/THQ_ctcvcp_HToGG_M125_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/THW_ctcvcp_HToGG_M125_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/TTHH_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTHH_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',
    '/TTZH_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/TTZH_TuneCUETP8M2_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v3/GEN',
    '/VBFHToBB_M-125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/VBFHToGG_M125_14TeV_amcatnlo_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/VBFHToMuMu_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/VBFHToTauTau_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/VBF_HToInvisible_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v2/GEN',
    '/VBF_HToZZTo4L_M125_14TeV_powheg2_JHUgenV702_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/VBF_LFV_HToETau_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/VBF_LFV_HToMuTau_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/VHToGG_M125_14TeV_amcatnloFXFX_madspin_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v3/GEN',
    '/VHToGG_M70_14TeV_amcatnloFXFX_madspin_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/VHToNonbb_M125_14TeV_amcatnloFXFX_madspin_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/WminusH_HToBB_WToLNu_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/WminusH_HToBB_WToQQ_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/WminusH_HToCC_WToLNu_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/WminusH_HToZZTo4L_M125_14TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/WplusH_HToBB_WToLNu_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/WplusH_HToBB_WToQQ_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/WplusH_HToCC_WToLNu_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/WplusH_HToZZTo4L_M125_14TeV_powheg2-minlo-HWJ_JHUgenV6_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZH_HToBB_ZToLL_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZH_HToBB_ZToNuNu_M125_13TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZH_HToCC_ZToLL_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ZH_HToZZ_M125_14TeV_powheg2-minlo-HZJ_JHUgenV702_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ggZH_HToBB_ZToLL_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ggZH_HToBB_ZToNuNu_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ggZH_HToBB_ZToQQ_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ggZH_HToGG_ZToLL_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ggZH_HToGG_ZToNuNu_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ggZH_HToGG_ZToQQ_M125_14TeV_powheg_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ttHJetToGG_M70_14TeV_amcatnloFXFX_madspin_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ttHToNonbb_M125_TuneCUETP8M2_14TeV-powheg-pythia8/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/ttH_HToZZ_4L_M125_14TeV_powheg2_JHUgenV702_pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_tch_14TeV_antitop_incl-powheg-pythia8-madspin/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v1/GEN',
    '/ST_tch_14TeV_antitop_incl-powheg-pythia8-madspin/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5_ext1-v1/GEN',
    '/ST_tch_14TeV_top_incl-powheg-pythia8-madspin/PhaseIISummer17wmLHEGENOnly-91X_upgrade2023_realistic_v3-v3/GEN',
    '/RSGluonToTTbar_M6000_TuneCUEP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',

    ## FNP
    ## Luca -------------------
    '/GluGluToHHTo2B2G_node_2_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGluToHHTo2B2G_node_SM_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGluToHHTo2B2Tau_node_2_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGluToHHTo2B2VTo2L2Nu_node_2_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGluToHHTo2B2VTo2L2Nu_node_SM_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGluToHHTo4B_node_2_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/GluGluToHHTo4B_node_SM_14TeV-madgraph/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/RSGluonToTTbar_M3000_TuneCUEP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/RSGluonToTTbar_M4000_TuneCUEP8M1_14TeV_pythia8/PhaseIISummer17GenOnly-93X_upgrade2023_realistic_v5-v1/GEN',
    '/ST_FCNC-TA_Tleptonic_kappa_act-Madgraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-TA_Tleptonic_kappa_aut-Madgraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-TH_Thadronic_HToaa_eta_hct-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-TH_Thadronic_HToaa_eta_hut-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-TH_Tleptonic_HToWWZZtautau_eta_hct-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-TH_Tleptonic_HToWWZZtautau_eta_hut-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-TH_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-TH_Tleptonic_HToaa_eta_hut-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-TH_Tleptonic_HTobb_eta_hct-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-TH_Tleptonic_HTobb_eta_hut-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-T_Tleptonic_kappa_gct-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/ST_FCNC-T_Tleptonic_kappa_gut-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_pair-M1000/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_pair-M1500/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_pair-M2000/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_pair-M2500/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_pair-M500/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_s-channel-M1000/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_s-channel-M1500/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_s-channel-M2000/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_s-channel-M2500/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_s-channel-M500/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_t-channel-M1000/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_t-channel-M1500/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_t-channel-M2000/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_t-channel-M2500/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/SingleLQ3ToTauB_5f_madgraph_LO_t-channel-M500/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-T2HJ_aTleptonic_HTobb_eta_hct-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-TtoHJ_aTleptonic_HToWWZZtautau_eta_hct-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-TtoHJ_aTleptonic_HToWWZZtautau_eta_hut-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-TtoHJ_aTleptonic_HToaa_eta_hut-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-TtoHJ_aTleptonic_HTobb_eta_hut-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-aTtoHJ_Tleptonic_HToWWZZtautau_eta_hct-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-aTtoHJ_Tleptonic_HToWWZZtautau_eta_hut-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hct-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-aTtoHJ_Tleptonic_HToaa_eta_hut-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-aTtoHJ_Tleptonic_HTobb_eta_hct-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TT_FCNC-aTtoHJ_Tleptonic_HTobb_eta_hut-MadGraph5-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-100_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-10_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-200_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-20_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-20_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-test_93X_upgrade2023_realistic_v5_ext1-v1/GEN',
    '/TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-300_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-500_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_pseudoscalar_NLO_Mchi-1_Mphi-50_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_scalar_NLO_Mchi-1_Mphi-100_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_scalar_NLO_Mchi-1_Mphi-10_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_scalar_NLO_Mchi-1_Mphi-200_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_scalar_NLO_Mchi-1_Mphi-20_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_scalar_NLO_Mchi-1_Mphi-300_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_scalar_NLO_Mchi-1_Mphi-500_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',
    '/TTbarDMJets_DiLept_scalar_NLO_Mchi-1_Mphi-50_TuneCUETP8M1_14TeV-madgraph-pythia8/PhaseIISummer17wmLHEGENOnly-93X_upgrade2023_realistic_v5-v2/GEN',

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
