function logout() {
    fetch('/logout', {
        // Use POST or GET based on your server's logout implementation
        method: 'POST', 
        headers: {
            'Content-Type': 'application/json'
        },
        // Include credentials for same-origin requests (important for session management)
        credentials: 'same-origin' 
    })
    .then(response => {
        if (response.ok) {
            window.location.href = '/login';
        } else {
            console.error('Logout failed', response);
        }
    })
    .catch(error => {
        console.error('Network error:', error);
    });
}

Array.from(document.getElementsByClassName("menu-gomb")).forEach( el => {
    el.addEventListener("click", event => {
        event.target.closest(".menu").classList.toggle("active");
    });
});
Array.from(document.getElementsByClassName("dropdown")).forEach( el => {
    el.addEventListener("mouseleave", event => {
        event.target.parentElement.classList.remove("active");
    });
});
Array.from(document.getElementsByClassName("dropdown-blur-layer")).forEach( el => {
    el.addEventListener("click", event => {
        event.target.parentElement.classList.remove("active");
    });
});

function headerClassDecider() {
    const header = document.getElementsByTagName("header")[0];
    const mainNav = document.getElementById("main-nav");
    const logo = document.getElementById("logo");
    const userMenu = document.getElementById("user-menu");
    
    header.classList.remove("small-header");
    if ( Math.max( (userMenu.getBoundingClientRect().left - logo.getBoundingClientRect().right),
                    (logo.getBoundingClientRect().left - mainNav.getBoundingClientRect().right)) < 30)
        header.classList.add("small-header");
}
window.addEventListener("resize", () => headerClassDecider());
headerClassDecider();