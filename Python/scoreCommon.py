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
import scipy.stats
import numpy as np

def findAllHeartbeats(truthFiles):

    cleanTruhDir = []
    for truthFile in sorted(truthFiles):
        tempStr = truthFile.rsplit('_')[0] + "_" + truthFile.rsplit('_')[1] + "_" + truthFile.rsplit('_')[2]
        cleanTruhDir.append(tempStr)

    uniqueTruhDir = []
    for x in cleanTruhDir:
        if x not in uniqueTruhDir:
            uniqueTruhDir.append(x)

    return uniqueTruhDir


### Takes in the file names of truth and test files and 
def matchInputFile( testFile, groundTruthFiles):

    testwithoutmat=os.path.splitext(os.path.split(testFile)[1])[0]
    
    testMatch = -1
    for truthIX in range(len(groundTruthFiles)):
        if testwithoutmat.find(groundTruthFiles[truthIX]) >= 0:
            testMatch = truthIX
       
    return testMatch


def checkFile(truthPath, testPath):

    truthMatrix = loadFileFromPath(truthPath)
    testMatrix = loadFileFromPath(testPath)
    #print ('TruthMatrix:')
    #print (truthMatrix.shape[0:2])
    #print ('TestMatrix:')
    #print (truthMatrix.shape)

    if testMatrix.shape[0:2] != truthMatrix.shape[0:2]:
        raise ScoreException('Matrix %s has dimensions %s; expected %s.' %
                             (os.path.basename(testPath), testMatrix.shape[0:2],
                              truthMatrix.shape[0:2]))

class ScoreException(Exception):
    pass

def magnitudesqure(vector):
    return np.sum([a ** 2 for a in vector])


def evaluateL2(truthMatrix, testMatrix):
    
    score = np.linalg.norm(truthMatrix-testMatrix,'fro')
    
    return score
