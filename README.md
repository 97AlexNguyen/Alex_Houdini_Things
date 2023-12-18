# **A : Create and load a packages in houdini (No need to edit the system environment variables ).** 

This method is used to load certain Python modules to Houdini without the need to edit the system environment variables. It relies on a relative path method which makes it work on any computer and any version of Houdini, as long as that version of Houdini is compatible with the Python version being used.

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
In Houdini, there is a script file named is [456.py](https://github.com/97AlexNguyen/Alex_Houdini_python/blob/main/tutorial_image/load_456py.png).
Houdini runs this script whenever a scene file is loaded (including when Houdini starts up with a scene file).
We can use this method to load a module python to every session houdini . 
Create a 456.py then put it in houdini.xx\packages\test_packages\scripts

In 456.py 
[See Image]()
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

## load python module via sys append.
sys.path.append(python_lib)
```
Test import module [See image](https://github.com/97AlexNguyen/Alex_Houdini_python/blob/main/tutorial_image/test_load_module.png)

# B : Python for HDA.

## Call a definition using callback script .

Create a definition in PythonModule (scripts tab).

```Python
def a_test(kwargs):
    print("a_test")

def b_test(kwargs):
    print("b_test")
```
[Image](https://github.com/97AlexNguyen/Alex_Houdini_python/blob/main/tutorial_image/create_a_def.png)

Then in callback script Button (Work with any parameter like a float , int , toggle...)
```Python
hou.pwd().hdaModule().a_test(kwargs)
```
Can call a multi def like this :

```Python
hou.pwd().hdaModule().a_test(kwargs);hou.pwd().hdaModule().b_test(kwargs)
```
[Image](https://github.com/97AlexNguyen/Alex_Houdini_python/blob/main/tutorial_image/callback_script.png)






