import visa

class Instrument:
    def __init__(self) -> None:
        self.rm = visa.ResourceManager()
        self.inst = self.rm.open_resource(resource, timeout=10000)
        self.inst.write("*RST;*CLS")

    # Add functions to set and configure the Instrument
