/*******************************************************************************
  Ethernet PHY Driver Configuration Definitions for the Template Version

  Company:
    Microchip Technology Inc.

  File Name:
    drv_ethphy_config.h

  Summary:
    Ethernet PHY driver configuration definitions template.

  Description:
    These definitions statically define the driver's mode of operation.
*******************************************************************************/

//DOM-IGNORE-BEGIN
/*****************************************************************************
 Copyright (C) 2013-2018 Microchip Technology Inc. and its subsidiaries.

Microchip Technology Inc. and its subsidiaries.

Subject to your compliance with these terms, you may use Microchip software 
and any derivatives exclusively with Microchip products. It is your 
responsibility to comply with third party license terms applicable to your 
use of third party software (including open source software) that may 
accompany Microchip software.

THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER 
EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED 
WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR 
PURPOSE.

IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE, 
INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND 
WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS 
BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE 
FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN 
ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY, 
THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
*****************************************************************************/

//DOM-IGNORE-END

#ifndef _DRV_ETHPHY_CONFIG_H
#define _DRV_ETHPHY_CONFIG_H

// *****************************************************************************
// *****************************************************************************
// Section: Initialization Overrides
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Ethernet PHY Negotiation Initiation time out

  Summary:
    Value of the PHY negotiation initiation time out as per IEEE 802.3 spec.

  Description:
    This definition sets the time out of the PHY negotiation initiation, in ms.

  Remarks:
    None.
*/

#define DRV_ETHPHY_NEG_INIT_TMO   (1)

// *****************************************************************************
/* Ethernet PHY Negotiation Complete time out

  Summary:
    Value of the PHY negotiation complete time out as per IEEE 802.3 spec.

  Description:
    This definition sets the time out of the PHY negotiation complete, in ms.

  Remarks:
    See IEEE 802.3 Clause 28 Table 28-9 autoneg_wait_timer value (max 1s).
*/

#define DRV_ETHPHY_NEG_DONE_TMO  (2000)

// *****************************************************************************
/* Ethernet PHY Reset self clear time out

  Summary:
    Value of the PHY Reset self clear time out as per IEEE 802.3 spec.

  Description:
    This definition sets the time out of the PHY Reset self clear, in ms.

  Remarks:
    See IEEE 802.3 Clause 22 Table 22-7 and paragraph "22.2.4.1.1 Reset" (max 0.5s)
*/

#define DRV_ETHPHY_RESET_CLR_TMO   (500)

// *****************************************************************************
// *****************************************************************************
// Section: Ethernet PHY Configuration
// *****************************************************************************
// *****************************************************************************

// *****************************************************************************
/* Ethernet PHY hardware instance configuration

  Summary:
    Selects the maximum number of hardware instances that can be supported by
    the dynamic driver.

  Description:
    This definition selects the maximum number of hardware instances that can be
    supported by the dynamic driver. Not defining it means using a static driver.

  Remarks:
    None.
*/

#define DRV_ETHPHY_INSTANCES_NUMBER                1


/*************************************************************************
  Summary:
    Selects the maximum number of clients.

  Description:
    Ethernet PHY Maximum Number of Clients
    This definition select the maximum number of clients that the Ethernet
    PHY driver can support at run time. Not defining it means using a
    single client.

  Remarks:
    The MAC driver is the only client of the PHY driver
    and the number of clients should always be 1.

  *************************************************************************/

#define DRV_ETHPHY_CLIENTS_NUMBER                1


// *****************************************************************************
/* Ethernet PHY Static Index Selection

  Summary:
    Ethernet PHY static index selection.

  Description:
    This definition selects the Ethernet PHY static index for the driver object
    reference.

  Remarks:
    This index is required to make a reference to the driver object.
*/

#define DRV_ETHPHY_INDEX                                DRV_ETHPHY_INDEX_1


// *****************************************************************************
/* Ethernet PHY Interrupt And Polled Mode Operation Control

*/
// Ethernet PHY has no interrupts
//#define DRV_ETHPHY_INTERRUPT_MODE          true


// *****************************************************************************
// *****************************************************************************
// Section: Initialization Overrides
// *****************************************************************************
// *****************************************************************************
/* This section defines the initialization overrides */

// *****************************************************************************
/* Ethernet PHY Peripheral ID Selection

  Summary:
    Defines an override of the peripheral ID.

  Description:
    Defines an override of the peripheral ID, using macros.

  Remarks:

    Note: Some devices also support ETHPHY_ID_0
*/

#define DRV_ETHPHY_PERIPHERAL_ID                         ETHPHY_ID_1


// *****************************************************************************
/* Ethernet PHY power state configuration

  Summary:
    Defines an override of the power state of the Ethernet PHY driver.

  Description:
    Defines an override of the power state of the Ethernet PHY driver.

  Remarks:
    Note: This feature may not be available in the device or the Ethernet PHY module
    selected.
*/

// Has no power modes
//#define DRV_ETHPHY_POWER_STATE                 SYS_MODULE_POWER_IDLE_STOP


#endif // #ifndef _DRV_ETHPHY_CONFIG_H

/*******************************************************************************
 End of File
*/

