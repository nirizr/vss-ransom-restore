#!/usr/bin/env python
import win32com.client
import platform
import os


class ShadowCopy:
    def __init__(self):
        """
        Creates shadow copies for each local drive in the set drive_letters.
        """
        python_bits, _ = platform.architecture()
        os_bits = self.__get_os_bits()
        if not python_bits == os_bits:
            raise Exception("Architecture ERROR: Tool must be written for the "
                            "architecture it's running on. You're running on "
                            "a {} architecture with a {} executable. Please "
                            "run script with a python build similar to the "
                            "target machine architecture".format(os_bits,
                                                                 python_bits))

        self.__shadow_paths = self.__vss_list()

    def shadow_path(self, path):
        """
        Takes a regular file system path and transforms it into an
        equivalent path in a shadow copy
        """
        # TODO: validate path starts with a drive letter
        drive_letter = path[0]
        for shadow_path in self.__shadow_paths:
            new_path = path.replace(drive_letter + u':',
                                    shadow_path,
                                    1)
            # TODO: handle exact exception
            try:
                with open(new_path, 'rb'):
                    return new_path
            except:
                pass
        return None

    def __get_os_bits(self):
        try:
            os.environ["PROGRAMFILES(X86)"]
            return "64bit"
        except KeyError:
            return "32bit"

    def __get_wmi(self):
        wcd = win32com.client.Dispatch("WbemScripting.SWbemLocator")
        return wcd.ConnectServer(".")

    def __vss_list(self):
        query = "SELECT * FROM Win32_ShadowCopy ORDER BY InstallDate DESC"
        obj = self.__get_wmi().ExecQuery(query)
        return [o.DeviceObject for o in obj]
