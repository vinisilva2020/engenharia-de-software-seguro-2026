import time
from enum import StrEnum

class CircuitState(StrEnum):
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF_OPEN"

class CircuitOpenError(RuntimeError): pass

class CircuitBreaker:
    def __init__(self, threshold=3, recovery_seconds=5):
        self.threshold, self.recovery_seconds = threshold, recovery_seconds
        self.state, self.failures, self.opened_at = CircuitState.CLOSED, 0, 0.0
    def refresh(self):
        if self.state == CircuitState.OPEN and time.monotonic() - self.opened_at >= self.recovery_seconds: self.state = CircuitState.HALF_OPEN
    def before_call(self):
        self.refresh()
        if self.state == CircuitState.OPEN: raise CircuitOpenError()
    def success(self): self.state, self.failures, self.opened_at = CircuitState.CLOSED, 0, 0.0
    def failure(self):
        self.failures = min(self.failures + 1, self.threshold)
        if self.failures >= self.threshold: self.state, self.opened_at = CircuitState.OPEN, time.monotonic()
    def reset(self): self.state, self.failures, self.opened_at = CircuitState.CLOSED, 0, 0.0
    def snapshot(self): self.refresh(); return {"state": self.state, "failures": self.failures, "threshold": self.threshold, "recovery_seconds": self.recovery_seconds}

circuit_breaker = CircuitBreaker()
