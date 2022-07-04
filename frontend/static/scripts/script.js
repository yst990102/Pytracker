const analyseCodeBtn = document.querySelector('.editor_btn');
const editordiv = document.getElementById("inputeditor")
const outputdiv = document.getElementById("output")

let editor = ace.edit("editor");
var res = {};
var count = -1;
var recent = [];
var depth = 0;
var depth_stack = [];
var prev_end = 0;
var instructions = [];

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
    buttons.append('<button id="next" type="submit" class="editor_btn_next">Next</button>')
    buttons.append('<button id="prev" type="submit" class="editor_btn_prev">Prev</button>')

    // var grid = $("#graph");
    // markup = "";
    // for (var i = 0; i < parselist.length; i++) {
    //     markup += '<div class="row">';
    //     for (var j = 0; j < 3; j++) {
    //         id = "" + i + j;
    //         markup += '<div id ="' + id + '" class="col"></div>'
    //     }
    //     markup += '</div>';
    // }
    // grid.append(markup);

    // // Normal step line
    // arrowLine({
    //     source: `#${CSS.escape('00')}`,
    //     destination: `#${CSS.escape('10')}`,
    //     sourcePosition: 'middleLeft',
    //     destinationPosition: 'middleLeft',
    //     pivots: [{x: 30 ,y: 0}, {x: 2, y: -2}],
    //     forceDirection: 'horizontal'
    // });

    // // Longer step line
    // arrowLine({
    //     source: `#${CSS.escape('10')}`,
    //     destination: `#${CSS.escape('50')}`,
    //     sourcePosition: 'middleLeft',
    //     destinationPosition: 'middleLeft',
    //     pivots: [{x: 50 ,y: 0}, {x: 2, y: -4}],
    //     forceDirection: 'horizontal'
    // });

    // // Dashed line
    // arrowLine({
    //     source: `#${CSS.escape('50')}`,
    //     destination: `#${CSS.escape('21')}`,
    //     sourcePosition: 'middleLeft',
    //     destinationPosition: 'middleLeft',
    //     curvature: 0,
    //     style: 'dot',
    //     forceDirection: 'horizontal',
    //     endpoint: {
    //         type: 'none'
    //     }
    // });

     // Reflexive line for while loops


    // res = {
    //     d: 3,
    //     list: [
    //         {
    //             type: "step",
    //             start: [0, 0],
    //             end: [1, 0]
    //         },
    //         {
    //             type: "step",
    //             start: [1, 0],
    //             end: [4, 0]
    //         },
    //         {
    //             type: "step",
    //             start: [4, 0],
    //             end: [10, 0]
    //         },
    //         {
    //             type: "dashed",
    //             start: [10, 0],
    //             end: [2, 1]
    //         },
    //         {
    //             type: "while",
    //             start: [2, 1],
    //             end: [2, 1]
    //         }
    //     ]
    // }

    res = {
        d: 5,
        list: [
            {
                type: "step",
                start: 0,
                end: 1
            },
            {
                type: "step",
                start: 1,
                end: 2,
            },
            {
                type: "step",
                start: 2,
                end: 3
            },
            {
                type: "circle",
                start: 3
            },
            {
                type: "while_start",
                depth: 0
            },
            {
                type: "step",
                start: 3,
                end: 4
            },
            {
                type: "step",
                start: 4,
                end: 5
            },
            {
                type: "circle",
                start: 5
            },
            {
                type: "while_start",
                depth: 1
            },
            {
                type: "step",
                start: 5,
                end: 7
            },
            {
                type: "step",
                start: 7,
                end: 10
            },
            {
                type: "circle",
                start: 5
            },
            {
                type: "step",
                start: 5,
                end: 9
            },
            {
                type: "step",
                start: 9,
                end: 10
            },
            {
                type: "while_end",
                start: 5,
                end: 10
            },
            {
                type: "step",
                start: 10,
                end: 11
            },
            {
                type: "while_end",
                start: 3,
                end: 11
            },
            {
                type: "step",
                start: 11,
                end: 13
            },
            {
                type: "step",
                start: 13,
                end: 14
            }
        ]
    }

    var grid = $("#graph");
    markup = "";
    for (var i = 0; i < parselist.length; i++) {
        markup += '<div class="row">';
        for (var j = 0; j < res['d']; j++) {
            id = "" + i + j;
            markup += '<div id ="' + id + '" class="col"></div>'
        }
        markup += '</div>';
    }
    grid.append(markup);

    // arrowLine({
    //     source: `#${CSS.escape('21')}`,
    //     destination: `#${CSS.escape('21')}`,
    //     sourcePosition: 'middleLeft',
    //     destinationPosition: 'middleLeft',
    //     pivots: [{x: 20, y: -40}, {x: 35, y: 6}],
    //     forceDirection: 'horizontal',
    // });

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

$(document).on('click', '#stepbtns .editor_btn_next', function() {
    console.log(instructions)
    get_next();
});

