# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    import frappe

    __version__ = "6.3.0"

    def console(*data):
        frappe.publish_realtime("toconsole", data, user=frappe.session.user)

except ImportError:
    # Optionally handle the error or just pass
    pass
