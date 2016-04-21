#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Java Bindings Generator
Copyright (C) 2012-2014 Matthias Bolte <matthias@tinkerforge.com>
Copyright (C) 2011-2013 Olaf Lüke <olaf@tinkerforge.com>

generate_json_bindings.py: Generator for Java bindings

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public
License along with this program; if not, write to the
Free Software Foundation, Inc., 59 Temple Place - Suite 330,
Boston, MA 02111-1307, USA.
"""

import datetime
import sys
import os

sys.path.append(os.path.split(os.getcwd())[0])
import common
import json


class JsonDevice(common.Device):

    def get_com(self):
        return self.raw_data

    def get_json_name(self):
        filename = self.raw_data['name'][0].lower()
        filename = filename .replace("/", "_").replace(" ", "_").replace("-", "").replace("2.0", "v2")
        return (self.raw_data['category'].lower()+"_"+filename+"_config")

        
class JsonBindingsGenerator(common.BindingsGenerator):
    released_files_name_prefix = 'json'

    def get_bindings_name(self):
        return 'json'

    def get_device_class(self):
        return JsonDevice

    def generate(self, device):

        filename = '{0}.json'.format(device.get_json_name())
       
        suffix = ''

        if self.is_matlab():
            suffix = '_matlab'
        elif self.is_octave():
            suffix = '_octave'

        jsonFile = open(os.path.join(self.get_bindings_root_directory(), 'bindings' + suffix, filename), 'wb')
        json.dump(device.raw_data, jsonFile, sort_keys=False, indent=4, separators=(',', ': '))
        jsonFile.close()

        if device.is_released():
            self.released_files.append(filename)

    def is_matlab(self):
        return False

    def is_octave(self):
        return False
        
        

def generate(bindings_root_directory):
    common.generate(bindings_root_directory, 'en', JsonBindingsGenerator)

if __name__ == "__main__":
    generate(os.getcwd())
    
