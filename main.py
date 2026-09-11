temperature = 23.0
air_humidity = 65
soil_moisture = 39.9
light_level = 70
print(f"""
Temperature: {temperature}
Air Humidity: {air_humidity}
Soil Moisture: {soil_moisture}
Light Level: {light_level}
""")
if soil_moisture < 40:
    print("Watering plant")
    soil_moisture = soil_moisture + 5
    





