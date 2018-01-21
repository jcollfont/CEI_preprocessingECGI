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

rootNames = ['Case2_PacingtoVTtoVF', 'Case2_Pacing',  'Healthy_OS_1058_2kHz', 'Healthy_OS_1117_1kHz']

# get a unique list of all the filenameRoots in this directory
def findFilesNameRoots(inputDir):

    # list directory contents
    fileList = os.listdir(inputDir)

    # find files with the matching root from the list
    matchName = []
    for fi in fileList:
        for rr in range(len(rootNames)):
            if fi.find(rootNames[rr]) != -1 :
                matchName.append(rr)
                break

    return matchName, rootNames


def findFilesNameRoots2(inputDir, compareMatch):

    # list directory contents
    fileList = os.listdir(inputDir)

    # find files with the matching root from the list
    matchName = []
    compareFiles = []
    for fi in range(len(fileList)):
        
        noMatch = True
        
        # find the corresponding matches
        for rr in range(len(rootNames)):
            if fileList[fi].find(rootNames[rr]) != -1 :
                matchName.append(rr)
                noMatch = False
                break
        
        # find the files to compare with same match
        compareFiles.append([])
        if noMatch == False:
            for cm in range(len(compareMatch)):
                if rr == compareMatch[cm]:
                    compareFiles[fi].append(cm)
        

    return matchName, compareFiles






