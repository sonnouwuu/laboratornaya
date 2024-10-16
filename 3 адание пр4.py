'''Составьте иерархию классов модуля logelement.py после добавленияв про-грамму функций «исключающее ИЛИ», «И-НЕ» и «ИЛИ-НЕ», «импликация».'''
# -*- coding: utf-8 -*-"""

def __init__(self):
    self.__in1 = False
    self.__in2 = False
    self._res = False
    self.__nextEl = None
    self.__nextIn = 0
# hasattr (<Объект>, <Атрибут>) – проверяет наличие указанного атрибута Если 
# атрибут существует, функция возвращает значение True.  
def __setIn1(self, newIn1):
    self.__in1 = newIn1
    self.calc()
    if self.__nextEl:
            if self.__nextIn == 1:
                self.__nextEl.In1 = self._res
            elif self.__nextIn == 2:
                __nextEl.In2 = self._res
    def __setIn2(self, newIn2):
        self.__in2 = newIn2
        self.calc()    
        if self.__nextEl:
            if self.__nextIn == 1:
                self.__nextEl.In1 = self._res
            elif self.__nextIn == 2:
                self.__nextEl.In2 = self._res  
    def link(self, nextEl, nextIn):
      self.__nextEl = nextEl
      self.__nextIn = nextIn
      In1 = property(lambda x: x.__in1, __setIn1)
      In2 = property(lambda x: x.__in2, __setIn2)
      Res = property(lambda x: x._res)
class TNot(TLogElement):
   def __init__(self): 
        TLogElement.__init__(self)
        def calc1(self):
          self._res = not self.In1
        return self._res
class TLog2In(TLogElement):
  """  Базовый класс для иерархии классов логических элементов
  с двумя входами.    """
  pass
class TAnd(TLog2In):  """
  Элемент 'И'.    Методы: calc - вычисление выхода
  """
def __init__(self):
        TLog2In.__init__(self)
def calc2(self):
      self._res = self.In1 * self.In2
      return self._res      
class TOr(TLog2In):  """
  Элемент 'ИЛИ'.    Методы: calc - вычисление выхода
  """
def __init__(self):
        TLog2In.__init__(self)
        def calc3(self):
          self._res = self.In1 + self.In2
        return self._res
class TOrNot(TOr,TNot):
  """  Элемент 'ИЛИ-НЕ'.  
  Методы: calc - вычисление выхода  """
  def calc4(self):
      self.In1 =self.calc3()
      self._res=self.calc1()         
      return self._res   
class TAndNot(TLogElement):  """
  Элемент 'И-НЕ'.  
  Методы: calc - вычисление выхода  """
def calc5(self):
      self._res=self.In1 * self.In2
      self._res=not self._res
      return self._res
class Mod2(TOr,TNot):
  """  Элемент 'Исключающее или'.  
  Методы: calc - вычисление выхода  def calc(self):
    self._res = self.In1 or self.In2"""
  def calc6(self):
      self._res =self.calc3()% 2
      return self._res
  
print('not')
n=TNot()
n.In1 =Trueprint(n._res)
print('')
print('mod2')
x = Mod2()
print ('-------------------')
for a in range(2):
     x.In1 = bool(a)
     for b in range(2):
         x.In2 = bool(b)
         x.calc6()
         print(a, b, int(x._res))
         
print('')
print('AndNot')
print ('-------------------')
x=TAndNot()
for a in range(2):
    x.In1 = (a)
    for b in range(2):
         x.In2 = (b)
         x.calc5()
         print(a, b, int(x._res))
print('')
print('OrNot')
print ('-------------------')
x=TOrNot()
for a in range(2):
     x.In1 = (a)
     for b in range(2):
         x.In2 = (b)
         x.calc4()
         print(a, b, int(x._res))
