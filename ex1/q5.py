#!/usr/bin/env python3

from datetime import datetime

now = datetime.now()

print(now, end='\n')
print(now.strftime("%x"), end='\n')
print(now.strftime("%X"), end='\n')
