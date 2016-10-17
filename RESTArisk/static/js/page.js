/**
 * Created by kovax on 2016. 10. 16..
 */

$(document).ready(function() {
    loadHTMLElements()
});

function loadHTMLElements(callback=null) {
    $("#navigation").load("navigation.html",function() {
        loadHTMLElementsReady(callback);
    });
    $("#header").load("header.html",function() {
        loadHTMLElementsReady(callback);
    });
};

function loadHTMLElementsReady(callback=null) {
};