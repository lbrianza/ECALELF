# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: reco -s RAW2DIGI,RECO,ALCA:EcalCalWElectronStream -n 100 --filein=/store/data/Run2016B/AlCaElectron/RAW/v1/000/272/775/00000/363B1493-3114-E611-A9C3-02163E011B18.root --data --conditions=80X_dataRun2_Prompt_v8 --era=Run2_2016 --scenario=pp --nThreads=4 --dirout=./ --customise Calibration/EcalAlCaRecoProducers/customElectronStream.StreamReco
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RECO',eras.Run2_2016)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.Reconstruction_Data_cff')
process.load('Configuration.StandardSequences.AlCaRecoStreams_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('/store/data/Run2016B/AlCaElectron/RAW/v1/000/272/775/00000/363B1493-3114-E611-A9C3-02163E011B18.root'),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('reco nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('./reco_RAW2DIGI_RECO_ALCA.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition
process.ALCARECOStreamEcalCalWElectronStream = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('pathALCARECOEcalCalWElectronStream')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('ALCARECO'),
        filterName = cms.untracked.string('EcalCalWElectronStream')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('./EcalCalWElectronStream.root'),
    outputCommands = cms.untracked.vstring('drop *', 
        'keep uint_bunchSpacingProducer_*_*', 
        'keep *_pfMet_*_*', 
        'keep *_kt6PFJetsForRhoCorrection_rho_*', 
        'keep *_kt6PFJets_rho_*', 
        'keep recoVertexs_offlinePrimaryVertices*_*_*', 
        'keep *BeamSpot_offlineBeamSpot_*_*', 
        'keep *_allConversions_*_*', 
        'keep *_conversions_*_*', 
        'keep *GsfTrack*_*_*_*', 
        'keep *_generator_*_*', 
        'keep *_addPileupInfo_*_*', 
        'keep *_genParticles_*_*', 
        'keep recoGsfElectron*_gsfElectrons*_*_*', 
        'keep recoGsfElectron*_gedGsfElectrons_*_*', 
        'keep recoGsfElectron*_gedGsfElectronCores_*_*', 
        'keep recoPhoton*_gedPhotons_*_*', 
        'keep recoCaloClusters_*_*_*', 
        'keep recoSuperClusters_*_*_*', 
        'keep recoPreshowerCluster*_*_*_*', 
        'keep *_pfElectronTranslator_*_*', 
        'keep *_alcaElectronTracksReducer_*_*', 
        'keep l1extraL1EmParticles_*_*_*', 
        'keep L1GlobalTriggerReadoutRecord_gtDigis_*_*', 
        'keep *_l1L1GtObjectMap_*_*', 
        'keep edmConditionsInEventBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInLumiBlock_conditionsInEdm_*_*', 
        'keep edmConditionsInRunBlock_conditionsInEdm_*_*', 
        'keep *_TriggerResults_*_*', 
        'keep *_hltTriggerSummaryAOD_*_HLT', 
        'keep *EcalRecHit*_alCaIsolatedElectrons_*_*', 
        'keep EcalRecHitsSorted_reducedEcalRecHitsES_*_*', 
        'keep *EcalRecHit*_*ecalPreshowerRecHit*_*EcalRecHitsES*_*', 
        'keep *CaloCluster*_*particleFlowEGamma*_*EBEEClusters*_*', 
        'keep *CaloCluster*_*particleFlowEGamma*_*ESClusters*_*', 
        'keep *_hltFixedGridRhoFastjetAllCaloForMuons_*_*', 
        'keep *_hltMetClean_*_*', 
        'keep *_*ecalMultiFitUncalibRecHit*_*_*', 
        'drop reco*Clusters_hfEMClusters_*_*', 
        'drop reco*Clusters_pfPhotonTranslator_*_*', 
        'drop *EcalRecHit*_ecalRecHit_*_*', 
        'drop *_*Cleaned_*_*', 
        'drop *_*cleaned*_*_*', 
        'drop *_*Unclean*_*_*', 
        'drop *_*unclean*_*_*', 
        'drop *_*_*Unclean*_*', 
        'drop *_*_*unclean*_*', 
        'keep recoSuperClusters_*_uncleanOnly_*', 
        'drop *_*_multi5x5Barrel*Clusters_*', 
        'drop *_dqmL1ExtraParticles_*_*', 
        'drop recoSuperClusters_mergedSuperClusters_*_*', 
        'keep *CaloCluster*_*alCaIsolatedElectrons*_*alcaCaloCluster*_*')
)

# Other statements
process.ALCARECOEventContent.outputCommands.extend(process.OutALCARECOEcalCalWElectronStream_noDrop.outputCommands)
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_dataRun2_Prompt_v8', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.reconstruction_step = cms.Path(process.reconstruction)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
process.ALCARECOStreamEcalCalWElectronStreamOutPath = cms.EndPath(process.ALCARECOStreamEcalCalWElectronStream)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.reconstruction_step,process.pathALCARECOEcalCalWElectronStream,process.endjob_step,process.RECOSIMoutput_step,process.ALCARECOStreamEcalCalWElectronStreamOutPath)

#Setup FWK for multithreaded
process.options.numberOfThreads=cms.untracked.uint32(4)
process.options.numberOfStreams=cms.untracked.uint32(0)

# customisation of the process.

# Automatic addition of the customisation function from Calibration.EcalAlCaRecoProducers.customElectronStream
from Calibration.EcalAlCaRecoProducers.customElectronStream import StreamReco 

#call to customisation function StreamReco imported from Calibration.EcalAlCaRecoProducers.customElectronStream
process = StreamReco(process)

# End of customisation functions

