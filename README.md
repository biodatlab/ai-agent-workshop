# แบบฝึกหัด Generative AI สำหรับผู้เข้าร่วม Sri Trang

ชุดแบบฝึกหัดสำหรับทดลอง LLM, RAG และเครื่องมือของ AI ทุกบทมีโค้ดใน notebook และติดตั้ง packages ที่ต้องใช้ด้วย `%pip install` ก่อน imports ไม่ต้องติดตั้ง repo เป็น Python package และไม่มี `pyproject.toml`

ตัวอย่างโรงงานยาง น้ำยาง QC และการขนส่งเป็นข้อมูลสมมติสำหรับการเรียน ไม่ใช่ข้อมูลหรือ SOP จริงของบริษัท

| Notebook | เนื้อหา | Runtime |
| --- | --- | --- |
| 01 | LLM API | Local / Colab |
| 02 | Structured output | Local / Colab |
| 03 | Local LLM ผ่าน Ollama | Local เป็นหลัก |
| 04 | Chunking | Local / Colab; ใช้ Python standard library ไม่ต้องติดตั้ง packages เพิ่ม |
| 05 | Semantic search | Local / Colab |
| 06 | Basic RAG | Local / Colab |
| 07 | PDF RAG | Local / Colab |
| 08 | Local RAG ด้วย LlamaIndex และ Ollama | Local เป็นหลัก |
| 09 | Multimodal RAG | Local / Colab |
| 10 | Tool calling | Local / Colab |
| 11 | OpenAI + MCP | Local / Colab |
| 12 | Local LLM + MCP | Local เป็นหลัก |
| 13 | Agent loop | Local / Colab |

## เปิดบนเครื่องผู้เรียน

ใช้ Python 3.11 หรือ 3.12 เปิด terminal ในโฟลเดอร์ repo และรันทีละบรรทัด

Windows PowerShell: ใช้ script ที่เตรียมไว้เพื่อสร้าง `.venv` ด้วย Python 3.11 และติดตั้ง JupyterLab กับ ipykernel ผ่าน pip ของ `.venv`:

```powershell
.\setup_env.ps1
.\.venv\Scripts\python.exe -m jupyterlab
```

หาก PowerShell ไม่อนุญาตให้รัน script ใช้คำสั่งนี้แทน โดยตั้งค่าสำหรับ process นี้เท่านั้น:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\setup_env.ps1
```

หรือสร้าง environment และติดตั้ง runtime ด้วยคำสั่งทีละบรรทัด:

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install "jupyterlab>=4,<5" "ipykernel>=7,<8"
.\.venv\Scripts\python.exe -m jupyterlab
```

ไม่ต้อง activate environment เพราะเรียก Python และ pip ของ `.venv` โดยตรง Packages ของแบบฝึกหัดยังติดตั้งด้วย `%pip install` ใน notebook

macOS / Linux:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install jupyterlab ipykernel
.venv/bin/python -m jupyterlab
```

เปิด notebook ใน JupyterLab หรือ VS Code เลือก Python kernel แล้วกด **Run All** cell ติดตั้ง packages จะทำงานก่อน imports หาก environment เดิมเคย import packages ต่างเวอร์ชัน ให้ restart kernel หลังติดตั้งแล้วรันใหม่

## บทที่ใช้ API: รันได้ทั้ง local และ Colab

บท API ใช้ OpenAI API key ของผู้เรียนและมีค่าบริการตามการใช้งาน แต่ละ notebook มีตัวแปรใน cell ตั้งค่า:

```python
OPENAI_API_KEY = "your_api_key"
client = OpenAI(api_key=OPENAI_API_KEY)
```

แทนที่ `your_api_key` ด้วย API key จริงก่อนกด **Run All** ใช้รูปแบบเดียวกันทั้ง local และ Colab โดยไม่ต้องตั้ง environment variable หรือ Colab Secrets ก่อนแชร์หรือ commit notebook ให้เปลี่ยน key กลับเป็น `your_api_key`

- **บท 07:** หากมี `sritrang_training_sop_th.pdf` ใน working directory จะอ่านไฟล์นั้น มิฉะนั้น local จะถาม path ของ PDF ส่วน Colab แสดงปุ่ม upload
- **บท 09:** หากมีภาพตัวอย่างชื่อ `01_*.png`, `02_*.png`, `03_*.png` จะใช้ภาพเหล่านั้น มิฉะนั้น local จะถาม paths คั่นด้วย `;` ส่วน Colab แสดงปุ่ม upload ใช้ภาพ PNG/JPEG 2–3 ภาพตามคำแนะนำในบท

## บท local: เตรียม Ollama

ติดตั้งและเปิด [Ollama](https://ollama.com/download) แล้วดาวน์โหลดโมเดลก่อนเริ่ม:

```text
ollama pull qwen3:4b
ollama pull bge-m3
```

`qwen3:4b` ใช้สร้างคำตอบและเลือกเครื่องมือ ส่วน `bge-m3` ใช้สร้าง embeddings ในบท 08 เปิด Ollama ไว้ระหว่างเรียน บท local ไม่ต้องมี cloud API key

ค่า `HOST = "http://localhost:11434"` หมายถึงเครื่องที่รัน notebook หากเรียก API ของ Ollama จาก Colab ต้องเปลี่ยน HOST เป็น endpoint ที่ runtime เข้าถึงได้ เพราะ localhost ของ Colab ไม่ใช่เครื่องผู้เรียน คู่มือนี้ไม่ติดตั้งหรือเปิด Ollama บน Colab

บท 08 มีเอกสารต้นทางใน cell และใช้ LlamaIndex ทำ retrieval จริง บท 12 มีโค้ด MCP server ใน cell โดยเริ่มและปิด subprocess อัตโนมัติ ไม่ต้องเตรียมไฟล์ server เพิ่ม

ต้องใช้อินเทอร์เน็ตเพื่อติดตั้ง packages ดาวน์โหลดโมเดล และเรียก cloud API ผู้สอนควรรันบท 08 ครั้งแรกขณะมีอินเทอร์เน็ตเพื่อเตรียม tokenizer cache ก่อนเรียน

## แหล่งอ้างอิง

รูปแบบคำอธิบายสั้น ๆ สลับ code cells อ้างอิง [CPF tutorial notebooks](https://github.com/biodatlab/cpf-genai-workshop/tree/main/tutorial_notebooks) ตัวอย่างเกี่ยวข้องกับธุรกิจตาม [เว็บไซต์ Sri Trang](https://www.sritranggroup.com/en/home)

สำหรับผู้ดูแล: `build_notebooks.py` สร้างเฉพาะ notebooks local 03, 08 และ 12 ส่วนบท API แก้ไขในไฟล์ notebook โดยตรง ผู้เรียนไม่ต้องรัน generator
