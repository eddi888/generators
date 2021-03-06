# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# GPS Bricklet communication config

com = {
    'author': 'Olaf Lüke <olaf@tinkerforge.com>',
    'api_version': [2, 0, 1],
    'category': 'Bricklet',
    'device_identifier': 222,
    'name': ('GPS', 'GPS', 'GPS Bricklet'),
    'manufacturer': 'Tinkerforge',
    'description': {
        'en': 'Determine position, velocity and altitude using GPS',
        'de': 'Bestimmt Position, Geschwindigkeit und Höhe mittels GPS'
    },
    'released': True,
    'packets': [],
    'examples': []
}

com['packets'].append({
'type': 'function',
'name': 'Get Coordinates',
'elements': [('Latitude', 'uint32', 1, 'out'),
             ('NS', 'char', 1, 'out'),
             ('Longitude', 'uint32', 1, 'out'),
             ('EW', 'char', 1, 'out'),
             ('PDOP', 'uint16', 1, 'out'),
             ('HDOP', 'uint16', 1, 'out'),
             ('VDOP', 'uint16', 1, 'out'),
             ('EPE', 'uint16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the GPS coordinates. Latitude and longitude are given in the
``DD.dddddd°`` format, the value 57123468 means 57.123468°.
The parameter ``ns`` and ``ew`` are the cardinal directions for
latitude and longitude. Possible values for ``ns`` and ``ew`` are 'N', 'S', 'E'
and 'W' (north, south, east and west).

PDOP, HDOP and VDOP are the dilution of precision (DOP) values. They specify
the additional multiplicative effect of GPS satellite geometry on GPS 
precision. See 
`here <https://en.wikipedia.org/wiki/Dilution_of_precision_(GPS)>`__
for more information. The values are give in hundredths.

EPE is the "Estimated Position Error". The EPE is given in cm. This is not the
absolute maximum error, it is the error with a specific confidence. See
`here <http://www.nps.gov/gis/gps/WhatisEPE.html>`__ for more information.

This data is only valid if there is currently a fix as indicated by
:func:`GetStatus`.
""",
'de':
"""
Gibt die GPS Koordinaten zurück. Breitengrad und Längengrad werden im Format
``DD.dddddd°`` angegeben, der Wert 57123468 bedeutet 57,123468°.
Die Parameter ``ns`` und ``ew`` sind Himmelsrichtungen für
Breiten- und Längengrad. Mögliche Werte für ``ns`` und ``ew`` sind 'N', 'S', 'E'
und 'W' (Nord, Süd, Ost, West).

PDOP, HDOP und VDOP sind die "Dilution Of Precision" (DOP) Werte. Sie
spezifizieren die zusätzlichen multiplikativen Effekte von der GPS
Satellitengeometrie auf die GPS-Präzision.
`hier <https://en.wikipedia.org/wiki/Dilution_of_precision_(GPS)>`__ gibt
es mehr Informationen dazu. Die Werte werden in Hundertstel gegeben.

EPE ist der "Estimated Position Error". Der EPE wird in cm gegeben.
Dies ist nicht der absolut maximale Fehler, es ist der Fehler mit einer
spezifischen Konfidenz. Siehe 
`hier <http://www.nps.gov/gis/gps/WhatisEPE.html>`__ für mehr Informationen.

Diese Daten sind nur gültig wenn ein Fix vorhanden ist (siehe :func:`GetStatus`).
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Status',
'elements': [('Fix', 'uint8', 1, 'out', ('Fix', [('No Fix', 1),
                                                 ('2D Fix', 2),
                                                 ('3D Fix', 3)])),
             ('Satellites View', 'uint8', 1, 'out'),
             ('Satellites Used', 'uint8', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the current fix status, the number of satellites that are in view and
the number of satellites that are currently used.

Possible fix status values can be:

.. csv-table::
 :header: "Value", "Description"
 :widths: 10, 100

 "1", "No Fix, :func:`GetCoordinates`, :func:`GetAltitude` and :func:`GetMotion` return invalid data"
 "2", "2D Fix, only :func:`GetCoordinates` and :func:`GetMotion` return valid data"
 "3", "3D Fix, :func:`GetCoordinates`, :func:`GetAltitude` and :func:`GetMotion` return valid data"

There is also a :ref:`blue LED <gps_bricklet_fix_led>` on the Bricklet that
indicates the fix status.
""",
'de':
"""
Gibt den aktuellen Fix-Status, die Anzahl der sichtbaren Satelliten und die
Anzahl der im Moment benutzten Satelliten zurück.

Mögliche Fix-Status Werte sind:

.. csv-table::
 :header: "Wert", "Beschreibung"
 :widths: 10, 100

 "1", "Kein Fix, :func:`GetCoordinates`, :func:`GetAltitude` und :func:`GetMotion` geben ungültige Daten zurück"
 "2", "2D Fix, nur :func:`GetCoordinates` und :func:`GetMotion` geben gültige Daten zurück"
 "3", "3D Fix, :func:`GetCoordinates`, :func:`GetAltitude` und :func:`GetMotion` geben gültige Daten zurück"

Auf dem Bricklet ist eine :ref:`blaue LED <gps_bricklet_fix_led>`, die den
Fix-Status anzeigt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Altitude',
'elements': [('Altitude', 'int32', 1, 'out'),
             ('Geoidal Separation', 'int32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the current altitude and corresponding geoidal separation.

Both values are given in cm.

This data is only valid if there is currently a fix as indicated by
:func:`GetStatus`.
""",
'de':
"""
Gibt die aktuelle Höhe und die dazu gehörige "Geoidal Separation"
zurück.

Beide Werte werden in cm angegeben.

Diese Daten sind nur gültig wenn ein Fix vorhanden ist (siehe :func:`GetStatus`).
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Motion',
'elements': [('Course', 'uint32', 1, 'out'),
             ('Speed', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the current course and speed. Course is given in hundredths degree
and speed is given in hundredths km/h. A course of 0° means the Bricklet is
traveling north bound and 90° means it is traveling east bound.

Please note that this only returns useful values if an actual movement
is present.

This data is only valid if there is currently a fix as indicated by
:func:`GetStatus`.
""",
'de':
"""
Gibt die aktuelle Richtung und Geschwindigkeit zurück. Die Richtung wird
in hundertstel Grad und die Geschwindigkeit in hundertstel km/h angegeben. Eine
Richtung von 0° bedeutet eine Bewegung des Bricklets nach Norden und 90°
einer Bewegung nach Osten.

Dabei ist zu beachten: Diese Funktion liefert nur nützlich Werte wenn
auch tatsächlich eine Bewegung stattfindet.

Diese Daten sind nur gültig wenn ein Fix vorhanden ist (siehe :func:`GetStatus`).
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Date Time',
'elements': [('Date', 'uint32', 1, 'out'),
             ('Time', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the current date and time. The date is
given in the format ``ddmmyy`` and the time is given
in the format ``hhmmss.sss``. For example, 140713 means
14.05.13 as date and 195923568 means 19:59:23.568 as time.
""",
'de':
"""
Gibt das aktuelle Datum und die aktuelle Zeit zurück. Das Datum ist
im Format ``ddmmyy`` und die Zeit im Format ``hhmmss.sss`` angegeben. Zum
Beispiel, 140713 bedeutet 14.05.13 als Datum und 195923568 bedeutet
19:59:23.568 als Zeit.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Restart',
'elements': [('Restart Type', 'uint8', 1, 'in', ('Restart Type', [('Hot Start', 0),
                                                                  ('Warm Start', 1),
                                                                  ('Cold Start', 2),
                                                                  ('Factory Reset', 3)]))],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Restarts the GPS Bricklet, the following restart types are available:

.. csv-table::
 :header: "Value", "Description"
 :widths: 10, 100

 "0", "Hot start (use all available data in the NV store)"
 "1", "Warm start (don't use ephemeris at restart)"
 "2", "Cold start (don't use time, position, almanacs and ephemeris at restart)"
 "3", "Factory reset (clear all system/user configurations at restart)"
""",
'de':
"""
Startet das GPS Bricklet neu. Die folgenden Neustart-Typen stehen zur
Verfügung:

.. csv-table::
 :header: "Wert", "Beschreibung"
 :widths: 10, 100

 "0", "Hot Start (alle verfügbaren Daten im NV-Speicher werden weiter genutzt)"
 "1", "Warm Start (Ephemerisdaten werden verworfen)"
 "2", "Cold Start (Zeit-, Position-, Almanach- und Ephemerisdaten werden verworfen)"
 "3", "Factory Reset (Alle System/User Einstellungen werden verworfen)"
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Coordinates Callback Period',
'elements': [('Period', 'uint32', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the period in ms with which the :func:`Coordinates` callback is triggered
periodically. A value of 0 turns the callback off.

:func:`Coordinates` is only triggered if the coordinates changed since the
last triggering.

The default value is 0.
""",
'de':
"""
Setzt die Periode in ms mit welcher der :func:`Coordinates` Callback ausgelöst wird.
Ein Wert von 0 deaktiviert den Callback.

:func:`Coordinates` wird nur ausgelöst wenn sich die Koordinaten seit der
letzten Auslösung geändert haben.

Der Standardwert ist 0.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Coordinates Callback Period',
'elements': [('Period', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the period as set by :func:`SetCoordinatesCallbackPeriod`.
""",
'de':
"""
Gibt die Periode zurück, wie von :func:`SetCoordinatesCallbackPeriod`
gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Status Callback Period',
'elements': [('Period', 'uint32', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the period in ms with which the :func:`Status` callback is triggered
periodically. A value of 0 turns the callback off.

:func:`Status` is only triggered if the status changed since the
last triggering.

The default value is 0.
""",
'de':
"""
Setzt die Periode in ms mit welcher der :func:`Status` Callback ausgelöst wird.
Ein Wert von 0 deaktiviert den Callback.

:func:`Status` wird nur ausgelöst wenn sich der Status seit der
letzten Auslösung geändert hat.

Der Standardwert ist 0.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Status Callback Period',
'elements': [('Period', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the period as set by :func:`SetStatusCallbackPeriod`.
""",
'de':
"""
Gibt die Periode zurück, wie von :func:`SetStatusCallbackPeriod`
gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Altitude Callback Period',
'elements': [('Period', 'uint32', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the period in ms with which the :func:`Altitude` callback is triggered
periodically. A value of 0 turns the callback off.

:func:`Altitude` is only triggered if the altitude changed since the
last triggering.

The default value is 0.
""",
'de':
"""
Setzt die Periode in ms mit welcher der :func:`Altitude` Callback ausgelöst wird.
Ein Wert von 0 deaktiviert den Callback.

:func:`Altitude` wird nur ausgelöst wenn sich die Höhe seit der
letzten Auslösung geändert hat.

Der Standardwert ist 0.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Altitude Callback Period',
'elements': [('Period', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the period as set by :func:`SetAltitudeCallbackPeriod`.
""",
'de':
"""
Gibt die Periode zurück, wie von :func:`SetAltitudeCallbackPeriod`
gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Motion Callback Period',
'elements': [('Period', 'uint32', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the period in ms with which the :func:`Motion` callback is triggered
periodically. A value of 0 turns the callback off.

:func:`Motion` is only triggered if the motion changed since the
last triggering.

The default value is 0.
""",
'de':
"""
Setzt die Periode in ms mit welcher der :func:`Motion` Callback ausgelöst wird.
Ein Wert von 0 deaktiviert den Callback.

:func:`Motion` wird nur ausgelöst wenn sich die Bewegung seit der
letzten Auslösung geändert hat.

Der Standardwert ist 0.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Motion Callback Period',
'elements': [('Period', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the period as set by :func:`SetMotionCallbackPeriod`.
""",
'de':
"""
Gibt die Periode zurück, wie von :func:`SetMotionCallbackPeriod`
gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Date Time Callback Period',
'elements': [('Period', 'uint32', 1, 'in')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the period in ms with which the :func:`DateTime` callback is triggered
periodically. A value of 0 turns the callback off.

:func:`DateTime` is only triggered if the date or time changed since the
last triggering.

The default value is 0.
""",
'de':
"""
Setzt die Periode in ms mit welcher der :func:`DateTime` Callback ausgelöst wird.
Ein Wert von 0 deaktiviert den Callback.

:func:`DateTime` wird nur ausgelöst wenn sich das Datum oder die Zeit seit der
letzten Auslösung geändert haben.

Der Standardwert ist 0.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Date Time Callback Period',
'elements': [('Period', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the period as set by :func:`SetDateTimeCallbackPeriod`.
""",
'de':
"""
Gibt die Periode zurück, wie von :func:`SetDateTimeCallbackPeriod`
gesetzt.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Coordinates',
'elements': [('Latitude', 'uint32', 1, 'out'),
             ('NS', 'char', 1, 'out'),
             ('Longitude', 'uint32', 1, 'out'),
             ('EW', 'char', 1, 'out'),
             ('PDOP', 'uint16', 1, 'out'),
             ('HDOP', 'uint16', 1, 'out'),
             ('VDOP', 'uint16', 1, 'out'),
             ('EPE', 'uint16', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically with the period that is set by
:func:`SetCoordinatesCallbackPeriod`. The parameters are the same
as for :func:`GetCoordinates`.

:func:`Coordinates` is only triggered if the coordinates changed since the
last triggering and if there is currently a fix as indicated by
:func:`GetStatus`.
""",
'de':
"""
Dieser Callback wird mit der Periode, wie gesetzt mit 
:func:`SetCoordinatesCallbackPeriod`, ausgelöst. Die Parameter sind die 
gleichen wie die von :func:`GetCoordinates`.

:func:`Coordinates` wird nur ausgelöst wenn sich die
Koordinaten seit der letzten Auslösung geändert haben und ein Fix vorhanden
ist (siehe :func:`GetStatus`).
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Status',
'elements': [('Fix', 'uint8', 1, 'out', ('Fix', [('No Fix', 1),
                                                 ('2D Fix', 2),
                                                 ('3D Fix', 3)])),
             ('Satellites View', 'uint8', 1, 'out'),
             ('Satellites Used', 'uint8', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically with the period that is set by
:func:`SetStatusCallbackPeriod`. The parameters are the same
as for :func:`GetStatus`.

:func:`Status` is only triggered if the status changed since the
last triggering.
""",
'de':
"""
Dieser Callback wird mit der Periode, wie gesetzt mit 
:func:`SetStatusCallbackPeriod`, ausgelöst. Die Parameter sind die 
gleichen wie die von :func:`GetStatus`.

:func:`Status` wird nur ausgelöst wenn sich der 
Status seit der letzten Auslösung geändert hat.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Altitude',
'elements': [('Altitude', 'int32', 1, 'out'),
             ('Geoidal Separation', 'int32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically with the period that is set by
:func:`SetAltitudeCallbackPeriod`. The parameters are the same
as for :func:`GetAltitude`.

:func:`Altitude` is only triggered if the altitude changed since the
last triggering and if there is currently a fix as indicated by
:func:`GetStatus`.
""",
'de':
"""
Dieser Callback wird mit der Periode, wie gesetzt mit 
:func:`SetAltitudeCallbackPeriod`, ausgelöst. Die Parameter sind die 
gleichen wie die von :func:`GetAltitude`.

:func:`Altitude` wird nur ausgelöst wenn sich die 
Höhe seit der letzten Auslösung geändert hat und ein Fix vorhanden
ist (siehe :func:`GetStatus`).
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Motion',
'elements': [('Course', 'uint32', 1, 'out'),
             ('Speed', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically with the period that is set by
:func:`SetMotionCallbackPeriod`. The parameters are the same
as for :func:`GetMotion`.

:func:`Motion` is only triggered if the motion changed since the
last triggering and if there is currently a fix as indicated by
:func:`GetStatus`.
""",
'de':
"""
Dieser Callback wird mit der Periode, wie gesetzt mit 
:func:`SetMotionCallbackPeriod`, ausgelöst. Die Parameter sind die 
gleichen wie die von :func:`GetMotion`.

:func:`Motion` wird nur ausgelöst wenn sich die 
Bewegung seit der letzten Auslösung geändert hat und ein Fix vorhanden
ist (siehe :func:`GetStatus`).
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Date Time',
'elements': [('Date', 'uint32', 1, 'out'),
             ('Time', 'uint32', 1, 'out')],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically with the period that is set by
:func:`SetDateTimeCallbackPeriod`. The parameters are the same
as for :func:`GetDateTime`.

:func:`DateTime` is only triggered if the date or time changed since the
last triggering.
""",
'de':
"""
Dieser Callback wird mit der Periode, wie gesetzt mit 
:func:`SetDateTimeCallbackPeriod`, ausgelöst. Die Parameter sind die 
gleichen wie die von :func:`GetDateTime`.

:func:`DateTime` wird nur ausgelöst wenn sich das Datum oder die Zeit 
seit der letzten Auslösung geändert haben.
"""
}]
})

com['examples'].append({
'name': 'Simple',
'functions': [('getter', ('Get Coordinates', 'coordinates'), [(('Latitude', 'Latitude'), 'uint32', 1000000.0, '°/1000000', '°', None), (('NS', 'N/S'), 'char', None, None, None, None), (('Longitude', 'Longitude'), 'uint32', 1000000.0, '°/1000000', '°', None), (('EW', 'E/W'), 'char', None, None, None, None), (('PDOP', None), 'uint16', None, None, None, None), (('HDOP', None), 'uint16', None, None, None, None), (('VDOP', None), 'uint16', None, None, None, None), (('EPE', None), 'uint16', 100.0, 'cm', 'm', None)], [])],
'incomplete': True # because of special print logic
})

com['examples'].append({
'name': 'Callback',
'functions': [('callback', ('Coordinates', 'coordinates'), [(('Latitude', 'Latitude'), 'uint32', 1000000.0, '°/1000000', '°', None), (('NS', 'N/S'), 'char', None, None, None, None), (('Longitude', 'Longitude'), 'uint32', 1000000.0, '°/1000000', '°', None), (('EW', 'E/W'), 'char', None, None, None, None), (('PDOP', None), 'uint16', None, None, None, None), (('HDOP', None), 'uint16', None, None, None, None), (('VDOP', None), 'uint16', None, None, None, None), (('EPE', None), 'uint16', 100.0, 'cm', 'm', None)], None, None),
              ('callback_period', ('Coordinates', 'coordinates'), [], 1000)],
'incomplete': True # because of special print logic
})
