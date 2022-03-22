// SPDX-License-Identifier: GPL-3.0-or-later
pragma solidity ^0.8.10;

interface Vm {
    function warp(uint256) external;
    function prank(address) external;
    function startPrank(address) external;
    function stopPrank() external;
    function expectRevert(bytes calldata) external;
}