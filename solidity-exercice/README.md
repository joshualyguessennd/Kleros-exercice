# Exercice Subject

create an inheritance smart contract in solidity. This smart contract should allow the owner to withdraw ETH from the contract . if the owner doesn't not withdraw ETH from the contract more than 1 month an heir can take control of the contract and designate a new heir. it should be possible for the owner to withdraw 0 ETH just to reset the one month counter

# Using the repo

1- Ensure you have install rust and cargo: INSTALL RUST

2- Install Foundry: cargo install --git https://github.com/gakonst/foundry --locked

3- Run the tests: forge test

# ToDo

The question is to know if the heir has the ability . set a function to allow heir to withdraw