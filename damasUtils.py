from thirdParty import damas
from pprint import pprint
import miscUtils as mu


#project = damas.http_connection("https://zombi.damas.io:8445/api")
project = damas.http_connection("http://10.0.0.27:8090/api")
project.signIn('alexandreb', 'MiaAB88al')


def get_node_id (pathS="", verboseB = False):
    log = mu.LogBuilder(funcName="get_node_id")
    pathS = "/".join(pathS.split('/')[-3:])
    idL = project.search("file:/." + pathS + "$/")

    if len(idL) == 0:
        log.printL("e", "No damas node found for: '{}'".format(pathS))
        return dict(resultB=log.resultB, logL=log.logL, nodeIdI = 0)
    elif len(idL) > 1:
        log.printL("e", "Several damas node found for: '{}', '{}'".format(pathS, idL))
        return dict(resultB=log.resultB, logL=log.logL, nodeIdI = 0)
    else:
        if verboseB:
            log.printL("i", "node: '{}', '{}'".format(idL[-1], pathS))
        return dict(resultB=log.resultB, logL=log.logL, nodeIdI=idL[-1])




def link_nodes(sourceL=[], targetPathS=""):
    log = mu.LogBuilder(funcName="linkNodes")

    resultD = get_node_id(pathS=targetPathS)
    targetIdI = resultD["nodeIdI"]
    if targetIdI == 0:
        log.printL("e", "could not identify target damas node: '{}'".format(targetPathS))
        return

    log.printL("i", "target: '{}', '{}'".format(targetPathS,targetIdI))
    for eachSourceS in sourceL:
        resultD = get_node_id(pathS=eachSourceS)
        sourceIdI = resultD["nodeIdI"]
        if sourceIdI == 0:
            log.printL("e", "could not identify source damas node: '{}'".format(eachSourceS))
            continue
        log.printL("i", "  <-- source: '{}', '{}'".format(eachSourceS, sourceIdI))


    #masterAnimS = project.search_one("file:chr_devTeam_testing_anim.ma$/")
    #refAnimS = project.search_one("file:/^/zomb/asset/.+chr_devTeam_testing_animRef.mb$/")


sourceL=['//ZOMBIWALK/Projects/zomb/asset/chr/chr_devTeam_testing/review/chr_devTeam_testing_previz.mov',
         '//ZOMBIWALK/Projects/zomb/asset/chr/chr_devTeam_testing/chr_devTeam_testing_anim.ma',
         '//ZOMBIWALK/Projects/zomb/asset/chr/chr_devTeam_testing/ref/chr_devTeam_testing_animRef.mb',
         'kjhfqskj']

link_nodes(targetPathS = '/zomb/asset/chr/chr_devTeam_testing/ref/chr_devTeam_testing_animRef.mb', sourceL=sourceL)