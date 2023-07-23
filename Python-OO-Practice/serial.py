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
   
    def __init__(self,start=0):
        """Make a new serial generator, starting at start"""

        self.start = start
        self.next = start



    def __repr__(self):
        """Show representation"""

        return f"<SerialGenerator start={self.start} next ={self.start + 1}"
    
    def generate(self):
        """Return next serial number."""

        self.next +=1
        return self.next

        # self.next = self.start +1
        # return self.next
    

    
    def reset(self):
        """Resets the serial number to the inital starting point"""

        self.next =self.start

    








