//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Reentrance {
    mapping (address => uint) userBalance;

    function getBalance(address u) view public returns(uint){
        return userBalance[u];
    }

    function addToBalance() public payable{
        userBalance[msg.sender] += msg.value;
    }

    function withdrawBalance() public {
        // send userBalance[msg.sender] ethers to msg.sender
        // if mgs.sender is a contract, it will call its fallback function
        bool b = (payable(msg.sender).send(userBalance[msg.sender]) );
        if( ! b){
           revert();
        }
        userBalance[msg.sender] = 0;
    }

    // function getBool (bool, bytes u) public{
    //     return u[0];
    // }
}