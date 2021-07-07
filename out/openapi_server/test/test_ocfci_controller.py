# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.advertisement import Advertisement  # noqa: E501
from openapi_server.test import BaseTestCase


class TestOCFCIController(BaseTestCase):
    """OCFCIController integration test stubs"""

    def test_oc_fci_get_advertisement(self):
        """Test case for oc_fci_get_advertisement

        get the FCI advertisements according to SVA and CDNI (RFC8008/RFC8804)
        """
        headers = { 
            'Accept': 'application/cdni',
        }
        response = self.client.open(
            '/oc/fci/advertisement',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
