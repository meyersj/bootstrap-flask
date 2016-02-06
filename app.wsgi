import os
import sys 


SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))


"""
use local python virtual-environment
"""
activate_this = os.path.join(SCRIPT_DIR, 'env/bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))


"""
load application directory onto path
"""
sys.path.insert(0, SCRIPT_DIR)


"""
import application for wsgi
"""
from app import app as application
