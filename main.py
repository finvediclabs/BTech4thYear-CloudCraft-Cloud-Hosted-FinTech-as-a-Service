from cloudcraft.service_controller import ServiceController
from cloudcraft.trading_service import TradingService
from cloudcraft.payment_service import PaymentService
from cloudcraft.cloud_deployment import CloudDeployment

if __name__ == "__main__":
    controller = ServiceController()
    trading = TradingService()
    payment = PaymentService()
    cloud = CloudDeployment(provider="AWS")

    controller.register_service("trading", trading)
    controller.register_service("payment", payment)

    controller.start_service("trading")
    controller.start_service("payment")
    cloud.deploy()
    cloud.autoscale()
