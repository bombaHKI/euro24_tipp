function displayMsg(msg, type) {
    var div = document.getElementById(type).cloneNode(true);
    document.body.appendChild(div);
    div.innerText = msg;
    div.classList.add("visible");

    setTimeout(() => {
        div.classList.remove("visible");
        setTimeout( () => {
            div.remove();
        },500);
    },2000);
}