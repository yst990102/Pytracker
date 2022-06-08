const analyseCodeBtn = document.querySelector('.editor__btn');

let editor = ace.edit("editor");

let editorlib = {
    init() {
        editor.session.setMode("ace/mode/python");

        editor.setOptions({
            fontSize: '12pt',
            enableBasicAutocompletion: true,
        });
    }
}

$("#codeSubmit").click(() => {
    const usercode = editor.getValue();
    $.ajax({
        type: 'POST',
        url: "/",
        data: JSON.stringify(usercode),
        contentType: 'application/json',
        success: function(data){
            console.log(data);
        },
        error: function(err) {
            console.log(err);
        }
    })
})

editorlib.init();