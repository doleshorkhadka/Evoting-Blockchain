from django.shortcuts import render
from web3 import Web3
import json
from .models import Candidate

# Initalizing connection with ganache .
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
if web3.isConnected():
	print('Web3 connected to local host...')

# Variable initilize 

# List of Candidates 
ListOfCandidate = []
for x in Candidate.objects.all():
	ListOfCandidate.append(x.name)
 

data = json.load(open("build/contracts/Evoting.json","r"))
# It indents the data format
# new_data = json.dumps(data, indent=2)    

# Getting the abi key and bytecode from json file
abi = data['abi']
bytecode = data["deployedBytecode"]
address = web3.toChecksumAddress(data['networks']['5777']['address'])

# Instantiating contract
MyContract = web3.eth.contract(
	abi= abi, 
	bytecode=bytecode,
	address=address
	)

# getting accounts form ganache
accounts = web3.eth.accounts

tx = {
	'from': accounts[1]
}
tx_for_vote = {
	'from': accounts[5]
}

def add_Candidate(cand):
    # for x in cand:
    #     ListOfCandidate.append(x.name)
    # for x in range(len(ListOfCandidate)):
    #     print('candidate added',x,str(ListOfCandidate[x]))
    #     MyContract.functions.addCandidate(str(ListOfCandidate[x])).transact(tx)
    
    for x in cand:
        print('candidate added',x.name)
        MyContract.functions.addCandidate(x.name).transact(tx)

def new_accounts():
     return accounts[0]

# Adding candidates to the Blockchain
# if not ListOfCandidate:
# 		add_Candidate(MyContract,accounts)

# def deployContract(Voter_name):
# 	#Function Calls
# 	res = {}
# 	res = Transactions(Voter_name)
# 	return res

#after the address is assigned add this to the Transaction sunctions

def Transactions(Voter_name,user_token):
	print("Transactions is up")
	print(ListOfCandidate)
	# c_user = request.User
	# print(c_user.id)
	for x in range(len(ListOfCandidate)):
		print(ListOfCandidate[x])
		if str(ListOfCandidate[x]) == str(Voter_name):
			tx_vote = {
				'from' : user_token
			}
			print(tx_vote)
			MyContract.functions.vote(x+1).transact(tx_vote)
			print("Voted for :",x+1,ListOfCandidate[x])
  
def final_result():
	result = {}
	results = []
	for x in range(1,len(ListOfCandidate)+1):
		results.append(MyContract.functions.getResult(x).call(tx))
	result['candidates']= ListOfCandidate
	result['result']= results
	print("Result: ",result)
	return (result)

# def res_Candidate(request):
#     MyContract.functions.resetCandidate().call(tx)
#     print("Reset complete")