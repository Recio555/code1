# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 20:04:32 2024

@author: usuario
"""

import sys
from model import NameModel, TimeModel
from view import GreetingView

class GreetingController(object):
    
    def __init__(self):
        self.model = NameModel()
        self.time_model  = TimeModel()
        self.view = GreetingView()
        
        
    def handle(self, request):
        if self.model.get_name_list():
            if request in self.model.get_name_list():
                self.view.generate_greeting(
                    name=request,
                    time_of_day=self.time_model.get_time_of_day(),
                    known=True)
            else:
                self.model.save_name(request)
                self.view.generate_greeting(
                    name=request,
                    time_of_day=self.time_model.get_time_of_day(),
                    known=False
                    )
            
            
def main(name):
        request_handler = GreetingController()
        request_handler.handle(name)
if __name__ == "__main__":
    main(sys.argv[1])

































