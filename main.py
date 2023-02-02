def get_result(guess, ans):
	a=0
	b=0
	for i in range(len(guess)):
		if guess[i]==ans[i]:
			a += 1
		elif guess[i] in ans:
			b += 1
	return (a, b)

#class comb +addtolist, filter , general valid (method)

class combination :
	combination_lists = []
	def __init__(self, comb_str) :
		self.combination = comb_str
	def valid(self, result, a, b):
		get_result_a, get_result_b = get_result(result,self.combination)
		if get_result_a>a+(self.combination).count("*") or get_result_a<a :
			return False
		elif get_result_b>b+(self.combination).count("*") or get_result_b<b:
			return False
		return True

#class include +addtolist, general valid (method)
class includes_digit:
	includes_digit_list = []
	def __init__(self, total, nums_include) :
		self.nums_include = nums_include
		self.total = total
	def valid_guess(self, guess):
		included_digit = 0
		for i in guess:
			if i in self.nums_include:
				included_digit += 1
		if included_digit==self.total:
			return True
		return False

	
#def next not repeat combination
def is_repeat(num:str):
	for i in range(len(num)-1):
		if num.count(num[i],i+1)>0:
			return True
	return False
def add_zero(digits, string):
	return "0"*(digits-len(string))+string
def next_combination(current_num):
	next_num = add_zero(len(current_num), str(int(current_num)+1))
	while is_repeat(next_num) :
		next_int = str(int(next_num)+1) #without zero starting
		next_num = add_zero(len(current_num), next_int)
	return next_num

#print title
print("+-------------------------+"+
      "\n| GUESSING 1A2B ALGORITHM |"+
	  "\n+-------------------------+")
#settings input number of digits
digits = int(input("\nENTER NUMBER OF DIGITS : "))

#create guessing num
guessing_num = "0"*digits
#do while loop
while True :
    #guess num
	#if guess num not possible continue

    #print guess num
    #get A
    #get B
    #if A = full break
    #if nA0B (generate comb)
    
    #include N numbers only (delete comb and add )
	pass

