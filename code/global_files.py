#------------------python lib--------------------------------------#
import sys
import os
##import _thread
import time
#import pygame
import numpy as np
import operator  #sort array
#------------------qt lib------------------------------------------#
##from PyQt4 import QtGui,QtCore
from PyQt4 import QtGui, QtCore, uic
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtGui import QPushButton
from PyQt4.uic import loadUi
import xlsxwriter
import xlrd
import xlwt
from xlutils.copy import copy
from shutil import copyfile
#------------------qt file import lib------------------------------#
#===========================HA========================================
from main_new_Mdi import*
from mainHA import*
from cableselectHA import*
from grid_main import*
from cuttingChart_main import*
#=========================HE==========================================
from log_page import*
from reset_page import*
from tester_info import*
from contact import*
from main import*
from config import*
from admin_landing import*
from teaching1 import*
from teaching2 import*
from teaching3 import*
from teaching4 import*
from teaching5 import*
from popup_window import*
from wirecolor import*
from ConnLib_main import*
from GrpLib_main import*
from global_grp_main import*
from ConnLib_main import*
from cuttingWindowmain import*
from Frontwin import*
from componenttest_main import*
from CuttingChart_import import*
from license_Doc import*
from fixturelib_main import*
from testingflow_main import*
from dignostics_main import*
from splice_visua_main import*
from log_file import*
from report_file import*
from messagelib import*
from cableselect import*
from Splicelib import*
from fo_main import*
import partload_main
from superloginmain import*
#------------------py file import lib------------------------------#
#==========================HA=====================================
import new_Mdi
import cable_selectHA
import grid_view2
import cutting_chart2
#==========================HE======================================
from login import * 
import reset_pw
import abt_tester
import contact_screen
import teaching_1
import teaching_2
import teaching_3
import teaching_4
import teaching_5
import wire_color_library
import ConnLibCreation
import grplib
import New_global_group
import Cutting_Window
import component_test
import Front_window
import licensce
import fixturelib
import testing_flow
import Diagnostics
import splice_visualization
import Prod_Logs
import Test_report
import message_library
import cable_select
import Add_splice
import fo
import superlogin
import partload
from datetime import datetime, date, time
import signal
