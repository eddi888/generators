#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Delphi Documentation Generator
Copyright (C) 2012 Matthias Bolte <matthias@tinkerforge.com>
Copyright (C) 2011 Olaf Lüke <olaf@tinkerforge.com>

generator_delphi_doc.py: Generator for Delphi documentation

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

import sys
import os
import shutil
import subprocess
import glob
import re
import delphi_common

sys.path.append(os.path.split(os.getcwd())[0])
import common

device = None
lang = 'en'
file_path = ''

def fix_links(text):
    cls = device.get_category() + device.get_camel_case_name()
    for packet in device.get_packets():
        name_false = ':func:`{0}`'.format(packet.get_camel_case_name())
        name = packet.get_camel_case_name()
        if packet.get_type() == 'callback':
            name_right = ':delphi:func:`On{1} <T{0}.On{1}>`'.format(cls, name)
        else:
            name_right = ':delphi:func:`{1} <T{0}.{1}>`'.format(cls, name)
        text = text.replace(name_false, name_right)

    text = text.replace(":word:`parameter`", "parameter")
    text = text.replace(":word:`parameters`", "parameters")

    return text

def make_examples():
    def title_from_file(f):
        f = f.replace('Example', '')
        f = f.replace('.pas', '')
        return common.camel_case_to_space(f)

    return common.make_rst_examples(title_from_file, device, file_path,
                                    'delphi', 'Example', '.pas', 'Delphi')

def make_methods(typ):
    version_method = """
.. delphi:function:: procedure T{0}.GetVersion(out name: string; out firmwareVersion: TDeviceVersion; out bindingVersion: TDeviceVersion)

 Returns the name (including the hardware version), the firmware version
 and the binding version of the device. The firmware and binding versions
 are given in arrays of size 3 with the syntax (major, minor, revision).

 The returned array contains name, firmwareVersion and bindingVersion.
"""

    methods = ''
    function = '.. delphi:function:: function T{0}.{1}({2}): {3}\n{4}'
    procedure = '.. delphi:function:: procedure T{0}.{1}({2})\n{3}'
    cls = device.get_category() + device.get_camel_case_name()
    for packet in device.get_packets('function'):
        if packet.get_doc()[0] != typ:
            continue

        ret_type = delphi_common.get_return_type(packet, True)
        name = packet.get_camel_case_name()
        params = delphi_common.make_parameter_list(packet, True)
        desc = fix_links(common.shift_right(packet.get_doc()[1][lang], 1))
        if len(ret_type) > 0:
            method = function.format(cls, name, params, ret_type, desc)
        else:
            method = procedure.format(cls, name, params, desc)
        methods += method + '\n'

    if typ == 'am':
        methods += version_method.format(cls)

    return methods

def make_callbacks():
    cbs = ''
    cb = """.. delphi:function:: property T{0}.On{1}

 .. code-block:: delphi

  procedure({2}) of object;

{3}
"""

    cls = device.get_category() + device.get_camel_case_name()
    for packet in device.get_packets('callback'):
        name = packet.get_camel_case_name()
        params = delphi_common.make_parameter_list(packet, True)
        desc = fix_links(common.shift_right(packet.get_doc()[1][lang], 1))
        cbs += cb.format(cls, name, params, desc)

    return cbs

    cbs = ''
    func_start = '.. delphi:attribute:: int '
    cls = device.get_category() + device.get_camel_case_name()
    for packet in device.get_packets('callback'):
        params = delphi_common.make_parameter_list(packet, True)
        desc = fix_links(common.shift_right(packet.get_doc()[1][lang], 1))

        signature = """
 .. delphi:function:: void callback({0})
    :noindex:
""".format(params)

        func = '{0}{1}.CALLBACK_{2}\n{3}{4}'.format(func_start,
                                                     cls,
                                                     packet.get_upper_case_name(),
                                                     signature,
                                                     desc)
        cbs += func + '\n'

    return cbs

