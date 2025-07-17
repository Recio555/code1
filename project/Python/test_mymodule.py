# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 17:06:38 2024

@author: usuario
"""



import unittest
import mymodule



class TestMyModule(unittest.TestCase):
     
    def test_sum(self):
         self.assertEqual(mymodule.Suma(5,7), 12)
         with self.assertRaises(TypeError):
             mymodule.Suma(5, "Python")
    
   
    
        
if __name__=='__main__':
    unittest.main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    