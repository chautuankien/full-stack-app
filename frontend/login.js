

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('login-form');

    form.addEventListener('submit', async function (event) {
        event.preventDefault(); // Prevent the default form submission
        console.log("Form submitted");

        // Get the values from the input fields
        const username = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        console.log("Username123:", username);
        console.log("Password:", password);

        // Create the data object to send
        try {
            const response = await fetch("http://localhost:8000/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    email: username,
                    password: password
                }),
            })

            const result = await response.json();
            console.log(result);

            if (response.ok) {
                // Handle successful login
                alert("Login successful!");
                
            } else {
                // Handle login failure
                alert("Login failed: " + result.message);
            }
        } catch (error) {
            console.error("Error:", error);
            alert("An error occurred. Please try again.");
        }
    });
});