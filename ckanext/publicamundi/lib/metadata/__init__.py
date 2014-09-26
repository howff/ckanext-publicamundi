import zope.interface
import zope.interface.adapter
import zope.schema

adapter_registry = zope.interface.adapter.AdapterRegistry()

from ckanext.publicamundi.lib.metadata.ibase import (
    ISerializer, IXmlSerializer, IFormatter, IObject)

from ckanext.publicamundi.lib.metadata.formatters import (
    field_format_adapter, field_format_multiadapter, formatter_for_field)

from ckanext.publicamundi.lib.metadata.serializers import (
    serializer_for_field, serializer_for_key_tuple)

from ckanext.publicamundi.lib.metadata.base import (
    Object, FieldContext, ErrorDict, object_null_adapter,
    object_serialize_adapter, serializer_for_object,
    object_format_adapter, formatter_for_object, ObjectFormatter)

from ckanext.publicamundi.lib.metadata.schemata import (
    IFoo, ICkanMetadata, IInspireMetadata)

from ckanext.publicamundi.lib.metadata.types import (
    Foo, CkanMetadata, InspireMetadata)

from ckanext.publicamundi.lib.metadata.xml_serializers import (
    object_xml_serialize_adapter, xml_serializer_for_object)

from ckanext.publicamundi.lib.metadata.widgets import (
    markup_for_field, markup_for_object,
    widget_for_field, widget_for_object)

# Declare dataset types (i.e. metadata formats).
# Note If, for a certain dataset-type, a "class" value is not given,
# then a suitable class will be lookup-up in the adapter registry.

dataset_types = {
    'ckan': {
        'title': 'CKAN',
        'description': u'Provide core CKAN metadata',
        'schema': ICkanMetadata,
        'class': CkanMetadata,
    },
    'inspire': {
        'title': 'INSPIRE',
        'description': u'Provide metadata according to the INSPIRE EU directive',
        'schema': IInspireMetadata,
        'class': InspireMetadata,
        'key_prefix': 'inspire', 
    },
    'foo': {
        'title': 'Foo',
        'description': u'Provide metadata according to an arbitrary "foo" schema',
        'schema': IFoo,
        'class': Foo,
        'key_prefix': 'foo', 
    },
}
