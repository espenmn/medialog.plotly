import zope.component
import zope.interface
import zope.schema.interfaces

from z3c.form import interfaces
from z3c.form import widget
from z3c.form.browser import text


class ITableWidget(interfaces.IWidget):
    """Table widget."""


class TableWidget(text.TextWidget):
    zope.interface.implementsOnly(ITableWidget)
    
    def update(self):
        super(TableWidget, self).update()
             
    def javascript(self):
        return ""

def TableFieldWidget(field, request):
    """IFieldWidget factory for TableWidget."""
    return widget.FieldWidget(field, TableWidget(request))
