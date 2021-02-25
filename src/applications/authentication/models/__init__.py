"""
    This folder can contains a lot of models
    each model can be adapted to differents versions of metin2
    you can change the import for your custom model

"""
import os

driver = os.environ['DATABASE_DRIVER']

if driver == 'lamda':
    from .lamda import (
        Account
    )

if driver == 'ainara2':
    from .ainara2 import (
        Account
    )
