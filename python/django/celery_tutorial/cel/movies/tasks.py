import random
from celery import shared_task

@shared_task
def add(x, y):
    # Celery recognizes this as the `movies.task.add` task
    # the name is purposefully omitted here.
    return x + y

@shared_task
def task_iter(n):
    start = 0
    while True:
        start += 1
        if start >= n:
            break

@shared_task(name="multiply_two_numbers")
def mul(x, y):
    # Celery recognizes this as the `multiple_two_numbers` task
    total = x * (y * random.randint(3,100))
    return total

@shared_task(name="sum_list_numbers")
def xsum(numbers):
    # Celery recognizes this as thre `sum_list_numbers` task
    return sum(numbers)
