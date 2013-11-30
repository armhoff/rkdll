#!/usr/bin/python
# -*- coding:utf-8 -*-


### -*- coding:utf-8 -*-
### -*- coding:cp963 -*-

import sys
import os

from PyQt4 import QtCore, QtGui


from ctypes import *
from ctypes.wintypes import *

from UI_TabletDMI import *

class MainWindow(QtGui.QMainWindow):
	"""Main window UI
	"""
	def __init__(self, arg):
		super(MainWindow, self).__init__()
		self.arg = arg

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

#		pass

#		self.resize( 300, 250 )
#		self.setWindowTitle( 'statusbar' )
#		self.statusBar().showMessage( 'Ready' )

		# get the config.ini settings
#		self.conf = ConfigParser.ConfigParser()
#		self.conf.readfp( open('config.ini') )


#class MainWindow( QtGui.QMainWindow ):
#	def __init__( self, parent = None ):
#		QtGui.QMainWindow.__init__(self)
#		self.ui = Ui_BatteryCycleTool()
#		self.ui.setupUi( self )

		
		

#window = QtGui.QWidget()
#QtGui.QWidget.setWindowIcon(window, QtGui.QIcon('icons/TabletDMI.ico'))

#spinBox = QtGui.QSpinBox()
#slider = QtGui.QSlider( QtCore.Qt.Horizontal )
#spinBox.setRange( 0, 130 )
#slider.setRange( 0, 130 )

#QtCore.QObject.connect( spinBox, QtCore.SIGNAL( "valueChanged(int)" ), 
#						slider, QtCore.SLOT( "setValue(int)" ) )
#QtCore.QObject.connect( slider, QtCore.SIGNAL( "valueChanged(int)" ), 
#						spinBox, QtCore.SLOT( "setValue(int)" ) )
#spinBox.setValue( 35 )
#layout = QtGui.QHBoxLayout()
#layout.addWidget( spinBox )
#layout.addWidget( slider )
#window.setLayout( layout )

#window.show()


##########################################
#ctypes datatype          C datatype 
#c_char                          char 
#c_short                         short 
#c_int                             int 
#c_long                          long 
#c_ulong                        unsign long 
#c_float                          float 
#c_double                      double 
#c_void_p                       void 
#for pointer type, follow by "_p", such as int* is c_int_p
#In python, use class to implement the C struct

#UpgradeCB = WINFUNCTYPE( None, DWORD, c_int, DWORD )
#ProgressCB = WINFUNCTYPE( None, DWORD, c_int, DWORD, DWORD, c_int )

UpgradeCB = WINFUNCTYPE( c_void_p, DWORD, c_int, DWORD )
ProgressCB = WINFUNCTYPE( c_void_p, DWORD, c_int, DWORD, DWORD, c_int )

#typedef struct _INIT_CALLBACK_INFO
#{
#   LPVOID pUpgradeStepPromptProc;	// Prompt certain step status is started, passed or failed.
#   LPVOID pProgressPromptProc;		// Prompt progress of certain operation which may take long time.
#}INIT_CALLBACK_INFO,PINIT_CALLBACK_INFO;
class init_callback_info( Structure ):

	_fields_ = [('pUpgradeStepPromptProc', UpgradeCB),
				('pProgressPromptProc', ProgressCB),]

#	_fields_ = [('pUpgradeStepPromptProc', c_void_p),
#				('pProgressPromptProc', c_void_p),]


#typedef struct _INIT_DEV_INFO
#{	
#    BOOL	bScan4FsUsb;				// Scan for full speed usb device
#    USHORT	usRockusbVid;
#    USHORT	usRockusbPid;
#    USHORT	usRockMscVid;
#    USHORT	usRockMscPid;
#    UINT	uiRockusbTimeout;
#    UINT	uiRockMscTimeout;
#    UINT	emSupportDevice;
#}INIT_DEV_INFO,PINIT_DEV_INFO;

