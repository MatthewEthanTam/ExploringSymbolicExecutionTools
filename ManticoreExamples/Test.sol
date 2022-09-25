contract Ownership{  // It can have an owner!
        address owner = msg.sender;
        function Onwer() public{
                owner = msg.sender;
        }
        // modifier isOwner(){
        //         require(owner == msg.sender);
        //         _;
        // }
}
contract Pausable is Ownership{ //It is also pausable. You can pause it. You can resume it.
    bool is_paused;
    modifier ifNotPaused(){
        require(!is_paused);
        _;
    }
    function paused() public{
        is_paused = true;
    }
    function resume() public{
        is_paused = false;
    }
}
contract Token is Pausable{ //<< HERE it is.
    mapping(address => uint) public balances; // It maintains a balance sheet
    function transfer(address to, uint value) ifNotPaused public{  //and can transfer value
        balances[msg.sender] -= value; // from one account
        balances[to] += value;         // to the other
    }
}