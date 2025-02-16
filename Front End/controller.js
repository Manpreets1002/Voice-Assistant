$(document).ready(function (){
    eel.expose(Displaymsg)
    function Displaymsg(message){
        $(".siri-message li:first").text(message);
        $(".siri-message").textillate("start");
    }

    eel.expose(ShowHood)
    function ShowHood(){
        $("#Oval").attr("hidden",false);
        $("#Siriwave").attr("hidden",true)
    }
});