def make_api():
    create_str = """
.. delphi:function:: constructor T{3}{1}.Create(const uid: string)

 Creates an object with the unique device ID *uid*:

 .. code-block:: delphi

    {0} := T{3}{1}.Create('YOUR_DEVICE_UID');

 This object can then be added to the IP connection (see examples
 :ref:`above <{0}_{2}_delphi_examples>`).
"""

    bm_str = """
Basic Methods
^^^^^^^^^^^^^

{0}

{1}
"""

    am_str = """
Advanced Methods
^^^^^^^^^^^^^^^^

{0}
"""

    ccm_str = """
Callback Configuration Methods
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

{0}
"""

    c_str = """
.. _{1}_{2}_delphi_callbacks:

Callbacks
^^^^^^^^^

*Callbacks* can be registered to receive time critical or recurring data from
the device. The registration is done by assigning a procedure to an callback
property of the device object:

 .. code-block:: delphi

  procedure TExample.MyCallback(const param: word);
  begin
    WriteLn(param);
  end;

  {1}.OnExample := {{$ifdef FPC}}@{{$endif}}example.MyCallback;

The available callback property and their type of parameters are described below.

 .. note::
  Using callbacks for recurring events is *always* prefered
  compared to using getters. It will use less USB bandwith and the latency
  will be a lot better, since there is no roundtrip time.

{0}
"""

    api = """
{0}
API
---

Since Delphi does not support multiple return values directly, we use the out
keyword to return multiple values from a function.

All functions and procedures listed below are thread-safe.

{1}

{2}
"""
    cre = create_str.format(device.get_underscore_name(),
                            device.get_camel_case_name(),
                            device.get_category().lower(),
                            device.get_category())

    bm = make_methods('bm')
    am = make_methods('am')
    ccm = make_methods('ccm')
    c = make_callbacks()
    api_str = ''
    if bm:
        api_str += bm_str.format(cre, bm)
    if am:
        api_str += am_str.format(am)
    if c:
        api_str += ccm_str.format(ccm)
        api_str += c_str.format(c, device.get_underscore_name(), device.get_category().lower(),
                                device.get_category(), device.get_camel_case_name())

    ref = '.. _{0}_{1}_delphi_api:\n'.format(device.get_underscore_name(),
                                          device.get_category().lower())

    api_desc = ''
    try:
        api_desc = device.com['api']
    except:
        pass

    return api.format(ref, api_desc, api_str)

def copy_examples_for_zip():
    examples = common.find_examples(device, file_path, 'delphi', 'Example', '.pas')
    dest = os.path.join('/tmp/generator/examples/',
                        device.get_category(),
                        device.get_camel_case_name())

    if not os.path.exists(dest):
        os.makedirs(dest)

    for example in examples:
        shutil.copy(example[1], dest)

def make_files(com_new, directory):
    global device
    device = common.Device(com_new)

    file_name = '{0}_{1}_Delphi'.format(device.get_camel_case_name(), device.get_category())

    directory += '/doc'
    if not os.path.exists(directory):
        os.makedirs(directory)

    f = file('{0}/{1}.rst'.format(directory, file_name), "w")
    f.write(common.make_rst_header(device, 'delphi', 'Delphi'))
    f.write(common.make_rst_summary(device, 'Delphi bindings'))
    f.write(make_examples())
    f.write(make_api())

    copy_examples_for_zip()

def generate(path):
    global file_path
    file_path = path
    path_list = path.split('/')
    path_list[-1] = 'configs'
    path_config = '/'.join(path_list)
    sys.path.append(path_config)
    configs = os.listdir(path_config)

    # Make temporary generator directory
    if os.path.exists('/tmp/generator'):
        shutil.rmtree('/tmp/generator/')
    os.makedirs('/tmp/generator/bindings')
    os.chdir('/tmp/generator/bindings')

    for config in configs:
        if config.endswith('_config.py'):
            module = __import__(config[:-3])
            print(" * {0}".format(config[:-10]))
            make_files(module.com, path)

    # Copy bindings and readme
    for filename in glob.glob(path + '/bindings/*.pas'):
        shutil.copy(filename, '/tmp/generator/bindings')

    shutil.copy(path + '/Base58.pas', '/tmp/generator/bindings')
    shutil.copy(path + '/BlockingQueue.pas', '/tmp/generator/bindings')
    shutil.copy(path + '/Device.pas', '/tmp/generator/bindings')
    shutil.copy(path + '/IPConnection.pas', '/tmp/generator/bindings')
    shutil.copy(path + '/LEConverter.pas', '/tmp/generator/bindings')
    shutil.copy(path + '/TimedSemaphore.pas', '/tmp/generator/bindings')
    shutil.copy(path + '/changelog.txt', '/tmp/generator/')
    shutil.copy(path + '/readme.txt', '/tmp/generator/')

    # Make zip
    version = common.get_changelog_version(path)
    common.make_zip('delphi', '/tmp/generator', path, version)

if __name__ == "__main__":
    generate(os.getcwd())
