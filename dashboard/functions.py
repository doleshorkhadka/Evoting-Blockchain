from django.shortcuts import render
from web3 import Web3
import json
from .models import Candidate
from officer.models import Election

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
	'from': accounts[7]
}
tx_for_vote = {
	'from': accounts[3]
}

def add_Candidate(cand):
	is_sts = Election.objects.get(id=1)
	if (is_sts.status):
		print("Candidate already added to Blockchain !")
	else:
		for x in cand:
			print('candidate added',x.name)
			MyContract.functions.addCandidate(x.name).transact(tx)
		is_sts.status = True
		is_sts.save()



def new_accounts():
     return accounts[0]



def Transactions(Voter_name,user_token):
	print("Transactions is up")
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