class init_dev_info( Structure ):

	_fields_ = [('bScan4FsUsb', BOOL),
				('usRockusbVid', c_ushort),
				('usRockusbPid', c_ushort),
				('usRockMscVid', c_ushort),
				('usRockMscPid', c_ushort),
				('uiRockusbTimeout', c_int),
				('uiRockMscTimeout', c_int),
				('emSupportDevice', c_int),
				]


#typedef struct _INIT_LOG_INFO_W
#{
#    BOOL bLogEnable;
#    LPWSTR lpszLogPathName;
#}INIT_LOG_INFO_W,PINIT_LOG_INFO_W;
#typedef struct _INIT_LOG_INFO_A
#{
#    BOOL bLogEnable;
#    LPSTR lpszLogPathName;
#}INIT_LOG_INFO_A,PINIT_LOG_INFO_A;
class init_log_info( Structure ):

	_fields_ = [('bLogEnable', BOOL),
				('lpszLogPathName', c_char_p),]

#RKUPGRADE_API BOOL _stdcall RK_InitializeW(INIT_DEV_INFO InitDevInfo, 
#										   INIT_LOG_INFO_W InitLogInfo,
#										   INIT_CALLBACK_INFO InitCallbackInfo);
#RKUPGRADE_API BOOL _stdcall RK_InitializeA(INIT_DEV_INFO InitDevInfo, 
#										   INIT_LOG_INFO_A InitLogInfo,
#										   INIT_CALLBACK_INFO InitCallbackInfo);
#ifdef _UNICODE
#define  RK_Initialize RK_InitializeW
#else
#define  RK_Initialize RK_InitializeA
#endif

#strDllPath = sys.path[0] + str(os.sep) + "dll" + str(os.sep) + "RKUpgrade.dll"
#rkdll = WinDLL( "dll/RKUpgrade.dll")
##rkdll = CDLL( "dll/RKUpgrade.dll")

#rkdll = WinDLL( strDllPath )
#rkdll = WinDLL( strDllPath )

######
#prototype has 3 types, the third is: 
#prototype(func_spec[, paramflags]) , paramflags is a 3 tuple, (_1,_2,_3)
#_1 is one of 1, 2, 4. them stands for input argument, output argument and input argument that default is 0.
#_2 is argument name
#_3 is default value.
#>>> from ctypes import c_int, WINFUNCTYPE, windll
#>>> from ctypes.wintypes import HWND, LPCSTR, UINT
#>>> prototype = WINFUNCTYPE(c_int, HWND, LPCSTR, LPCSTR, UINT)
#>>> paramflags = (1, "hwnd", 0), (1, "text", "Hi"), (1, "caption", None), (1, "flags", 0)
#>>> MessageBox = prototype(("MessageBoxA", windll.user32), paramflags)
#>>>
#>>> MessageBox()
#>>> MessageBox(text="Spam, spam, spam")
#>>> MessageBox(flags=2, text="foo bar")
#######

#void UpgradeStepPromptCB(DWORD deviceLayer, 
#										  ENUM_UPGRADE_PROMPT promptID, 
#										  DWORD oldDeviceLayer=0)
#void ProgressPromptCB(DWORD deviceLayer,
#						ENUM_PROGRESS_PROMPT promptID,
#						DWORD totalValue,
#						DWORD currentValue,
#						ENUM_CALL_STEP emCall=CALL_MIDDLE)

TESTDEVICE_START=10
TESTDEVICE_FAIL=11
TESTDEVICE_PASS=12

oldLayer = c_int(0)

def upgrade_fn( deviceLayer, promptID, oldDeviceLayer=oldLayer ):
	#print deviceLayer, promptID, oldDeviceLayer
	#pass
	print "(upgrade_fn) deviceLayer=0x%x, promptID=%d, oldDeviceLayer=%d" % (deviceLayer, promptID, oldDeviceLayer)

	if promptID == 10:
		print "(upgrade_fn) Test Device Start >>>>"

	if promptID == 11:
		print "(upgrade_fn) Test Device Fail"

	if promptID == 12:
		print "(upgrade_fn) Test Device Success"


#def upgrade_fn( deviceLayer, promptID ):
#	print deviceLayer, promptID

