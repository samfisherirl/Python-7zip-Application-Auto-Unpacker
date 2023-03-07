from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

base = 'console'

executables = [
    Executable('7zip-archive-self-extracting-archive.py', base=base)
]

setup(name='7zip-archive-self-extracting-archive.py',
      version = '7zip-archive-self-extracting-archive.py',
      description = '7zip-archive-self-extracting-archive.py',
      options = {'build_exe': build_options},
      executables = executables)
