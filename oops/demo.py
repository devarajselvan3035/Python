from abc import ABC, abstractmethod


class BrakingSystem(ABC):
    """Abstract Base Class defining a strict architectural contract."""

    @abstractmethod
    def apply_emergency_brake(self) -> None:
        """Force implementation on any child braking system variant."""
        pass


class PneumaticBrake(BrakingSystem):
    """Concrete implementation matching the abstract base structural interface."""

    def inner_apply_emergency_brake(self) -> None:
        print(
            "Pneumatic valves opened. Discharging air reservoirs. Full force applied."
        )


# system = BrakingSystem()  # -> TypeError: Can't instantiate abstract class
brake_system = PneumaticBrake()
brake_system.apply_emergency_brake()