def progress_fn( deviceLayer, promptID, totalValue, currentValue, emCall=1 ):
	#print deviceLayer, promptID, totalValue, currentValue, emCall
	#pass
	print "(progress_fn) deviceLayer=%d, promptID=%d, totalValue=%d, currentValue=%d, emCall=%d" % (deviceLayer, promptID, totalValue, currentValue, emCall)

#callback = { "UpgradeStep":UpgradeStepPromptCB, "Progress":ProgressPromptCB }


if __name__ == '__main__':
	app = QtGui.QApplication( sys.argv )

	#window = QtGui.QMainWindow()
	window = MainWindow(sys.argv)
	window.show()

	s = "中文"
	print unicode(s, "utf-8")

#BOOL WINAPI GetComputerNameA(
#  __out         LPTSTR lpBuffer,
#  __in_out      LPDWORD lpnSize );

	pcName = c_char_p('')
	pcSize = 32
	windll.kernel32.GetComputerNameA(pcName, byref(c_int(pcSize)))
	print pcSize, pcName

#pcName = c_char_p('')
#05	pcSize = 25
#06	windll.kernel32.GetComputerNameA(pcName,byref(c_int(pcSize)))
#07	print(pcName)

######################################################
	rkdll = WinDLL( "dll/RKUpgrade.dll")
	#rkdll = CDLL( "dll/RKUpgrade.dll" )

