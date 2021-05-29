 var Evoting = artifacts.require("./Evoting.sol")
 var evotingInstance
 contract("Evoting",
 	function(accounts){
	 	it("initializes with two candidates",function(){
	 		return Evoting.deployed().then(function (instance){
	 			return instance.candidateCount();
	 			}).then(function(count){
	 				assert.equal(count, 2);
	 			});
 		});

 		it("it initializes the candidates with the correct values",function(){
 			return Evoting.deployed().then(function(instance){
 				evotingInstance = instance;
 				return evotingInstance.candidate(1);
 			}).then(function (candidate){
 				assert.equal(candidate[0],1,"Contains the correct candidates id");
 				assert.equal(candidate[1],"Sunil Khadka","Contains the correct candidates Name");
 				assert.equal(candidate[2],0,"Contains the correct vote count");
 				return evotingInstance.candidate(2);
 			}).then(function(candidate){
 				assert.equal(candidate[0],2,"Contains the correct candidates id");
 				assert.equal(candidate[1],"Surakshya Khadka","Contains the correct candidates Name");
 				assert.equal(candidate[2],0,"Contains the correct vote count");
 			});
 		});
 });

