# vss-ransom-restore
A VSS-based restoration tool created specifically for restoring files encrypted by ransomware from Windows' Virtual Shadow Service.

This tool is "special" only for providing easily accessible functionality tailored to restoring files previously encrypted by ransomware.

Such features as:

1. Instead of restoring state of all files, only files matched against a regular expression are considered as files to restore. (i.e. only cosider on-disk-files with the `.crypt` extension for restoration)
2. files to restore will be applied another regular expression before searched for in the VSS. (i.e. of files found on disk with the `.crypt` extension, find and restore files with that extension stipped in VSS)
3. instead of restoring a specific snapshot, this script walks over *all* snapshot states to find missing files. Files that we're deleted or partially valid snapshots will not interfere with successful restoration.
4. Control over location of restored files is available, to easily collect all restored files in a single location for easy machine reimaging.
5. Provides statistics of number of restored files compared to number of encrypted files.
6. Deliverable as an executable to avoid any dependancies for easily deployment on multiple machines.

## Usage caveats

There are several caveats to using, especially when building the tool using PyInstaller. They're listed here for future referance:

1. PyInstaller does not currently support Python 3.6 or Python 2.X. You'll need to install a Python version in between those two for now.
2. To use pywin32, especially when packaging it with PyInstaller, you might need to install "Microsoft Visual C++ 2010 Redistributable Package" or manually install pywin32. For more details see [this github issue][1].
3. You'll need a version made using Python of the same architecture "bitness" (64bit vs 32bit) you're intending to run the tool on. If you need to run it on both 32 and 64 bit machines, you'll need to isntall 32bit AND 64bit versions of python on a 64bit machine and build the tool twice.


[1]: https://github.com/pyinstaller/pyinstaller/issues/1840
