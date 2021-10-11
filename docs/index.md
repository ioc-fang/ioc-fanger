# IOC Fanger

Welcome to the documentation for the `ioc-fanger` package!
This documentation is interactive, so feel free to edit the code and try it out!

<script src="https://cdn.jsdelivr.net/pyodide/v0.18.0/full/pyodide.js"></script>

<p>
    The code below shows a simple use-case. Feel free to edit and run it.
</p>

```python
import ioc_fanger

ioc_fanger.fang("example[.]com hXXp://bad[.]com/phishing[.]php")
# ioc_fanger.defang("example.com http://bad.com/phishing.php")
```

[Run][1]{ .md-button }

[1]: javascript:evaluatePython();

<div>Output:</div>
<textarea id="output" style="width: 100%;" rows="6" disabled></textarea>

<script>
    const output = document.getElementById("output");
    const code = document.getElementsByTagName("code")[0];

    function print(s) {
        output.value += s + "\n";
        // $('textarea').autoResize();
    }

    output.value = "Initializing...\n";
    // init Pyodide
    async function main() {
        let pyodide = await loadPyodide({
            indexURL: "https://cdn.jsdelivr.net/pyodide/v0.18.0/full/",
        });

        await pyodide.loadPackage('micropip');
        await pyodide.runPythonAsync(`
                import micropip
                await micropip.install('ioc-fanger')
                `);

        output.value += "Ready!\n";
        code.contentEditable = "true";

        return pyodide;
    }
    let pyodideReadyPromise = main();

    async function evaluatePython() {
    let pyodide = await pyodideReadyPromise;
    try {
        let output = pyodide.runPython(code.innerText);
        print(output);
    } catch (err) {
        print(err);
    }
    }
</script>
