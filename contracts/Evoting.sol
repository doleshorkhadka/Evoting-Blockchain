pragma solidity 0.5.16;


contract Evoting{
	//store candidates
	struct Candidate{
		uint id;
		string name;
		uint voteCount;
	}

	mapping(address => bool) public votedList;
	mapping(uint => Candidate) public candidate;

	uint public candidateCount;
    
    // modifier OnlyIfNotVoted{
    //     require(
    //     	votedList[msg.sender] == false,
    //     	"Sorry! You have already voted"
    //     	);
    //     	_;
    // }
	constructor() 
		public
		{
			addCandidate("Sunil Khadka");
			addCandidate("Surakshya Khadka");
		}
	function addCandidate
		(
			string memory _name
		) 
			private 
		{
			candidateCount ++;
			candidate[candidateCount] = Candidate(candidateCount,_name,0);
		}	

	function vote(uint _candidateID) public {
		// Checking wether the voter has already voted or not .
		require(
        	votedList[msg.sender] == false //or you can also use !votedList[msg.sender] foe condition
        	//"Sorry! You have already voted"
        ); 

        // Checking the candidate is a valid
        require(
        	_candidateID >0 && _candidateID <=candidateCount
        	//"Invalid candidate"
        );

		// update candidate vote count
		candidate[_candidateID].voteCount ++;
		votedList[msg.sender] = true;
	}
}