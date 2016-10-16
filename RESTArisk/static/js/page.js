/**
 * Created by kovax on 2016. 10. 16..
 */

$(document).ready(function() {
    loadSite()
})

function loadSite() {
    console.log($(location).attr('href'));
    $('#content').html()
}