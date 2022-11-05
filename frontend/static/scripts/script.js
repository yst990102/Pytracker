const analyseCodeBtn = document.querySelector(".editor_btn");
const editordiv = document.getElementById("inputeditor");
const outputdiv = document.getElementById("output");

let editor = ace.edit("editor");
var res = {};
var count = -1;
var recent = [];
var depth = 0;
var depth_stack = [];
var prev_end = 0;
var instructions = [];
var no_starts = 0;
var inner_while = null;
var same_depth_while = false;
var prev_while_depth = 0;
var cur_line_num = 0;
var line_arrow_list = [];
var line_num_list = [];
var local_variables_list = [];
var program_output_list = [];

let editorlib = {
    init() {
        editor.session.setMode("ace/mode/python");

        editor.setOptions({
            fontSize: "12pt",
            enableBasicAutocompletion: true,
        });
    },
};

$("#codeSubmit").click(() => {
    frontend_main();
});

async function frontend_main(){
    var userinput_list = [];
    userinput_list = get_prompt_inputs();
    await $.ajax({
        type: "POST",
        url: "/userinput",
        data: JSON.stringify(userinput_list),
        contentType: "application/json",
        success: function(data){
            receive_status = data['receive_status'];
            if (receive_status != true){
                alert("userinput receive_status failed!!");
                return false;
            }
        },
        error: function(err) {
            console.log(err);
        },
    });
    
    if (!traceback_check()){
        analyse_usercode();
    }
}

function get_prompt_inputs(){
    var usercode_list = editor.getValue().trim().split('\n');
    var match_regex = /input\s?\(.*\)/g;
    var userinput_list = [];

    for (let i = 0; i < usercode_list.length; i++) {
        if (usercode_list[i].match(match_regex)){
            var userinput = prompt(usercode_list[i], "enter ur value here...");
            userinput_list.push({"usercode": usercode_list[i], "userinput": userinput});
        }
    }

    return userinput_list;
}


function traceback_check(){
    var traceback_result = false;
    $.ajax({
        type: "POST",
        async: false,
        url: "/traceback",
        data: JSON.stringify(editor.getValue().trim()),
        contentType: "application/json",
        success: function(data){
            If_Error = data['error'];
            if (If_Error){
                alert(data['error_msg']);
                traceback_result = true;
            }
        },
        error: function(err) {
            console.log(err);
        },
    });
    return traceback_result;
}

function analyse_usercode(){
    if (editordiv.style.display !== "none") {
        editordiv.style.display = "none";
    }
    
    const txt = editor.getValue();
    var usercode = txt.trim();
    var lines = usercode.split("\n");
    
    $.ajax({
        type: "POST",
        url: "/",
        data: JSON.stringify(usercode),
        contentType: "application/json",
        success: function (data) {
            code = data['code'].split('\n')
            console.log(code)

            parselist = [];
            parselist.push({
                num: "Program Start",
                content: "",
            })

            for (var i = 1; i < code.length; i++) {
                parselist.push({
                    num: i,
                    content: code[i - 1],
                });
            }
            var table = $("#code_output");
            parselist.forEach((dt, index) => {
                line_num = dt["num"];
                line_content = dt["content"];
                console.log(line_num);
                console.log(line_content);
                markup =
                    '<tr><td class="line_arrow" id="arr' + index + '" style="white-space: pre;"></td>' +
                    '<td class="line_num" style="white-space: pre;">' +
                    line_num +
                    '</td><td class="line_content" style="white-space: pre;">' +
                    line_content +
                    "</td></tr>";
                table.append(markup);
            });

            var line0_arrow = "arr" + 0
            line_num_list.push(0);
            line_arrow_list.push(
                arrowLine({
                    source: `#${CSS.escape(line0_arrow)}`,
                    destination: `#${CSS.escape(line0_arrow)}`,
                    sourcePosition: "middleLeft",
                    destinationPosition: "middleRight",
                    thickness: 1.3,
                    forceDirection: "horizontal",
                })
            )

            var buttons = $("#stepbtns");
            buttons.append(
                '<button id="next" type="submit" class="editor_btn_next">Next</button>'
            );
            buttons.append(
                '<button id="prev" type="submit" class="editor_btn_prev">Prev</button>'
            );
                
            var output_div = $("#prog_out");
            output_div.append(
                '<p class="prog_out_text">Program Output</p>' +
                '<div class="program_output_scroll"><table class="prog_table" id="prog_out_table"></table></div>'
            )

            var prev_var_div = $("#prev_var");
            prev_var_div.append(
                '<p class="prev_var_text">Previous variables</p>' +
                '<div class="prev_var_table_scroll"><table class="variable_table" id="prev_var_table"></table></div>'
            )
                
            var next_var_dix = $("#curr_var");
            next_var_dix.append(
                '<p class="curr_var_text">Current variables</p>' +
                '<div class="curr_var_table_scroll"><table class="variable_table" id="curr_var_table"></table></div>'
            )

            console.log(data)
            console.log(data['step_json']);
            res = data['step_json'];
            var grid = $("#graph");
            markup = "";
            for (var i = 0; i < parselist.length; i++) {
                markup += '<div class="row">';
                for (var j = 0; j < 20/*res['d']*/; j++) {
                    id = "r" + i + "c" + j;
                    markup += '<div id ="' + id + '" class="col"></div>';
                }
                markup += "</div>";
            }
            grid.append(markup);
            console.log("HERE")
            const height = $(window).height();
            const width = $(window).width();
            console.log(height, width)
            document.body.style.width = width;
            document.body.style.height = height;


        },
        error: function (err) {
            console.log(err);
        },
    });
}

