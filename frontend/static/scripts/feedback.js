function openForm() {
    document.getElementById("myForm").style.display = "block";
}

function closeForm() {
    document.getElementById("myForm").style.display = "none";
}

$("#feedbackSubmit").click(() => {
    var first_name = document.getElementById("fname").value;
    var last_name = document.getElementById("lname").value;
    var country = document.getElementById("country").value;
    var feedback_message = document.getElementById("feedback").value;
    
    var feedback_info = {"first_name": first_name, "last_name": last_name, "country": country,"feedback_message": feedback_message};
    $.ajax({
        type: "POST",
        url: "/feedback",
        data: JSON.stringify(feedback_info),
        contentType: "application/json",
        success: function submitForm() {
            confirm("Thanks for your feedback.")
            return true;
        },
        error: function (err) {
            console.log(err);
        },
    });
});