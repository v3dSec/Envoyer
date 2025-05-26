# Envoyer

**Envoyer** is a tool designed for penetration testers and red team operators. It generates linker export directives from a DLL’s export table — a crucial step in crafting proxy DLLs for techniques like DLL sideloading and DLL hijacking.

By automating the creation of accurate export declarations, Envoyer streamlines proxy DLL development, reducing manual effort and minimizing the risk of errors during operations.

---

## 🔍 What is DLL Sideloading?

DLL sideloading is a technique where a malicious DLL is placed in a location where a legitimate application mistakenly loads it instead of the trusted, original DLL. This enables attackers to execute arbitrary code within the context of a trusted process.

To implement this effectively, proxy DLLs must forward the exported functions of the original DLL. Envoyer simplifies this process by extracting the required export information and generating the appropriate linker directives, enabling streamlined development of proxy DLL payloads that forward calls seamlessly.

---

## 💡 Why Use Envoyer?

Publicly available proxy DLL tools often include full implementations that generate the DLL, making them easily detectable by modern security solutions. In contrast, Envoyer takes a more flexible and stealthy approach by focusing solely on generating export directives, enabling experienced operators to craft custom proxy DLLs precisely tailored to their engagement.

Envoyer empowers red teamers to:

- Save time and reduce manual work  
- Maintain operational stealth  
- Create custom proxy DLLs that avoid signature-based detection  

---

## ✨ Key Features

- Extracts both named and ordinal (unnamed) exports from any DLL  
- Generates accurate `#pragma comment(linker, "/export:...")` directives  
- Lightweight and easy-to-use command-line interface  

---

## 🛠️ Installation

**Requirements**: Python 3.6+ and the `pefile` library

Clone the repository:

```bash
git clone https://github.com/v3dSec/envoyer.git  
cd envoyer
```
Install dependencies:

```bash
pip install -r requirements.txt
```
---

## 🚀 Usage

Basic syntax:

```bash
python3 envoyer.py -d <path_to_dll> [-p <proxy_dll_name>] [-o <output_file>]
```

### Arguments

- `-d`, `--dll-path`: Path to the target DLL **(required)**  
- `-p`, `--proxy-dll`: Name of the proxy DLL *(optional, defaults to the original DLL's name)*  
- `-o`, `--output-file`: Path to the output file *(optional, prints to console if omitted)*  

---

## 📘 Examples

Extract exports from `kernel32.dll` and print them to the console:

```bash
python3 envoyer.py -d kernel32.dll
```

Generate export directives proxying to `proxy.dll` and save to `exports.h`:

```bash
python3 envoyer.py -d kernel32.dll -p proxy.dll -o exports.h
```

---

## ⚠️ Disclaimer

**Envoyer** is intended strictly for **authorized security assessments and research**.  
Use only on systems and binaries where you have **explicit, documented permission**.