$(document).on("click", "#stepbtns .editor_btn_next", function () {
    console.log("NEXT CLICK")
    console.log("Instructions = ", instructions);
    get_next();
    console.log(local_variables_list)
    console.log("DEPTH = ", depth)
    const height = $(window).height();
    const width = $(window).width();
    document.getElementById('__arrowLineInternal-svg-canvas').style.width = width
    document.getElementById('__arrowLineInternal-svg-canvas').style.height = height
    document.getElementById('__arrowLineInternal-svg-canvas').style.overflow = "visible"
});

$(document).on("click", "#stepbtns .editor_btn_prev", function () {
    get_prev();
});

function get_prev() {
    if (count >= 0) {
        count -= 1;
        console.log("PREV CLICK")
        if (
            instructions[instructions.length - 1]["type"] == "step" &&
            instructions.length - 2 >= 0 &&
            instructions[instructions.length - 2]["type"] == "circle"
        ) {
            console.log(depth_stack)
            console.log("HERE")
            const circle_depth = depth;
            depth--;
            console.log(instructions)
            // Remove step
            recent[recent.length - 1].remove();
            recent.pop();
            instructions.pop();
            local_variables_list.pop()
            program_output_list.pop()

            // Remove circle and iteration number
            recent[recent.length - 1].remove();
            recent.pop();
            const it_row = instructions[instructions.length - 1]["start"] - 1;
            const it_cell_id = "r" + it_row + "c" + circle_depth + "t";
            console.log(it_cell_id)
            console.log(depth)
            $("#" + it_cell_id).remove();
            instructions.pop();
            local_variables_list.pop()

            // Remove dashed line
            const dashed_line = instructions[instructions.length - 1];
            console.log("dashed_line")
            console.log(dashed_line)
            if (dashed_line['check'] === true) {
                depth = dashed_line['pdepth'];
                inner_while = dashed_line['ndepth'];
            }
            prev_end = instructions[instructions.length - 1]["start"];
            if (dashed_line['number'] !== 1) {
                recent[recent.length - 1].remove();
                recent.pop();
            }
            recent[recent.length - 1].remove();
            recent.pop();
            instructions.pop();

            count -= 1;
            prev_end = res["list"][count]["end"];
            if (res["list"][count]["type"] == "circle") {
                count -= 1;
                local_variables_list.pop()
            } else if (res['list'][count]['type'] == "while_end") {
                // If while_end then pop from instructions
                const pdepth = instructions[instructions.length - 1]["depth"];
                console.log(pdepth)
                depth = pdepth;
                depth_stack.push(instructions[instructions.length - 1]["wdepth"]);
                console.log(depth_stack)
                instructions.pop();

                while (instructions[instructions.length - 1]['type'] == "while_end") {
                    depth_stack.push(instructions[instructions.length - 1]["wdepth"]);
                    instructions.pop();
                    count -= 1;
                }
                count -= 1;
            }
        } else if (
            instructions[instructions.length - 1]["type"] == "step" &&
            instructions.length - 2 >= 0 &&
            instructions[instructions.length - 2]["type"] == "while_end"
        ) {
            console.log("STARTTTTTTTTTT =============")
            console.log("Instructions = ", instructions)
            recent[recent.length - 1].remove();
            recent.pop();
            recent[recent.length - 1].remove();
            recent.pop();
            instructions.pop();
            program_output_list.pop();

            if (instructions[instructions.length - 1]['type'] == "while_end") {
                inner_while = null;
            }

            /*
            recent[recent.length - 1].remove();
            recent.pop();
            instructions.pop();
            */

            const pdepth = instructions[instructions.length - 1]["depth"];
            console.log(pdepth)
            depth = pdepth;
            depth_stack.push(instructions[instructions.length - 1]["wdepth"]);
            console.log(depth_stack)
            instructions.pop();

            while (instructions[instructions.length - 1]['type'] == "while_end") {
                depth_stack.push(instructions[instructions.length - 1]["wdepth"]);
                instructions.pop();
                count -= 1;
            }

            count -= 1;
            local_variables_list.pop()
        } else if (
            instructions[instructions.length - 1]["type"] == "step" &&
            instructions.length - 2 >= 0 &&
            instructions[instructions.length - 2]["type"] == "while_start"
        ) {
            console.log("HERERERERE")
            const circle_depth = depth;
            // Remove step
            depth--;
            recent[recent.length - 1].remove();
            recent.pop();
            instructions.pop();
            local_variables_list.pop()
            program_output_list.pop()

            // Remove while_start
            if (same_depth_while === true) {
                same_depth_while = false;
            }
            instructions.pop();
            depth_stack.pop();
            no_starts--;

            // Remove circle
            recent[recent.length - 1].remove();
            recent.pop();
            const it_row = instructions[instructions.length - 1]["start"] - 1;
            const it_cell_id = "r" + it_row + "c" + circle_depth + "t";
            console.log(it_cell_id)
            console.log(depth)
            $("#" + it_cell_id).remove();
            instructions.pop();
            local_variables_list.pop()

            // Remove dashed
            prev_end = instructions[instructions.length - 1]["start"];
            recent[recent.length - 1].remove();
            recent.pop();
            instructions.pop();

            while (
                instructions[instructions.length - 1]["type"] == "step" &&
                instructions.length - 2 >= 0 &&
                instructions[instructions.length - 2]["type"] == "while_start"
            ) {
                const circle_depth = depth;
                // Remove step
                depth--;
                recent[recent.length - 1].remove();
                recent.pop();
                instructions.pop();
                program_output_list.pop()

                // Remove while_start
                if (same_depth_while === true) {
                    same_depth_while = false;
                }
                instructions.pop();
                depth_stack.pop();
                no_starts--;

                // Remove circle
                recent[recent.length - 1].remove();
                recent.pop();
                const it_row = instructions[instructions.length - 1]["start"] - 1;
                const it_cell_id = "r" + it_row + "c" + circle_depth + "t";
                console.log(it_cell_id)
                console.log(depth)
                $("#" + it_cell_id).remove();
                instructions.pop();

                // Remove dashed
                prev_end = instructions[instructions.length - 1]["start"];
                recent[recent.length - 1].remove();
                recent.pop();
                instructions.pop();
                count -= 3
                local_variables_list.pop()
                local_variables_list.pop()
            }
            console.log(instructions)

            console.log(instructions[instructions.length - 2])
            if (instructions.length - 2 >= 0 && instructions[instructions.length - 2]["type"] != "while_start") {
                if (instructions.length - 2 >= 0 && instructions[instructions.length - 2]["type"] == "while_end") {
                    prev_end = instructions[instructions.length - 1]["start"];
                    recent[recent.length - 1].remove();
                    recent.pop();
                    recent[recent.length - 1].remove();
                    recent.pop();
                    instructions.pop();
                    local_variables_list.pop()
                    program_output_list.pop()

                    if (instructions[instructions.length - 1]['type'] == "while_end") {
                        inner_while = null;
                    }
                    const pdepth = instructions[instructions.length - 1]["depth"];
                    console.log(pdepth)
                    depth = pdepth;
                    depth_stack.push(instructions[instructions.length - 1]["wdepth"]);
                    console.log(depth_stack)
                    instructions.pop();
                    count -= 1;
                } else if (instructions.length - 2 >= 0 && instructions[instructions.length - 2]["type"] == "circle") { 
                    console.log("AKSHDASHJDI")
                    const circle_depth = depth;
                    // Remove step
                    recent[recent.length - 1].remove();
                    recent.pop();
                    instructions.pop();
                    program_output_list.pop()

                    // Remove circle
                    depth--;
                    recent[recent.length - 1].remove();
                    recent.pop();
                    const it_row = instructions[instructions.length - 1]["start"] - 1;
                    const it_cell_id = "r" + it_row + "c" + circle_depth + "t";
                    console.log(it_cell_id)
                    console.log(depth)
                    $("#" + it_cell_id).remove();
                    instructions.pop();

                    // Remove dashed
                    prev_end = instructions[instructions.length - 1]["start"];
                    recent[recent.length - 1].remove();
                    recent.pop();
                    instructions.pop();
                    count -= 1
                    local_variables_list.pop()
                    local_variables_list.pop()
                } else {
                    // Remove step
                    recent[recent.length - 1].remove();
                    recent.pop();
                    instructions.pop();
                    local_variables_list.pop()
                    program_output_list.pop()
                }

                count -= 3;
            } else {
                count -= 2;
            }
            console.log(res['list'][count])
            console.log(count)

        } else {
            recent[recent.length - 1].remove();
            recent.pop();
            instructions.pop();
            local_variables_list.pop()
            program_output_list.pop();
        }
        console.log("stdout", program_output_list)
        if (program_output_list[program_output_list.length - 1] !== "" && program_output_list.length > 0) {
            var output_list = program_output_list[program_output_list.length - 1].split(/\r?\n/);
            var stdout_table = $("#prog_out_table")
            stdout_table.empty();
            output_list.forEach(item => {
                if (item !== "") {
                    if (program_output_list.length > 0) {
                        stdout_table.append(
                            '<tr><td class="prog_arr" style="white-space: pre;"> > </td>' +
                            '<td class="prog_stdout" style="white-space: pre;">' + item + '</td>' +
                            '</tr>'
                        )
                    }
                }
            })
        } else {
            var stdout_table = $("#prog_out_table")
            stdout_table.empty();
        }

        console.log(local_variables_list)
        var prev_table = $("#prev_var_table");
        var curr_table = $("#curr_var_table");
        if (local_variables_list.length > 1) {
            prev_table.empty();
            for (const [key, value] of Object.entries(local_variables_list[local_variables_list.length - 2])) {
                console.log(key, value)
                prev_table.append(
                    '<tr><td class="key_var" style="white-space: pre;">' + key + '</td>' +
                    '<td class="value_var" style="white-space: pre;">' + value + '</td>' +
                    '</tr>'
                )
            }
        } else {
            prev_table.empty();
        }
        if (local_variables_list.length > 0) {
            curr_table.empty();
            for (const [key, value] of Object.entries(local_variables_list[local_variables_list.length - 1])) {
                console.log(key, value)
                curr_table.append(
                    '<tr><td class="key_var" style="white-space: pre;">' + key + '</td>' +
                    '<td class="value_var" style="white-space: pre;">' + value + '</td>' +
                    '</tr>'
                )
            }
        } else {
            prev_table.empty();
            curr_table.empty();
        }

        console.log("DEPTH = ", depth)
        line_num_list.pop()
        console.log("line_num_list = ",line_num_list)
        var pv = line_num_list[line_num_list.length - 1]
        var line_num_arrow = "arr" + pv
        line_arrow_list[line_arrow_list.length - 1].remove();
        line_arrow_list.pop();
        line_arrow_list.push(
            arrowLine({
                source: `#${CSS.escape(line_num_arrow)}`,
                destination: `#${CSS.escape(line_num_arrow)}`,
                sourcePosition: "middleLeft",
                destinationPosition: "middleRight",
                thickness: 1.3,
                forceDirection: "horizontal",
            })
        )
    }
}

