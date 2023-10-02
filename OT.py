# Constants
LITERS_PER_CUBIC_METER = 1000  # Conversion factor from cubic meters to liters

# Input from the user
room_area = float(input("Enter the room area in square meters: "))
ceiling_height = float(input("Enter the ceiling height in meters: "))
air_changes_per_hour = float(input("Enter the air changes per hour: "))

# Calculate the volume of the room in cubic meters
room_volume = room_area * ceiling_height

# Calculate the air flow rate in cubic meters per hour
air_flow_rate_cubic_meters_per_hour = room_volume * air_changes_per_hour

# Convert the air flow rate to liters per second
air_flow_rate_liters_per_second = air_flow_rate_cubic_meters_per_hour * LITERS_PER_CUBIC_METER / 3600

# Display the result
print(f"The air flow rate in liters per second is: {air_flow_rate_liters_per_second:.2f} L/s")