$(document).on('click', '#stepbtns .editor_btn_prev', function() {
    if (count >= 0) {
        count -= 1;
        console.log(instructions[instructions.length - 1])
        console.log(instructions[recent.length - 2])
        if (instructions[recent.length - 1]['type'] == "step" && recent.length - 2 >= 0 && instructions[recent.length - 2]['type'] == "circle") {
            depth--;
            recent[recent.length - 1].remove();
            recent.pop();
            instructions.pop()

            recent[recent.length - 1].remove();
            recent.pop();
            instructions.pop()

            prev_end = instructions[recent.length - 1]['start']
            recent[recent.length - 1].remove();
            recent.pop();
            instructions.pop()

            count -= 1;
            if (res['list'][count]['type'] == "circle") {
                count -= 1;
            }
        } else if (instructions[instructions.length - 1]['type'] == "step" && instructions.length - 2 >= 0 && instructions[instructions.length - 2]['type'] == "dashed") {
            console.log("HERE")
            
            recent[recent.length - 1].remove();
            recent.pop();
            instructions.pop()

            recent[recent.length - 1].remove();
            recent.pop();
            instructions.pop()

            const pdepth = instructions[instructions.length - 1]['depth']
            depth = pdepth
            depth_stack.push(instructions[instructions.length - 1]['wdepth'])
            instructions.pop()

            count -= 1;
        } else {
            recent[recent.length - 1].remove();
            recent.pop();
            instructions.pop()
        }
    }
});

function get_next() {
    if (res['list'].length - 1 > count) {
        count += 1;
        if (res['list'][count]["type"] == "step") {
            var s = "" + res['list'][count]['start'] + depth;
            var e = "" + res['list'][count]['end'] + depth;
            console.log(s, e)
            dist = 1 + (res['list'][count]['end'] - res['list'][count]['start'])
            console.log(dist)
            recent.push(arrowLine({
                source: `#${CSS.escape(s)}`,
                destination: `#${CSS.escape(e)}`,
                sourcePosition: 'middleLeft',
                destinationPosition: 'middleLeft',
                pivots: [{x: 30 + dist ,y: 0}, {x: 2, y: -dist}],
                forceDirection: 'horizontal'
            }));
            prev_end = res['list'][count]['end']
            instructions.push(res['list'][count])
        } else if (res['list'][count]['type'] == "dashed") {
            var s = "" + res['list'][count]['start'][0] + res['list'][count]['start'][1];
            var e = "" + res['list'][count]['end'][0] + res['list'][count]['end'][1];
            recent.push(arrowLine({
                source: `#${CSS.escape(s)}`,
                destination: `#${CSS.escape(e)}`,
                sourcePosition: 'middleLeft',
                destinationPosition: 'middleLeft',
                curvature: 0,
                style: 'dot',
                forceDirection: 'horizontal',
                endpoint: {
                    type: 'none'
                }
            }));
            get_next()
        } else if (res['list'][count]['type'] == "circle") {    
            var prev_depth = depth;
            var p = "" + res['list'][count]['start'] + depth;
            depth++;
            var s = "" + res['list'][count]['start'] + depth;
            if (res['list'][count]['start'] == prev_end) {
                recent.push(arrowLine({
                    source: `#${CSS.escape(p)}`,
                    destination: `#${CSS.escape(s)}`,
                    sourcePosition: 'middleLeft',
                    destinationPosition: 'middleLeft',
                    curvature: 0,
                    style: 'dot',
                    forceDirection: 'horizontal',
                    endpoint: {
                        type: 'none'
                    }
                }));
                instructions.push({
                    type: "dashed",
                    start: res['list'][count]['start']
                })
            } else {
                p = "" + prev_end + prev_depth;
                recent.push(arrowLine({
                    source: `#${CSS.escape(p)}`,
                    destination: `#${CSS.escape(s)}`,
                    sourcePosition: 'middleLeft',
                    destinationPosition: 'middleLeft',
                    curvature: 0,
                    style: 'dot',
                    forceDirection: 'horizontal',
                    endpoint: {
                        type: 'none'
                    }
                }));
                instructions.push({
                    type: "dashed",
                    start: prev_end
                })
            }
            recent.push(arrowLine({
                source: `#${CSS.escape(s)}`,
                destination: `#${CSS.escape(s)}`,
                sourcePosition: 'middleLeft',
                destinationPosition: 'middleLeft',
                pivots: [{x: 20, y: -40}, {x: 35, y: 6}],
                forceDirection: 'horizontal',
            }));
            instructions.push(res['list'][count])
            get_next();
        } else if (res['list'][count]['type'] == "while_start") {
            depth_stack.push(res['list'][count]['depth'])
            console.log(depth_stack)
            get_next();
        } else if (res['list'][count]['type'] == "while_end") {
            const pdepth = depth;
            depth = depth_stack.pop()
            const while_depth = depth + 1;
            var s = "" + res['list'][count]['end'] + depth;
            var e = "" + res['list'][count]['end'] + while_depth;
            recent.push(arrowLine({
                source: `#${CSS.escape(s)}`,
                destination: `#${CSS.escape(e)}`,
                sourcePosition: 'middleLeft',
                destinationPosition: 'middleLeft',
                curvature: 0,
                style: 'dot',
                forceDirection: 'horizontal',
                endpoint: {
                    type: 'none'
                }
            }));
            instructions.push({
                type: "while_end",
                depth: pdepth,
                wdepth: depth
            })
            instructions.push({
                type: "dashed",
                start: res['list'][count]['start']
            })
            get_next();
        }
    }
}

editorlib.init();