// IIFE NOTATION
(() => {
    setInterval(()=>{
        $.ajax('/getdata', {
            success: function (data, status, xhr){
                if(data.data !== null) {
                    console.log(data.data);
                    showCounter(data.data);
                    // let carStatus;
                    for(let i=0 ; i < data.data.length ; i++){
                        console.log(data.data.length);
                        console.log('#ind-' + (i+1));
                        let indicator = $('#ind-' + (i+1));

                        if(data.data[i] === '1'){
                            indicator.css("background-color", "red");
                            // carStatus = "parked at";
                        }
                        else{
                            indicator.css("background-color", "limegreen");
                            // carStatus = "unparked from";
                        }
                    }

                    // $('#data-console div ol').append(`<li> car ${carStatus} spot ${data.data}</li>`)
                }
            }
        });
    }, 0);

    function showCounter(data){
        let count = 0;
        for(let i of data){
            if (i === "1"){count++;}
        }
        $("#spots-counter p").html(count);
    }
})();