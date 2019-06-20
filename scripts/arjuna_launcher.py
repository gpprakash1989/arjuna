import os
import sys
import time

def join_paths(*paths):
    return os.path.abspath(os.path.join(*paths))

root_dir = join_paths(os.path.dirname(os.path.realpath(__file__)), "..")
importables_dir = join_paths(root_dir, "third_party")

sys.path.insert(0, importables_dir)
sys.path.insert(0, root_dir)

try:
    import signal
    import sys
    def signal_handler(sig, frame):
            print('Exiting...')
            sys.exit(0)
    signal.signal(signal.SIGINT, signal_handler)
    from arjuna import Arjuna
    Arjuna.launch(sys.argv)
except Exception as e:
    # The following sleep is to accommodate a common IDE issue of
    # interspersing main exception with console output.
    time.sleep(0.5)
    msg = '''
{0}
Sorry. Looks like this is an error Arjuna couldn't handle.
If Arjuna should handle this error, write to us: support@testmile.com
{0}

Message: {1}
    '''.format("-" * 70, str(e))
    print(msg)
    import traceback
    print(traceback.format_exc())
