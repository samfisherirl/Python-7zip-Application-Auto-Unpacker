from pathlib import Path
import subprocess
from time import sleep

cwd = Path.cwd() # working dir
cwd = cwd / 'exports' 
# exports C:\__mainfile__\exports\__7zip-file__
# change to subfolder to prevent files going everywhere on extract

sevenz = cwd /  '7za.exe'
file = cwd / 'exports.7z' # my app archive
sevenz_cmd = ['PowerShell.exe', sevenz, 'x', file, '-y', '-p321']

file_to_run = cwd / 'Steam_VDF_Main.exe' # my app


def powershell(cmd):

  p = subprocess.Popen(cmd, shell=True, cwd=cwd, stdout=subprocess.PIPE)
  print(p.stdout) 
  # Wait for the process to terminate and collect its stdout and stderr output.
  p_out, p_err = p.communicate() 
  # Split the single multi-line string that contains the links
  # into individual lines.
  lines = p_out.splitlines() 
  print(lines)

if __name__ == '__main__':
  powershell(sevenz_cmd) 
  # exported, now check for file existance 
  for i in range(0, 10):
    if file_to_run.is_file(): 
      # does file exist (sometimes file can take time to export)
      powershell([file_to_run])
      # if exist, run app in archive
    else:
      sleep(1)
      print('\n\nwaiting for export from else')

