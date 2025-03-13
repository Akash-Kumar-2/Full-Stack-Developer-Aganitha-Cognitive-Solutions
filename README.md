# 📚 PubMed Paper Fetcher

A Python-based CLI tool that fetches research papers from PubMed, extracts authors affiliated with pharmaceutical/biotech companies, and saves the results as a CSV file.

## 🚀 Features
- ✅ Fetches PubMed papers based on a user query  
- ✅ Filters non-academic authors affiliated with **pharmaceutical/biotech companies**  
- ✅ Extracts **corresponding author emails** (if available)  
- ✅ Saves results in a structured **CSV file**  
- ✅ CLI supports **query, debug mode, and custom file output**  
- ✅ Uses **venv for virtual environment** and **Poetry for dependency management & operations**  
- ✅ Implements **robust error handling and modular code structure**  

---

## 📂 Project Structure
```bash
pubmed_fetcher/
│── pubmed_fetcher/  # Package directory
│   ├── __init__.py
│   ├── fetch_papers.py  # Fetches PubMed papers
│   ├── filter_authors.py  # Identifies non-academic authors
│   ├── csv_writer.py  # Writes filtered data to CSV
│   ├── cli.py  # CLI command-line interface
│── .gitignore
│── README.md
│── pyproject.toml  # Poetry configuration file
```

---

## 🛠 Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/yourusername/pubmed-fetcher.git
cd pubmed
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
```

### **3️⃣ Activate the Virtual Environment**
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux:**
  ```bash
  source venv/bin/activate
  ```

### **4️⃣ Install Poetry** (if not installed)
Poetry is used for dependency management.
```bash
pip install poetry
```

### **5️⃣ Install Dependencies Using Poetry**
```bash
poetry install
```

---

## 🎯 Usage

### **Run the CLI to Fetch PubMed Papers**
```bash
poetry run get-papers-list "deep learning"
```

### **Save Results to a Specific CSV File**
```bash
poetry run get-papers-list "cancer research" -f cancer_papers.csv
```

### **Enable Debug Mode for More Details**
```bash
poetry run get-papers-list "machine learning" --debug
```

### **Show Help Menu**
```bash
poetry run get-papers-list --help
```

---

## 🛠 Scripts & Commands
| Command | Description |
|---------|-------------|
| `python -m venv venv` | Create a virtual environment |
| `venv\Scripts\activate` (Windows) / `source venv/bin/activate` (Mac/Linux) | Activate the virtual environment |
| `pip install poetry` | Install Poetry |
| `poetry install` | Install dependencies |
| `poetry run get-papers-list "query"` | Run the CLI with a query |
| `poetry run get-papers-list "query" -f output.csv` | Save results to a file |
| `poetry run get-papers-list "query" --debug` | Run in debug mode |
| `pytest` | Run tests (if added) |

---

## 🛠 Dependencies
- **Python 3.8+** (Ensure Python is installed)
- **venv** (For virtual environment management)
- **Poetry** (For dependency management & operations)
- **Requests** (For API calls)

---

## 📜 License
This project is licensed under the **MIT License**.

---

