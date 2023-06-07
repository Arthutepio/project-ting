from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue = PriorityQueue()
    assert len(queue) == 0

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(6)

    queue.enqueue({"qtd_linhas": 2})
    assert len(queue) == 1

    queue.enqueue({"qtd_linhas": 7})
    assert len(queue) == 2

    queue.enqueue({"qtd_linhas": 4})
    assert queue.dequeue() == {"qtd_linhas": 2}

    assert queue.search(0) == {"qtd_linhas": 4}
