import pytest
import multiprocessing
from tutor.verify_engine import _sympy_worker, verify_equivalence_safe
import asyncio
from unittest.mock import patch
import time

def test_sympy_worker_valid_equivalence():
    ctx = multiprocessing.get_context("spawn")
    queue = ctx.Queue()
    _sympy_worker("x + x", "2*x", queue)
    res = queue.get()
    assert res["status"] == "ok"
    assert res["result"] is True

def test_sympy_worker_invalid_equivalence():
    ctx = multiprocessing.get_context("spawn")
    queue = ctx.Queue()
    _sympy_worker("x + 1", "2*x", queue)
    res = queue.get()
    assert res["status"] == "ok"
    assert res["result"] is False

def test_sympy_worker_syntax_error():
    ctx = multiprocessing.get_context("spawn")
    queue = ctx.Queue()
    _sympy_worker("x + * 2", "2*x", queue)
    res = queue.get()
    assert res["status"] == "error"
    assert "Parse Error" in res["error"]

@pytest.mark.asyncio
async def test_async_wrapper_timeout():
    def slow_worker(expr1, expr2, queue):
        time.sleep(100)
    
    with patch("tutor.verify_engine._sympy_worker", side_effect=slow_worker):
        with pytest.raises(TimeoutError) as exc_info:
            await verify_equivalence_safe("x", "x", timeout=0.2)
        assert "exceeded timeout" in str(exc_info.value)
