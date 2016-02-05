# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# CAN Bricklet communication config

com = {
    'author': 'Matthias Bolte <matthias@tinkerforge.com>',
    'api_version': [2, 0, 0],
    'category': 'Bricklet',
    'device_identifier': 270,
    'name': ('CAN', 'CAN', 'CAN Bricklet'),
    'manufacturer': 'Tinkerforge',
    'description': {
        'en': 'Communicates with CAN devices',
        'de': 'Kommuniziert mit CAN Geräten'
    },
    'released': False,
    'packets': [],
    'examples': []
}

com['packets'].append({
'type': 'function',
'name': 'Write Frame',
'elements': [('Frame Type', 'uint8', 1, 'in', ('Frame Type', [('Standard Data', 0),
                                                              ('Standard Remote', 1),
                                                              ('Extended Data', 2),
                                                              ('Extended Remote', 3)])),
             ('Identifier', 'uint32', 1, 'in'),
             ('Data', 'uint8', 8, 'in'),
             ('Length', 'uint8', 1, 'in'),
             ('Success', 'bool', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Read Frame',
'elements': [('Success', 'bool', 1, 'out'),
             ('Frame Type', 'uint8', 1, 'out', ('Frame Type', [('Standard Data', 0),
                                                               ('Standard Remote', 1),
                                                               ('Extended Data', 2),
                                                               ('Extended Remote', 3)])),
             ('Identifier', 'uint32', 1, 'out'),
             ('Data', 'uint8', 8, 'out'),
             ('Length', 'uint8', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Configuration',
'elements': [('Baud Rate', 'uint8', 1, 'in', ('Baud Rate', [('10000', 0),
                                                            ('20000', 1),
                                                            ('50000', 2),
                                                            ('125000', 3),
                                                            ('250000', 4),
                                                            ('500000', 5),
                                                            ('800000', 6),
                                                            ('1000000', 7)])),
             ('Transceiver', 'uint8', 1, 'in', ('Transceiver Mode', [('Normal', 0),
                                                                     ('Loopback', 1),
                                                                     ('Read Only', 2)])),
             ('Write Timeout', 'int32', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
""",
'de':
"""
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Configuration',
'elements': [('Baud Rate', 'uint8', 1, 'out', ('Baud Rate', [('10000', 0),
                                                             ('20000', 1),
                                                             ('50000', 2),
                                                             ('125000', 3),
                                                             ('250000', 4),
                                                             ('500000', 5),
                                                             ('800000', 6),
                                                             ('1000000', 7)])),
             ('Transceiver Mode', 'uint8', 1, 'out', ('Transceiver Mode', [('Normal', 0),
                                                                           ('Loopback', 1),
                                                                           ('Read Only', 2)])),
             ('Write Timeout', 'int32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the configuration as set by :func:`SetConfiguration`.
""",
'de':
"""
Gibt die Konfiguration zurück, wie von :func:`SetConfiguration` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Error',
'elements': [('Error Mask', 'uint32', 1, 'out', ('Error', [('Read Register Full', 1),
                                                           ('Read Buffer Full', 2)]))],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
""",
'de':
"""
"""
}]
})
