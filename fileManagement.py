from pprint import pprint
import os
import shutiloptim as shutil

def get_dep_from_ma(inFileS=""):
    fileO = open(inFileS)
    resultL = []
    for eachLineS in fileO:
        if "/" in eachLineS:
            eachLineL = eachLineS.split('"')
            for each in eachLineL:
                if "/" in each and " " not in each and "<" not in each:
                    resultS = str(each)
                    resultS = str(resultS.replace("\\", ""))
                    if resultS not in resultL:
                        resultL.append(resultS)
    fileO.close()
    return resultL

myMayaFile = "//ZOMBIWALK/Projects/private/alexandreb/zomb/asset/chr/chr_aurelien_manteau/chr_aurelien_manteau_render-v023.000.ma"
# myMayaFile = "//ZOMBIWALK/Projects/private/alexandreb/zomb/shot/sq0810/sq0810_sh0030a/08_render/sq0810_sh0030a_render-v004-readonly.ma"

#dependenciesL = get_dep_from_ma(inFileS=myMayaFile)
#pprint(dependenciesL)


def backup_zombi(rootPathS = "//ZOMBIWALK/Projects/zomb/shot", ignoreDirL=['.mayaSwatches', '_left', '_right'], ignoreFileL=['.swatch','Thumbs.db', '.DS_Store', '_right.mov', '_left.mov']):
    skipedElemL = []
    sourceDriveS = "//ZOMBIWALK/Projects"
    targetDriveS = "E://"

    for root, dirs, files in os.walk(rootPathS):
        sourceS = str(root.replace("\\", "/"))
        targetS = sourceS.replace(sourceDriveS,targetDriveS)

        fileL = []
        skipedFileL = []
        for each in files:
            if not any(eachFile in each for eachFile in ignoreFileL):
                fileL.append(each)
            else:
                skipedFileL.append(each)


        if any(eachDir in sourceS for eachDir in ignoreDirL):
            skipedElemL.append(sourceS)
            continue
        elif "ref/_version" in sourceS:
            skipedElemL.append(sourceS)
            continue
        elif "_version" in sourceS:
            skipedElemL.append(sourceS)
            continue
        else:
            print ""
            print sourceS.replace(sourceDriveS,"")
            print fileL
            if not os.path.isdir(targetS):
                os.makedirs(targetS)
            for eachFile in fileL:
                if not os.path.isfile(targetS+"/"+eachFile):
                    shutil.copyfile(sourceS+"/"+eachFile, targetS+"/"+eachFile)


            for eachSkipedFile in skipedFileL:
                skipedElemL.append(sourceS+"/"+eachSkipedFile)

    print ""
    print "skipped files and directories"
    pprint(skipedElemL)

    skippedFileO = open(targetDriveS+"/skippedFile.txt", "w")
    for each in skipedElemL:
        skippedFileO.write(each + "\n")
    skippedFileO.close()


backup_zombi()