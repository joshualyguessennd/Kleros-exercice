// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.10;


contract KlerosExercice {
    address public owner;
    address public heir;
    uint public lastUpdate;

    event ReceivedAmount(uint amount, uint timeStamp);
    
    constructor() payable {
        owner = msg.sender;
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "!owner");
        _;
    }

    function withdraw() external onlyOwner {
        uint amount = address(this).balance;
        (bool success, ) = payable(msg.sender).call{value: amount}('');
        require(success);
        if (amount == 0) {
            lastUpdate = 0;
        } else {
            lastUpdate = block.timestamp;
        }
        
    }


    receive() external payable {
        emit ReceivedAmount(msg.value, block.timestamp);
    }
}

contract KlerosSolution is KlerosExercice {
    constructor(address _heir)  payable {
        heir = _heir;
    }

    function designateNewHair(address _newHeir) external {
        require(msg.sender == heir, "!heir");
        require(lastUpdate + 30 days <= block.timestamp, "!time");
        heir = _newHeir;
    }

}