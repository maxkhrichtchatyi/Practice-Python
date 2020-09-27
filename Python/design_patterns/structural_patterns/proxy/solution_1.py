import time


class Worker:
    """Define the 'resource-intensive' object to instantiate!"""

    @staticmethod
    def do() -> None:
        print("Start a job!")

    @staticmethod
    def welcome() -> None:
        print("I'm a worker!")


class Proxy:
    """Define the 'relatively less resource-intensive' proxy to intensive as a middleman"""

    def __init__(self):
        self.occupied = None
        self.worker = None

    def start(self) -> None:
        """Check if Worker is available"""
        print("Checking if Worker is available...")

        if not self.occupied:
            # If the Worker is available, create Worker object.
            self.worker = Worker()
            time.sleep(2)

            # Make the Worker meet the guests!
            self.worker.welcome()
        else:
            # Otherwise, don't instantiate a Worker
            time.sleep(2)
            print("Worker is busy!")


# Instantiate a Proxy
proxy = Proxy()

# Make the Proxy: work until Worker is available.
proxy.start()

# Change the state to 'occupied'
proxy.occupied = True

# Make the Worker work
proxy.start()
