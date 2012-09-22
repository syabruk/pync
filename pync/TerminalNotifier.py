#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import platform
import subprocess
import urllib
import shutil
from dateutil.parser import parse

LIST_FIELDS = ["group", "title", "sublitle", "message", "delivered_at"]


class TerminalNotifier(object):
    def __init__(self):
        """
        Raises if not supported on the current platform or if terminal-notifier.app does not find.
        """
        self.app_path = os.path.join(os.path.dirname(__file__), "vendor/terminal-notifier.app")
        self.bin_path = os.path.join(self.app_path, "Contents/MacOS/terminal-notifier")
        if not self.is_available:
            raise Exception("pync is only supported on Mac OS X 10.8, or higher.")
        if not os.path.exists(self.bin_path):
            self.__download_app()
        if not os.access(self.bin_path, os.X_OK):
            os.chmod(self.bin_path, 111)
            if not os.access(self.bin_path, os.X_OK):
                raise Exception("You have no privileges to execute \"%s\"" % self.bin_path)

    def __download_app(self):
        """ Downloads vendor/teminal-notifier.app from github.com/alloy """
        link = "https://github.com/downloads/alloy/terminal-notifier/terminal-notifier_1.4.2.zip"
        path_to_arch, _ = urllib.urlretrieve(link, link.split("/")[-1])
        path_to_folder = os.path.join("vendor", os.path.splitext(path_to_arch)[0])

        # why python resets permissions while unzipping?!
        # with zipfile.ZipFile(path_to_arch) as arch:
        #     arch.extractall()

        if subprocess.call("unzip -o -u -d vendor %s" % path_to_arch, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT):
            raise Exception("Error while unzip.")

        os.remove(path_to_arch)
        if os.path.exists(self.app_path):
            shutil.rmtree(self.app_path)

        try:
            shutil.move(os.path.join(path_to_folder, "terminal-notifier.app"), self.app_path)
        except shutil.Error:
            raise Exception("File already exists.")
        if os.path.exists(path_to_folder):
            shutil.rmtree(path_to_folder)

    def notify(self, message, **kwargs):
        """
        Sends a User Notification.

        The available options are `title`, `group`, `activate`, `open`, and
        `execute`. For a description of each option see:

          https://github.com/alloy/terminal-notifier/blob/master/README.markdown

        Examples are:

          Notifier = TerminalNotifier()

          Notifier.notify('Hello World')
          Notifier.notify('Hello World', title='Python')
          Notifier.notify('Hello World', group=os.getpid())
          Notifier.notify('Hello World', activate='com.apple.Safari')
          Notifier.notify('Hello World', open='http://github.com/')
          Notifier.notify('Hello World', execute='say "OMG"')
        """
        args = ['-message', message]
        args += [a for b in [("-%s" % arg, str(key)) for arg, key in kwargs.items()] for a in b]  # flatten list
        return self.execute(args)

    def execute(self, args):
        output = subprocess.Popen([self.bin_path, ] + args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if output.returncode:
            raise Exception("Some error during subprocess call.")
        return output

    def remove(self, group="ALL"):
        """
        Removes a notification that was previously sent with the specified
        ‘group’ ID, if one exists.

        If no ‘group’ ID is given, all notifications are removed.
        """
        return self.execute(["-remove", group])

    def list(self, group="ALL"):
        """
        If a ‘group’ ID is given, and a notification for that group exists,
        returns a dict with details about the notification.

        If no ‘group’ ID is given, an array of hashes describing all
        notifications.

        If no information is available this will return [].
        """
        output = self.execute(["-list", group]).communicate()[0]
        res = list()
        for line in output.splitlines()[1:]:
            res.append(dict(zip(LIST_FIELDS, line.split("\t"))))
            try:
                res[-1]["delivered_at"] = parse(res[-1]["delivered_at"])
            except ValueError:
                pass

        return res

    @staticmethod
    def is_available(self):
        """ Returns wether or not the current platform is Mac OS X 10.8, or higher."""
        return platform.system() == 'Darwin' and platform.mac_ver()[0] >= '10.8'

Notifier = TerminalNotifier()

if __name__ == '__main__':
    Notifier.notify("Notification from %s" % __file__, open="http://github.com")
