# CloudCraft: Cloud-Hosted FinTech-as-a-Service

## Description
Deploy trading/payment services on AWS/Azure with cloud deployment and auto-scaling features.

### Theme
Cloud Deployment + Auto-scaling

## Project Structure
- `cloudcraft/service_controller.py`: Manages services
- `cloudcraft/trading_service.py`: Trading service (contains a bug)
- `cloudcraft/payment_service.py`: Payment service (contains a bug)
- `cloudcraft/cloud_deployment.py`: Simulates cloud deployment and auto-scaling (contains a bug)
- `main.py`: Example usage

## Requirements
See `requirements.txt` for dependencies:
- boto3
- azure-mgmt-resource

## Installation
```powershell
pip install -r requirements.txt
```

## Intentional Bugs & How to Fix

### 1. TradingService Bug
File: `cloudcraft/trading_service.py`
```python
	def start(self):
		self.active = False  # BUG: Should be True
```
**Fix:** Change to `self.active = True`

### 2. PaymentService Bug
File: `cloudcraft/payment_service.py`
```python
	def stop(self):
		print("Payment Service stopped.")  # BUG: Should set self.active = False
```
**Fix:** Add `self.active = False` before the print statement.

### 3. CloudDeployment Bug
File: `cloudcraft/cloud_deployment.py`
```python
		print(f"Deployment to {self.providr} complete!")  # BUG: Should be self.provider
```
**Fix:** Change `self.providr` to `self.provider`

---
Feel free to run `main.py` and try fixing the bugs!