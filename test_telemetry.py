from telemetry_engine import OceanSensorBuoy

def test_pressure_exceeds_limit():
    buoy = OceanSensorBuoy("BayOfBengal_01")
    buoy.water_pressure = 45.0
    
    assert buoy.validate_telemetry() == "ERROR: Sensor Overpressure"

def test_gps_signal_loss():
    buoy = OceanSensorBuoy("ArabianSea_02")
    buoy.water_pressure = 15.0
    buoy.gps_signal = 10.0
    
    assert buoy.validate_telemetry() == "WARNING: GPS Signal Lost"