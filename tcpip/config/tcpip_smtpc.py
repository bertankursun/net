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

    
def instantiateComponent(tcpipSmtpcComponent):
    print("TCPIP SMTP Client Component")
    configName = Variables.get("__CONFIGURATION_NAME")
    
    # Use SMTPC Client
    tcpipSmtpcClient = tcpipSmtpcComponent.createBooleanSymbol("TCPIP_USE_SMTPC_CLIENT", None)
    tcpipSmtpcClient.setLabel("Use SMTPC")
    tcpipSmtpcClient.setVisible(False)
    tcpipSmtpcClient.setDescription("Use SMTPC Client")
    tcpipSmtpcClient.setDefaultValue(True) 
    #tcpipSmtpcClient.setDependencies(tcpipSmtpcMenuVisibleSingle, ["tcpipTcp.TCPIP_USE_TCP"])

    # Number of Mail Connections to be Created
    tcpipSmtpcMailConnNum = tcpipSmtpcComponent.createIntegerSymbol("TCPIP_SMTPC_MAIL_CONNECTIONS", None)
    tcpipSmtpcMailConnNum.setLabel("Number of Mail Connections to be Created")
    tcpipSmtpcMailConnNum.setVisible(True)
    tcpipSmtpcMailConnNum.setDescription("Number of Mail Connections to be Created")
    tcpipSmtpcMailConnNum.setDefaultValue(2)
    #tcpipSmtpcMailConnNum.setDependencies(tcpipSmtpcMenuVisibleSingle, ["TCPIP_USE_SMTPC_CLIENT"])

    # String that Identifies the SMTPC Client Mail Date
    tcpipSmtpcClientMsgDate = tcpipSmtpcComponent.createStringSymbol("TCPIP_SMTPC_CLIENT_MESSAGE_DATE", None)
    tcpipSmtpcClientMsgDate.setLabel("String that Identifies the SMTPC Client Mail Date")
    tcpipSmtpcClientMsgDate.setVisible(True)
    tcpipSmtpcClientMsgDate.setDescription("String that Identifies the SMTPC Client Mail Date")
    tcpipSmtpcClientMsgDate.setDefaultValue("Wed, 20 July 2016 14:55:06 -0600")
    #tcpipSmtpcClientMsgDate.setDependencies(tcpipSmtpcMenuVisibleSingle, ["TCPIP_USE_SMTPC_CLIENT"])

    # General Server Response Timeout in seconds
    tcpipSmtpcServerReplyTimeout = tcpipSmtpcComponent.createIntegerSymbol("TCPIP_SMTPC_SERVER_REPLY_TIMEOUT", None)
    tcpipSmtpcServerReplyTimeout.setLabel("General Server Response Timeout, Seconds")
    tcpipSmtpcServerReplyTimeout.setVisible(True)
    tcpipSmtpcServerReplyTimeout.setDescription("General Server Response Timeout in seconds")
    tcpipSmtpcServerReplyTimeout.setDefaultValue(60)
    #tcpipSmtpcServerReplyTimeout.setDependencies(tcpipSmtpcMenuVisibleSingle, ["TCPIP_USE_SMTPC_CLIENT"])

    # Server Acknowledgment of the Mail Data: Body, Attachments etc. in Seconds
    tcpipSmtpcServerDataTimeout = tcpipSmtpcComponent.createIntegerSymbol("TCPIP_SMTPC_SERVER_DATA_TIMEOUT", None)
    tcpipSmtpcServerDataTimeout.setLabel("Server Acknowledgment of the Mail Data: Body, Attachments etc. Seconds")
    tcpipSmtpcServerDataTimeout.setVisible(True)
    tcpipSmtpcServerDataTimeout.setDescription("Server Acknowledgment of the Mail Data: Body, Attachments etc. in Seconds")
    tcpipSmtpcServerDataTimeout.setDefaultValue(60)
    #tcpipSmtpcServerDataTimeout.setDependencies(tcpipSmtpcMenuVisibleSingle, ["TCPIP_USE_SMTPC_CLIENT"])

    # Timeout for the TLS Handshake to Complete in seconds
    tcpipSmtpcTlsHandshakeTimeout = tcpipSmtpcComponent.createIntegerSymbol("TCPIP_SMTPC_TLS_HANDSHAKE_TIMEOUT", None)
    tcpipSmtpcTlsHandshakeTimeout.setLabel("Timeout for the TLS Handshake to Complete, Seconds")
    tcpipSmtpcTlsHandshakeTimeout.setVisible(True)
    tcpipSmtpcTlsHandshakeTimeout.setDescription("Timeout for the TLS Handshake to Complete in seconds")
    tcpipSmtpcTlsHandshakeTimeout.setDefaultValue(10)
    #tcpipSmtpcTlsHandshakeTimeout.setDependencies(tcpipSmtpcMenuVisibleSingle, ["TCPIP_USE_SMTPC_CLIENT"])

    # Number of Retries for Sending a Mail Message
    tcpipSmtpcMailRetryNum = tcpipSmtpcComponent.createIntegerSymbol("TCPIP_SMTPC_MAIL_RETRIES", None)
    tcpipSmtpcMailRetryNum.setLabel("Number of Retries for Sending a Mail Message")
    tcpipSmtpcMailRetryNum.setVisible(True)
    tcpipSmtpcMailRetryNum.setDescription("Number of Retries for Sending a Mail Message")
    tcpipSmtpcMailRetryNum.setDefaultValue(3)
    #tcpipSmtpcMailRetryNum.setDependencies(tcpipSmtpcMenuVisibleSingle, ["TCPIP_USE_SMTPC_CLIENT"])

    # The Retry Interval Because of a Server Transient Error in seconds
    tcpipSmtpcSrvrTransientRetryTimeout = tcpipSmtpcComponent.createIntegerSymbol("TCPIP_SMTPC_SERVER_TRANSIENT_RETRY_TIMEOUT", None)
    tcpipSmtpcSrvrTransientRetryTimeout.setLabel("The Retry Interval Because of a Server Transient Error, Seconds")
    tcpipSmtpcSrvrTransientRetryTimeout.setVisible(True)
    tcpipSmtpcSrvrTransientRetryTimeout.setDescription("The Retry Interval Because of a Server Transient Error in seconds")
    tcpipSmtpcSrvrTransientRetryTimeout.setDefaultValue(600)
    #tcpipSmtpcSrvrTransientRetryTimeout.setDependencies(tcpipSmtpcMenuVisibleSingle, ["TCPIP_USE_SMTPC_CLIENT"])

    # The Retry Interval Because of a SMTPC Temporary Error in seconds
    tcpipSmtpcInternRetryTimeout = tcpipSmtpcComponent.createIntegerSymbol("TCPIP_SMTPC_INTERNAL_RETRY_TIMEOUT", None)
    tcpipSmtpcInternRetryTimeout.setLabel("The Retry Interval Because of a SMTPC Temporary Error, Seconds")
    tcpipSmtpcInternRetryTimeout.setVisible(True)
    tcpipSmtpcInternRetryTimeout.setDescription("The Retry Interval Because of a SMTPC Temporary Error in seconds")
    tcpipSmtpcInternRetryTimeout.setDefaultValue(10)
    #tcpipSmtpcInternRetryTimeout.setDependencies(tcpipSmtpcMenuVisibleSingle, ["TCPIP_USE_SMTPC_CLIENT"])

    # Size of the RX Buffer for Processing the Server Replies
    tcpipSmtpcSrvrReplyBuffSize = tcpipSmtpcComponent.createIntegerSymbol("TCPIP_SMTPC_SERVER_REPLY_BUFFER_SIZE", None)
    tcpipSmtpcSrvrReplyBuffSize.setLabel("Size of the RX Buffer for Processing the Server Replies")
    tcpipSmtpcSrvrReplyBuffSize.setVisible(True)
    tcpipSmtpcSrvrReplyBuffSize.setDescription("Size of the RX Buffer for Processing the Server Replies")
    tcpipSmtpcSrvrReplyBuffSize.setDefaultValue(512)
    #tcpipSmtpcSrvrReplyBuffSize.setDependencies(tcpipSmtpcMenuVisibleSingle, ["TCPIP_USE_SMTPC_CLIENT"])

    # Size of a Buffer that Can Hold the 2 x Username and Password
    tcpipSmtpcClientAuthBuffSize = tcpipSmtpcComponent.createIntegerSymbol("TCPIP_SMTPC_CLIENT_AUTH_BUFFER_SIZE", None)
    tcpipSmtpcClientAuthBuffSize.setLabel("Size of a Buffer that Can Hold the 2 x Username and Password")
    tcpipSmtpcClientAuthBuffSize.setVisible(True)
    tcpipSmtpcClientAuthBuffSize.setDescription("Size of a Buffer that Can Hold the 2 x Username and Password")
    tcpipSmtpcClientAuthBuffSize.setDefaultValue(100)
    #tcpipSmtpcClientAuthBuffSize.setDependencies(tcpipSmtpcMenuVisibleSingle, ["TCPIP_USE_SMTPC_CLIENT"])

    # Size of a Buffer that Can Hold an Email Address: user@domain.smth
    tcpipSmtpcClientAddrBuffSize = tcpipSmtpcComponent.createIntegerSymbol("TCPIP_SMTPC_CLIENT_ADDR_BUFFER_SIZE", None)
    tcpipSmtpcClientAddrBuffSize.setLabel("Size of a Buffer that Can Hold an Email Address: user@domain.smth")
    tcpipSmtpcClientAddrBuffSize.setVisible(True)
    tcpipSmtpcClientAddrBuffSize.setDescription("Size of a Buffer that Can Hold an Email Address: user@domain.smth")
    tcpipSmtpcClientAddrBuffSize.setDefaultValue(80)
    #tcpipSmtpcClientAddrBuffSize.setDependencies(tcpipSmtpcMenuVisibleSingle, ["TCPIP_USE_SMTPC_CLIENT"])

    # Size of an Email Line when Sending the Email Body as Plain Text
    tcpipSmtpcPlainLineBuffSize = tcpipSmtpcComponent.createIntegerSymbol("TCPIP_SMTPC_PLAIN_LINE_BUFF_SIZE", None)
    tcpipSmtpcPlainLineBuffSize.setLabel("Size of an Email Line when Sending the Email Body as Plain Text")
    tcpipSmtpcPlainLineBuffSize.setVisible(True)
    tcpipSmtpcPlainLineBuffSize.setDescription("Size of an Email Line when Sending the Email Body as Plain Text")
    tcpipSmtpcPlainLineBuffSize.setDefaultValue(256)
    #tcpipSmtpcPlainLineBuffSize.setDependencies(tcpipSmtpcMenuVisibleSingle, ["TCPIP_USE_SMTPC_CLIENT"])

    # Size of the TX Buffer for the SMTPC Socket
    tcpipSmtpcSktTxBuffSize = tcpipSmtpcComponent.createIntegerSymbol("TCPIP_SMTPC_SKT_TX_BUFF_SIZE", None)
    tcpipSmtpcSktTxBuffSize.setLabel("Size of the TX Buffer for the SMTPC Socket")
    tcpipSmtpcSktTxBuffSize.setVisible(True)
    tcpipSmtpcSktTxBuffSize.setDescription("Size of the TX Buffer for the SMTPC Socket")
    tcpipSmtpcSktTxBuffSize.setDefaultValue(0)
    #tcpipSmtpcSktTxBuffSize.setDependencies(tcpipSmtpcMenuVisibleSingle, ["TCPIP_USE_SMTPC_CLIENT"])

    # Size of the RX Buffer for the SMTPC Socket
    tcpipSmtpcSktRxBuffSize = tcpipSmtpcComponent.createIntegerSymbol("TCPIP_SMTPC_SKT_RX_BUFF_SIZE", None)
    tcpipSmtpcSktRxBuffSize.setLabel("Size of the RX Buffer for the SMTPC Socket")
    tcpipSmtpcSktRxBuffSize.setVisible(True)
    tcpipSmtpcSktRxBuffSize.setDescription("Size of the RX Buffer for the SMTPC Socket")
    tcpipSmtpcSktRxBuffSize.setDefaultValue(0)
    #tcpipSmtpcSktRxBuffSize.setDependencies(tcpipSmtpcMenuVisibleSingle, ["TCPIP_USE_SMTPC_CLIENT"])

    # SMTPC Task Tick Rate in ms
    tcpipSmtpcTskTickRate = tcpipSmtpcComponent.createIntegerSymbol("TCPIP_SMTPC_TASK_TICK_RATE", None)
    tcpipSmtpcTskTickRate.setLabel("SMTPC Task Tick Rate in ms")
    tcpipSmtpcTskTickRate.setVisible(True)
    tcpipSmtpcTskTickRate.setDescription("SMTPC Task Tick Rate in ms")
    tcpipSmtpcTskTickRate.setDefaultValue(55)
    #tcpipSmtpcTskTickRate.setDependencies(tcpipSmtpcMenuVisibleSingle, ["TCPIP_USE_SMTPC_CLIENT"])

    # Use the Sample TCP/IP Console mail Command
    tcpipSmtpcMailCommand = tcpipSmtpcComponent.createBooleanSymbol("TCPIP_SMTPC_USE_MAIL_COMMAND", None)
    tcpipSmtpcMailCommand.setLabel("Use the Sample TCP/IP Console mail Command")
    tcpipSmtpcMailCommand.setVisible(True)
    tcpipSmtpcMailCommand.setDescription("Use the Sample TCP/IP Console mail Command")
    tcpipSmtpcMailCommand.setDefaultValue(False)
    #tcpipSmtpcMailCommand.setDependencies(tcpipSmtpcMenuVisibleSingle, ["TCPIP_USE_SMTPC_CLIENT"])

    tcpipSmtpcheapdependency = ["TCPIP_SMTPC_MAIL_CONNECTIONS", "tcpipStack.TCPIP_STACK_HEAP_CALC_MASK"]    
        
    # SMTPC Heap Size
    tcpipSmtpcHeapSize = tcpipSmtpcComponent.createIntegerSymbol("TCPIP_SMTPC_HEAP_SIZE", None)
    tcpipSmtpcHeapSize.setLabel("SMTPC Heap Size (bytes)") 
    tcpipSmtpcHeapSize.setVisible(False)
    tcpipSmtpcHeapSize.setDefaultValue(tcpipSmtpcHeapCalc())
    tcpipSmtpcHeapSize.setReadOnly(True)
    tcpipSmtpcHeapSize.setDependencies(tcpipSmtpcHeapUpdate, tcpipSmtpcheapdependency)  
    
    #Add to system_config.h
    tcpipSmtpcHeaderFtl = tcpipSmtpcComponent.createFileSymbol(None, None)
    tcpipSmtpcHeaderFtl.setSourcePath("tcpip/config/smtpc.h.ftl")
    tcpipSmtpcHeaderFtl.setOutputName("core.LIST_SYSTEM_CONFIG_H_MIDDLEWARE_CONFIGURATION")
    tcpipSmtpcHeaderFtl.setMarkup(True)
    tcpipSmtpcHeaderFtl.setType("STRING")

    # Add smtpc.c file
    tcpipSmtpcSourceFile = tcpipSmtpcComponent.createFileSymbol(None, None)
    tcpipSmtpcSourceFile.setSourcePath("tcpip/src/smtpc.c")
    tcpipSmtpcSourceFile.setOutputName("smtpc.c")
    tcpipSmtpcSourceFile.setOverwrite(True)
    tcpipSmtpcSourceFile.setDestPath("library/tcpip/src/")
    tcpipSmtpcSourceFile.setProjectPath("config/" + configName + "/library/tcpip/src/")
    tcpipSmtpcSourceFile.setType("SOURCE")
    tcpipSmtpcSourceFile.setEnabled(True)
    #tcpipSmtpcSourceFile.setDependencies(tcpipSmtpcGenSourceFile, ["TCPIP_USE_SMTPC_CLIENT"])
    

def tcpipSmtpcMenuVisibleSingle(symbol, event):
    if (event["value"] == True):
        print("SMTPC Menu Visible.")        
        symbol.setVisible(True)
    else:
        print("SMTPC Menu Invisible.")
        symbol.setVisible(False)

def tcpipSmtpcGenSourceFile(sourceFile, event):
    sourceFile.setEnabled(event["value"])

def tcpipSmtpcHeapCalc(): 
    numMailConn = Database.getSymbolValue("tcpipSmtpc","TCPIP_SMTPC_MAIL_CONNECTIONS")
    heap_size = numMailConn * 176
    return heap_size    
    
def tcpipSmtpcHeapUpdate(symbol, event): 
    heap_size = tcpipSmtpcHeapCalc()
    symbol.setValue(heap_size)
    if(event["id"] == "TCPIP_STACK_HEAP_CALC_MASK"):
        symbol.setVisible(event["value"])

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
    Database.setSymbolValue("tcpipSmtpc", "TCPIP_USE_SMTPC_CLIENT", False, 2)
    
