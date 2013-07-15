# Copyright 2010-2013, Sikuli.org
# Released under the MIT License.
from org.sikuli.script import Env as JEnv
from org.sikuli.basics import HotkeyListener

class Env(JEnv):

    @classmethod
    def addHotkey(cls, key, modifiers, handler):
        class AnonyListener(HotkeyListener):
            def hotkeyPressed(self, event):
                handler(event)
        return JEnv.addHotkey(key, modifiers, AnonyListener())


