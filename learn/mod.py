import os
import sys
name = sys.platform
for i in range(1, 6):
    new_path= os.path.join(os.getswd(), '{}_{}'.format(name, i))
    os.mkdir(new_path)