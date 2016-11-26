import maya.cmds as cmds

# Rename all selected objects
#kitList = cmds.ls(sl=True)
#for part in kitList:
#    cmds.rename(str(part), 'ship_' + str(part))

# Select all kit parts for export by naming convention
kitList = cmds.ls('ship_*')
transformList = cmds.listRelatives(kitList, parent=True, fullPath=True)

exportDir = "/Users/delainey/Documents/School/Goldsmiths/Intro to Modeling and Animation/MarshEffect/modelExports/"

# Iterate through all transform nodes
for part in transformList:
    cmds.select(part)

    #save original position
    x = cmds.getAttr(str(part) + ".translateX")
    y = cmds.getAttr(str(part) + ".translateY")
    z = cmds.getAttr(str(part) + ".translateZ")
    
    #move to origin
    cmds.setAttr(str(part) + ".translateX", 0)
    cmds.setAttr(str(part) + ".translateY", 0)
    cmds.setAttr(str(part) + ".translateZ", 0)
         
    #freeze transforms
    cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)
    
    #delete history
    cmds.DeleteHistory()
    
    #export fbx
    exportFileName = str(exportDir) + str(part[1:])
    cmds.file(exportFileName, force=True, options='v=0', type="FBX export", pr=True, es=True)
    
    #reset to previous position
    cmds.setAttr(str(part) + ".translateX", x)
    cmds.setAttr(str(part) + ".translateY", y)
    cmds.setAttr(str(part) + ".translateZ", z)