async function updateMatches() {
    try {
        const fetchData = {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
        };

        const response = await fetch(document.URL, fetchData);
        
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const responseJson = await response.json();
        if (responseJson.type === "error")
            console.log(responseJson.error)
        displayMsg(responseJson.response, responseJson.type);
    } catch (error) {
        // Display an error message if something goes wrong
        displayMsg("Valami hiba történt!", "error");
        console.error('There was a problem with the fetch operation:', error);
    }
}