function signIN(){
    const userIsSignedIn = false; // Change this to your authentication check    
        // Get the sign-in button element
        const signInButton = document.getElementById('prediction');
            
        // Add a click event listener to the button
        signInButton.addEventListener('click', () => {
            if (userIsSignedIn) {
            // If the user is signed in, redirect to another page
                window.location.href = 'data_monitoring.html'; // Replace 'anotherpage.html' with your desired page URL
            } else {
                // If the user is not signed in, redirect to the sign-in page
                window.location.href = 'login.html'; // Replace 'signin.html' with your sign-in page URL
            }
        });
}