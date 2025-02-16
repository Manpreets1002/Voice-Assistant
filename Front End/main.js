$(document).ready(function () {
    $('.text').textillate({
        loop: true,
        sync: true,
        in:{
            efforts:"bounceIn",
        },
        out: {
            efforts: "bounceOut",
        },
    });
    // siriwave design
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
      });
      // text animation
      $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            sync: true,
        },

    });
    
    $("#MicBtn").click(function () { 
        // eel.playAssistantSound()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.all_commands()()
    });
    
    function doc_keyUp(e) {      
        if (e.key === 'j' && e.metaKey) {
            // eel.playAssistantSound()
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.all_commands()()
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    function PlayAssistant(message){
        if (message != ""){
            $("#Oval").attr("hidden",true);
            $("#SiriWave").attr("hidden",false);
            eel.all_commands(message);
            $("#chatbox").val("")
            $("#MicBtn").attr("hidden",false);
            $("#SendBtn").attr("hidden",true);
        }
    }

    function ShowHideBtn(message){
        if(message.length == 0){
            $("#MicBtn").attr("hidden",false);
            $("SendBtn").attr("hidden",true);
        }
        else{
            $("#MicBtn").attr("hidden",true);
            $("#SendBtn").attr("hidden",false);
        }
    }

    $("#chatbox").keyup(function(){
        let message = $("#chatbox").val();
        ShowHideBtn(message)
    });

    $("#SendBtn").click(function(){
        let message = $("#chatbox").val();
        PlayAssistant(message)
    });

});