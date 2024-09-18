document.addEventListener("DOMContentLoaded", function () {
  const form = document.getElementById("cv-sender-form");
  const statusMessage = document.getElementById("status-message");
  const dismissButton = document.getElementById("dismiss-btn");
  const loadingSpinner = document.getElementById("loading-spinner");
  const resetButton = document.getElementById("reset-btn");
  const sendButton = document.getElementById("send-btn");
  const notificationSound = document.getElementById("notification-sound");

  // Form submission handler
  form.addEventListener("submit", async function (e) {
    e.preventDefault(); // Prevent default form submission behavior

    const formData = new FormData(form);

    // Show loading spinner
    loadingSpinner.style.display = "block";
    statusMessage.textContent = "Sending emails...";
    statusMessage.style.color = "blue";
    statusMessage.classList.add("fade-in"); // Adding animation class
    dismissButton.style.display = "none"; // Hide dismiss button initially
    sendButton.disabled = true; // Disable the send button to prevent multiple submissions

    try {
      const response = await fetch("http://localhost:5000/send-cv", {
        method: "POST",
        body: formData,
      });

      const result = await response.json(); // Parse the JSON response

      if (result.status === "success") {
        // Handle success response
        statusMessage.textContent = "Emails sent successfully!";
        statusMessage.style.color = "green";
        form.reset(); // Reset the form fields
        notificationSound.play(); // Play success notification sound
      } else {
        throw new Error(result.message); // Handle error response
      }
    } catch (error) {
      // Handle errors
      statusMessage.textContent = `Error: ${error.message}`;
      statusMessage.style.color = "red";
      notificationSound.play(); // Play error notification sound
    } finally {
      // Hide loading spinner and enable send button after processing
      loadingSpinner.style.display = "none";
      sendButton.disabled = false;
      dismissButton.style.display = "block"; // Show dismiss button
    }
  });

  // Dismiss button functionality
  dismissButton.addEventListener("click", function () {
    statusMessage.classList.add("fade-out"); // Add fade-out animation class
    setTimeout(() => {
      statusMessage.textContent = ""; // Clear status message
      statusMessage.classList.remove("fade-out"); // Remove fade-out class for future use
    }, 500); // Timeout for fade-out duration
  });

  // Reset form functionality
  resetButton.addEventListener("click", function () {
    form.reset(); // Reset the form fields
    statusMessage.textContent = ""; // Clear status message
    sendButton.disabled = false; // Enable send button
  });
});
