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
        for (var j = 0; j < res["d"]; j++) {
          id = "" + i + j;
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
  console.log(instructions);
  get_next();
});

$(document).on("click", "#stepbtns .editor_btn_prev", function () {
  if (count >= 0) {
    count -= 1;
    console.log(instructions[instructions.length - 1]);
    console.log(instructions[recent.length - 2]);
    if (
      instructions[instructions.length - 1]["type"] == "step" &&
      instructions.length - 2 >= 0 &&
      instructions[instructions.length - 2]["type"] == "circle"
    ) {
      console.log(instructions);
      const circle_depth = depth;
      depth--;

      // Remove step
      recent[recent.length - 1].remove();
      recent.pop();
      instructions.pop();

      // Remove circle and iteration number
      recent[recent.length - 1].remove();
      recent.pop();
      const it_row = instructions[instructions.length - 1]["start"] - 1;
      const it_cell_id = "" + it_row + circle_depth + "t";
      $("#" + it_cell_id).remove();
      instructions.pop();

      // Remove dashed line
      prev_end = instructions[recent.length - 1]["start"];
      recent[recent.length - 1].remove();
      recent.pop();
      instructions.pop();

      count -= 1;
      console.log(res["list"][count]);
      prev_end = res["list"][count]["end"];
      if (res["list"][count]["type"] == "circle") {
        count -= 1;
      }
    } else if (
      instructions[instructions.length - 1]["type"] == "step" &&
      instructions.length - 2 >= 0 &&
      instructions[instructions.length - 2]["type"] == "dashed"
    ) {
      console.log("HERE");

      recent[recent.length - 1].remove();
      recent.pop();
      instructions.pop();

      recent[recent.length - 1].remove();
      recent.pop();
      instructions.pop();

      const pdepth = instructions[instructions.length - 1]["depth"];
      depth = pdepth;
      depth_stack.push(instructions[instructions.length - 1]["wdepth"]);
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
      instructions.pop();
      no_starts--;

      // Remove circle
      recent[recent.length - 1].remove();
      recent.pop();
      const it_row = instructions[instructions.length - 1]["start"] - 1;
      const it_cell_id = "" + it_row + circle_depth + "t";
      $("#" + it_cell_id).remove();
      instructions.pop();

      // Remove dashed
      prev_end = instructions[recent.length - 1]["start"];
      recent[recent.length - 1].remove();
      recent.pop();
      instructions.pop();

      // Remove step
      recent[recent.length - 1].remove();
      recent.pop();
      instructions.pop();
      count -= 3;

      console.log("LAST TYPE");
      console.log(res["list"][count]);
      console.log(instructions);
    } else {
      recent[recent.length - 1].remove();
      recent.pop();
      instructions.pop();
    }
  }
});

function get_next() {
  if (res["list"].length - 1 > count) {
    count += 1;
    console.log(instructions);
	console.log("DEPTH=")
	console.log(depth)
    if (res["list"][count]["type"] == "step") {
      var s = "" + res["list"][count]["start"] + depth;
      var e = "" + res["list"][count]["end"] + depth;
      console.log(s, e);
      dist = 1 + (res["list"][count]["end"] - res["list"][count]["start"]);
      console.log(dist);
      recent.push(
        arrowLine({
          source: `#${CSS.escape(s)}`,
          destination: `#${CSS.escape(e)}`,
          sourcePosition: "middleLeft",
          destinationPosition: "middleLeft",
          pivots: [
            { x: 30 + dist, y: 0 },
            { x: 2, y: -dist },
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
      var prev_depth = depth;
      var p = "" + res["list"][count]["start"] + depth;
	  if (inner_while !== null) {
		depth = inner_while
		inner_while = null
	  }
      depth++;
      var s = "" + res["list"][count]["start"] + depth;
      var it = res["list"][count]["start"] - 1;
      var it_cell_id = "" + it + depth;
      var iteration_cell = $("#" + it_cell_id);
      iteration_cell.append(
        '<p id="' +
          it_cell_id +
          't" class="iteration_number">' +
          res["list"][count]["iteration"] +
          "</p>"
      );
      console.log(iteration_cell);
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
        p = "" + prev_end + prev_depth;
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
          start: prev_end,
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
        depth_stack.push(res["list"][count]["depth"]);
        console.log(depth_stack);
      }
      instructions.push({
        type: "while_start",
      });
      get_next();
    } else if (res["list"][count]["type"] == "while_end") {
      const pdepth = depth;
      depth = depth_stack.pop();
	  if (depth_stack.length !== 0) {
		inner_while = pdepth;
	  }
      const while_depth = depth + 1;
      var s = "" + res["list"][count]["end"] + depth;
      var e = "" + res["list"][count]["end"] + while_depth;
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
