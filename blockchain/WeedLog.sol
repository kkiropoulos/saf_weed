// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract WeedLog {
    struct Record {
        string imageName;
        uint cropCount;
        uint weedCount;
        string decision;
        string explanation;
        uint timestamp;
    }

    Record[] public records;

    function addRecord(
        string memory _imageName,
        uint _cropCount,
        uint _weedCount,
        string memory _decision,
        string memory _explanation
    ) public {
        records.push(Record(
            _imageName,
            _cropCount,
            _weedCount,
            _decision,
            _explanation,
            block.timestamp
        ));
    }

    function getRecordsCount() public view returns (uint) {
        return records.length;
    }
}