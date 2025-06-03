# Usage: locust -f locustfile.py --headless --users 10 --spawn-rate 1 -H http://localhost:8000
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task(10)
    def home(self):
        self.client.get("/observability_demo", name="/home")

    @task(5)
    def io_task(self):
        self.client.get("/observability_demo/io_task", name="/io_task")

    @task(5)
    def cpu_task(self):
        self.client.get("/observability_demo/cpu_task", name="/cpu_task")

    @task(3)
    def random_sleep(self):
        self.client.get("/observability_demo/random_sleep", name="/random_sleep")

    @task(10)
    def random_status(self):
        self.client.get("/observability_demo/random_status", name="/random_status")

    @task(3)
    def chain(self):
        self.client.get("/observability_demo/chain", name="/chain")

    @task()
    def error_test(self):
        self.client.get("/observability_demo/error_test", name="/error_test")
