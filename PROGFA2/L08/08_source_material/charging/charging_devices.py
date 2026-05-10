from electronic_device import ElectronicDevice

# Create 2 instances of electronic device:
laptop = ElectronicDevice("laptop", "X200")
phone = ElectronicDevice("phone", "iPhone")

# Print both instances:
print(laptop)
print(phone)
print() # empty line

# Boot both devices:
laptop.boot()
phone.boot()
print() # empty line

# Run some programs on it:
laptop.run("Photoshop")
laptop.run("Pycharm")
phone.run("TikTok")