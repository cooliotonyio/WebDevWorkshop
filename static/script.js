var bee = document.getElementById("cursor");
document.addEventListener("mousemove", getMouse); 

bee.style.position = "absolute"; //css		
var beepos = {x:0, y:0};

var mouse = {x:0, y:0}; //mouse.x, mouse.y

function getMouse(e){
    mouse.x = e.pageX-100;
    mouse.y = e.pageY-100;
}

setInterval(followMouse, 50);

function followMouse(){
    var distX = mouse.x - beepos.x;
    var distY = mouse.y - beepos.y;
    beepos.x += distX/5;
    beepos.y += distY/2;
    bee.style.left = beepos.x + "px";
    bee.style.top = beepos.y + "px";
}