# ./models/__init__.py
# For scalability Using __init__.py

from .insuarance_model import InsuranceModel, IntegratedInsuranceModel
from .test import TestModel

__all__ = [
        'InsuranceModel',
        'IntegratedInsuranceModel',
        'TestModel'
        ]
