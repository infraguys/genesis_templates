#    Copyright 2025 Genesis Corporation.
#
#    All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT

import datetime


def now(tz=None):
    """
    Returns the current date and time in the specified timezone.

    :param tz: The timezone whose current date and time to return. If None,
               the local timezone is used.
    :type tz: datetime.tzinfo or None

    :rtype: datetime.datetime
    """
    return datetime.datetime.now(tz=tz)


FUNCTIONS = {
    "now": now,
}


def get_jinja_functions():
    """
    Retrieves a copy of the available Jinja functions.

    :return: A dictionary containing Jinja function names as keys and their
             corresponding callable objects as values.
    :rtype: dict
    """

    return FUNCTIONS.copy()


__all__ = ["get_jinja_functions"]
