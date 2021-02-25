import os

driver = os.environ['DATABASE_DRIVER']

if  driver == 'default':
    from .account import (
        Player, 
        Guild
    )


if driver == 'lamda':
    from .lamda import (
        Player, 
        Guild
    )

if driver == 'ainara2':
    from .ainara2 import (
        Player, 
        Guild
    )
