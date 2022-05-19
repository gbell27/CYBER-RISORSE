#!/usr/bin/env node

const fs = require('fs');
const inquirer = require('inquirer');
const dig = require('node-dig-dns');
const netstat = require('node-netstat');

fs.readFile('rootservers.json', 'utf8', (err, data) => {
    if(err) {
        console.error(err);
    }
    console.log(data);
});


inquirer
.prompt([
	{
	  type : "list",
          name : "serverdns",
          message: "Select root dns server",
          choices : ["nessuno", "a", "b", "c", "d"]
        }])
