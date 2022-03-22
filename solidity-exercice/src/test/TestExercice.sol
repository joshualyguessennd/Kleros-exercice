// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.10;

import "ds-test/test.sol";
import "./interfaces/IVM.sol";
import "../Exercice.sol";

contract Solution is DSTest {
    Vm vm = Vm(0x7109709ECfa91a80626fF3989D68f67F5b1DD12D);
    address deployer = 0x27a1876A09581E02E583E002E42EC1322abE9655;
    address heir = 0x451237d0e02721dBaB3E7E806d609f550EC1ee77;

    KlerosSolution solution;
    

    function setUp() public {
        vm.prank(deployer);
        solution = new KlerosSolution(heir);
    }

    function testOwner() public {
        assertEq(deployer, solution.owner());
    }

    function testWithdraw() public {
        vm.prank(deployer);
        solution.withdraw();
        assertEq(0, solution.lastUpdate());
        vm.expectRevert("!owner");
        solution.withdraw();
        // test withdraw heir
        vm.startPrank(heir);
        vm.expectRevert("!time");
        solution.withdrawHasHeir();
        vm.warp(2700000);
        solution.withdrawHasHeir();
    }



    function testnewHair() public {
        vm.prank(deployer);
        solution.withdraw();
        vm.startPrank(heir);
        vm.expectRevert("!time");
        solution.designateNewHair(deployer);
        vm.warp(2700000);
        solution.designateNewHair(deployer);
        assertEq(deployer, solution.heir());  
    }
}