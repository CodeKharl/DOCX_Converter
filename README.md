# Code to DOCX Converter

A simple **command-line tool** that converts one or more source code files into a **formatted DOCX document**. This is useful for documentation, submissions, reports, or academic requirements where code needs to be presented in a readable Word file.

The tool supports custom **font name** and **font size**, making it flexible for different formatting standards.

---

## ✨ Features

* Convert **multiple input files** into a single DOCX document
* Each input file is added under its own **heading** (the file name)
* Customizable **font name** and **font size**
* Sensible defaults for quick usage
* Reads files as UTF-8 text
* Clean and minimal CLI interface using `argparse`

---

## 📦 Requirements

* Python 3.8+
* [python-docx](https://pypi.org/project/python-docx/)

---

## 🛠️ Installation

It is recommended to use a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install python-docx
```

---

## 🚀 Usage

### Basic Usage (script | non script)

```bash
./scripts/convert file1.py file2.c file3.java
```

```python
python3 docx_file_converter file1.py file2.c file3.java
```

This will generate a DOCX file using the default output name and font settings
(`output.docx`, `Times New Roman`, 12pt).

> **Note:** The `./scripts/convert` wrapper activates the `.venv` virtual
> environment, so the venv must exist before using it (see Installation).

---

### Specify Output File

```bash
./scripts/convert file1.py file2.py -o output.docx
```

```python
python3 docx_file_converter file1.py file2.py -o output.docx
```

---

### Customize Font Name and Size

```bash
./scripts/convert file1.py \
  --fontname "Courier New" \
  --fontsize 11
```

```python
python3 docx_file_converter file1.py \
  --fontname "Courier New" \
  --fontsize 11
```

---

## 🧾 Command-Line Arguments

| Argument          | Description                          | Default          |
| ----------------- | ------------------------------------ | ---------------- |
| `inputs`          | One or more input files to convert (required) | —        |
| `-o`, `--output`  | Output DOCX file name                | `output.docx`    |
| `--fontname`      | Font name used in the DOCX file      | `Times New Roman`|
| `--fontsize`      | Font size used in the DOCX file      | `12`             |

---

## 🛠️ Example

```bash
./scripts/convert src/main.py src/utils.py -o code.docx --fontname Consolas --fontsize 10
```

```python
python3 docx_file_converter src/main.py src/utils.py -o code.docx --fontname Consolas --fontsize 10
```

---

## 📁 Project Structure

```text
.
├── docx_file_converter/   # Python package
│   ├── __main__.py        # CLI entry point (argparse)
│   └── converter.py       # DOCX conversion logic
├── scripts/
│   └── convert            # Bash wrapper (activates .venv)
├── .gitignore
├── LICENSE                # MIT License
└── README.md              # Project documentation
```

---

## 🧠 How It Works

1. The CLI parses arguments using `argparse`
2. A new DOCX document is created
3. For each input file:
   - A heading is added using the file name
   - The file content is read as UTF-8 text
   - The content is added to the document with the given font name and size
   - A blank paragraph separates the files
4. The document is saved to the output path and a confirmation message is printed

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 👤 Author

Developed by **Kharl Denzell Bugarin**
Focused on clean tooling, automation, and practical developer utilities.

---
