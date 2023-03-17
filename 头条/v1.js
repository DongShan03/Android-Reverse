const jsdom = require('jsdom');
const {JSDOM} = jsdom;

const resourceLoader = new jsdom.ResourceLoader({
    userAgent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
});

const html = '<!DOCTYPE html><p>Hello world</p>'

const xx = new JSDOM(html, {
    url: "https://www.toutiao.com",
    referrer: "https://example.com",
    contentType: "text/html",
    resources: resourceLoader,
})


console.log(xx.window.location)
console.log(xx.window.navigator.userAgent)

