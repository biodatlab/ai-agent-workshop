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

## เตรียมเครื่องและเริ่มเรียน (Windows)

### 1. ดาวน์โหลดและติดตั้งโปรแกรมจากเว็บไซต์ทางการ

- **Git:** [ดาวน์โหลด Git สำหรับ Windows](https://git-scm.com/install/windows) เปิด installer แล้วติดตั้งด้วยค่าเริ่มต้น
- **Ollama:** [ดาวน์โหลด Ollama สำหรับ Windows](https://ollama.com/download/windows) เปิด `OllamaSetup.exe` แล้วติดตั้ง ไม่ต้องเข้า UI ของแอปหรือเลือกโมเดลเอง

Script ใช้ **Python 3.11** หากยังไม่มี จะติดตั้งด้วย Windows Package Manager (`winget`) ให้ หากเครื่องไม่มี winget ให้ติดตั้ง [Python 3.11](https://www.python.org/downloads/release/python-3119/) จากเว็บไซต์ทางการก่อน โดยเลือก Python Launcher ระหว่างติดตั้ง

ติดตั้งโปรแกรมเสร็จแล้วเปิด PowerShell หน้าต่างใหม่ ต้องมีอินเทอร์เน็ตและพื้นที่ว่างสำหรับ packages กับโมเดล

### 2. Clone repo

เปิด PowerShell ในโฟลเดอร์ที่ต้องการเก็บงาน แล้วรันทีละบรรทัด:

```powershell
git clone https://github.com/biodatlab/sritrang-ai-workshop.git
cd sritrang-ai-workshop
```

### 3. รัน setup เพียงคำสั่งเดียว

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\setup.ps1
```

Script จะทำตามลำดับ:

1. เตรียม Python 3.11 โดยใช้เวอร์ชันที่ติดตั้งอยู่ หรือให้ winget ติดตั้งเมื่อไม่มี
2. สร้าง `.venv` และใช้ pip ของ `.venv` ติดตั้ง JupyterLab กับ ipykernel
3. เปิด Ollama server ใน background หากยังไม่ทำงาน ไม่ต้องเปิดแอปเอง
4. ดาวน์โหลด `qwen3:4b` สำหรับสร้างคำตอบและใช้เครื่องมือ และ `bge-m3` สำหรับ embeddings
5. เปิด JupyterLab ใน browser จากโฟลเดอร์ repo

รอจนติดตั้งและดาวน์โหลดเสร็จ การดาวน์โหลดครั้งแรกอาจใช้เวลาหลายนาที จากนั้นเปิด notebook เลือก Python kernel และกด **Run → Run All Cells** Packages ของแต่ละบทจะติดตั้งจาก `%pip install` ใน cell แรก ไม่ต้อง activate environment หรือตั้งค่าโมเดลเพิ่ม

เปิด PowerShell ที่รัน JupyterLab ค้างไว้ระหว่างเรียน ส่วน Ollama server ทำงานใน background หาก browser ไม่เปิดอัตโนมัติ ให้เปิดลิงก์ที่ JupyterLab แสดงใน terminal

### เปิดเรียนครั้งถัดไป

ใช้คำสั่ง setup เดิมได้อีกครั้ง Script ใช้ environment และโมเดลที่มีอยู่ต่อ และตรวจให้ Ollama พร้อมก่อนเปิด JupyterLab

หากต้องการเตรียมเครื่องอย่างเดียวโดยยังไม่เปิด JupyterLab:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\setup.ps1 -NoLaunch
```

ใช้ `setup.ps1` ไฟล์เดียวสำหรับเตรียม environment และ Ollama

## บทที่ใช้ API: รันได้ทั้ง local และ Colab

บท API ใช้ OpenAI API key ของผู้เรียนและมีค่าบริการตามการใช้งาน แต่ละ notebook มีตัวแปรใน cell ตั้งค่า:

```python
OPENAI_API_KEY = "your_api_key"
client = OpenAI(api_key=OPENAI_API_KEY)
```

แทนที่ `your_api_key` ด้วย API key จริงก่อนกด **Run All** ใช้รูปแบบเดียวกันทั้ง local และ Colab โดยไม่ต้องตั้ง environment variable หรือ Colab Secrets ก่อนแชร์หรือ commit notebook ให้เปลี่ยน key กลับเป็น `your_api_key`

- **บท 07:** หากมี `sritrang_training_sop_th.pdf` ใน working directory จะอ่านไฟล์นั้น มิฉะนั้น local จะถาม path ของ PDF ส่วน Colab แสดงปุ่ม upload
- **บท 09:** หากมีภาพตัวอย่างชื่อ `01_*.png`, `02_*.png`, `03_*.png` จะใช้ภาพเหล่านั้น มิฉะนั้น local จะถาม paths คั่นด้วย `;` ส่วน Colab แสดงปุ่ม upload ใช้ภาพ PNG/JPEG 2–3 ภาพตามคำแนะนำในบท

## บท local: Ollama

`setup.ps1` เปิด server และดาวน์โหลดโมเดลให้แล้ว บท 03, 08 และ 12 จึงพร้อมเรียก Ollama โดยไม่ต้องเข้า UI บท local ไม่ต้องมี cloud API key

ค่า `HOST = "http://127.0.0.1:11434"` หมายถึงเครื่องที่รัน notebook หากเรียก API ของ Ollama จาก Colab ต้องเปลี่ยน HOST เป็น endpoint ที่ runtime เข้าถึงได้ เพราะ localhost ของ Colab ไม่ใช่เครื่องผู้เรียน คู่มือนี้ไม่ติดตั้งหรือเปิด Ollama บน Colab

บท 08 มีเอกสารต้นทางใน cell และใช้ LlamaIndex ทำ retrieval จริง บท 12 มีโค้ด MCP server ใน cell โดยเริ่มและปิด subprocess อัตโนมัติ ไม่ต้องเตรียมไฟล์ server เพิ่ม

ต้องใช้อินเทอร์เน็ตเพื่อติดตั้ง packages ดาวน์โหลดโมเดล และเรียก cloud API ผู้สอนควรรันบท 08 ครั้งแรกขณะมีอินเทอร์เน็ตเพื่อเตรียม tokenizer cache ก่อนเรียน

## แหล่งอ้างอิง

รูปแบบคำอธิบายสั้น ๆ สลับ code cells อ้างอิง [CPF tutorial notebooks](https://github.com/biodatlab/cpf-genai-workshop/tree/main/tutorial_notebooks) ตัวอย่างเกี่ยวข้องกับธุรกิจตาม [เว็บไซต์ Sri Trang](https://www.sritranggroup.com/en/home)

สำหรับผู้ดูแล: `build_notebooks.py` สร้างเฉพาะ notebooks local 03, 08 และ 12 ส่วนบท API แก้ไขในไฟล์ notebook โดยตรง ผู้เรียนไม่ต้องรัน generator
