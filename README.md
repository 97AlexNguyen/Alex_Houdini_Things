# Houdini python . 



## 1. Load Python packages (Relative path)

```python
import hou
import os
import sys
## Retrieve the current Houdini version when a Houdini session is opened.
hou_version = hou.applicationVersion()
hou_int_version = str(hou_version[0]) + "." + str(hou_version[1])
current_document = os.path.join(os.environ['USERPROFILE'], 'Documents')
current_document.replace("\\","/")
houdini_split_version = "houdini"+hou_int_version


```
