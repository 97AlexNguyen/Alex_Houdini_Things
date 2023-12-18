#"""Perform tasks when houdini is launched."""
# =============================================================================
# IMPORTS
# =============================================================================

from msilib import Directory
from socket import timeout
from urllib import response
import hou
import os
import sys
import os.path
import requests
import stat
import pprint
import json
import datetime
import tempfile

print("Load : 456.py")
hou_version = hou.applicationVersion()
hou_int_version = str(hou_version[0]) + "." + str(hou_version[1])
current_document = os.path.join(os.environ['USERPROFILE'], 'Documents')
current_document.replace("\\","/")
houdini_split_version = "houdini"+hou_int_version
temp_dir = tempfile.gettempdir() 





base_fps = 30.0
base_save = 10
######################## Setting for new houdini ##############
if hou.hipFile.name() == "untitled.hip":
    print("This is new a scene , FPS set to 30 ")
    hou.setFps(base_fps)
if hou.isUIAvailable():
    hip_file = hou.hipFile.path()
    if os.access(hip_file, os.W_OK) or not os.path.exists(hip_file):
        hou.appendSessionModuleSource('''hou.hscript("autosave on")''')
        hou.setPreference('general.autosaveinterval.val',str(base_save))
        print(f"Auto save in every {base_save} minutes")
        print("Be sure to clean up backup file !!!")


def read_current_version():
    current_path = current_document + "/" + houdini_split_version +"/packages"+"/" + "version_tool" + "/" + "version.py"
   # print(current_path)
    if os.path.exists(current_path):
        return current_path
    else:
        return "break"
    
def read_latest_sparx_sever():
    path = r"\\vnnas\projects\SPM\09_Share(SPM)\Q.An\packages"
    get_list_version = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path,f))]
    list_float_version = [float (i) for i in get_list_version]
    #print(max(list_float_version))
    return max(list_float_version)

houdini_document = current_document + "/" + houdini_split_version #+"/packages"+"/" + "version_tool" + "/" + "version.py"
houdini_packages_document = houdini_document + "/packages/Lyx_data"
python_lib = houdini_packages_document + "/Python/site-packages"
python_script = houdini_packages_document + "/Python/Scripts"
    
python_lib = houdini_packages_document + "/Python/site-packages"
python_script = houdini_packages_document + "/Python/Scripts"
python_lib = python_lib.replace("\\","/")
ffmgep = houdini_document + "/packages/Lyx_data/ffmpeg/bin"
ffmgep = ffmgep.replace("\\","/")

def check_current():
    try:        
        path = read_current_version()
        check_file = os.path.isfile(path)
        with open(path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                #print(line)
                return str(line)
    except:
        return "-1"
    

print("Trying to load Python Lib")
try:
    sys.path.append(python_lib)
    print("Load Done")
except:
    print("Cannot Load Python Lib")
print("Trying to append ffmgep codec")
try:
    sys.path.append(ffmgep)
    os.environ["PATH"] += os.pathsep + ffmgep
    print("Append Done !!!")
except:
    print("Cannot Load ffmgep codec")