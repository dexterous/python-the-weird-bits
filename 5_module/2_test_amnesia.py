from hamcrest import assert_that, has_length, is_
from acme.tests.units.integration.custom.customer_event_factory.utils import make_object

from datetime import datetime
from decimal import Decimal
from acme.integration.custom.customer_event_factory import Builder, ProcessExcelOutputTaeguTecFormat
from acme.statemachine.base import START, EV_INV_CREATED
from acme.utils.constants import INV

def should_map_int_total_to_amount():
    row = make_object(total=2000)
    invoice = Builder(date_format).build_invoice([row], 'entid', 'userid', 'url')
    assert_that(invoice.amount, is_(Decimal('2000')))
    assert_that(invoice.items_total, is_(Decimal('2000')))

def should_map_long_total_to_amount():
    row = make_object(total=2000L)
    invoice = Builder(date_format).build_invoice([row], 'entid', 'userid', 'url')
    assert_that(invoice.amount, is_(Decimal('2000')))
    assert_that(invoice.items_total, is_(Decimal('2000')))

def should_map_float_total_to_amount():
    row = make_object(total=2000.00)
    invoice = Builder(date_format).build_invoice([row], 'entid', 'userid', 'url')
    assert_that(invoice.amount, is_(Decimal('2000')))
    assert_that(invoice.items_total, is_(Decimal('2000')))

def should_map_float_total_with_upto_two_significant_non_zero_decimals_to_amount():
    row = make_object(total=2000.1200)
    invoice = Builder(date_format).build_invoice([row], 'entid', 'userid', 'url')
    assert_that(invoice.amount, is_(Decimal('2000.12')))
    assert_that(invoice.items_total, is_(Decimal('2000.12')))

def should_map_string_total_to_amount():
    row = make_object(total='2000.00')
    invoice = Builder(date_format).build_invoice([row], 'entid', 'userid', 'url')
    assert_that(invoice.amount, is_(Decimal('2000')))
    assert_that(invoice.items_total, is_(Decimal('2000')))

def should_map_string_total_with_upto_two_significant_non_zero_decimals_to_amount():
    row = make_object(total='2000.1200')
    invoice = Builder(date_format).build_invoice([row], 'entid', 'userid', 'url')
    assert_that(invoice.amount, is_(Decimal('2000.12')))
    assert_that(invoice.items_total, is_(Decimal('2000.12')))

def should_map_unicode_total_to_amount():
    row = make_object(total=u'2000.00')
    invoice = Builder(date_format).build_invoice([row], 'entid', 'userid', 'url')
    assert_that(invoice.amount, is_(Decimal('2000')))
    assert_that(invoice.items_total, is_(Decimal('2000')))

def should_map_unicode_total_with_upto_two_significant_non_zero_decimals_to_amount():
    row = make_object(total=u'2000.1200')
    invoice = Builder(date_format).build_invoice([row], 'entid', 'userid', 'url')
    assert_that(invoice.amount, is_(Decimal('2000.12')))
    assert_that(invoice.items_total, is_(Decimal('2000.12')))

def should_map_decimal_total_to_amount():
    row = make_object(total=Decimal('2000.00'))
    invoice = Builder(date_format).build_invoice([row], 'entid', 'userid', 'url')
    assert_that(invoice.amount, is_(Decimal('2000')))
    assert_that(invoice.items_total, is_(Decimal('2000')))

def should_map_decimal_total_with_upto_two_significant_non_zero_decimals_to_amount():
    row = make_object(total=Decimal('2000.1200'))
    invoice = Builder(date_format).build_invoice([row], 'entid', 'userid', 'url')
    assert_that(invoice.amount, is_(Decimal('2000.12')))
    assert_that(invoice.items_total, is_(Decimal('2000.12')))
