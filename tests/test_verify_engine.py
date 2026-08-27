import pytest
import multiprocessing
from tutor.verify_engine import _sympy_worker

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
