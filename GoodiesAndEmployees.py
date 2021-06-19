
class Goodie:
	def __init__(self, name,price):
		self.name=name
		self.price=price

	def getName(self):
		return self.name

	def getPrice(self):
		return self.price

def askInput(goodies):

	print("____Goodies and Prices____")
	n=int(input("\nnumber of Goodies:"))
	
	i=0
	while(i<n):
		try:
			inputString = input("")
			name,price = inputString.split(":")
			price = int(price.strip())
			goodies.append(Goodie(name,price))
		except :
			print("__enter valid details__")
			i-=1

		i+=1

	return goodies

def sortGoodies(goodies):
	goodies.sort(key=lambda x: x.price)

def processOutputs(goodies):
	max_int=2147483647
	while(True):
		n=int(input("\nNumber of employes and 0 to stop:"))

		mincost = max_int
		startIndex = -1
	
		for i in range(len(goodies)-(n-1)):
			temp=goodies[i+n-1].price-goodies[i].price
			if(temp<mincost):
				mincost=temp
				startIndex=i

		if(startIndex==-1):
			print("not possible")
		else:
			print("Here the goodies that are selected for distribution are:")
			for i in range(startIndex,startIndex+n):
				print(goodies[i].name+":"+str(goodies[i].price))
			print("\nAnd the difference between the choosen goodie with higest price and lowest price is "+str(mincost))

		

if __name__ == '__main__':
	goodies=list()
	goodies=askInput(goodies)
	sortGoodies(goodies)
	processOutputs(goodies)
	