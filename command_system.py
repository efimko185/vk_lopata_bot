from datetime import datetime

command_list = []

def date():
  global dat
  dat = datetime.strftime(datetime.now(), "[%Y.%m.%d][%H:%M:%S]")

class Command:
  def __init__(self):
    self.__keys = []
    self.admin_keys = []
    self.description = ''
    self.admin_description = ''
    command_list.append(self)

  @property
  def keys(self):
    return self.__keys

  @keys.setter
  def keys(self, mas):
    for k in mas:
      self.__keys.append(k.lower())

  def process(self):
    pass

