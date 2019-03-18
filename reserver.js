/*
 * JS version (to use, paste to DevTools)
 */

function generate_data(seat) {
    let result = [], time_list = [], today = new Date();
    if (today.getDay() % 6) time_list = [1, 4];
    else time_list = [7, 9, 10]
    for (time of time_list)
        result.push(`code=001&s_code=${seat}&t_code=${time}`);
    return result;
}

for (let i = 1; i <= 72; ++i) {
    console.log(`Trying seat #${i}`);
    let payloads = generate_data(i);
    for (payload of payloads) {
        let xhttp = new XMLHttpRequest();
        let url = 'http://hi.hana.hs.kr/SYSTEM_Plan/Lib_System/Lib_System_Reservation/reservation_exec.asp';
        xhttp.open('POST', url, true);
        xhttp.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhttp.send(payload);
    }
}
