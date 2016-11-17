# -*- coding: utf-8 -*-
from model_mommy import mommy
from rest_framework import status
from rest_framework.test import APITestCase

from suppliers.models import Supplier, RepresentationOrder, Defendant


class SupplierApiTestCase(APITestCase):
    endpoint = '/api/v1/suppliers'

    def setUp(self):
        self.supplier = mommy.make(Supplier)
        defendant1 = mommy.make(Defendant)
        defendant2 = mommy.make(Defendant)
        self.reporder = mommy.make(RepresentationOrder, supplier=self.supplier,
                                   defendant=defendant1)
        mommy.make(RepresentationOrder, supplier=self.supplier,
                   defendant=defendant2)

    def _test_get_not_allowed(self, url):
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def _test_post_not_allowed(self, url, data={}):
        response = self.client.post(url, data,)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def _test_put_not_allowed(self, url, data={}):
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def _test_patch_not_allowed(self, url, data={}):
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def _test_delete_not_allowed(self, url):
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_get_list_available(self):
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_detail_available(self):
        response = self.client.get('%s/%s' % (self.endpoint, self.supplier.code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_reporder_list_available(self):
        response = self.client.get(
            '%s/%s/reporders' % (self.endpoint, self.supplier.code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_get_reporder_detail_available(self):
        response = self.client.get(
            '%s/%s/reporders/%s' % (self.endpoint, self.supplier.code,
                                    self.reporder.code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_methods_not_allowed(self):
        for url in [self.endpoint, '%s/%s' % (self.endpoint, self.supplier.code),
                    '%s/%s/reporders/%s' % (self.endpoint, self.supplier.code,
                                            self.reporder.code)]:
            self._test_post_not_allowed(url)
            self._test_put_not_allowed(url)
            self._test_patch_not_allowed(url)
            self._test_delete_not_allowed(url)
