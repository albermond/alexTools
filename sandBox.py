import os

# --
try:
except Exception, err:

# --
ignoreL = ['.mayaSwatches']
testS = "//ZOMBIWALK/Projects/zomb/asset/c2d/c2d_zombChute_sq0535sh0130/texture/.mayaSwatches"
if any(each in testS for each in ignoreL):
    print "ss"

# --
regex exemples
targetIdL = project.search_one("file:/.+chr_devTeam_testing/ref/chr_devTeam_testing_animRef.mb$/")


# maya

# pour effacer tous les uvs
import pymel.core as pm
sUvSetList = pm.polyUVSet(q=1,auv=1)
for each in reversed(sUvSetList):
    print each
    pm.polyUVSet(d=1, uvSet=each)

for i in pm.getAttr(".uvSet", mi=True):
    if i > 0:
        pm.removeMultiInstance(".uvSet[{}]".format(i))


# NUKE
# ----------------------------------------------

os.environ["zombi_output_dir"] = "//diskstation/z2k/05_3D/zombillenium/output"
[getenv zombi_output_dir]/AurelienMonstre_test.jpg
https://www.thefoundry.co.uk/products/nuke/developers/90/pythondevguide/startup.html#init-py
nuke.pluginPath()


print nuke.pluginPath()

import sys
print sys.version

import PySide
PySide.__version__


sel = nuke.selectedNode()
for i in range (sel.getNumKnobs()):
    print sel.knob (i).name()


nuke.filename(nuke.selectedNode())
x['file'].toScript()
# Result: '/foo/bar/[value Read1.label]/frame.####.jpg'
# This is the literal text typed in AFAIK

x['file'].value()
# Result: '/foo/bar/[value Read1.label]/frame.%04d.jpg'
# note that the frame padding is normalised to the % notation here, but no TCL eval

x['file'].evaluate()
# Result: '/foo/bar/testframes/frame.0002.jpg'
# evaluated at current time, which is frame 2

----------------------------------------------------------------------

