const crypto = require('crypto-js');

function a(method, obj) {
    var appId = '8799d365982d550c1951012ccd155e06';
    var clienttype = 'WEB';
    var timestamp = new Date().getTime();
    var param = {
        appId: appId,
        method: method,
        timestamp: timestamp,
        clienttype: clienttype,
        object: obj,
        secret: hex_md5(appId + method + timestamp + clienttype + JSON.stringify(ObjectSort(obj)))
    };
    param = BASE64.encrypt(JSON.stringify(param));
    return param
}

function hex_md5(text) {
    return crypto.createHash("md5").update(text).digest("hex");
}

function b(data) {
    var pFFCSlm = a("GETCITYWEATHER", data);
    return pFFCSlm;
}

