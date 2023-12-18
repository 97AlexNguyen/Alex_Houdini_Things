# Create and load a packages to houdini . 


## 1. Create a [Houdini packages](https://www.sidefx.com/docs/houdini/ref/plugins.html)

```json
{
    "enable": true,
    "path": "$HOUDINI_PACKAGE_PATH/test_packages",    
    "env": 
    [
        {
            "HOUDINI_OTLSCAN_PATH": "$HOUDINI_PACKAGE_PATH/test_packages/hda;"
        }
    ]
}
```
[See Image](https://github.com/97AlexNguyen/Alex_Houdini_python/blob/main/tutorial_image/houdini_packages_json.png)




## 2. Auto Load Python module every session houdini (Relative path)
In Houdini, there is a script file named is [456.py](https://www.sidefx.com/docs/houdini/hom/locations.html).

Houdini runs this script whenever a scene file is loaded (including when Houdini starts up with a scene file).

```python
import hou
import os
import sys
## Retrieve the current Houdini version when a Houdini session is opened.
hou_version = hou.applicationVersion()
hou_int_version = str(hou_version[0]) + "." + str(hou_version[1])
houdini_split_version = "houdini"+hou_int_version


## Get Relative Path of Documents.
current_document = os.path.join(os.environ['USERPROFILE'], 'Documents')
current_document.replace("\\","/")
houdini_document = current_document + "/" + houdini_split_version

##  Get Relative Path of houdini packages.
## Read about houdini packages form here https://www.sidefx.com/docs/houdini/ref/plugins.html
houdini_packages_document = houdini_document + "/packages/test_packages"

## All python module here . 
python_lib = houdini_packages_document + "/Python/site-packages"

```
