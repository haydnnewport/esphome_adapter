# -*- coding: utf-8 -*-

"""ESPhome adapter for Mozilla WebThings Gateway."""
from . import ADAPTER_NAME
from gateway_addon import Adapter, Database

_PAIRING_TIMEOUT = 3

class ESPhomeAdapter(Adapter):
    """Adapter for ESPhome devices"""

    def __init__(self, verbose=False):
        """
        Initialize the object.

        verbose -- whether or not to enable verbose logging
        """
        self.name = self.__class__.__name__
        Adapter.__init__(self, ADAPTER_NAME, ADAPTER_NAME, verbose=verbose)
        self.pairing = False
        self.add_from_config()
        self.start_pairing(_PAIRING_TIMEOUT)

    def add_from_config(self):
        """Attempt to add all previously configured devices."""
        database = Database(ADAPTER_NAME)

        if not database.open():
            return

        config = database.load_config()
        database.close()

        for address in config['addresses']:
            try:
                # Try to reconnect with the existing device
                # dev = find_device()
                pass
            except (OSError, UnboundLocalError) as e:
                print('Failed to connect to {}: {}'.format(address, e))
                continue

            if dev:
                self._add_device(dev)

    def start_pairing(self, timeout):
        """
        Start the pairing process.

        timeout -- Timeout in seconds at which to quit pairing
        """
        if self.pairing:
            return

        self.pairing = True
        # Run discovery and _add_devices here

        self.pairing = False


    def _add_device(self, dev):
        """
        Add the given device, if necessary.

        dev -- the device object from connection library
        """
        # Instantiate a device object (or several)
        device = None
        self.handle_device_added(device)

    def cancel_pairing(self):
        """Cancel the pairing process."""
        self.pairing = False