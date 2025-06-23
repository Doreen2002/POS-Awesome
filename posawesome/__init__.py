
from __future__ import unicode_literals

__version__ = "6.3.0"

def console(*data):
    try:
        import frappe
        frappe.publish_realtime("toconsole", data, user=frappe.session.user)
    except ImportError:
        pass
