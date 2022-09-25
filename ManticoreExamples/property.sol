//  MIT License
import "ManticoreExamples/Test.sol";
pragma solidity ^0.8.0;
contract TestToken is Token{
        constructor() public{
                //here lets initialize the thing
                balances[msg.sender] = 10000; //deployer account owns it all!
        }

        function crytic_test_balance() public returns (bool){
                return balances[msg.sender] <= 10000; //nobody can have more than 100% of the tokens
        }

}