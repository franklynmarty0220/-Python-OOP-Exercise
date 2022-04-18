"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        """ Make a new generator, starting with start"""
        self.start = self.next = start

    def __repr__(self):
        """Show representation of the generator."""

        return f"<Serial Generator start= {self.start} next= {self.next}>"

    def generate(self):
        """ Generate next serial"""
        self.next += 1
        return self.next

    def reset(self):
        """Resets the serial generator"""
        self.next = self.start