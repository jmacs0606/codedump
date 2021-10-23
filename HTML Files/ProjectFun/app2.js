const warning1_div = document.getElementById("warning1");
const warning2_div = document.getElementById("warning2");
warning1_div.style.visibility = 'hidden'
warning2_div.style.visibility = 'hidden'
warning1_div.style.height = 0;
warning2_div.style.height = 0;


const boopy_div = document.getElementById("boopy");
const boopyMsg_div = document.getElementById("boopyMsg");
const header_div = document.getElementById("h");
const record_div = document.getElementById("record");
var boobyClickCount = 0;
var audio = new Audio("assets/horror.mp3");
var audio2 = new Audio("assets/hit.mp3");
var audio3 = new Audio("assets/fun.mp3");
var audio4 = new Audio("assets/mhm.mp3");
var audio5 = new Audio("assets/wow.mp3");
var audio6 = new Audio("assets/HeadPop.mp3");
var audio7 = new Audio("assets/creepy.mp3");
var trigger = 0;

function jumpScare(){
    if (trigger == 0){
        trigger = 1;
        setTimeout(function(){
        audio3.pause();
        boopyMsg_div.remove();
        boopy_div.remove();
        header_div.remove();
        record_div.remove();
        document.body.style.backgroundImage = "url('assets/demon.jpg')";
        document.title = "patients kills";
        document.head.icon
        audio.play();
        audio2.play();
        setTimeout(function(){
            audio.pause();
            audio7.play();
        
        }, Math.floor((Math.random()+1) * 4000));

        setTimeout(function(){
            warning1_div.style.visibility = 'visible'

            warning1_div.style.height = 200;
            document.title = "go away";

        
        }, Math.floor((Math.random()+15)* 30000));
        setTimeout(function(){
            warning1_div.remove();
            warning2_div.style.visibility = 'visible'
            document.title = "the beginning";
            warning2_div.style.height = 200;

        
        }, Math.floor((Math.random()+16) * 30000));
        

        
    
    }, Math.floor((Math.random()+1) * 70000));
    }
}

boopy_div.addEventListener("click", function(){
    console.log("BOOPY HAS BEEN CLICKED");
    if(boobyClickCount < 69){
        boobyClickCount += 1;
    }
        
    if(boobyClickCount == 10 ||boobyClickCount == 20 || boobyClickCount == 30 || boobyClickCount == 40 ){
        audio5.pause();
        audio5.play();
    }
    if(boobyClickCount > 66 && boobyClickCount < 69){
        audio3.pause();
        audio4.pause();
        audio4.play();
        boopyMsg_div.innerHTML = "Boopy Has Been Clicked " + boobyClickCount.toString(10) + " times!<br> PLEASE DONT CLICK BOOPY MORE THAN 70 TIMES!";
    }
    else if(boobyClickCount > 1){
        boopyMsg_div.innerHTML = "Boopy Has Been Clicked " + boobyClickCount.toString(10) + " times!";
    }
    else if(boobyClickCount == 1){
        boopyMsg_div.innerHTML = "Boopy Has Been Clicked " + boobyClickCount.toString(10) + " time!";
        audio3.play();
    }
    if(boobyClickCount >68){
        audio6.play();
        jumpScare();
    }
})