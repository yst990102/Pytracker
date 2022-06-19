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

    var buttons = $("#stepbtns")
    buttons.append('<button type="submit" class="editor_btn_prev">Prev</button>')
    buttons.append('<button type="submit" class="editor_btn_next">Next</button>')

    var grid = $("#graph");
    markup = "";
    for (var i = 0; i < parselist.length; i++) {
        markup += '<div class="row">';
        for (var j = 0; j < 3; j++) {
            id = "" + i + j;
            markup += '<div id ="' + id + '" class="col"></div>'
        }
        markup += '</div>';
    }
    grid.append(markup);

    // Normal step line
    arrowLine({
        source: `#${CSS.escape('00')}`,
        destination: `#${CSS.escape('10')}`,
        sourcePosition: 'middleLeft',
        destinationPosition: 'middleLeft',
        pivots: [{x: 30 ,y: 0}, {x: 2, y: -2}],
        forceDirection: 'horizontal'
    });

    // Longer step line
    arrowLine({
        source: `#${CSS.escape('10')}`,
        destination: `#${CSS.escape('50')}`,
        sourcePosition: 'middleLeft',
        destinationPosition: 'middleLeft',
        pivots: [{x: 50 ,y: 0}, {x: 2, y: -4}],
        forceDirection: 'horizontal'
    });

    // Dashed line
    arrowLine({
        source: `#${CSS.escape('50')}`,
        destination: `#${CSS.escape('21')}`,
        sourcePosition: 'middleLeft',
        destinationPosition: 'middleLeft',
        curvature: 0,
        style: 'dot',
        forceDirection: 'horizontal',
        endpoint: {
            type: 'none'
        }
    });

     // Reflexive line for while loops
    arrowLine({
        source: `#${CSS.escape('21')}`,
        destination: `#${CSS.escape('21')}`,
        sourcePosition: 'middleLeft',
        destinationPosition: 'middleLeft',
        pivots: [{x: 30, y: -40}, {x: 30, y: 15}],
        forceDirection: 'horizontal',

    });
    // console.log(arrow)
    // instance = jsPlumb.getInstance({});
    // instance.setContainer("diagram");
    // instance.bind("ready", function() {
    //     instance.connect({
    //         source:"00", 
    //         target:"10",
    //         anchors:["Right", "Right" ],
    //         endpoint: "Blank",
    //         paintStyle: { width: 10, stroke:"black"},
    //         detachable: false
    //     });
    // })

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