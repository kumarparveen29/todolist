var user = document.getElementById('user');
var logout = document.getElementById('logout');
var star = document.getElementById('star');
var cross = document.getElementById('cross');

star.onclick = function(){
    logout.classList.toggle('close');
    user.classList.toggle('close');
} 

user.onclick = function(){
    document.querySelector('.bgmodel').style.display = "flex";
}

cross.onclick = function(){
    document.querySelector('.bgmodel').style.display = "none";
}