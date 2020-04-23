class Flights:
	def __init__(self, origin, destination, duration):
		self. origin = origin
		self. destination = destination
		self.duration = duration

	def print_info(self):
		print(f"Flight origin: {self.origin}")
		print(f"Flight destination: {self.destination}")
		print(f"Flgiht duration: {self.duration}")

	def delay(self, amount):
		self.duration+=amount


def main():
	f=Flights("Moscow", "Washigton", 890)
	f.print_info()
	f.delay(56)
	f.print_info()

if __name__ == "__main__":
	main()