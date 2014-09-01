import zope.interface
import zope.schema
import copy
import json
import datetime
import nose.tools
from lxml import etree

from ckan.tests import TestController as BaseTestController
from ckanext.publicamundi.tests.functional import with_request_context

from ckanext.publicamundi.lib.metadata.types.common import *
from ckanext.publicamundi.lib.metadata.types.inspire_metadata import ThesaurusTerms, Thesaurus
from ckanext.publicamundi.lib.metadata.types.inspire_metadata import InspireMetadata
from ckanext.publicamundi.lib.metadata.base import *
from ckanext.publicamundi.tests.helpers import assert_faulty_keys
from ckanext.publicamundi.tests import fixtures

from ckanext.publicamundi.lib.metadata import xml_serializers
from ckanext.publicamundi.lib.metadata.xml_serializers import object_xml_serialize_adapter
from ckanext.publicamundi.lib.metadata.xml_serializers import xml_serializer_for_object

# Tests

class TestController(BaseTestController):
    #@nose.tools.istest
    #def test_to_xml(self):
    #    yield self._to_xml, fixtures.inspire1, '/tmp/inspire1.xml'

    #@nose.tools.istest
    #def test_from_xml(self):
    #    yield self._from_xml, '../samples/3.xml'
    #    yield self._from_xml, '../samples/aktogrammh.xml'

    @nose.tools.istest
    def test_to_xsd(self):
        yield self._validate_with_xsd, fixtures.inspire1, '../samples/3.xml'
        yield self._validate_with_xsd, fixtures.inspire1, '../samples/aktogrammh.xml'

    @with_request_context('publicamundi-tests', 'index')
    def _to_xml(self, obj, outfile):
        #obj = InspireMetadata()
        ser = xml_serializer_for_object(obj)
        #ser.to_xml()
        iso_xml = ser.dumps()
        #assert isinstance(iso_xml, str)
        #print '1'
        #print iso_xml
        fp = open(outfile, "w")
        fp.write(iso_xml)
        fp.close()

    def _from_xml(self, infile):
        ser = xml_serializer_for_object(InspireMetadata())

        e = etree.parse(infile)
        assert isinstance(e, etree._ElementTree)
        out = ser.from_xml(e)
        assert isinstance(out, InspireMetadata)
        #errors = out.validate()
        #assert not errors

    def _validate_with_xsd(self, obj, xml_file):
        ser = xml_serializer_for_object(obj)
        xsd = ser.to_xsd()

        #path = os.path.dirname(os.path.dirname('/home/ckaner/xsd_files/1'))
        #path = os.path.dirname(os.path.dirname(__file__))
        #data_file = os.path.join(path, DATA_FILE)

        #print 'validating'
        xml = etree.parse(xml_file)
        #print 'validation result:'
        #assert xsd.validate(xml)
        if not xsd.validate(xml):
            log = xsd.error_log
            #print log
            raise TypeError('Invalid XML\nerrors:\n',log)

        #out = ser.from_xml(e)
        #assert isinstance(out, InspireMetadata)
        #errors = out.validate()
        #assert not errors

if __name__ == '__main__':
    pass
