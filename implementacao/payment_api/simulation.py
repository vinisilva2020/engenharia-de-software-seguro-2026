from dataclasses import dataclass

@dataclass
class SimulationState:
    # Falha fixa para a apresentação: cada chamada demonstra a proteção do circuito.
    failure: bool = True
    rejection: bool = False
    latency: float = 0.0

state = SimulationState()
