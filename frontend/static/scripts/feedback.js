function openForm() {
    document.getElementById("myForm").style.display = "block";
}

function closeForm() {
    document.getElementById("myForm").style.display = "none";
}

$("#feedbackSubmit").click(() => {
    var first_name = document.getElementById("fname").value;
    var last_name = document.getElementById("lname").value;
    var issue_type = document.getElementById("issue-type").value;
    var feedback_message = document.getElementById("feedback").value;
    
    var feedback_info = {"first_name": first_name, "last_name": last_name, "issue-type": issue_type,"feedback_message": feedback_message};
    
    // append a i tag to submit button
    document.getElementById("feedbackSubmit").innerText = "Sending email your feedback to us...";
    var loading_tag = document.createElement("i");
    loading_tag.setAttribute("id", "loading-spinner");
    loading_tag.setAttribute("class", "fa fa-spinner fa-spin"); 
    if(!document.getElementById("loading-spinner")){
        document.getElementById("feedbackSubmit").appendChild(loading_tag);
    
        $.ajax({
            type: "POST",
            url: "/feedback",
            data: JSON.stringify(feedback_info),
            contentType: "application/json",
            success: function submitForm() {
                confirm("Thanks for your feedback.");
                document.getElementById("feedbackSubmit").innerText = "Submit";
                return true;
            },
            error: function (err) {
                console.log(err);
            },
        });
    }
});