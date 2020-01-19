from typing import List, Callable


def logistic_wrapper(r: float) -> Callable:
    def logistic_fn(x: float) -> float:
        return r * x * (1 - x)
    return logistic_fn


def iterate(initial_state: float, iterations: int, map_fn: Callable) -> List[float]:
    current_state = initial_state
    states = list()
    for _ in range(iterations):
        current_state = map_fn(current_state)
        states.append(current_state)
    return states

