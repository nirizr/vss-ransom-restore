import sys
import os
import string
import re
import shutil
import traceback

import argh
import vss


def get_drives():
  return ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]


def find_files(drive, regex):
  path = "{}:\\".format(drive)
  for root, _, files in os.walk(path):
    for f in files:
      result = regex.search(f)
      if result:
        yield os.path.join(root, f)


def restore_drive(drive, vss, regex, quiet=False):
  print("Restoring drive {}".format(drive))
  successful = 0
  total = 0
  for encrypted_file in find_files(drive, regex):
    total += 1
    original_file = os.path.splitext(encrypted_file)[0]
    try:
      vss_file = vss.shadow_path(original_file)
    except:
      print("Original file: {}".format(original_file))
      print("ERROR: failed converting to VSS name")
      traceback.print_exc(file=sys.stdout)
      continue
    restored_file = os.path.splitext(original_file)[0] + ".restored" + os.path.splitext(original_file)[1]
    try:
      with open(vss_file, 'rb') as vss_fh:
        with open(restored_file, 'wb') as restored_fh:
          shutil.copyfileobj(vss_fh, restored_fh)
          successful += 1
          print("Successfully restored file at {}".format(restored_file))
    except:
      if not quiet:
        print("Restoring file {}".format(encrypted_file))
        print("Original file: {}".format(original_file))
        print("VSS file: {}".format(vss_file))
        print("Restored file: {}".format(restored_file))
        print("ERROR: failed restoring above file!")
        traceback.print_exc(file=sys.stdout)
  print("Finished restoring attempt. Found {} files, restored {}".format(total, successful))


def main(extension="moments2900", regex=None, quiet=False):
  drives = get_drives()
  print("Found following drives: {}".format(drives))

  if not regex:
    print("Looking for extension: {}".format(extension))
    regex = "\.{}$".format(extension)

  regex = re.compile(regex)

  vss = vss.ShadowCopy()
  for drive in drives:
    handle_drive(drive, vss, regex, quiet)


if __name__ == "__main__":
  argh.dispatch_command(main)
