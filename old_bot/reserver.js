/*
 * JS version (to use, paste to DevTools)
 */

let url = 'http://hi.hana.hs.kr/SYSTEM_Plan/Lib_System';
url += '/Lib_System_Reservation/reservation_exec.asp';

function generate_data(seat) {
    let result = [], today = new Date();
    let time_list = [...Array(5).keys()];
    for (time of time_list)
        result.push(`code=001&s_code=${seat}&t_code=${time}`);
    return result;
}

function sleepFor( sleepDuration ){
    var now = new Date().getTime();
    while(new Date().getTime() < now + sleepDuration){ /* do nothing */ } 
}

for (let i = 1; i <= 72; ++i) {
    console.log(`Trying seat #${i}`);
    let payloads = generate_data(i);
    for (payload of payloads) {
        let xhttp = new XMLHttpRequest();
        xhttp.open('POST', url, true);
        xhttp.setRequestHeader('Content-Type',
                               'application/x-www-form-urlencoded');
        xhttp.send(payload);
        sleepFor(500);
        console.log(xhttp)
    }
}
