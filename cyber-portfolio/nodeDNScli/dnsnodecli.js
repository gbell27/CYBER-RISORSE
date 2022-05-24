#!/usr/bin/env node

const fs = require('fs');
const inquirer = require('inquirer');
const dig = require('node-dig-dns');


const rawdata = fs.readFileSync('rootservers.json');
const rootservers = JSON.parse(rawdata);
const domainToSolve = process.argv[2]; // ex. node dnsnodecli.js facebook.com


function makeChoiceList(jsonResponse){
    let choices = [];
    for (var entry of jsonResponse){
	if('value' in entry){ // using this function also for DIG
            choices.push(`${entry['domain']} ${entry['value']}`);
        }
	else{ // this one for rootservers.json file
            choices.push(`${entry['hostname']} ${entry['ipv4']}`);
	}
    }
    return choices;
}


function makePrompt(choiceList) {
    let promptChoice = inquirer.prompt([{
	type : "list",
        name : "receiver",
        message: "To whom do you want to talk?",
        choices : choiceList,
        }]);
    return Promise.resolve(promptChoice);
}


function digCall(host, domainName) {
    let dnslookup = dig([`@${host}`, `${domainName}`]);
    return Promise.resolve(dnslookup);
}


const main = async () => {
    var firstQuest = await makePrompt(makeChoiceList(rootservers));
    var ipField = firstQuest.receiver.split(" ")[1]; // only need ipv4 key
    
    var foundFlag = false;
    while(foundFlag != true){
        var dnsResponse = await digCall(ipField, domainToSolve);

        if ('additional' in dnsResponse) {
	    var secondQuest = await makePrompt(makeChoiceList(dnsResponse.additional));
	    ipField = secondQuest.receiver.split(" ")[1]; // only need 'value' key
	    // value CAN be IPV6, still not implemented.
        }
        else if ('answer' in dnsResponse){
	    foundFlag = true;
	    return Promise.resolve(makeChoiceList(dnsResponse.answer));
	}
        else {
	    //sometimes results are returned in 'authority' field, not implemented.
            throw new Error("Error. Something has happened. Try again.");
        }
    }
}


main()
.then((ans) => { 
	console.log(`Found "${domainToSolve}" at: ${ans}`);
})
.catch((err) => {
	console.log("Error. There are no 'additional' or 'answer' field in result. Sorry.")
})

