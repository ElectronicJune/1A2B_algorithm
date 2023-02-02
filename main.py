#class comb
#class include
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