function get_next() {
    if (res["list"].length - 1 > count) {
        count += 1;
        console.log(instructions)
        if (res["list"][count]["type"] == "step" && count - 1 >= 0 && res['list'][count - 1]["type"] == "while_end") {
            var s = "r" + res["list"][count]["start"] + "c" + prev_while_depth;
            var e = "r" + res["list"][count]["end"] + "c" + depth;
            dist = 1 + (res["list"][count]["end"] - res["list"][count]["start"]);

            var straight_s = res["list"][count]["end"]
            var straight_depth = prev_while_depth - 1
            var temp_s = "r" + straight_s + "c" + straight_depth;

            recent.push(
                arrowLine({
                    source: `#${CSS.escape(s)}`,
                    destination: `#${CSS.escape(temp_s)}`,
                    sourcePosition: "middleLeft",
                    destinationPosition: "topCenter",
                    pivots: [
                        { x: 0, y: 0 },
                        { x: 25, y: 0 },
                    ],
                    forceDirection: "horizontal",
                    endpoint: {
                        type: "none",
                    },
                })
            )

            recent.push(
                arrowLine({
                    source: `#${CSS.escape(temp_s)}`,
                    destination: `#${CSS.escape(e)}`,
                    sourcePosition: "topCenter",
                    destinationPosition: "middleLeft",
                    curvature: 0.5,
                    forceDirection: "horizontal",
                })
            )



            prev_end = res["list"][count]["end"];
            line_num_list.push(prev_end);
            local_variables_list.push(res["list"][count]['local_variables'])
            instructions.push(res["list"][count]);
            program_output_list.push(res["list"][count]['stdout'])

            if (res["list"][count]['stdout'] !== "") {
                var output_list = res["list"][count]['stdout'].split(/\r?\n/);
                var stdout_table = $("#prog_out_table")
                stdout_table.empty();
                output_list.forEach(item => {
                    if (item !== "") {
                        if (program_output_list.length > 0) {
                            stdout_table.append(
                                '<tr><td class="prog_arr" style="white-space: pre;"> > </td>' +
                                '<td class="prog_stdout" style="white-space: pre;">' + item + '</td>' +
                                '</tr>'
                            )
                        }
                    }
                })
            }

            if (
                count + 1 < res["list"].length - 1 &&
                res["list"][count + 1]["type"] == "circle" &&
                count + 2 < res["list"].length - 1 &&
                res["list"][count + 2]["type"] == "while_start"
            ) {
                get_next();
            }
        } else if (res["list"][count]["type"] == "step") {
            var s = "r" + res["list"][count]["start"] + "c" + depth;
            var e = "r" + res["list"][count]["end"] + "c" + depth;
            dist = 1 + (res["list"][count]["end"] - res["list"][count]["start"]);
            recent.push(
                arrowLine({
                    source: `#${CSS.escape(s)}`,
                    destination: `#${CSS.escape(e)}`,
                    sourcePosition: "middleLeft",
                    destinationPosition: "middleLeft",
                    pivots: [
                        { x: 30 + dist, y: 0 },
                        { x: 2, y: - dist },
                    ],
                    forceDirection: "horizontal",
                })
            );
            prev_end = res["list"][count]["end"];
            line_num_list.push(prev_end);
            local_variables_list.push(res["list"][count]['local_variables'])
            instructions.push(res["list"][count]);
            program_output_list.push(res["list"][count]['stdout'])

            if (res["list"][count]['stdout'] !== "") {
                var output_list = res["list"][count]['stdout'].split(/\r?\n/);
                var stdout_table = $("#prog_out_table")
                stdout_table.empty();
                output_list.forEach(item => {
                    if (item !== "") {
                        if (program_output_list.length > 0) {
                            stdout_table.append(
                                '<tr><td class="prog_arr" style="white-space: pre;"> > </td>' +
                                '<td class="prog_stdout" style="white-space: pre;">' + item + '</td>' +
                                '</tr>'
                            )
                        }
                    }
                })
            }

            if (
                count + 1 < res["list"].length - 1 &&
                res["list"][count + 1]["type"] == "circle" &&
                count + 2 < res["list"].length - 1 &&
                res["list"][count + 2]["type"] == "while_start"
            ) {
                get_next();
            }
        } else if (res["list"][count]["type"] == "circle") {
            var p_depth = depth;
            var p = "r" + res["list"][count]["start"] + "c" + depth;
            var n_depth = null;
            var depth_check = false;
            console.log("inner_while = ", inner_while)
            if (inner_while !== null && res['list'][count + 1]['type'] !== "while_start" && !same_depth_while) {
                console.log("HERE")
                n_depth = inner_while;
                depth = inner_while;
                inner_while = null;
                depth_check = true;
            } else if (inner_while !== null && res['list'][count + 1]['type'] === "while_start") {
                same_depth_while = true;
            }
            depth++;
            var s = "r" + res["list"][count]["start"] + "c" + depth;
            var it = res["list"][count]["start"] - 1;
            var it_cell_id = "r" + it + "c" + depth;
            var iteration_cell = $("#" + it_cell_id);
            iteration_cell.append(
                '<p id="' +
                it_cell_id +
                't" class="iteration_number">' +
                res["list"][count]["iteration"] +
                "</p>"
            );
            if (res["list"][count]["start"] == prev_end) {
                line_num_list.pop();
                recent.push(
                    arrowLine({
                        source: `#${CSS.escape(p)}`,
                        destination: `#${CSS.escape(s)}`,
                        sourcePosition: "middleLeft",
                        destinationPosition: "middleLeft",
                        curvature: 0,
                        style: "dot",
                        forceDirection: "horizontal",
                        endpoint: {
                            type: "none",
                        },
                    })
                );
                instructions.push({
                    type: "dashed",
                    start: res["list"][count]["start"],
                });
            } else {
                p = "r" + prev_end + "c" + p_depth;
                var depth_diff = depth - p_depth;
                if (depth_diff === 1) {
                    recent.push(
                        arrowLine({
                            source: `#${CSS.escape(p)}`,
                            destination: `#${CSS.escape(s)}`,
                            sourcePosition: "middleLeft",
                            destinationPosition: "middleLeft",
                            curvature: 0,
                            style: "dot",
                            forceDirection: "horizontal",
                            endpoint: {
                                type: "none",
                            },
                        })
                    );
                } else {
                    var previous_depth = depth - 1;
                    var previous_line = prev_end - 1;
                    var second_line_start = "r" + previous_line + "c" + previous_depth;
                    recent.push(
                        arrowLine({
                            source: `#${CSS.escape(p)}`,
                            destination: `#${CSS.escape(second_line_start)}`,
                            sourcePosition: "middleLeft",
                            destinationPosition: "middleRight",
                            pivots: [
                                { x: 0, y: 0 },
                                { x: 5, y: 40 },
                            ],
                            style: "dot",
                            forceDirection: "horizontal",
                            endpoint: {
                                type: "none",
                            },
                        })
                    );
                    recent.push(
                        arrowLine({
                            source: `#${CSS.escape(second_line_start)}`,
                            destination: `#${CSS.escape(s)}`,
                            sourcePosition: "middleRight",
                            destinationPosition: "middleLeft",
                            pivots: [
                                { x: 0, y: 0 },
                                { x: 0, y: 0 },
                            ],
                            style: "dot",
                            forceDirection: "horizontal",
                            endpoint: {
                                type: "none",
                            },
                        })
                    );
                }
                instructions.push({
                    type: "dashed",
                    start: prev_end,
                    pdepth: p_depth,
                    ndepth: n_depth,
                    check: depth_check,
                    number: depth_diff
                });
            }
            recent.push(
                arrowLine({
                    source: `#${CSS.escape(s)}`,
                    destination: `#${CSS.escape(s)}`,
                    sourcePosition: "middleLeft",
                    destinationPosition: "middleLeft",
                    pivots: [
                        { x: 20, y: -40 },
                        { x: 35, y: 6 },
                    ],
                    forceDirection: "horizontal",
                })
            );
            local_variables_list.push(res["list"][count]['local_variables'])
            instructions.push(res["list"][count]);
            get_next();
        } else if (res["list"][count]["type"] == "while_start") {
            no_starts++;
            if (depth_stack.length < no_starts) {
                depth_stack.push(depth - 1);
            }
            console.log("depth stack = ", depth_stack)
            instructions.push({
                type: "while_start",
            });
            get_next();
        } else if (res["list"][count]["type"] == "while_end") {
            console.log("curr = ", res['list'][count])
            console.log("count = ", count)
            console.log(inner_while)
            const pdepth = depth;
            console.log(same_depth_while)
            if (inner_while === null && same_depth_while === false) {
                inner_while = depth
            } else if (inner_while !== null && same_depth_while === true) {
                console.log(inner_while, depth);
                inner_while = Math.max(inner_while, depth);
                same_depth_while = false;
            }
            // For one line
            prev_while_depth = depth
            console.log("depth_stack = ", depth_stack)
            depth = depth_stack.pop();
            const while_depth = depth + 1;
            var s = "r" + res["list"][count]["end"] + "c" + depth;
            var e = "r" + res["list"][count]["end"] + "c" + while_depth;

            instructions.push({
                type: "while_end",
                depth: pdepth,
                wdepth: depth,
            });

            while (res['list'][count + 1]['type'] == "while_end" && count + 1 < res["list"].length - 1) {
                depth = depth_stack.pop();
                count += 1;
                instructions.push({
                    type: "while_end",
                    depth: pdepth,
                    wdepth: depth,
                });
            }
            /*
            recent.push(
                arrowLine({
                    source: `#${CSS.escape(s)}`,
                    destination: `#${CSS.escape(e)}`,
                    sourcePosition: "middleLeft",
                    destinationPosition: "middleLeft",
                    curvature: 0,
                    style: "dot",
                    forceDirection: "horizontal",
                    endpoint: {
                        type: "none",
                    },
                })
            );
            */
            /*
            instructions.push({
                type: "dashed",
                start: res["list"][count]["start"],
            });
            */

            if (res['list'][count + 1]['type'] == "circle" && count + 1 < res["list"].length - 1) {
                console.log("ASJDBHAJSBDJASDK =", prev_while_depth)
                depth = prev_while_depth;
                //inner_while = null;
            }
            console.log("DEPTH_STACK", depth_stack)
            get_next();
        }

        if (res["list"][count]["type"] == "step" || res["list"][count]["type"] == "circle") {
            console.log(res["list"][count]['local_variables'])
            console.log(local_variables_list)
    
            if (local_variables_list.length > 1) {
                var prev_table = $("#prev_var_table");
                prev_table.empty();
                for (const [key, value] of Object.entries(local_variables_list[local_variables_list.length - 2])) {
                    console.log(key, value)
                    prev_table.append(
                        '<tr><td class="key_var" style="white-space: pre;">' + key + '</td>' +
                        '<td class="value_var" style="white-space: pre;">' + value + '</td>' +
                        '</tr>'
                    )
                }
            }
    
            var curr_table = $("#curr_var_table");
            curr_table.empty();
            for (const [key, value] of Object.entries(local_variables_list[local_variables_list.length - 1])) {
                console.log(key, value)
                curr_table.append(
                    '<tr><td class="key_var" style="white-space: pre;">' + key + '</td>' +
                    '<td class="value_var" style="white-space: pre;">' + value + '</td>' +
                    '</tr>'
                )
            }
        }
        var line_num_arrow = "arr" + prev_end
        line_arrow_list[line_arrow_list.length - 1].remove();
        line_arrow_list.pop();
        line_arrow_list.push(
            arrowLine({
                source: `#${CSS.escape(line_num_arrow)}`,
                destination: `#${CSS.escape(line_num_arrow)}`,
                sourcePosition: "middleLeft",
                destinationPosition: "middleRight",
                thickness: 1.3,
                forceDirection: "horizontal",
            })
        )
    }
}

$(window).resize(function () {
    console.log("HERE")
    /*
    const height = $(window).height();
    const width = $(window).width();
    const svgParent = recent[recent.length - 1].getParentSvgId();
    $("#" + svgParent).attr("height", height);
    $("#" + svgParent).attr("width", width);
    */
    var line_num_arrow = "arr" + prev_end
    line_arrow_list[line_arrow_list.length - 1].remove();
    line_arrow_list.pop();
    line_arrow_list.push(
        arrowLine({
            source: `#${CSS.escape(line_num_arrow)}`,
            destination: `#${CSS.escape(line_num_arrow)}`,
            sourcePosition: "middleLeft",
            destinationPosition: "middleRight",
            thickness: 1.3,
            forceDirection: "horizontal",
        })
    )
    var temp_count = count;
    while (count >= 0) {
        get_prev();
    }
    while (count < temp_count) {
        get_next();
    }
    console.log(count)
    console.log(temp_count)
});

editorlib.init();
