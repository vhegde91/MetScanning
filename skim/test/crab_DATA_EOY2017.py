from CRABClient.UserUtilities import config
config = config()

config.General.requestName = ''

config.General.workArea = 'crabworkarea_v1'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'

config.JobType.psetName = 'skimMINIAOD_EOY2017.py'
config.JobType.outputFiles = ['output.root']
config.Data.inputDataset = ''
config.Data.inputDBS = 'global'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 20
config.Data.lumiMask = 'Cert_294927-306462_13TeV_EOY2017ReReco_Collisions17_JSON.txt'

config.Data.outLFNDirBase = '/store/user/mukherje/MET_PAPER_2021_RunII/2017_EOY_v1/' 
config.Data.publication = True
config.Data.outputDatasetTag = ''

config.Site.storageSite = 'T2_IN_TIFR'
#config.Site.blacklist = ['T2_US_Vanderbilt','T1_IT_CNAF']

config.section_("Debug")
config.Debug.extraJDL = ['+CMS_ALLOW_OVERFLOW=False']

if __name__ == '__main__':

    from CRABAPI.RawCommand import crabCommand
    for dataset in [
	'/JetHT/Run2017B-31Mar2018-v1/MINIAOD',
	'/JetHT/Run2017C-31Mar2018-v1/MINIAOD',
	'/JetHT/Run2017D-31Mar2018-v1/MINIAOD',
	'/JetHT/Run2017E-31Mar2018-v1/MINIAOD',
	'/JetHT/Run2017F-31Mar2018-v1/MINIAOD'
                  ]:
        config.Data.inputDataset = dataset
        config.General.requestName = dataset.split('/')[2]
        crabCommand('submit', config = config)

