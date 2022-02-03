#!/usr/bin/env python
import rumps

class Notch(rumps.App):
    """Add a software notch to any Mac"""
    def __init__(self):
        center = " "*69
        super().__init__(name=self.__class__.__name__, title=center, icon="img.png")
        self._icon_nsimage.setSize_((180, 24))

Notch().run()
