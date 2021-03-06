"""*****************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************"""

    
def instantiateComponent(tcpipIgmpComponent):
	print("TCPIP IGMP Component")
	configName = Variables.get("__CONFIGURATION_NAME")
	
	# Use IGMPv3 Module
	tcpipIgmp = tcpipIgmpComponent.createBooleanSymbol("TCPIP_USE_IGMP", None)
	tcpipIgmp.setLabel("Use IGMPv3 Module")
	tcpipIgmp.setVisible(False)
	tcpipIgmp.setDescription("Use IGMPv3 Module")
	tcpipIgmp.setDefaultValue(True)   
	#tcpipIgmp.setDependencies(tcpipIgmpMenuVisibleSingle, ["tcpipIPv4.TCPIP_STACK_USE_IPV4"])

	# Number of IGMP Interfaces
	tcpipIgmpInterfaceNum = tcpipIgmpComponent.createIntegerSymbol("TCPIP_IGMP_INTERFACES", None)
	tcpipIgmpInterfaceNum.setLabel("Number of IGMP Interfaces")
	tcpipIgmpInterfaceNum.setVisible(True)
	tcpipIgmpInterfaceNum.setDescription("Number of IGMP Interfaces")
	tcpipIgmpInterfaceNum.setDefaultValue(1)
	#tcpipIgmpInterfaceNum.setDependencies(tcpipIgmpMenuVisibleSingle, ["TCPIP_USE_IGMP"])

	# Number of Multicast Groups
	tcpipIgmpMcastGrpNum = tcpipIgmpComponent.createIntegerSymbol("TCPIP_IGMP_MCAST_GROUPS", None)
	tcpipIgmpMcastGrpNum.setLabel("Number of Multicast Groups")
	tcpipIgmpMcastGrpNum.setVisible(True)
	tcpipIgmpMcastGrpNum.setDescription("Number of Multicast Groups")
	tcpipIgmpMcastGrpNum.setDefaultValue(7)
	#tcpipIgmpMcastGrpNum.setDependencies(tcpipIgmpMenuVisibleSingle, ["TCPIP_USE_IGMP"])

	# IGMPv2 Support Only
	tcpipIgmpv2Support = tcpipIgmpComponent.createBooleanSymbol("TCPIP_IGMPV2_SUPPORT_ONLY", None)
	tcpipIgmpv2Support.setLabel("IGMPv2 Support Only")
	tcpipIgmpv2Support.setVisible(True)
	tcpipIgmpv2Support.setDescription("IGMPv2 Support Only")
	tcpipIgmpv2Support.setDefaultValue(False)   
	#tcpipIgmpv2Support.setDependencies(tcpipIgmpMenuVisibleSingle, ["TCPIP_USE_IGMP"])

	# Number of Sources in Each Group
	tcpipIgmpSourceNum = tcpipIgmpComponent.createIntegerSymbol("TCPIP_IGMP_SOURCES_PER_GROUP", None)
	tcpipIgmpSourceNum.setLabel("Number of Sources in Each Group")
	tcpipIgmpSourceNum.setVisible(True)
	tcpipIgmpSourceNum.setDescription("Number of Sources in Each Group")
	tcpipIgmpSourceNum.setDefaultValue(11)
	#tcpipIgmpSourceNum.setDependencies(tcpipIgmpMenuVisibleSingle, ["TCPIP_USE_IGMP"])

	# Number of Sockets per Source
	tcpipIgmpSktNum = tcpipIgmpComponent.createIntegerSymbol("TCPIP_IGMP_SOCKET_RECORDS_PER_SOURCE", None)
	tcpipIgmpSktNum.setLabel("Number of Sockets per Source")
	tcpipIgmpSktNum.setVisible(True)
	tcpipIgmpSktNum.setDescription("Number of Sockets per Source")
	tcpipIgmpSktNum.setDefaultValue(4)
	#tcpipIgmpSktNum.setDependencies(tcpipIgmpMenuVisibleSingle, ["TCPIP_USE_IGMP"])

	# Default Robustness Variable Value
	tcpipIgmpRobustVarValue = tcpipIgmpComponent.createIntegerSymbol("TCPIP_IGMP_ROBUSTNESS_VARIABLE", None)
	tcpipIgmpRobustVarValue.setLabel("Default Robustness Variable Value")
	tcpipIgmpRobustVarValue.setVisible(True)
	tcpipIgmpRobustVarValue.setDescription("Default Robustness Variable Value")
	tcpipIgmpRobustVarValue.setDefaultValue(2)
	#tcpipIgmpRobustVarValue.setDependencies(tcpipIgmpMenuVisibleSingle, ["TCPIP_USE_IGMP"])

	# Default Unsolicited Report Interval in ms
	tcpipIgmpUnsoilicitReportInterval = tcpipIgmpComponent.createIntegerSymbol("TCPIP_IGMP_UNSOLICITED_REPORT_INTERVAL", None)
	tcpipIgmpUnsoilicitReportInterval.setLabel("Default Unsolicited Report Interval - ms")
	tcpipIgmpUnsoilicitReportInterval.setVisible(True)
	tcpipIgmpUnsoilicitReportInterval.setDescription("Default Unsolicited Report Interval in ms")
	tcpipIgmpUnsoilicitReportInterval.setDefaultValue(1000)
	#tcpipIgmpUnsoilicitReportInterval.setDependencies(tcpipIgmpMenuVisibleSingle, ["TCPIP_USE_IGMP"])

	# Enable User Notification Functions"
	tcpipIgmpUsrNotify = tcpipIgmpComponent.createBooleanSymbol("TCPIP_IGMP_USER_NOTIFICATION", None)
	tcpipIgmpUsrNotify.setLabel("Enable User Notification Functions")
	tcpipIgmpUsrNotify.setVisible(True)
	tcpipIgmpUsrNotify.setDescription("Enable User Notification Functions")
	tcpipIgmpUsrNotify.setDefaultValue(False)   
	#tcpipIgmpUsrNotify.setDependencies(tcpipIgmpMenuVisibleSingle, ["TCPIP_USE_IGMP"])

	# IGMP Task Rate
	tcpipIgmpTskTickRate = tcpipIgmpComponent.createIntegerSymbol("TCPIP_IGMP_TASK_TICK_RATE", None)
	tcpipIgmpTskTickRate.setLabel("IGMP Task Rate")
	tcpipIgmpTskTickRate.setVisible(True)
	tcpipIgmpTskTickRate.setDescription("IGMP Task Rate")
	tcpipIgmpTskTickRate.setDefaultValue(33)
	#tcpipIgmpTskTickRate.setDependencies(tcpipIgmpMenuVisibleSingle, ["TCPIP_USE_IGMP"])

	#Add to system_config.h
	tcpipIgmpHeaderFtl = tcpipIgmpComponent.createFileSymbol(None, None)
	tcpipIgmpHeaderFtl.setSourcePath("tcpip/config/igmp.h.ftl")
	tcpipIgmpHeaderFtl.setOutputName("core.LIST_SYSTEM_CONFIG_H_MIDDLEWARE_CONFIGURATION")
	tcpipIgmpHeaderFtl.setMarkup(True)
	tcpipIgmpHeaderFtl.setType("STRING")

	# Add igmp.c file
	tcpipIgmpSourceFile = tcpipIgmpComponent.createFileSymbol(None, None)
	tcpipIgmpSourceFile.setSourcePath("tcpip/src/igmp.c")
	tcpipIgmpSourceFile.setOutputName("igmp.c")
	tcpipIgmpSourceFile.setOverwrite(True)
	tcpipIgmpSourceFile.setDestPath("library/tcpip/src/")
	tcpipIgmpSourceFile.setProjectPath("config/" + configName + "/library/tcpip/src/")
	tcpipIgmpSourceFile.setType("SOURCE")
	tcpipIgmpSourceFile.setEnabled(True)
	#tcpipIgmpSourceFile.setDependencies(tcpipIgmpGenSourceFile, ["TCPIP_USE_IGMP"])

def tcpipIgmpMenuVisibleSingle(symbol, event):
	if (event["value"] == True):
		print("IGMP Menu Visible.")		
		symbol.setVisible(True)
	else:
		print("IGMP Menu Invisible.")
		symbol.setVisible(False)

def tcpipIgmpGenSourceFile(sourceFile, event):
	sourceFile.setEnabled(event["value"])

#Set symbols of other components
def setVal(component, symbol, value):
    triggerDict = {"Component":component,"Id":symbol, "Value":value}
    if(Database.sendMessage(component, "SET_SYMBOL", triggerDict) == None):
        print "Set Symbol Failure" + component + ":" + symbol + ":" + str(value)
        return False
    else:
        return True

#Handle messages from other components
def handleMessage(messageID, args):
    retDict= {}
    if (messageID == "SET_SYMBOL"):
        print "handleMessage: Set Symbol"
        retDict= {"Return": "Success"}
        Database.setSymbolValue(args["Component"], args["Id"], args["Value"])
    else:
        retDict= {"Return": "UnImplemented Command"}
    return retDict
    
def destroyComponent(component):
	Database.setSymbolValue("tcpipIgmp", "TCPIP_USE_IGMP", False, 2)