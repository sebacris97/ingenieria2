var count = 5;
var redirect = "http://localhost:8000/";

function countDown(){
    var timer = document.getElementById("timer");
    if(count > 0){
        count--;
        timer.innerHTML = "Esta pagina lo redireccionara en "+count+" segundos.";
        setTimeout("countDown()", 1000);
}else{
        window.location.href = redirect;
    }
}

countDown();