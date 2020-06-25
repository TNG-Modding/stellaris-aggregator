function parseEventFile(filepath) {
    var python = require("python-shell")
    var path = require("path")
    var options = {
        scriptPath: path.join(__dirname, "/../eventParser"),
        args: [filepath]
    }
    python.PythonShell.run('parseEventFile.py', options, function (err, results) {
        if (err) throw err;
        console.log(results);
    });
}