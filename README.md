# CEI_preprocessingECGI
This repo contains python code to localize pacing sites


To run this code, go to the covalic pacing site challenge:


This code runs from a docker container here:


## Running code in covalic
To run this code in covalic, make sure the docker repository has a build
with the recent changes.   Note the repo and build tag name, eg,
ecgimaging/cei_preprocessingecgi:latest.

In the covalic phase, choose the 'Customize scoring behavior' options from
the actions menu.  Input the docker repo name in the 'Image identifier'
field.  You can leave the 'Container Arguments' as the default.  

Next, choose 'Scoring metrics' from the action menu.  Add a metric to match
each metric name in the scoreCommon.py file.  

A final note: It may be neccessary to make sure that the submissions do not
need to match the ground truth files.  Choose the 'Configure submission'
option and uncheck the 'Require submission filenames to match ground truth
filenames' option.

## Testing the code locally
To run the code locally, Install docker and make sure that the docker
container is up to date.  Run the container with the call similar to
the following:

`docker run -v /path/to/data/folder:/mnt/girder_worker/data ecgimaging/cei_preprocessingecgi:latest --groundtruth=/mnt/girder_worker/data/ground_truth --submission=/mnt/girder_worker/data/ground_truth`
