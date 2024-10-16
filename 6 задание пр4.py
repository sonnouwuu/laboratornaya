'''Варианты 1-6: Вставьте нужную информацию в указанных местах в файле decoder for st.py.Программа должна вывести таблицу истинности дешифратора “2 в 4”.'''
# -*- coding: utf-8 -*- 
"""    
  дешифратор "2 в 4"  
""" from logelement import * 
 """--------------------------------------------- 
  Класс TDecoder - дешифратор "2 в 4" ---------------------------------------------""" 
class TDecoder(TLog2In):     def init(self): 
        TLog2In.init(self)          
    def calc(self):         self._res4 = not self.In1 and not self.In2 
        self._res2 = not self.In1 and self.In2         self._res1 = self.In1 and not self.In2 
        self._res3 = self.In1 and self.In2         
    def Output(self, no):         if no == 1: return self._res1 
        elif no == 2: return self._res2         elif no == 3: return self._res3 
        else: return self._res4      
#--------------------------------------------------- # Основная программа 
#---------------------------------------------------  
decoder = TDecoder()    
print(' C1 C0 | X3 X2 X1 X0'); print('---------------------'); 
   for C1 in range(2): 
    for C0 in range(2):         decoder.In1 = bool(C0) 
        decoder.In2 = bool(C1)         print('  ', int(C1), '  ', int(C0), 
              ' |  ', int(decoder.Output(3)),                '  ', int(decoder.Output(2)), 
               '  ', int(decoder.Output(1)),                '  ', int(decoder.Output(0)), sep="")
