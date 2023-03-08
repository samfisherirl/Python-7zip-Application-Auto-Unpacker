from pathlib import Path
import subprocess
from time import sleep

cwd = Path.cwd() # working dir
cwd = cwd / 'exports' 

################################################
# exports C:\__mainfile__\exports\__7zip-file__
# this script == '__mainfile__'
################################################


sevenz = cwd /  '7za.exe'
file = cwd / 'exports.7z' # my app archive

#########################################################################
sevenz_cmd = ['PowerShell.exe', sevenz, 'x', file, '-y', '-p321']
# 7Zip commands above:
# x == extract with full paths 
# -y == suppress all prompts
# f'-p{password}' password for archive,
# follows the lowercase '-p'. '321' is the password. as weird as it looks. 
##########################################################################


file_to_run = cwd / 'Steam_VDF_Main.exe' # my app


def run_powershell(cmd):

  p = subprocess.Popen(cmd, shell=True, cwd=cwd, stdout=subprocess.PIPE)
  print(p.stdout) 
  # Wait for the process to terminate and collect its stdout and stderr output.
  p_out, p_err = p.communicate() 
  # Split the single multi-line string that contains the links
  # into individual lines.
  lines = p_out.splitlines() 
  print(lines)

def is_extraction_complete(file_to_run):
  for i in range(0, 10):
    if file_to_run.is_file(): 
      # if exist, run app in archive
      return True
    else:
      sleep(1)
      print('\n\nwaiting for export from else statement')
  return False
  
  def main():

    run_powershell(sevenz_cmd) 
    # does file exist (sometimes file can take time to export)  
    if is_extraction_complete(file_to_run):
        # run File
        run_powershell([file_to_run])
    else:
      print("\n\nError, file designated to run was not found.")

if __name__ == '__main__':
  main()
