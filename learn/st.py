import os
import time
sourse =['"C:\\saves"']
target_dir = 'E:\\save'
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S')+'.zip'
zip_command = "zip -qr {0} {1}".format(target,' '.join(sourse))

if os.system(zip_command)==0:
    print('Резервная копия успешно создана в',target)
else:
    print('Не удалось')