from app.services.circuit_breaker import CircuitBreaker, CircuitState, CircuitOpenError

def test_circuit_opens_after_consecutive_failures_and_recovers(monkeypatch):
    clock = [100.0]
    monkeypatch.setattr("app.services.circuit_breaker.time.monotonic", lambda: clock[0])
    breaker = CircuitBreaker(threshold=2, recovery_seconds=10)
    breaker.failure(); breaker.failure()
    assert breaker.snapshot()["state"] == CircuitState.OPEN.value
    try:
        breaker.before_call()
        assert False
    except CircuitOpenError:
        pass
    clock[0] += 11
    breaker.before_call()
    assert breaker.snapshot()["state"] == CircuitState.HALF_OPEN.value
    breaker.success()
    assert breaker.snapshot()["state"] == CircuitState.CLOSED.value
