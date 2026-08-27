import multiprocessing
import pytest
from tutor.verify_engine import _sympy_worker

def test_sympy_worker_valid():
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=_sympy_worker, args=("x+x", "2*x", queue))
    process.start()
    process.join(timeout=2)
    assert not process.is_alive()
    
    result = queue.get_nowait()
    assert result is True

def test_sympy_worker_invalid():
    queue = multiprocessing.Queue()
    process = multiprocessing.Process(target=_sympy_worker, args=("x+1", "2*x", queue))
    process.start()
    process.join(timeout=2)
    assert not process.is_alive()
    
    result = queue.get_nowait()
    assert result is False
