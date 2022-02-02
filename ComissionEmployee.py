# ComissionEmployee.py
"""ComissionEmployee base class."""

from decimal import Decimal

class ComissionEmployee:
    """An employee who gets paid comission based on gross sales."""

    def __init__(self, first_name, last_name, ssn, gross_sales, commission_rate):

        """Initialize CommissionEmployee's attributes"""

        self._first_name = first_name
        self._last_name = last_name
        self._ssn = ssn
        self.gross_sales = gross_sales
        self.commission_rate = commission_rate

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def ssn(self):
        return self._ssn

    @property
    def gross_sales(self):
        return self._gross_sales

    @gross_sales.setter
    def gross_sales(self, sales):
        if sales < Decimal('0.00'):
            raise ValueError('Gross sales must be >= 0')

        self._gross_sales = sales

    @property
    def commission_rate(self):
        return self._commission_rate

    @commission_rate.setter
    def commission_rate(self, rate):
        if not (Decimal('0.0') < rate < Decimal('1.0')):
            raise ValueError('Interest rate must be between 0 and 1')

        self._commission_rate = rate

    def earning(self):
        return self.gross_sales * self.commission_rate

    def __repr__(self):
        """Return the strig representation for repr(). """
        return ('CommissionEmployee: ' +
                f'{self.first_name} {self.last_name}\n' +
                f'social security number: {self.ssn}\n' +
                f'gross sales: {self.gross_sales:.2f}\n' +
                f'commission rate: {self.commission_rate:.2}')


