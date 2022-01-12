import os
import time

for i in range(â)
      os.system("clear")
      op = int(input("Pilih salah satu option di bawah))
      print("1. install pip2 dan python2")
      print("2. install pip3 dan python3")
      print("3. Close")
      if op == 1:
            os.system("clear")
            print("please waitt")
            time.sleep(2)
            os.system("apt update -y && apt upgrade -y && apt install python2 -y && curl https://bootstrap.pypa.io/pip/2.7/get-pip.py--output get-pip.py && python2 get-pip.py")
             print("Instalasi Sukses")
             time.sleep(5)
      if op == 2:
            os.system("clear")
            print("please waitt")
            time.sleep(2)
            os.system("apt update -y && apt upgrade -y && apt install python pip")
            print("instalasi sukses,")
            time.sleep(5)
      if op == 3:
            brea