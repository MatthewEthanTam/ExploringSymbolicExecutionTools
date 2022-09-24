//  MIT License
pragma solidity ^0.8.0;
import "ManticoreExamples/Test.sol"; 

contract TestToken is Token{ 
    constructor() public{ 
        balances[msg.sender] = 10000; // deployer account owns all the tokens (10000) 
    }
    function crytic_test_balance() view public returns (bool) {
        return balances[msg.sender] <= 10000;
    }

}