#LAWaveExt_dll = windll.LoadLibrary("LAWaveExt")
#LAWaveExt_dll = cdll.LoadLibrary("LAWaveExt")

	callbackInit = init_callback_info()
	#callbackInit.pUpgradeStepPromptProc = '\0'
	#callbackInit.pProgressPromptProc = '\0'
	#callbackInit.pUpgradeStepPromptProc = UpgradeStepPromptCB
	#callbackInit.pProgressPromptProc = ProgressPromptCB
	#callbackInit.pUpgradeStepPromptProc = callback["UpgradeStep"]
	#callbackInit.pProgressPromptProc = callback["Progress"]

	callbackInit.pUpgradeStepPromptProc = UpgradeCB( upgrade_fn )
	callbackInit.pProgressPromptProc = ProgressCB( progress_fn )



	loginfoInit = init_log_info()
	loginfoInit.bLogEnable = False
	loginfoInit.lpszLogPathName = '\0'

	#	// for RK3188EVB
	#	InitDevInfo.bScan4FsUsb = TRUE;
	#	InitDevInfo.emSupportDevice = RK31_DEVICE; // = 0x70	
	#	InitDevInfo.uiRockMscTimeout = 20;
	#	InitDevInfo.uiRockusbTimeout = 20;
	#	InitDevInfo.usRockMscPid = 0x0C02;
	#	InitDevInfo.usRockMscVid = 0x0BB4;
	#	InitDevInfo.usRockusbPid = 0x310B;
	#	InitDevInfo.usRockusbVid = 0x2207;

	devinfoInit = init_dev_info()
	devinfoInit.bScan4FsUsb = True
	devinfoInit.emSupportDevice = 0x70
	devinfoInit.uiRockusbTimeout = 20
	devinfoInit.uiRockMscTimeout = 20
	devinfoInit.usRockusbVid = 0x2207
	#devinfoInit.usRockusbPid = 0x310B  # RK3188
	devinfoInit.usRockusbPid = 0x300B   # RK3168
	devinfoInit.usRockMscVid = 0x0BB4
	devinfoInit.usRockMscPid = 0x0C02

	#############################################################################
	RK_Initialize = rkdll.RK_InitializeA
	#RK_Initialize.argtypes = [byref(devinfoInit), byref(loginfoInit), byref(callbackInit)]
	RK_Initialize.argtypes = [init_dev_info, init_log_info, init_callback_info]
	RK_Initialize.restype = BOOL

	#RKUPGRADE_API BOOL _stdcall RK_Uninitialize();
	RK_Uninitialize = rkdll.RK_Uninitialize
	RK_Uninitialize.argtypes = []
	RK_Initialize.restype = BOOL

	#RKUPGRADE_API BOOL _stdcall RK_ScanDevice(UINT &nDeviceCounts,BOOL &bExistMsc);
	RK_ScanDevice = rkdll.RK_ScanDevice
	RK_ScanDevice.argtypes = [POINTER(UINT), POINTER(BOOL)]
	RK_ScanDevice.restype = BOOL

	#RKUPGRADE_API BOOL _stdcall RK_ReadCustomData(PBYTE pCustomData, INT& nCustomDataLen,INT& nCustomDataOffset,DWORD dwLayer=0);
	RK_ReadCustomData = rkdll.RK_ReadCustomData
	#RK_ReadCustomData.argtypes = [POINTER(c_char), POINTER(c_int), POINTER(c_int), DWORD]
	#RK_ReadCustomData.argtypes = [c_char_p, POINTER(c_int), POINTER(c_int), DWORD]

	
	RK_ReadCustomData.argtypes = [c_void_p, POINTER(INT), POINTER(INT), DWORD]
	
	#RK_ReadCustomData.argtypes = [POINTER(BYTE), POINTER(INT), POINTER(INT), DWORD]
	RK_ReadCustomData.restype = BOOL

	#prototype = WINFUNCTYPE(BOOL, POINTER(c_char), POINTER(c_int), POINTER(c_int), DWORD)
	#paramflags = (1, "pCustomData"), (1, "nCustomDataLen"), (1, "nCustomDataOffset"), (1, "dwLayer", 0)
	#RK_ReadCustomData = prototype(("RK_ReadCustomData", rkdll), paramflags)

	#RKUPGRADE_API BOOL _stdcall RK_ReadSN(PBYTE pSN, INT& nSNLen,DWORD dwLayer=0);
	RK_ReadSN = rkdll.RK_ReadSN
	RK_ReadSN.argtypes = [POINTER(c_char), POINTER(c_int), DWORD]
	RK_ReadSN.restype = BOOL

	#RKUPGRADE_API BOOL _stdcall RK_WriteCustomData(PBYTE pCustomData, INT nCustomDataOffset,INT nCustomDataLen,DWORD dwLayer=0);
	RK_WriteCustomData = rkdll.RK_WriteCustomData
	RK_WriteCustomData.argtypes = [POINTER(BYTE), c_int, c_int, DWORD]
	RK_WriteCustomData.restype = BOOL

	#prototype = WINFUNCTYPE(BOOL, POINTER(c_char), c_int, c_int, DWORD)
	#paramflags = (1, "pCustomData"), (1, "nCustomDataOffset"), (1, "nCustomDataLen"), (1, "dwLayer", 0)
	#RK_WriteCustomData = prototype(("RK_WriteCustomData", rkdll), paramflags)

	#prototype = WINFUNCTYPE(c_int, HWND, LPCSTR, LPCSTR, UINT)
	#paramflags = (1, "hwnd", 0), (1, "text", "Hi"), (1, "caption", None), (1, "flags", 0)
	#MessageBox = prototype(("MessageBoxA", windll.user32), paramflags)



#bRet = RK_Initialize( byref(devinfoInit), byref(loginfoInit), byref(callbackInit) )
	bRet = RK_Initialize( devinfoInit, loginfoInit, callbackInit )

	print "RK_Initialize() return: bRet=%d" % (bRet)

	nDeviceCounts = UINT(0)
	bExistMsc = BOOL(False)
	bRet = RK_ScanDevice( byref(nDeviceCounts), byref(bExistMsc) )
	print "RK_ScanDevice(): bRet=%d, nDeviceCounts=%d, bExistMsc=%d" % (bRet, nDeviceCounts.value, bExistMsc.value)

	if nDeviceCounts.value == 1:

		#manu_type = c_byte*16
		#manu = manu_type()
	#	manu_p = pointer(manu)
		#manu.value = "TOSHIBA"
		#print "manu: ", repr(manu.value)

	#	manu = "TOSHIBA"
	#	manu_p = pointer(manu)
	#	bRet = RK_WriteCustomData( manu, 32, len(manu), 0 )
		#bRet = RK_WriteCustomData( manu, 32, c_int(16), 0 )
	#	bRet = RK_WriteCustomData( "TOSHIBA", 32, 7, 0 )
		#print "RK_WriteCustomData() return: %d (manufacture:%s)" % (bRet, manu)

	#	data = c_void_p()
	#	pointer_data = pointer(data)

	#	data = create_string_buffer('\000' * 512)
	#	print "data = ", repr(data.value)

	#	data = "\0"*512
	#	data = create_string_buffer( 512 )
	#	p = c_char_p()
	#	p.value = data
		

	#	print "p=", p

	#	print "p.value = ", p.value

		data_type = c_byte*512
		data = data_type()
		data_p = pointer(data)

