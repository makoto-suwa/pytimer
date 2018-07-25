# coding:utf-8
import string
import datetime
import threading
import time

class pycolor:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    END = '\033[0m'
    BOLD = '\038[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE = '\033[07m'

now = datetime.datetime.now()

print("-------You launched Red-Pomodoro! YogaFlame-------")
print("Start:1, Stop:0, Cancel:9")

class TimerClass(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.event = threading.Event()
    self.count = 20

  def run(self):
    while self.count > 0 and not self.event.is_set():
      if self.count == 1:
        print('1')
        print('Your Work is done!! {0:%Y/%m/%d %H:%M} Push 0'.format(now))
        break
      elif self.count % 3 ==0:
        print pycolor.PURPLE + "■■■■■■■■■■" + pycolor.END
        self.event.wait(6)
        print pycolor.PURPLE + "■■■■■■■■" + pycolor.END
        self.event.wait(6)
        print pycolor.PURPLE + "■■■■■■" + pycolor.END
        self.event.wait(6)
        print pycolor.PURPLE + "■■■■" + pycolor.END
        self.event.wait(6)
        print pycolor.PURPLE + "■■■" + pycolor.END
        self.event.wait(6)
        print pycolor.PURPLE + "■■" + pycolor.END
        self.event.wait(6)
        print pycolor.PURPLE + "■" + pycolor.END
        self.event.wait(6)
        self.count -= 1
      else:
        print (self.count)
        self.count -= 1
        self.event.wait(70)

  def stop(self):
    self.event.set()


tmr = TimerClass()

while True:
  inputNum = input()
  if int(inputNum) == 1:
    print("OK! 20 minutes timer started!")
    tmr.start()
    time.sleep(1)

  elif int(inputNum) == 0:
    tmr.stop()
    print("Write down ticket number below...(Chores.7月->#20197)")
    input_num = raw_input('#')
    print ('')
    print("Write down comment below...")
    input_word = raw_input('')
    print ('')
    print ("The number is 【" + input_num + "】  Comment is [ " + input_word + " ]")
    break

  else:
    print("Canceled!")
    tmr.stop()
    break
