#!usr/bin/env python
# -*- coding: utf-8 -*-
"""This is a docstring for task 01."""

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal(273.15)

def fahrenheit_to_celsius(degrees):
    """Convert a fahrenheit to celsius.

    Args:
        degrees(mixed): shows the degree in fahrenheit
        
    Returns:
        decimal: returns a degree in celcius

    Examples:
        >>> fahrenheit_to_celsius(212)
        Decimal('100')

        >>> fahrenheit_to_celsius(100)
        Decimal('37.77777777777777777777777778')
    """

    degrees = decimal.Decimal(degrees)
    degrees = (degrees - 32) * 5 / 9
    return degrees

def celsius_to_kelvin(degrees):
    """Convert celsius to kelvin.

    Args:
        degree(mixed): shows the degree in celsius

    Returns:
        decimal: returns a degree in kelvin

    Examples:
        >>> celsius_to_kelvin(100)
        Decimal('373.1499999999999772626324557')
        
        >>> celsius_to_kelvin(200)
        Decimal('473.1499999999999772626324557')
    """
    degrees = degrees + ABSOLUTE_DIFFERENCE
    return degrees

def fahrenheit_to_kelvin(degrees):
    """Convert fahrenheit to kelvin.

    Args:
        degree(mixed): shows the degree in fahrenheit

    Returns:
        decimal: returns a degree in kelvin

    Examples:
        >>> fahrenheit_to_kelvin(212)
        Decimal('373.1499999999999772626324557')
        
        >>> fahrenheit_to_kelvin(100)
        Decimal('310.9277777777777550404102335')
    """
    degrees = fahrenheit_to_celsius(degrees)
    degrees = celsius_to_kelvin(degrees)
    return degrees
