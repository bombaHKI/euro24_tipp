function labelClicked(event) {
    const label = event.target;
    label.parentElement.children[0].focus();
}
Array.from(document.getElementsByTagName("label")).forEach( label => {
    label.addEventListener("click", labelClicked);
});
const fedlap = document.getElementById("fedlap");
function switchForm() {
    fedlap.classList.toggle("signup");
}

// input üres -> label felemel
Array.from(document.querySelectorAll(".input-container input")).forEach( input => {
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


const loginForm = document.getElementById("login-form");
if (loginForm) {
    const signupForm = document.getElementById("signup-form");
    loginForm.addEventListener("focusin", () => {
        fedlap.classList.remove("signup");
    });
    signupForm.addEventListener("focusin", () => {
        fedlap.classList.add("signup");
    });
    loginForm.addEventListener("submit", async event => {
        sendFormData(event, "login");
    });
    signupForm.addEventListener("submit", async event => {
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
                throw new Error();
            }
    
            const responseJson = await response.json();
            if ( actionType === "login" && responseJson.type !== "error")     
                window.location.href = "/";
            else
                displayMsg(responseJson.response, responseJson.type);
        } catch (error) {
            displayMsg("Valami hiba történt!","error");
            console.error(error);
        }
    }
}
else {
    document.getElementById("data-change-form").addEventListener("submit", async event => {
        sendFormData(event, "data-change");
    });
    document.getElementById("password-change-form").addEventListener("submit", async event => {
        sendFormData(event, "password-change");
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

        if (actionType === "password-change") {
            if (postJson["new-password"] !== postJson["confirm-password"]) {
                displayMsg("Jelszó megerősítése nem egyezik!", "error");
                return;
            }
        }
    
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
                throw new Error();
            }    
            const responseJson = await response.json();
            displayMsg(responseJson.response, responseJson.type);
        } catch (error) {
            displayMsg("Valami hiba történt!", "error");
            console.error(error);
        }
    }
}




