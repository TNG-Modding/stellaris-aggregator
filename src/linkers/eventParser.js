import {PythonShell} from "python-shell"

function parseEventFile(filepath) {
    var path = require("path")

    var options = {
        mode: "text",
        args : [filepath]
    }

    PythonShell.run('./parseEventFile.py', options, function (err, results) {
        if (err) throw err;
        console.log('results: ', results);
    });
}

export default parseEventFile; 