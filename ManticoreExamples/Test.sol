// MIT License
pragma solidity ^0.8.0;
contract Ownership {
    address  owner = msg.sender;
    function Owner() public {
        owner = msg.sender;
    }
    modifier isOwner() {
        require(owner == msg.sender);
        _;
    }
}
contract Pausable is Ownership {
    bool public paused = false;
    event Pause();
    event Unpause();
    modifier whenNotPaused() {
        require(!paused);
        _;
    }
    modifier whenPaused() {
        require(paused);
        _;
    }
    function pause() public isOwner {
        paused = true;
        emit Pause();
    }
    function unpause() public isOwner {
        paused = false;
        emit Unpause();
    }
}

contract Token is Pausable {
    mapping (address => uint256) public balances;
    function transfer (address to, uint value) whenNotPaused public {
        balances[msg.sender] -= value;
        balances[to] += value;
    }
}