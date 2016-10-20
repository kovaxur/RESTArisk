/**
 * Created by kovax on 2016. 10. 16..
 */

$(document).ready(function() {
    loadHTMLElements()
});

function loadHTMLElements(callback) {
    $("#header").load("header.html",function() {
        loadHTMLElementsReady(callback);
    });
    $("#navigation").load("navigation.html",function() {
        loadHTMLElementsReady(callback);
        navReady()
    });

};

function loadHTMLElementsReady(callback) {
};