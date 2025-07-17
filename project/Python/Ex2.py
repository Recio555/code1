# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 13:47:04 2024

@author: usuario
"""

import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')
asyncio.run(main())
