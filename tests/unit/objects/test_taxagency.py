import unittest

from quickbooks.objects.taxagency import TaxAgency


class TaxAgencyTests(unittest.TestCase):
    def test_unicode(self):
        deposit = TaxAgency()
        deposit.DisplayName = "test"

        self.assertEquals(deposit.__unicode__(), "test")
