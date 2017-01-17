from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'ntuple_AlCaElectron_RUN2016B'
config.General.workArea = 'ntuple_AlCaElectron_RUN2016B'
config.section_('JobType')
config.JobType.psetName = 'EcalAlCaRecoProducers/python/alcaSkimming.py'
config.JobType.pluginName = 'Analysis'
config.JobType.outputFiles= ['ntuple.root','extraCalibTree.root']
config.JobType.pyCfgParams = ['isCrab=1', 'skim=WSkim', 'maxEvents=-1', 'type=ALCARECO', 'tagFile=EcalAlCaRecoProducers/config/reRecoTags/80X_dataRun2_Prompt_v8.py','doTreeOnly=1', 'electronStream=1','doTree=3']
config.JobType.allowUndistributedCMSSW = True
config.section_('Data')
config.Data.inputDataset = '/AlCaElectron/lbrianza-crab_AlCaElectron_alcareco_RUN2015D-c2f08da413a109f58849306beef921b4/USER' #CHANGE THIS
config.Data.unitsPerJob = 10
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-282092_13TeV_PromptReco_Collisions16_JSON.txt' #change this
config.Data.inputDBS = 'phys03' #'http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet'
config.Data.splitting = 'FileBased'
config.Data.outLFNDirBase = '/store/group/dpg_ecal/alca_ecalcalib/ecalMIBI/lbrianza/ntuple_AlCaElectron_RUN2016B/'
#config.Data.useParent = True
#config.Data.publication = True
config.section_('User')
config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
