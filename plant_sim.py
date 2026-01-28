from abc import ABC, abstractmethod
from datetime import datetime, timedelta
class Maintainable(ABC):
    @abstractmethod
    def perform_maintenance(self):
        pass
    @abstractmethod
    def get_next_service_date(self):
        pass
class Equipment(ABC): #abstract base class for all equipment
    def __init__(self, serial_number, location):
        self.serial_number = serial_number
        self.location = location
        self.is_running = False
    def start(self):
        self.is_running = True
        print(f"[{self.serial_number}] Equipment at {self.location} has STARTED.")
    def stop(self):
        self.is_running = False
        print(f"[{self.serial_number}] Equipment at {self.location} has STOPPED.")
class CentrifugalPump(Equipment, Maintainable):
    def __init__(self, serial_number, location, impeller_size_mm, max_rpm):
        super().__init__(serial_number, location)
        self.impeller_size_mm = impeller_size_mm
        self.max_rpm = max_rpm
    def perform_maintenance(self):
        print(f" MAINTAINING PUMP {self.serial_number}: Checking impeller wear and lubricating bearings.")
    def get_next_service_date(self):
        return datetime.now() + timedelta(days=180)
    def adjust_rpm(self, new_rpm):
        if new_rpm > self.max_rpm:
            print(f" DANGER: {new_rpm} RPM exceeds safety limit of {self.max_rpm}!")
        else:
            print(f"Checking Pump {self.serial_number}: RPM adjusted to {new_rpm}.")
class CSTR(Equipment, Maintainable):
    def __init__(self, serial_number, location, volume_liters, agitator_speed):
        super().__init__(serial_number, location)
        self.volume_liters = volume_liters
        self.agitator_speed = agitator_speed
    def perform_maintenance(self):
        print(f" CLEANING REACTOR {self.serial_number}: Flushing tank volume ({self.volume_liters}L) and inspecting agitator seals.")
    def get_next_service_date(self):
        return datetime.now() + timedelta(days=90)
if __name__ == "__main__":
    print("--- PLANT SIMULATION STARTED ---\n")
    pump_01 = CentrifugalPump("P-101", "Zone A", impeller_size_mm=250, max_rpm=3000)
    reactor_01 = CSTR("R-502", "Zone B", volume_liters=5000, agitator_speed=150)
    pump_02 = CentrifugalPump("P-102", "Zone A", impeller_size_mm=100, max_rpm=1500)
    plant_equipment = [pump_01, reactor_01, pump_02]
    print(">>> Initiating Plant Startup...")
    for machine in plant_equipment:
        machine.start()
        if isinstance(machine, CentrifugalPump):
            machine.adjust_rpm(2800)
    print("\n>>> Scheduling Maintenance...")
    for machine in plant_equipment:
        machine.perform_maintenance()
        service_date = machine.get_next_service_date()
        print(f"   -> Next service due: {service_date.strftime('%Y-%m-%d')}")
        print("-" * 30)