# -*- coding: utf-8 -*-
from datetime import datetime
from xml.etree import ElementTree

from django.core.management import BaseCommand

from ...models import Supplier, Defendant, RepresentationOrder
from ...constants import SUTY_SUPPLIER_TYPES


def get_records(file_path):
    data = []
    for record in ElementTree.parse(file_path).getroot().iter('record'):
        row = {}
        for r in record:
            row[r.tag] = r.text
        data.append(row)
    return data


def to_address(supplier):
    al = []
    for i in range(1, 5):
        l = supplier.get('address%s' % i)
        if l:
            al.append(l)
    return "\n".join(al)


def get_supplier(code):
    if code:
        try:
            return Supplier.objects.get(code=code)
        except Supplier.DoesNotExist:
            print('Error finding supplier code: %s' % code)


def get_defendant(code):
    if code:
        try:
            return Defendant.objects.get(code=code)
        except Defendant.DoesNotExist:
            print('Error finding defendant code: %s' % code)


def parse_date(d):
    return datetime.strptime(d, '%Y-%m-%d').date()


class Command(BaseCommand):
    help = 'Load Suppliers, Defendants and Representation Orders from xml ' \
           'files.'

    def add_arguments(self, parser):
        parser.add_argument(
            '-s', '--suppliers', type=str,
            help='xml file containing Suppliers')
        parser.add_argument(
            '-d', '--defendants', type=str,
            help='xml file containing Suppliers')
        parser.add_argument(
            '-r', '--reporders', type=str,
            help='xml file containing Suppliers')

    def handle(self, *args, **options):
        for supplier in sorted(get_records(options['suppliers']),
                               key=lambda x: x.get('parent', '')):
            Supplier.objects.create(
                code=supplier.get('accCode'),
                parent=get_supplier(supplier.get('parent')),
                name=supplier.get('accName'),
                suty_supplier_type=SUTY_SUPPLIER_TYPES.for_constant(
                    supplier.get('sutySuppType')
                ).value,
                vat_reg=True if supplier.get('vatReg') == 'Y' else False,
                address=to_address(supplier),
                postcode=supplier.get('postCode'),
                country=supplier.get('country'),
            )

        for defendant in get_records(options['defendants']):
            Defendant.objects.get_or_create(
                code=defendant.get('id'),
                first_name=defendant.get('firstName'),
                other_name=defendant.get('otherName'),
                last_name=defendant.get('lastName'),
                date_of_birth=parse_date(defendant.get('dateOfBirth')),
            )

        for order in get_records(options['reporders']):
            RepresentationOrder.objects.create(
                code=order.get('id'),
                defendant=get_defendant(order.get('defID')),
                supplier=get_supplier(order.get('suppAccCd')),
                date=parse_date(order.get('dateReceived')),
            )
