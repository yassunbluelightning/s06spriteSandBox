#s06spriteSandBox.py
import pj
import pjTkInter as tk
import pjSound as sound
from logStdErr import logStdErrClass
lse=logStdErrClass()
lse.setProjectName("s06spriteSandBox")
lse.errToFile()
###
tk.stopTkTimer() ####Avoid influence from the OtherApp Which Uses Timer in the Same Project;YassunAdd;2025-1001;;
tk.updateMainLabel("s06spriteSandBox")
tk.title("This shows how to create Sprite from SandBox.")
###
fileName="2022-0421-1128PM(Thurs) Aim(64x64).png"
##fileName="JS-20WKA-GD_CalcuLator.png"
srcAbsPath=lse.bundleAppPath + \
"/PeterJohnImages/" + fileName
destAbsPath=lse.sandBoxProjDirPath + \
"/images/" + fileName
import os
import shutil
if os.path.isfile( srcAbsPath ) and not os.path.isfile( destAbsPath ):
  shutil.copy2( srcAbsPath, destAbsPath )
if os.path.isfile( destAbsPath ):
  tk.createSprite("spr1",
destAbsPath,
64,64,1,
200,200,65000)
tk.setPosition("spr1",
150,150)

##tk.bindKeyPressFunction("s06spriteSandBox:s06spriteSandBox.keyPress")

##tk.bindButtonFunction("s06spriteSandBox:s06spriteSandBox.button")

##tk.bindMotionFunction("s06spriteSandBox:s06spriteSandBox.motion")

##tk.bindMotionCanvasFunction("s06spriteSandBox:s06spriteSandBox.motionCanvas")

##tk.startTimerFunctionAfter("s06spriteSandBox:s06spriteSandBox.gameLoop", 0.2)
