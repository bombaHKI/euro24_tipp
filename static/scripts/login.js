function labelClicked(event) {
    const label = event.target;
    label.parentElement.children[0].focus();
}
Array.from(document.getElementsByTagName("label")).forEach( label => {
    label.addEventListener("click", labelClicked);
});
function switchForm() {
    document.getElementById("fedlap").classList.toggle("signup");
}
document.getElementById("login-form").addEventListener("focusin", () => {
    document.getElementById("fedlap").classList.remove("signup");
});
document.getElementById("signup-form").addEventListener("focusin", () => {
    document.getElementById("fedlap").classList.add("signup");
});


document.getElementById("login-form").addEventListener("submit", async event => {
    sendFormData(event, "login");
});
document.getElementById("signup-form").addEventListener("submit", async event => {
    sendFormData(event, "signup");
});

/**
 * @param {SubmitEvent} event 
 * @param {String} actionType 
 */
async function sendFormData(event, actionType) {    
    event.preventDefault();    
    const form = event.currentTarget;
    const url = form.action;
    var postJson = Object.fromEntries(new FormData(form));
    postJson["action"] = actionType;
    postJson["email"] = postJson["email"].trim();
    if (actionType === "signup")
        postJson["username"] = postJson["username"].trim();

    try {
        const fetchData = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json",
            },
            body: JSON.stringify(postJson),
        };
        
        const response = await fetch(url, fetchData);

        if (!response.ok) {
            const errorMessage = "Valami hiba történt!";
            throw new Error(errorMessage);
        }

        const responseJson = await response.json();
        if ( actionType === "login" && responseJson.type != "error")     
            window.location.href = "/";
        else
            displayMsg(responseJson.response, responseJson.type);
    } catch (error) {
        console.error(error);
    }
}