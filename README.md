# MetScanning
For recent recommendations please visit: https://twiki.cern.ch/twiki/bin/view/CMS/MissingETScanners
## Install
```
export SCRAM_ARCH=slc7_amd64_gcc700
cmsrel CMSSW_13_1_0
cd CMSSW_13_1_0/src/
cmsenv
git cms-init
git cms-addpkg RecoMET/METFilters
git clone -b Run2023_13_1_0 https://github.com/vhegde91/MetScanning.git
  
cd $CMSSW_BASE/src/

scram b -j10

cmsRun MetScanning/skim/test/skimMINIAOD_Run2023.py
 
```
  You might need to run the following command if you want to access files via XROOT:
```
  voms-proxy-init --voms cms
```
## Run on local file:
## Make sure you have input root file, global tag ( USE json file in CRAB onfiguration while generating ntuples for data)
```
  cmsRun MetScanning/skim/python/skimMINIAOD_BadRuns.py
```



```
In order to submit job with large input data:
```
  voms-proxy-init --voms cms
  source /cvmfs/cms.cern.ch/crab3/crab.sh
  
  Before submitting the jobs do a dryrun:

  crab --debug submit --config=crab.py --dryrun   

  In everything works fine you can then fully submit the jobs by:

  crab proceed
```
