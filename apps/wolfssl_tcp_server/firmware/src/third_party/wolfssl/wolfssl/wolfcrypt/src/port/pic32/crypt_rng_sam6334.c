/**************************************************************************
  Crypto Framework Library Source

  Company:
    Microchip Technology Inc.

  File Name:
    random_same70.c

  Summary:
    Crypto Framework Library source for cryptographic functions.

  Description:
    This source file contains functions that make up the Cryptographic
	Framework Library for PIC32 families of Microchip micro-controllers.
**************************************************************************/

//DOM-IGNORE-BEGIN
/*****************************************************************************
 Copyright (C) 2017-2019 Microchip Technology Inc. and its subsidiaries.

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


#ifdef HAVE_CONFIG_H
    #include "config.h"
#endif
#include "configuration.h"
#if defined(WOLFSSL_HAVE_MCHP_HW_CRYPTO) && defined(WOLFSSL_HAVE_MCHP_HW_CRYPTO_TRNG_HW_6334) && defined(WOLFSSL_HAVE_MCHP_HW_RANDOM)

#include "wolfssl/wolfcrypt/settings.h"

#include "wolfssl/wolfcrypt/random.h"

#include "wolfssl/wolfcrypt/error-crypt.h"

#include "definitions.h"
#include "wolfssl/wolfcrypt/port/pic32/crypt_rng_hw.h"


#define RNG_BYTES_AT_A_TIME 4


int CRYPT_RNG_HwInit(void)
{
        /* enable */
#if defined(TRNG_CR_WAKEY_PASSWD)
        /* Enable Peripheral clock for TRNG in Power Management Controller */
#ifdef CRYPT_TRNG_HW_6334_A5D2
    uint32_t PmcBit = 1u << (ID_TRNG - 32);
    if ((PMC_REGS->PMC_PCSR1 & PmcBit) != PmcBit)
    {
        /* turn on */
        PMC_REGS->PMC_PCER1 = PmcBit;

        /* memory barrier */
        __DMB();
    }
#endif
    TRNG_REGS->TRNG_CR = TRNG_CR_WAKEY_PASSWD | TRNG_CR_ENABLE_Msk;        
#else
    TRNG_REGS->TRNG_CR = TRNG_CR_KEY_PASSWD | TRNG_CR_ENABLE_Msk;
#endif

    return 0;
}



/* sz is number of bytes */
int CRYPT_RNG_GenerateBlock(byte* output, word32 sz)
{
    while (sz)
    {
        /* get 32 bits - BLOCKING */
        while (!(TRNG_REGS->TRNG_ISR & TRNG_ISR_DATRDY_Msk))
        {
            /* Wait until data ready. */
        }

        /* get 32 bits */
        uint32_t result = TRNG_REGS->TRNG_ODATA;

        /* stuff the data into the output buffer. Watch for buffer overrun */
        if (sz < RNG_BYTES_AT_A_TIME)
        {
            memcpy((void *)output, (void*)&result, sz);
            sz = 0;
        }
        else
        {
            memcpy((void *)output, (void*)&result, RNG_BYTES_AT_A_TIME);
            sz -= RNG_BYTES_AT_A_TIME;

            /* bump the byte buffer by 4 since we are doing 32 bit randoms */
            output += RNG_BYTES_AT_A_TIME;
        }

        /* memory barrier */
        __DMB();
    }

    return 0;
}


int CRYPT_RNG_FreeRng(void)
{
    /* disable */
#if defined(TRNG_CR_WAKEY_PASSWD)
        TRNG_REGS->TRNG_CR = TRNG_CR_WAKEY_PASSWD | TRNG_CR_ENABLE_Msk;        
#else
        TRNG_REGS->TRNG_CR = TRNG_CR_KEY_PASSWD | TRNG_CR_ENABLE_Msk;
#endif

    /* Disable Peripheral Clock to TRNG by writing 1 to bit position */
    /* TRNG >=32 use PCDR1 not PCDR0 and remove 32 bit positions */

    return 0;
}



/* used by random.c */
int wc_GenerateSeed(OS_Seed* os, byte* output, word32 sz)
{
    int status;

    /* Make sure power is on, etc */
    status = CRYPT_RNG_HwInit();
    if (!status)
    {
        status = CRYPT_RNG_GenerateBlock(output, sz);
    }

    return status;
}


#endif
