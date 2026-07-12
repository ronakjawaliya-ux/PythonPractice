# module = a file containing Python code. May contain  functions, classes, etc.
# used with modular programming, which is to separate a program into parts


#method_01
import module_demo

module_demo.hello()
module_demo.bye()


#method_02
import module_demo as md

md.hello()
md.bye()


#method_03
from module_demo import hello,bye

hello()
bye()


#method_04                  #DangerousOne
from module_demo import *   #NotIdealForBigProgram!

hello()
bye()


#CheckAvailablePythonModulesUsing:
help("modules")