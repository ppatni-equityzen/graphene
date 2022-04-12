from __future__ import absolute_import

from decimal import Decimal as _Decimal

from graphql.language.ast import StringValueNode, IntValueNode

from .scalars import Scalar


class Decimal(Scalar):
    """
    The `Decimal` scalar type represents a python Decimal.
    """

    @staticmethod
    def serialize(dec):
        if isinstance(dec, str):
            dec = _Decimal(dec)
        assert isinstance(
            dec, _Decimal
        ), f'Received not compatible Decimal "{repr(dec)}"'
        return str(dec)

    @staticmethod
    def parse_literal(node):
        if isinstance(node, (StringValueNode, IntValueNode)):
            return _Decimal(node.value)

    @staticmethod
    def parse_value(value):
        try:
            return _Decimal(value)
        except ValueError:
            return None
