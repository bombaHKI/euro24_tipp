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

{ //inputok
    function labelClicked(event) {
        const label = event.target;
        label.parentElement.children[0].focus();
    }
    Array.from(document.getElementsByTagName("label")).forEach(label => {
        label.addEventListener("click", labelClicked);
    });

    // input üres -> label felemel
    Array.from(document.querySelectorAll(".input-container input")).forEach(input => {
        input.classList.toggle("non-empty",
            input.value !== ""
        );
        input.addEventListener("input", (ev) => {
            const inp = ev.target;
            inp.classList.toggle("non-empty",
                inp.value !== ""
            );
        });
    });
} //inputok

function dateToString(date) {
    const monthNuerals = ["I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII"];
    return monthNuerals[date.getMonth()] + ". " +
        date.getDate() + ". " +
        date.getHours() + ":" +
        String(date.getMinutes()).padStart(2,'0') + ".";
}