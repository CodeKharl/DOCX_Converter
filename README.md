# Code to DOCX Converter

A simple **command-line tool** that converts one or more source code files into a **formatted DOCX document**. This is useful for documentation, submissions, reports, or academic requirements where code needs to be presented in a readable Word file.

The tool supports custom **font name** and **font size**, making it flexible for different formatting standards.

---

## ✨ Features

* Convert **multiple input files** into a single DOCX document
* Customizable **font name** and **font size**
* Sensible defaults for quick usage
* Clean and minimal CLI interface using `argparse`

---

## 📦 Requirements

* Python 3.8+
* Required dependencies (install via pip):

```bash
pip install python-docx
```

---

## 🚀 Usage

### Basic Usage

```bash
python main.py file1.py file2.c file3.java
```

This will generate a DOCX file using the default output name and font settings.

---

### Specify Output File

```bash
python main.py file1.py file2.py -o output.docx
```

---

### Customize Font Name and Size

```bash
python main.py file1.py \
  --fontname "Courier New" \
  --fontsize 11
```

---

## 🧾 Command-Line Arguments

| Argument         | Description                                   |
| ---------------- | --------------------------------------------- |
| `inputs`         | One or more input files to convert (required) |
| `-o`, `--output` | Output DOCX file name                         |
| `--fontname`     | Font name used in the DOCX file               |
| `--fontsize`     | Font size used in the DOCX file               |

---

## 🛠️ Example

```bash
python main.py src/main.py src/utils.py -o code.docx --fontname Consolas --fontsize 10
```

---

## 📁 Project Structure

```text
.
├── main.py           # CLI entry point
├── converter.py      # Core conversion logic
└── README.md         # Project documentation
```

---

## 🧠 How It Works

1. The CLI parses arguments using `argparse`
2. Input files are read sequentially
3. Code content is passed to the converter
4. The converter formats and writes everything into a DOCX file

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## 👤 Author

Developed by **Kharl Denzell Bugarin**
Focused on clean tooling, automation, and practical developer utilities.

---

If you want enhancements like syntax highlighting, line numbers, or per-file headers, feel free to extend the converter module.
