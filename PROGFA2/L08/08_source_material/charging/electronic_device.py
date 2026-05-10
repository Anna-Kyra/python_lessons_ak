from tkinter.ttk import Progressbar


class ElectronicDevice:
    def __init__(self, device: str, model: str):
        self.device = device
        self.model = model

    def __str__(self):
        info = f"{self.device} ({self.model})"
        return info

    def boot(self):
        """Boots the device, draining its battery with 20%."""
        print(f"Booting {self.__str__()}...")

    def run(self, program: str):
        """
        Runs a program on the device, draining its battery between 10% and 30%.
        :param program: the name of the program to run on the device
        """
        print(f"Running {program} on {self.__str__()}...")

    def battery(self, progressbar:Progressbar):
        


# symbol for electrical power: ⚡