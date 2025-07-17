# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 12:36:27 2024

@author: usuario
"""

import  smtplib
server = smatplib.SMTP('localhost')
server.sendmail('hnorecio@gmail.com,', 'hnorecio@gmail.com,', """ To: hnorecio@gmail.com,
                From: hnorecio@gmail.com
                Ojo al piojo
                """)