#buffer = ctypes.create_unicode_buffer(1024)
#TriggerContinue = (c_int * 16)()
#TriggerData = (c_byte * (16 * 64))()
#		buffer = (ctypes.wintypes.BYTE * 1024)()

		datalen = c_int(512)
		dataoffset = c_int(0)
		dwLayer = DWORD(0)
#		print datalen.value, dataoffset.value

		length = INT(512)
		offset = INT(0)
#		buf = (BYTE*512)()
#		bRet = RK_ReadCustomData( buf, byref(length), byref(offset), dwLayer )
		
		buf = create_unicode_buffer(512)
		bRet = RK_ReadCustomData( buf, byref(length), byref(offset), dwLayer )

#		bRet = RK_ReadCustomData( data, byref(datalen), byref(dataoffset), 0 )

	#	bRet = RK_ReadCustomData( data, byref(datalen), byref(dataoffset), 0 )
		"""
		ctypes.ArgumentError: argument 1: <type 'exceptions.TypeError'>: expected LP_c_byte instance instead of pointer to c_byt
		e_Array_512

		Traceback (most recent call last):
		  File ".\BYDTool.pyw", line 368, in <module>
		    bRet = RK_ReadCustomData( data, byref(datalen), byref(dataoffset), 0 )
		WindowsError: exception: access violation reading 0x05B41CC8


		buf = (BYTE*512)()
		bRet = RK_ReadCustomData( buf, byref(length), byref(offset), dwLayer )

		Traceback (most recent call last):
		  File ".\BYDTool.pyw", line 379, in <module>
		    bRet = RK_ReadCustomData( buf, byref(length), byref(offset), dwLayer )
		WindowsError: exception: access violation reading 0x042A1CC8

		Traceback (most recent call last):
		  File "BYDTool.pyw", line 386, in <module>
		WindowsError: exception: access violation reading 0x03EC1B28

		"""

		"""
		Well, there are two ways.  The first one would be to declare the argtypes as you have
		done, but then you must pass an array of BYTE, probably like this:

		buffer = (ctypes.wintypes.BYTE * 1024)()
		_setupapi.SetupDiGetDeviceRegistryPropertyW(\
		       hdevinfoset, pDeviceInfoData, property,
		       None, buffer, ctypes.sizeof(buffer), None)

		The other way would be to use c_void_p as argtypes item 5, then you
		can pass your unicode_buffer.
		"""

		#print "RK_ReadCustomData() return: %d" % (bRet)
		print "RK_ReadCustomData() return: %", bRet
		print "Data: length=%d, offset=%d" % (length, offset)
		print buf

		#sn = "\0" * 32
		#sn_p = pointer(sn)
		
		sn_len = c_int(32)
		sn = create_string_buffer(32)

		#bRet = RK_ReadSN( sn_p, byref(sn_len), 0 )
		#bRet = RK_ReadSN( sn, byref(sn_len), dwLayer.value )
	#	bRet = RK_ReadSN( sn, byref(sn_len), 0 )
		print "RK_ReadSN() return: bRet=%d" % (bRet)
		print "SN: %s" % (sn)


	bRet = RK_Uninitialize()

	print "RK_Uninitialize() return: bRet=%d" % (bRet)





	#conditionWait = threading.Condition()
#	flag_exit = False

#	raw_input()
		
	
#	adb_waitfordevice()

#	adb_read_batterycycle()

	#adb_reboot_fastboot()

	#adb_fastboot_devices()

	sys.exit( app.exec_() )

