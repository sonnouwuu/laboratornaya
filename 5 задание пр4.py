'''Получить таблицы истинности следующих логических функций(‘*’ - конъюнкция, ‘+’ - дизъюнкция, ‘→’ - импликация, ‘↔️’ - эквивалентность,
‘mod2’ – неравнозначность (предварительно формулы не упрощать!):1 (not B) mod2 C + A'''

class TLogElement:  """
  Базовый класс для иерархии классов логических элементов  Абстрактный класс.
  Свойства:    In1 - первый вход
    In2 - второй вход    Res - выход
  Методы:    calc - вычисление выхода, абстрактный метод
    link - установить связь выхода со следующим элементом в схеме  """
  def __init__(self):        self.__in1 = False
        self.__in2 = False        self._res = False
        class TNot(TLogElement):
  """  Элемент 'НЕ'.  
  Методы:     calc - вычисление выхода
  """  def __init__(self): 
        TLogElement.__init__(self)  def calc1(self):
        self._res = not self.In1        return self._res
class TLog2In(TLogElement):
  """  Базовый класс для иерархии классов логических элементов
  с двумя входами.    """
  pass
      class TOr(TLog2In):
  """  Элемент 'ИЛИ'.  
  Методы: calc - вычисление выхода  """
  def __init__(self):        TLog2In.__init__(self)
  def calc2(self):        
        self._res = self.In1 + self.In2        return self._res
   
class Mod2(TOr):  """
  Элемент 'Исключающее или'.    Методы: calc - вычисление выхода
  def calc(self):    self._res = self.In1 or self.In2"""
  def calc3(self):        self._res =self.calc2()% 2
        return self._res
  
print('a','b','c','1','2','3')
print('-----------')x=TNot()
y = Mod2()z=TOr()
for a in range(2):     for b in range(2):
         for c in range(2):             x.In1 =b
             y.In1=int(x.calc1())             z.In1=a
             z.In2=c             m=int(z.calc2())
             if m>0:                 n=1
             else:                 n=0
             y.In2=n             
             m=int(y.calc3())             if m>0:
                 n=1
             else:                 n=0
             f=n             print(a, b, c,y.In1,y.In2,f)
