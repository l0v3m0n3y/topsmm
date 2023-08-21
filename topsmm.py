import requests,json
class Client():
	def __init__(self,key: str):
		self.api_key=key
		self.api="https://topsmm.ru/api/v2"
	def add_order(self,service:str,quantity:str,link:str,sex:str,age_from:str=None
,age_to:str=None,country:str=None,comments_type:str=None,votes_type:str=None):
		url =(f"{self.api}/?action=add&service={service}&quantity={quantity}&link={link}&sex={sex}")
		if age_from:
			url=(f"{url}&age_from={age_from}")
		if age_to:
			url=(f"{url}&age_to={age_to}")
		if country:
			url=(f"{url}&country={country}")
		if comments_type:
			url=(f"{url}&comments_type={comments_type}")
		if votes_type:
			url=(f"{url}&votes_type={votes_type}")
		return requests.get(f"{url}").json()
	def get_orders(self):
		return requests.get(f"{self.api}/?action=orders&key={self.api_key}").json()
	def get_balance(self):
		return requests.get(f"{self.api}/?key={self.api_key}&action=balance").json()
	def order_details(self,order:int):
		return requests.get(f"{self.api}/?action=refill&key={self.api_key}&order={order}").json()
	def status(self,order: int):
		return requests.get(f"{self.api}/?action=order_details&key={self.api_key}&order={order}").json()
	def refill(self,order: int):
		return requests.get(f"{self.api}/?action=refill&key={self.api_key}&order={order}").json()
	def cancel(self,order: int):
		return requests.get(f"{self.api}/?action=cancel&key={self.api_key}&order={order}").json()