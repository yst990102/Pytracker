const analyseCodeBtn = document.querySelector('.editor_btn');
const editordiv = document.getElementById("inputeditor")
const outputdiv = document.getElementById("output")

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
    if (editordiv.style.display !== "none") {
        editordiv.style.display = "none";
    }

    const txt = editor.getValue();
    var usercode = txt.trim()
    var lines = usercode.split('\n');
    parselist = []
    for (var i = 1; i <= lines.length; i++) {
        parselist.push({
            num: i,
            content: lines[i - 1]
        })
    }
    console.log(parselist)

    var table = $("#code_output")
    parselist.forEach((dt) => {
        line_num = dt["num"]
        line_content = dt["content"]
        console.log(line_num)
        console.log(line_content)
        markup = '<tr><td class="line_num" style="white-space: pre;">' + line_num + '</td><td class="line_content" style="white-space: pre;">' + line_content + '</td></tr>';
        table.append(markup);

    });

    var grid = $("#graph");
    markup = "";
    for (var i = 0; i < parselist.length; i++) {
        markup += '<div class="row">';
        for (var j = 0; j < 3; j++) {
            markup += '<div class="col"></div>'
        }
        markup += '</div>';
    }
    grid.append(markup);

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