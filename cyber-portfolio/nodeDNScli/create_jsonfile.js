const fs = require('fs');
const axios = require('axios');
const $ = require('cheerio').default; //adding .default, otherwise Error: $ is not a function



function parse_fields (hostname, ips, operator) {
    let ip_field = ips.split(", ");
    let record = {
            "hostname" : hostname,
	    "ipv4": ip_field[0],
	    "ipv6": ip_field[1],
	    "operator" : operator
    }
    return record;
}


const parsingCallback = (res) => {
    let entries = []
    let final_obj = []
    $(".iana-table tr td", res.data).each((idx, el) => {
	entries.push($(el).text());
    })
    for (var i=0;i<entries.length;i+=3) {
        var record = parse_fields(entries[i], entries[i+1], entries[i+2]);
	final_obj.push(record);
        } 
    return Promise.resolve(final_obj);
}


let final_obj = axios.get("https://www.iana.org/domains/root/servers")
.then(parsingCallback)
.then((jsonObj) => {
    const fileStream = fs.createWriteStream('rootservers.json');
    fileStream.write(JSON.stringify(jsonObj));   //final object containing all parsed lines
    fileStream.end();  //closing file. Bye.
} )

