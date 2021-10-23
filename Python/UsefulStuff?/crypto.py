class wallet:
	from random import randint
	def __init__(self):
		self.balance = float(100)
		self.account = {} #empty dictionary that holds coin name as key and list of amount owned and address as value [amount owned,address]

	def openCoin(self,coinObj):
		tempAddress = str(int(list(coinObj.openAddresses)[len(list(coinObj.openAddresses))-1])+1).zfill(4) #creates 4 digit address that is 1 higher than last address created
		self.account[coinObj]=[0,tempAddress] #adding coin to account with 0 amount
		coinObj.addToDict(tempAddress) #communicates to coin to add wallets address to storage
		self.balance





	def marketBuy(self,coinObj,amount):
		#calls on requestBuy method and retrieves the error outcome
		log = coinObj.requestBuy(amount,self.account[coinObj][1],self.balance)


		if log[0] == "S":

			#if transaction went through, substract value of trade from balance
			self.balance -= amount * coinObj.price
			#Adds coin to our wallet, amount is zero'ith index of values in dictionary
			self.account[coinObj][0] += amount 
			#print success
			print(log)
		else:
			#print error
			print(log)


			

class coin:
	#initializer method
	def __init__(self,name,marketCap,price):

		self.name = name
		self.marketCap = marketCap
		self.price = price
		self.openAddresses = {"0001":0}

	def resetPrice(self,price):
		self.price = price

	#adds an address to memory	
	def addToDict(self,key):
		self.openAddresses[key] = 0


	def requestBuy(self,amount,address,balance):
		#checks if buyer has enough funds
		if balance >= amount * self.price:
			try:
				#tries to add coin to wallet
				self.openAddresses[address] += amount
				return "Success, you have bought " + str(amount) + " " + str(self.name)
				
				
			except:
				return "Unknown Error"
		else:
			return "Insufficient Funds"



DOGE = coin("Dogecoin",100,.07)

w1 = wallet()
print("Your balance is: " + str("{:.2f}".format(w1.balance)+"USD"))
w1.openCoin(DOGE)



w1.marketBuy(DOGE,100)
print("Your balance is: " + str("{:.2f}".format(w1.balance)+"USD"))
print("DOGE balance: " + str(w1.account[DOGE][0]))



