"""Write a program to create a back up pf your folder by giving the
source folder and destination folder """
import os
import time

source = ['/Users/Radhika/Documents/Resumes']



target_dir = '/Users/Radhika/Backup'

target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'


zip_command = 'zip -r {0} {1}'.format(target,
                                      ' '.join(source))

print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
