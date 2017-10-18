#!/usr/bin/env python
# -*- coding: utf-8 -*-

###############################################################################
  #  Copyright Kitware Inc.
#
#  Licensed under the Apache License, Version 2.0 ( the "License" );
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
###############################################################################

import os

# groundTruthFiles = ['Case2_Pacing_', 'Case2_PacingtoVTtoVF_', 'Healthy_OS_1058_2kHz_', 'Healthy_OS_1117_1kHz_']

##  Associate each submitted file with the right GT
def assocSubmissions2GroundTruh( groundTruthFiles, submittedFiles, sbType):

    
    groundTruthFilesWithoutMat = []
    for gtFile in groundTruthFiles:
        groundTruthFilesWithoutMat.append( os.path.splitext(os.path.split(gtFile)[-1])[0] )

    # prealocate
    matchedFiles = []
    # for all files in submitted files
    for sbFile in submittedFiles:
        
        sbFileClean = os.path.split(sbFile)[-1] 
        
#        print( sbFileClean )
        
        
        for s in range(len(groundTruthFilesWithoutMat)):
#            print( groundTruthFilesWithoutMat[s] + '_' + sbType )
            if ( sbFileClean ==  groundTruthFilesWithoutMat[s] + '_' + sbType ):
                matchedFiles.append(s)

    return groundTruthFilesWithoutMat, matchedFiles


## reference ground truth files


## Detect group types
def findSubmissionGroups(testDir, groundTruthFiles):

	# list all the submitted files
	submittedFiles = os.listdir(testDir)

	# prealocate
	sbGroups = []

	# for every submitted file
	for sbFile in submittedFiles:

		# retrieve the type (last ID section)
		splitText = sbFile.rsplit('_')
		sbType = splitText[-1]


		# evaluate if the type exists and is one of the ground truth files
		if any( (sbFile.find(s)>=0) for s in groundTruthFiles):
			if not any(sbType == s for s in sbGroups):
				sbGroups.append(sbType)

	return sbGroups

## Group all submissions by the type
def groupSubmissions(testDir,groundTruthFiles):

	# list all the submitted files
    submittedFiles = os.listdir(testDir)

	# retrieve groups
    sbGroups = findSubmissionGroups(testDir, groundTruthFiles)

	# prealocate
    groupedSubmissions = {}
    for sbType in sbGroups:
            groupedSubmissions.update({ sbType : [] })
 
	# for all submissions
    for sbFile in submittedFiles:

        splitText = sbFile.rsplit('_')
        fileType = splitText[-1]
      
        if any( (fileType.find(s)>=0) for s in sbGroups):
            groupedSubmissions[fileType].append(testDir + '/' + sbFile)
            

    return {'groupNames' : sbGroups, 'groupFiles': groupedSubmissions}
