# Service Controller for CloudCraft
class ServiceController:
    def __init__(self):
        self.services = {}

    def register_service(self, name, service):
        self.services[name] = service

    def start_service(self, name):
        if name in self.services:
            self.services[name].start()
        else:
            raise Exception(f"Service {name} not found")

    def stop_service(self, name):
        if name in self.services:
            self.services[name].stop()
        else:
            raise Exception(f"Service {name} not found")
