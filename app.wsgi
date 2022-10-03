import sys
sys.path.insert(0, '/root/test/hk_iro_server')
active = '/root/test/hk_iro_server/venv/bin/activate_this.py'
with open(active) as fl:
    exec(fl.read(), dict(__file__=active))
from main import app as application