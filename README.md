![Houdini Logo](https://static.sidefx.com/images/ui/sfx_logo.svg)

![Unreal Logo](https://github.com/97AlexNguyen/Alex_Houdini_python/blob/main/logo/UE_Logo_horizontal_unreal-engine_white.svg)

![Python Logo](https://github.com/97AlexNguyen/Alex_Houdini_Things/blob/main/logo/python_and_qt_logo.svg)

![Main Logo](https://github.com/97AlexNguyen/Alex_Houdini_Things/blob/main/logo/Main_logo.svg)

<p align="center">
   <a href="https://github.com/97AlexNguyen">
    <img alt="Website" src="https://img.shields.io/website?label=main%20project&up_message=Community%20Projects&url=https%3A%2F%2Fgithub.com%2Fnitzan-treg%2Fcommunity_projects">
  </a>
  <a href="https://github.com/97AlexNguyen/Alex_Houdini_python">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/97AlexNguyen/Alex_Houdini_python">
  </a>
</p>
   
## Authors 
 
- [@97AlexNguyen](https://github.com/97AlexNguyen)

<h3 align="center">🔭 This is a document that I created for my personal use. It includes Python scripts , VEX , python qt , Math , VFX like RBD sim , Vellum Sim , and working with unreal engine as well. You can find a lot of useful information here, such as Python scripts for working with HDA, tips and tricks for parameter settings like toggle and button strip and etc. Please note that this document is not yet complete, but I will update it whenever I have some free time </h3>


> You can find many Python scripts for Houdini Digital Assets (HDAs) here, such as callback scripts, working with button strips, toggles, dynamic UI, and PyQt5 as well.

> All examples you can find in ["Test HDA"](https://github.com/97AlexNguyen/Alex_Houdini_Things/tree/58b5f0697b660aca390d42ff69e0f789f65f5117/hip_exams)
>To use test packages, download the latest version of the repo and extract all files to the "packages" folder. All folders and files should be directly inside the "packages" folder, not within a subfolder of the "packages" folder.

 
<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://fb.com/nguyenvuquocan" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/facebook.svg" alt="nguyenvuquocan" height="30" width="40" /></a>
<a href="https://www.youtube.com/@anquoc/videos" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/youtube.svg" alt="uczhcuz1wi4wwsmvauvmigbq" height="30" width="40" /></a>
</p>

- 📫 How to reach me **8197alexnguyen@gmail.com**

- 👯 Pm me If you want to collaborate on [this repo](https://github.com/97AlexNguyen/Alex_Houdini_Things/tree/main) 

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://unrealengine.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/kenangundogan/fontisto/036b7eca71aab1bef8e6a0518f7329f13ed62f6b/icons/svg/brand/unreal-engine.svg" alt="unreal" width="40" height="40"/> </a> <a href="https://www.sidefx.com/" target="_blank" rel="noreferrer"> <img src="https://github.com/97AlexNguyen/Alex_Houdini_Things/blob/main/logo/sidefx_badge.png" alt="houdini" width="40" height="40"/> </a> </a> <a href="https://www.qt.io/" target="_blank" rel="noreferrer"> <img src="https://upload.wikimedia.org/wikipedia/commons/0/0b/Qt_logo_2016.svg" alt="qt" width="40" height="40"/> </a></p>

# 📊 GitHub Stats:
![](https://github-readme-stats.vercel.app/api?username=97AlexNguyen&theme=nord&hide_border=true&include_all_commits=true&count_private=true)<br/>
![](https://github-readme-streak-stats.herokuapp.com/?user=97AlexNguyen&theme=nord&hide_border=true)<br/>
![](https://github-readme-stats.vercel.app/api/top-langs/?username=97AlexNguyen&theme=nord&hide_border=true&include_all_commits=true&count_private=true&layout=compact)

<h1 align="center"><img src="https://raw.githubusercontent.com/ABSphreak/ABSphreak/master/gifs/Hi.gif" width="40px" /> "Okay, let's get started." </h1>

# $\color[RGB]{122, 255, 253} A \ : \ Houdini \ Packages \ and \ Python \ Script \ locations $ 

## 1 : Create a [Houdini packages](https://www.sidefx.com/docs/houdini/ref/plugins.html)

>This is a method that enables loading of specific Python modules to Houdini without requiring any modification to the system environment variables. It utilizes a relative path technique which allows it to function on any computer and with any version of Houdini, as long as the Python version being used is compatible with that particular version of Houdini. Additionally, this method is easier to manage, especially when there are multiple Houdini packages involved.

A Houdini Package is like a main document where you can store HDAs, toolbars, Python modules, include codes, and more. This method is extremely helpful for those who want to maintain a clean Houdini document and wish to easily re-install it at a later time or share the package with someone who needs to use it.

To create a Houdini package, you need to create a json file that saves the path to the package and loads it into Houdini. This json file is essential for using and sharing the package. The json file working with relative path so we dont need to care about name of pc or houdini version.


Create a json file :

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




## 2 : Auto Load Python module in every houdini session (Relative path)
In Houdini, there is a script file named is [456.py](https://github.com/97AlexNguyen/Alex_Houdini_python/blob/main/tutorial_image/load_456py.png).
Houdini runs this script whenever a scene file is loaded (including when Houdini starts up with a scene file).
We can use this method to load a module python to every session houdini . 
Create a 456.py then put it in houdini.xx\packages\test_packages\scripts

In [456.py](https://github.com/97AlexNguyen/Alex_Houdini_python/blob/main/test_packages/scripts/456.py) 
```python
import os
import sys
import hou
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


## 3 : Somethings fun with 456.py
How to turn on auto save , set fps , realtime , frame range... in every houdini session
```Python
import sys
import os
import hou
##  auto save
hou.appendSessionModuleSource('''hou.hscript("autosave on")''')
## Set auto save every 10 Minutes
hou.setPreference('general.autosaveinterval.val','10')
## Set RealTime On
hou.playbar.setRealTime("On")
## Set Fps
hou.setFps(30.0)
## Set Frame Range
hou.playbar.setFrameRange(1.0,100.0)
```

# $\color[RGB]{122, 255, 253} B \ : \ Houdini \ HDA \ and \ Python \ Module  $ 


## 1 : Call a definition.
- Call def in PythonModule of HDA :
   + Create a definition in PythonModule (scripts tab).    
      ```Python
      def a_test(kwargs):
          print("a_test")
      
      def b_test(kwargs):
          print("b_test")
      ```
      [Image](https://github.com/97AlexNguyen/Alex_Houdini_python/blob/main/tutorial_image/create_a_def.png)
       
   + Then create a Button > Callback script (Work with any parameter like a float , int , toggle...)
      ```Python
      hou.pwd().hdaModule().a_test(kwargs)
      ```
      Can call a multi def like this :
      
      ```Python
      hou.pwd().hdaModule().a_test(kwargs);hou.pwd().hdaModule().b_test(kwargs)
      ```
      [Image](https://github.com/97AlexNguyen/Alex_Houdini_python/blob/main/tutorial_image/callback_script.png)
     
      > Dont know what "kwargs" meaning ? . [Read this](https://www.sidefx.com/docs/houdini/hom/locations.html)

- Call def in a Python Sop inside HDA :
   + Inside a HDA create a Python Sop and set name this node is "Python_test":
      ```Python
      def a_test():
          print("a_test")
      
      def b_test():
          print("b_test")
      ```
   + Then create a Button > Callback script (Work with any parameter like a float , int , toggle...)
      ```Python
      exec(hou.node("Python_test").parm("python").eval());a_test()
      ```     
   [Image](https://github.com/97AlexNguyen/Alex_Houdini_Things/blob/main/tutorial_image/call_def_in_python_sop.png)

  > "When calling a function in a Python SOP, it's not necessary to use the keyword argument 'kwargs'."
  
  > hou.node("Python_test") -> is name of python sop inside hda .
  > parm("python" -> is name of python parameter in Python Sop .
  > a_test() -> is definition .
  

## 2 : Read paramater and get the value of parameter . 

> In the HDA module’s code, you can get a reference to the HDA’s node name using:

```Python
node = kwargs["node"]
```
Test with callback script :
In python module : 
```
def _kwargs(kwargs):
    node = kwargs["node"]
    print(node)
```
In callback script of button :
```Python
hou.pwd().hdaModule()._kwargs(kwargs)
```
[Image](https://github.com/97AlexNguyen/Alex_Houdini_python/blob/main/tutorial_image/kwargs_node.png)

## 3 :Get the value of parameter: 
> "All parameters need to be identified by their 'name' rather than their 'label'."

Create float and int parameters named "float_test" and "int_test".
Create a def in PythonModule :
```Python
def load_parm(kwargs):
    node = kwargs["node"]
    _float = node.parm("float_test").eval()
    _int = node.parm("int_test").eval()
    print(_float)
    print(_int)
```
Create a Button and in "Callback Script":
```Python
hou.pwd().hdaModule().load_parm(kwargs)
```
[Image](https://github.com/97AlexNguyen/Alex_Houdini_python/blob/main/tutorial_image/load_parm_hda.png)


## 4 : Set the value of parameter: 

Create float and int parameters named "float_test_for_set" and "int_test_for_set".
Now we are using value of float_test and int_test to set value for float_test_for_set and int_test_for_set.

```Python
def set_parm_value(kwargs):
    node = kwargs["node"]
    _float = node.parm("float_test").eval()
    _int = node.parm("int_test").eval()
    ## Set value
    node.parm("float_test_for_set").set(_float)
    node.parm("int_test_for_set").set(_int)    
```
Then in callback script of a button :
```Python
hou.pwd().hdaModule().set_parm_value(kwargs)
```
[Image](https://github.com/97AlexNguyen/Alex_Houdini_python/blob/main/tutorial_image/set_parm.png)

## 5 : Python and Hda Parameter:
- Button and Press Button :
  ![Button Image](https://github.com/97AlexNguyen/Alex_Houdini_Things/blob/main/tutorial_image/button_image.png)
  + Press Button with callback script :
    In PythonModule of HDA
    > ```Python
    > def press_button(kwargs):
    >    ## kwargs['node'] is the top-level node, e.g. if this is wrapped in an HDA
    >    node = kwargs["node"]
    >    ## "test_press" is a node located within an HDA. The name of the button parameter inside the node is "execute".
    >    node.node("test_press").parm('execute').pressButton()
    > ```
    In callback script of button :
    > ```Python
    > hou.pwd().hdaModule().press_button(kwargs)
    > ```
    [Image](https://github.com/97AlexNguyen/Alex_Houdini_Things/blob/main/tutorial_image/press_button_def.png)


- Button Strip :
   
  + Create a button strip and set name is : "Button_strip_replace".
    In the button strip native to the menu > menu script :
      ```Python
      r = []
      node = hou.pwd()
      def menu():
         r.extend([0, "A"])
         r.extend([1, "B"])
         r.extend([2, "C"])
         return r
      return menu()
      ```
  + Single Selection :
    
    - In PythonModule :
         ```Python
         def replace_button_strip(kwargs):
             node = kwargs["node"]
             value_select = node.parm("Button_strip_replace").eval()
             print(value_select)
         ```   
    - In Callback script of button strip :
         ```Python
         hou.pwd().hdaModule().replace_button_strip(kwargs)
         ```
     
       ![menu script](https://github.com/97AlexNguyen/Alex_Houdini_Things/blob/main/tutorial_image/button_strip_single_select.png)

  + Multiple Selection :
    
    - Working with multiple selections in a button strip is not as easy as working with a single selection. . The button strip returns a [Bit field]([https://rb.gy/1b6b2m](https://en.wikipedia.org/wiki/Bit_field#:~:text=A%20bit%20field%20is%20a,can%20be%20set%20or%20inspected.)) value , 
    - which means that we need to translate it into a more usable form . This is an example to show how we can do that :
   ![bitconvert](https://github.com/97AlexNguyen/Alex_Houdini_Things/blob/main/tutorial_image/bitf_convert.png)
      ```Python
        bitfield_list = [1, 0, 1, 1, 0, 0, 1]
        for bit in bitfield_list:
           result = (result << 1) | bit
      ```
        
    - Create a button strip and set name is : "multiple_button_strip" .
    - Native to the menu , in menu option , switch to use : Toggle (Field + Multiple selection menu)
    - In menu script :
       ```Python
       r = []
       node = hou.pwd()
       def menu():
           r.extend([0, "A"])
           r.extend([1, "B"])
           r.extend([2, "C"])
           return r
       return menu()
       
       ```
    - In PythonModule :
       ```Python
      def multiple_button_strip(kwargs):
          node = kwargs["node"]
          bit_value = node.parm("multiple_button_strip").eval()
          list_selcted = []
          for i in range(1,4):
              if ( bit_value & (1<<i-1)):
                  list_selcted.append(i-1)
          print(list_selcted)    
       ```     
    - In Callback script at button strip :
      ```Python
         hou.pwd().hdaModule().multiple_button_strip(kwargs)
      ```
    - And this is result :
      ![Multiple_selection](https://github.com/97AlexNguyen/Alex_Houdini_Things/blob/main/tutorial_image/gif/multiple_section_example.gif)
  + Okay, I will show you how this method can be used through examples.
    > For example , we have an HDA which contains three objects . These objects can be any shape such as a box, sphere, or tube.
    [See](https://github.com/97AlexNguyen/Alex_Houdini_Things/blob/main/tutorial_image/objects_example_for_button_strip.png)
    > The idea is to use a button strip to display which object we want.
    - Create three switchs called is "sphere" , "tube" and "box"
    - Each switch's first input should link to "null", and the second input should link to the object and finally is merge all switches ![image](https://github.com/97AlexNguyen/Alex_Houdini_Things/blob/main/tutorial_image/stubebox.png)
    - Create a button strip parameter in HDA and set name is : "display_multip_object_button_strip"
    - Go to the script tap of button strip:
      ```Python
         r = []         
         node = hou.pwd()
         def menu():
             r.extend([0, "Sphere"])
             r.extend([1, "Tube"])
             r.extend([2, "Box"])
             return r
         return menu()
      ```
      
    - In PythonModule :
      ```Python
      def display_multip_object(kwargs):
          node = kwargs["node"]
          bit_value = node.parm("display_multip_object_button_strip").eval()
          list_object = ["sphere","tube","box"]
          object_to_display = []
          for i in range(1,len(list_object)+1):
              if ( bit_value & (1<<i-1)):
                  object_to_display.append(list_object[i-1])    
          for z in list_object:
              node.node(z).parm("input").set(0)            
                  
          for x in object_to_display:
              node.node(x).parm("input").set(1)
      ```
    - In Callback script :
      ```Python
      hou.pwd().hdaModule().display_multip_object(kwargs)
      ```
      ![Image](https://github.com/97AlexNguyen/Alex_Houdini_Things/blob/main/tutorial_image/gif/multip_sect_object.gif)
  + I will update two examples in the future -- one for working with a for loop feedback and another for dynamic UI.
 

# 7 : Selection Geometry :
  





  + $\mathscr{\color{red}{Updating...}}$
      
    
# $\color[RGB]{122, 255, 253} C \ : \ Vex $ 

   



# $\color[RGB]{122, 255, 253} D \ : \ Python Qt \ for \ Houdini$ 


# $\color[RGB]{122, 255, 253} E \ : \ RBD \ in \ Houdini$ 


# $\color[RGB]{122, 255, 253} F \ : \ Math$   



$\mathscr{\color{red}{Updating...}}$













