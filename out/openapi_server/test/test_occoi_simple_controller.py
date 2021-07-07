# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.mi_host_index import MIHostIndex  # noqa: E501
from openapi_server.test import BaseTestCase


class TestOCCOISimpleController(BaseTestCase):
    """OCCOISimpleController integration test stubs"""

    @unittest.skip("application/cdni;ptype&#x3D;MI.HostIndex not supported by Connexion")
    def test_oc_ci_configure(self):
        """Test case for oc_ci_configure

        Communicates the metadata/configuration (RFC8006 + RFC8804) to the ISP with a simple API
        """
        mi_host_index = openapi_server.MIHostIndex()
        headers = { 
            'Accept': 'application/cdni;ptype&#x3D;ci-trigger-status',
            'Content-Type': 'application/cdni;ptype&#x3D;MI.HostIndex',
        }
        response = self.client.open(
            '/oc/ci/configuration',
            method='PUT',
            headers=headers,
            data=json.dumps(mi_host_index),
            content_type='application/cdni;ptype=MI.HostIndex')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
