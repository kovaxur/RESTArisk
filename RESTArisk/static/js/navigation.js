/**
 * Created by kovax on 2016. 10. 17..
 */

var loggedin = false

function navReady() {
    getData("/isAuthenticated",ifLoggedIn)

    $('#login').click(function() {
        if(loggedin == true ) {
            $('#login').text('Logging out..');
            getData("/logout",ifLoggedIn)
        } else {
            $('#login').text('Logging in..');
            window.location.replace("/auth");
        }
    });
};

function ifLoggedIn(data) {
    if( data === "true" ) {
        $('#login').text('Logout');
        loggedin = true
    } else {
        $('#login').text('Login');
        loggedin = false
    }
};

