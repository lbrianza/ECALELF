import FWCore.ParameterSet.Config as cms

def StreamReco(process):
    process.csctfDigis.producer       = cms.InputTag("hltSelectedElectronFEDListProducerGsf:StreamElectronRawFed")
    process.dttfDigis.DTTF_FED_Source = cms.InputTag("hltSelectedElectronFEDListProducerGsf:StreamElectronRawFed")
    process.ecalDigis.InputLabel      = cms.InputTag("hltSelectedElectronFEDListProducerGsf:StreamElectronRawFed")
    process.ecalPreshowerDigis.sourceTag = cms.InputTag("hltSelectedElectronFEDListProducerGsf:StreamElectronRawFed")
    process.castorDigis.InputLabel    = cms.InputTag("hltSelectedElectronFEDListProducerGsf:StreamElectronRawFed")
    process.gctDigis.inputLabel       = cms.InputTag("hltSelectedElectronFEDListProducerGsf:StreamElectronRawFed")
    process.gtDigis.DaqGtInputTag     = cms.InputTag("hltSelectedElectronFEDListProducerGsf:StreamElectronRawFed")
    #process.gtEvmDigis.EvmGtInputTag  = cms.InputTag("hltSelectedElectronFEDListProducerGsf:StreamElectronRawFed") 
    process.hcalDigis.InputLabel      = cms.InputTag("hltSelectedElectronFEDListProducerGsf:StreamElectronRawFed")
    process.muonCSCDigis.InputObjects = cms.InputTag("hltSelectedElectronFEDListProducerGsf:StreamElectronRawFed")
    process.muonDTDigis.inputLabel    = cms.InputTag("hltSelectedElectronFEDListProducerGsf:StreamElectronRawFed")
    process.muonRPCDigis.InputLabel   = cms.InputTag("hltSelectedElectronFEDListProducerGsf:StreamElectronRawFed")
    process.scalersRawToDigi.scalersInputTag = cms.InputTag("hltSelectedElectronFEDListProducerGsf:StreamElectronRawFed")
    process.siPixelDigis.InputLabel   = cms.InputTag("hltSelectedElectronFEDListProducerGsf:StreamElectronRawFed")
    process.siStripDigis.ProductLabel = cms.InputTag("hltSelectedElectronFEDListProducerGsf:StreamElectronRawFed")

    return process
