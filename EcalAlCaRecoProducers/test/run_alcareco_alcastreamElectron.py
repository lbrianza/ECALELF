from WMCore.Configuration import Configuration
config = Configuration()
config.section_('General')
config.General.transferOutputs = True
config.General.requestName = 'AlCaElectron_alcareco_RUN2016B' #change this
config.General.workArea = 'AlCaElectron_alcareco_RUN2016B' #change this
config.section_('JobType')
config.JobType.psetName = 'reco_RAW2DIGI_RECO_ALCA.py'
config.JobType.pluginName = 'Analysis'
config.JobType.allowUndistributedCMSSW = True
config.section_('Data')
config.Data.inputDataset = '/AlCaElectron/Run2016B-v2/RAW' #change this
config.Data.unitsPerJob = 1
config.Data.lumiMask = '/afs/cern.ch/cms/CAF/CMSCOMM/COMM_DQM/certification/Collisions16/13TeV/Cert_271036-282092_13TeV_PromptReco_Collisions16_JSON.txt' #change this
config.JobType.maxMemoryMB = 2500    # 2.5 GB       
config.JobType.maxJobRuntimeMin = 1400
config.JobType.outputFiles=["EcalCalWElectronStream.root"] #please specify: EcalCalZElectronStream.root if you are running on Z
config.Data.inputDBS = 'phys03' #'http://cmsdbsprod.cern.ch/cms_dbs_prod_global/servlet/DBSServlet'
config.Data.splitting = 'FileBased'
config.Data.outLFNDirBase = '/store/group/dpg_ecal/alca_ecalcalib/ecalMIBI/lbrianza/AlCaElectron_alcareco_RUN2016B/'
config.Data.useParent = True
config.Data.publication = True
config.section_('User')
config.section_('Site')
config.Site.storageSite = 'T2_CH_CERN'
#config.Site.whitelist = ['T2_US_Caltech', 'T2_US_Florida', 'T2_US_MIT', 'T2_US_Nebraska', 'T2_US_Purdue', 'T2_US_UCSD', 'T2_US_Vanderbilt']
