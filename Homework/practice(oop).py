### draft ###
# verhicle_ID (unique)
# brand
# model
# mileage (Kilometer/mile convered [1km/0.62mil])

vehicle_ids = []
class vehicles:
	def __init__(self, vehicle_id, brand, model, mileage):
		if vehicle_id in vehicle_ids:
			print(f'Vehicle ID {vehicle_id} already exist in database')
		else:	
			self.vehicle_id = vehicle_id
			self.brand = brand
			self.model = model
			vehicle_ids.append(vehicle_id)

			# update_mileage(mileage) error because update_mileage function create below this function
			if isinstance(mileage, (int, float)) and mileage > 0:
				self.mileage = mileage
			else:
				raise ValueError("Mileage input is negative number or not float, integer!")

	def show_info(self):
		print(f"Vehicle ID: {self.vehicle_id}\nBrand: {self.brand}\nModel: {self.model}\nMileage: {self.mileage} Km")

	def update_mileage(self, mileage):
		if isinstance(mileage, (int, float)) and mileage > 0:
			self.mileage = mileage
		else:
			raise ValueError("Mileage input is negative number or not float, integer!")
try:
	vehicle1 = vehicles("001", "Porchers", "911", 50000)
	vehicle1.show_info()

	vehicle2 = vehicles("002", "Porchers", "Panamera", 50000)
	vehicle2.show_info()

	vehicle1.update_mileage(-1000)
except AttributeError:
	print('Some car has exist in database')

except ValueError as error:
	print('Something wrong: ', error)