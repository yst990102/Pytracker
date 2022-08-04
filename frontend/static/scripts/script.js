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
    if (editordiv.style.display !== "none") {
        editordiv.style.display = "none";
    }

    const txt = editor.getValue();
    var usercode = txt.trim();
    var lines = usercode.split("\n");
    parselist = [];
    for (var i = 1; i <= lines.length; i++) {
        parselist.push({
            num: i,
            content: lines[i - 1],
        });
    }
    console.log(parselist);

    var table = $("#code_output");
    parselist.forEach((dt) => {
        line_num = dt["num"];
        line_content = dt["content"];
        console.log(line_num);
        console.log(line_content);
        markup =
            '<tr><td class="line_num" style="white-space: pre;">' +
            line_num +
            '</td><td class="line_content" style="white-space: pre;">' +
            line_content +
            "</td></tr>";
        table.append(markup);
    });

    var buttons = $("#stepbtns");
    buttons.append(
        '<button id="next" type="submit" class="editor_btn_next">Next</button>'
    );
    buttons.append(
        '<button id="prev" type="submit" class="editor_btn_prev">Prev</button>'
    );

    $.ajax({
        type: "POST",
        url: "/",
        data: JSON.stringify(usercode),
        contentType: "application/json",
        success: function (data) {
            console.log(data);
            res = data;
            var grid = $("#graph");
            markup = "";
            for (var i = 1; i <= parselist.length; i++) {
                markup += '<div class="row">';
                for (var j = 0; j < 70; j++) {
                    id = "r" + i + "c" + j;
                    markup += '<div id ="' + id + '" class="col"></div>';
                }
                markup += "</div>";
            }
            grid.append(markup);
        },
        error: function (err) {
            console.log(err);
        },
    });
});

$(document).on("click", "#stepbtns .editor_btn_next", function () {
    console.log("NEXT CLICK")
    console.log("Instructions = ", instructions);
    get_next();
    console.log("DEPTH = ", depth)
});

$(document).on("click", "#stepbtns .editor_btn_prev", function () {
    if (count >= 0) {
        count -= 1;
        console.log("PREV CLICK")
        if (
            instructions[instructions.length - 1]["type"] == "step" &&
            instructions.length - 2 >= 0 &&
            instructions[instructions.length - 2]["type"] == "circle"
        ) {
			console.log("HERE")
            const circle_depth = depth;
            depth--;
			console.log(instructions)
            // Remove step
            recent[recent.length - 1].remove();
            recent.pop();
            instructions.pop();

            // Remove circle and iteration number
            recent[recent.length - 1].remove();
            recent.pop();
            const it_row = instructions[instructions.length - 1]["start"] - 1;
            const it_cell_id = "r" + it_row + "c" + circle_depth + "t";
            console.log(it_cell_id)
            console.log(depth)
            $("#" + it_cell_id).remove();
            instructions.pop();

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
            }
        } else if (
            instructions[instructions.length - 1]["type"] == "step" &&
            instructions.length - 2 >= 0 &&
            instructions[instructions.length - 2]["type"] == "dashed"
        ) {

            recent[recent.length - 1].remove();
            recent.pop();
            instructions.pop();

            recent[recent.length - 1].remove();
            recent.pop();
            instructions.pop();

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
        } else if (
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

            // Remove step
            recent[recent.length - 1].remove();
            recent.pop();
            instructions.pop();
            count -= 3;

        } else {
            recent[recent.length - 1].remove();
            recent.pop();
            instructions.pop();
        }
        console.log("DEPTH = ", depth)
    }
});

function get_next() {
    if (res["list"].length - 1 > count) {
        count += 1;
        if (res["list"][count]["type"] == "step") {
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
            instructions.push(res["list"][count]);
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
                                { x: 0, y: 30 },
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
            const pdepth = depth;
            console.log(same_depth_while)
			if (inner_while === null && same_depth_while === false) {
				inner_while = depth
			} else if (inner_while !== null && same_depth_while === true) {
                console.log(inner_while, depth);
                inner_while = Math.max(inner_while, depth);
                same_depth_while = false;
            }
            console.log("depth_stack = ", depth_stack)
            depth = depth_stack.pop();
            const while_depth = depth + 1;
            var s = "r" + res["list"][count]["end"] + "c" + depth;
            var e = "r" + res["list"][count]["end"] + "c" + while_depth;
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
            instructions.push({
                type: "while_end",
                depth: pdepth,
                wdepth: depth,
            });
            instructions.push({
                type: "dashed",
                start: res["list"][count]["start"],
            });
            get_next();
        }
    }
}

$(window).resize(function () {
    const height = $(window).height();
    const width = $(window).width();
    const svgParent = recent[recent.length - 1].getParentSvgId();
    $("#" + svgParent).attr("height", height);
    $("#" + svgParent).attr("width", width);

    console.log(svgParent, height, width);
});

editorlib.init();
