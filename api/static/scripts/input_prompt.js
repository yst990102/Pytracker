$("#inputbutton").click(() => {
    input_prompt_popup("prompt_message");
});

function input_prompt_popup(prompt_message){
    let user_input = prompt(prompt_message);
    $.ajax({
        type: "POST",
        url: "/input",
        data: JSON.stringify(user_input),
        contentType: "application/json",
        success: function submitForm() {
            return true;
        },
        error: function (err) {
            console.log(err);
        },
    });
}