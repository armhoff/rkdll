# A simple setup script to create various executables with 
# different User Access Control flags in the manifest.

# Run the build process by entering 'setup.py py2exe' or
# 'python setup.py py2exe' in a console prompt.
#
# If everything works well, you should find a subdirectory named 'dist'
# containing lots of executables

from distutils.core import setup
import py2exe

# The targets to build

# create a target that says nothing about UAC - On Python 2.6+, this
# should be identical to "asInvoker" below.  However, for 2.5 and
# earlier it will force the app into compatibility mode (as no
# manifest will exist at all in the target.)
#t1 = dict(script="hello.py",
#          dest_base="not_specified")
# targets with different values for requestedExecutionLevel
#t2 = dict(script="hello.py",
 #         dest_base="as_invoker",
 #         uac_info="asInvoker")
#t3 = dict(script="hello.py",
#          dest_base="highest_available",
 #         uac_info="highestAvailable")
t4 = dict(script="BYDTool.pyw",
          dest_base="BYDTool",
          icon_resource=[(1, "TabletDMI.ico")],
          uac_info="requireAdministrator")
#console = [t1, t2, t3, t4]
console = [t4]

# hack to make windows copies of them all too, but
# with '_w' on the tail of the executable.
#windows = [t1.copy(), t2.copy(), t3.copy(), t4.copy()]
windows = [t4.copy()]
for t in windows:
    t['dest_base'] += "_w"

#setup(
#    version = "0.1.0",
#    description = "py2exe user-access-control BYDTool script",
#    name = "py2exe BYDTool",
#    # targets to build
#    windows = windows,
##    windows = ["rkdll.pyw"],
#    #console = ["rkdll.pyw"]
#    console = console,
##    options = { "py2exe": { "dll_excludes": ["MSVCP90.dll"] } }
#    options = { "py2exe": { "dll_excludes": ["MSVCP90.dll"], "includes": ["sip"] } }
#    )


#includes = ["encodings", "encodings.*"]
includes = ["encodings", "encodings.*", "sip"]

options = {"py2exe":

    {"compressed": 1,
     "optimize": 2,
     "ascii": 1,
     "includes":includes,
     "bundle_files": 1,
     "dll_excludes": ["MSVCP90.dll"],
     }
    }
setup(     
    options = options,      
    zipfile=None,   #not create library.zip
#    console=[{"script": "hello.py", "icon_resources": [(1, "hello.ico")] }]
#    console = [{"script": "BYDTool.pyw",
#                "dest_base": "BYDTool",
#                "uac_info": "requireAdministrator",
#                "icon_resource": [(1, "TabletDMI.ico")]}]
    console = console,
    windows = windows,  
    )
           

