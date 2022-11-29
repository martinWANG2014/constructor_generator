# constructor_generator 
An automatic class generator with constructor, getters and setters method for the attributes

# An example

```
class Demand:
	def __init__(self,fare_class,unit_fare_value,volume,container_type,orig,dest,date_avail,date_due,cat_customer):
		self.fare_class = fare_class
		self.unit_fare_value = unit_fare_value
		self.volume = volume
		self.container_type = container_type
		self.orig = orig
		self.dest = dest
		self.date_avail = date_avail
		self.date_due = date_due
		self.cat_customer = cat_customer

	@property
	def fare_class(self):
		return self.__fare_class

	@fare_class.setter
	def fare_class(self, new_fare_class):
		self.__fare_class = new_fare_class

	@property
	def unit_fare_value(self):
		return self.__unit_fare_value

	@unit_fare_value.setter
	def unit_fare_value(self, new_unit_fare_value):
		self.__unit_fare_value = new_unit_fare_value

	@property
	def volume(self):
		return self.__volume

	@volume.setter
	def volume(self, new_volume):
		self.__volume = new_volume

	@property
	def container_type(self):
		return self.__container_type

	@container_type.setter
	def container_type(self, new_container_type):
		self.__container_type = new_container_type

	@property
	def orig(self):
		return self.__orig

	@orig.setter
	def orig(self, new_orig):
		self.__orig = new_orig

	@property
	def dest(self):
		return self.__dest

	@dest.setter
	def dest(self, new_dest):
		self.__dest = new_dest

	@property
	def date_avail(self):
		return self.__date_avail

	@date_avail.setter
	def date_avail(self, new_date_avail):
		self.__date_avail = new_date_avail

	@property
	def date_due(self):
		return self.__date_due

	@date_due.setter
	def date_due(self, new_date_due):
		self.__date_due = new_date_due

	@property
	def cat_customer(self):
		return self.__cat_customer

	@cat_customer.setter
	def cat_customer(self, new_cat_customer):
		self.__cat_customer = new_cat_customer

```