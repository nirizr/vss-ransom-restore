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
