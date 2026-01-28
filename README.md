# iPlant - Industrial Plant Simulator

A Python-based simulation designed to model the maintenance lifecycles of industrial process equipment.

This project demonstrates **Object-Oriented Programming (OOP)** principles by translating physical engineering concepts (Pumps, Reactors) into a scalable software architecture.

##  Key Features
* **Polymorphism:** A unified interface (`Maintainable`) handles maintenance routines differently for pumps vs. reactors.
* **Inheritance:** Uses an abstract base class (`Equipment`) to share logic across different machine types.
* **Scalability:** Designed so new equipment types (e.g., Heat Exchangers) can be added without modifying the core simulation loop.

##  How It Works
The system simulates a plant startup and maintenance scheduling run:
1.  **Initialization:** Concrete objects (`CentrifugalPump`, `CSTR`) are instantiated with engineering specifications (RPM, Volume).
2.  **Startup:** The `Equipment` base class handles state changes (Running/Stopped).
3.  **Maintenance Loop:** The system iterates through a registry of machines. Using polymorphism, it triggers specific maintenance tasks (e.g., checking impeller wear vs. flushing reactor tanks) and calculates the next service date based on the equipment type.

##  Technical Implementation
* **Language:** Python 3.x
* **Core Concepts:**
    * Abstract Base Classes (`ABC`)
    * Interfaces
    * Method Overriding
    * Type Hinting (Implicit)

##  Usage
1.  Clone the repository:
    ```bash
    git clone [https://github.com/mdhvnth-s/industrial-plant-sim.git](https://github.com/mdhvnth-s/industrial-plant-sim.git)
    ```
2.  Run the simulation:
    ```bash
    python plant_sim.py
    ```

##  Future Improvements
* Add a `HeatExchanger` class to calculate fouling factors.
* Implement a JSON logger to save maintenance records to a file.
* Add exception handling for equipment failures (e.g., `OverPressureError`).