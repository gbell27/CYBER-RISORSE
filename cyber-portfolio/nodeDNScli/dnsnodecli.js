#!/usr/bin/env node

const fs = require('fs');
const inquirer = require('inquirer');
const dig = require('node-dig-dns');


const rawdata = fs.readFileSync('rootservers.json');
const rootservers = JSON.parse(rawdata);
const domainToSolve = process.argv[2];


function makeChoiceList(jsonResponse){
    let choices = [];
    for (var entry of jsonResponse){
	if('value' in entry){ // using this function also for DIG
            choices.push(`${entry['domain']}  ${entry['value']}`);
        }
	else{ // this one for rootservers.json file
            choices.push(`${entry['hostname']}  ${entry['ipv4']}`);
	}
    }
    return choices;
}


function makePrompt(choiceList) {
    inquirer.prompt([{
	type : "list",
        name : "receiver",
        message: "To whom do you want to talk?",
        choices : choiceList,
        }])
}


// const res = await makePrompt();
// res.receiver

function digCall(host, domainName){
    dig([`@${host}`, `${domainName}`]).then(res => {
    if ('additional' in res) {
        console.log(res.additional);
      }
    else if ('answer' in res){
        console.log('FOUND: ', res.answer);
      }
    else {
        throw new Error("Error. Something has happened. Try again.");
      }
    })
}



