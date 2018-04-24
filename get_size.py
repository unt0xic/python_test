print('This is using getsize to see how much every file consumes')
print("---------------")
import os
from os.path import join, getsize
for root, dirs, files in os.walk('Y:\\python\\'):
    print (root, "consumes", sum(getsize(join(root, name)) for name in files), "bytes in", len(files), "non-directory files")
