import random

class OceanSensorBuoy:
    def __init__(self, buoy_id):
        self.buoy_id = buoy_id
        self.water_pressure = round(random.uniform(1.0, 50.0), 2)  # measured in bar
        self.water_temperature = round(random.uniform(4.0, 30.0), 2) # measured in Celsius
        self.gps_signal = round(random.uniform(0, 100), 2) # percentage

    def validate_telemetry(self):
        """Analyzes the simulated ocean data to trigger error flags."""
        if self.water_pressure > 40.0:
            return "ERROR: Sensor Overpressure"
        if self.gps_signal < 20.0:
            return "WARNING: GPS Signal Lost"
        return "STATUS: Nominal"