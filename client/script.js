/* jshint esversion: 8 */
'use strict';

const BASE_URL = "http://127.0.0.1:5000/api/v1"

var languages = ['en', 'de', 'es', 'gl', 'eus'];
var categories= ['neutral', 'chuck', 'all'];

async function requestData(specification) {
    return fetch(`${BASE_URL}/${specification}`)
    .then(response => response.json())
    .then(json => printData(json[typeOfData]))
    .catch(error => console.log(error))
}

async function getJokes() {
    var formdata = new FormData(document.getElementsByName('jokeType')[0]);
    let language = formdata.get('language');
    let category = formdata.get('category');
    var number = 1;
    if (formdata.has('id')) {
        let id = formdata.get('id');
        let specification = `?language=${language}&category=${category}&id=${id}`;
        return requestData(specification);
    }
    else if (formdata.has('number')) {
        number = formdata.get('number');
    }
    let specification = `?language=${language}&category=${category}&number=${number}`;
        return requestData(specification);
}

function printData(data) {
    let responseDiv = document.querySelector("#response");
    responseDiv.innerHTML = data;
}

function populateSelect(selectId, sList) {
    let sel = document.getElementById(selectId);
    console.log(languages)
    for (let s of sList) {
        let opt = document.createElement("option");
        opt.value = s;
        opt.innerHTML = s;
        sel.appendChild(opt);
    }
}

window.onload = function() {
    populateSelect("langSelect", languages);
    populateSelect("catSelect", categories);
};
