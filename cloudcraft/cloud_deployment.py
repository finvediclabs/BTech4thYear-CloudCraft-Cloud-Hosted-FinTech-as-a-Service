# Cloud Deployment (AWS/Azure) - Simulated
class CloudDeployment:
    def __init__(self, provider):
        self.provider = provider

    def deploy(self):
        print(f"Deploying services to {self.provider}...")
        # Intentional bug: misspelled variable
        print(f"Deployment to {self.providr} complete!")  # BUG: Should be self.provider

    def autoscale(self):
        print(f"Auto-scaling enabled on {self.provider}.")
