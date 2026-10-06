# แบบฝึกหัด Generative AI สำหรับผู้เข้าร่วม Sri Trang

## เริ่มใช้งานบน Windows

### 1. ติดตั้ง Git, Python 3.11 และ Ollama

- **Git:** [ดาวน์โหลดจากเว็บไซต์ทางการ](https://git-scm.com/install/windows) แล้วติดตั้งด้วยค่าเริ่มต้น
- **Python 3.11:** [ดาวน์โหลดจากเว็บไซต์ทางการ](https://www.python.org/downloads/release/python-3119/) เลือก **Windows installer (64-bit)** และติดตั้ง Python Launcher ด้วย
- **Ollama:** [ดาวน์โหลดจากเว็บไซต์ทางการ](https://ollama.com/download/windows) แล้วเปิด installer เพื่อติดตั้ง

เมื่อติดตั้งครบแล้ว เปิด PowerShell หน้าต่างใหม่

### 2. ดาวน์โหลด repo

```powershell
git clone https://github.com/biodatlab/sritrang-ai-workshop.git
cd sritrang-ai-workshop
```

### 3. รัน setup

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\setup.ps1
```

รอจน setup เสร็จและ JupyterLab เปิดใน browser เปิด PowerShell นี้ค้างไว้ระหว่างเรียน หากเครื่องไม่มี winget และ Python 3.11 ให้ติดตั้ง [Python 3.11](https://www.python.org/downloads/release/python-3119/) ก่อนรัน setup

### 4. เปิด notebook แล้วรัน

เปิด notebook ใน JupyterLab และเลือก Python kernel สำหรับบท API ให้แทนที่ `OPENAI_API_KEY = "your_api_key"` ด้วย key จริง จากนั้นเลือก **Run → Run All Cells**

บท PDF และภาพให้เลือกไฟล์เมื่อ notebook ถาม หากใช้ Colab ให้เปิดจากลิงก์ในตารางด้านล่าง ใส่ API key แล้วเลือก **Runtime → Run all** โดยไม่ต้องรัน setup บนเครื่อง

## Notebooks

| Notebook | เนื้อหา | Runtime | เปิดใน Colab |
| --- | --- | --- | --- |
| [01](01_llm_api.ipynb) | LLM API | Colab | [เปิดใน Colab](https://colab.research.google.com/drive/1m-mJM4a6mCDEQRFcG4H0T_DFMa_M0NpQ?usp=sharing) |
| [02](02_structured_output.ipynb) | Structured output | Colab | [เปิดใน Colab](https://colab.research.google.com/drive/1ef20YWY0vV-VMNOCweiEPRbOBTiSjiD3?usp=sharing) |
| [03](03_local_llm.ipynb) | Local LLM ผ่าน Ollama | Local เป็นหลัก | รัน local |
| [04](04_chunking.ipynb) | Chunking | Colab | [เปิดใน Colab](https://colab.research.google.com/drive/1kVJ2cVmKXgi2a3d9xA19NvVXte5ObjyX?usp=sharing) |
| [05](05_semantic_search.ipynb) | Semantic search | Colab | [เปิดใน Colab](https://colab.research.google.com/drive/1D7zy4-lcLgiwqzG0FP6djdctFH_6MCrX?usp=sharing) |
| [06](06_basic_rag.ipynb) | Basic RAG | Colab | [เปิดใน Colab](https://colab.research.google.com/drive/1yVNXvgDHKiJcBJ--9AHgpFIO5QGjC3s1?usp=drive_link) |
| [07](07_pdf_rag.ipynb) | PDF RAG | Colab | [เปิดใน Colab](https://colab.research.google.com/drive/18zSRK-AsaoEn961nRzetXxhHZyWdJmuF?usp=drive_link) |
| [08](08_local_rag.ipynb) | Local RAG ด้วย LlamaIndex และ Ollama | Local เป็นหลัก | รัน local |
| [09](09_multimodal_rag.ipynb) | Multimodal RAG | Colab | [เปิดใน Colab](https://colab.research.google.com/drive/1Ndbr7FwCftYtmh-0iW6TyQ8z34eIkotx?usp=sharing) |
| [10](10_tool_calling.ipynb) | Tool calling | Colab | [เปิดใน Colab](https://colab.research.google.com/drive/1yJodowG5kF_ay4JmDTSv0SsQAKYmlJwn?usp=drive_link) |
| [11](11_openai_mcp.ipynb) | OpenAI + MCP | Colab | [เปิดใน Colab](https://colab.research.google.com/drive/1trr6mt5WsObKcaa2I6p0uK3FSXKTZjLR?usp=drive_link) |
| [12](12_local_mcp.ipynb) | Local LLM + MCP | Local เป็นหลัก | รัน local |
| [13](13_agent_loop.ipynb) | Agent loop | Colab | [เปิดใน Colab](https://colab.research.google.com/drive/1kAVsZz4z_OOrxrcqCE6CKzYhQQ0penyM?usp=drive_link) |

## รายละเอียดเพิ่มเติม

ตัวอย่างโรงงานยาง น้ำยาง QC และการขนส่งเป็นข้อมูลสมมติสำหรับการเรียน ไม่ใช่ข้อมูลหรือ SOP จริงของบริษัท

ทุกบทมีโค้ดใน notebook และติดตั้ง packages ที่ต้องใช้ด้วย `%pip install` ก่อน imports ไม่ต้องติดตั้ง repo เป็น Python package บท 04 ใช้ Python standard library จึงไม่ต้องติดตั้ง packages เพิ่ม

### Setup ทำอะไรบ้าง

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
- **บท 09:** เลือกภาพ PNG/JPEG ของคุณเองหนึ่งภาพหรือหลายภาพผ่านปุ่ม upload ใน Colab หรือหน้าต่างเลือกไฟล์ใน local แล้วพิมพ์คำถามในขั้นตอนสุดท้าย ภาพ คำบรรยาย และ embeddings เก็บใน `image_index` ของ runtime

## บท local: Ollama

`setup.ps1` เปิด server และดาวน์โหลดโมเดลให้แล้ว บท 03, 08 และ 12 จึงพร้อมเรียก Ollama โดยไม่ต้องเข้า UI บท local ไม่ต้องมี cloud API key

ค่า `HOST = "http://127.0.0.1:11434"` หมายถึงเครื่องที่รัน notebook หากเรียก API ของ Ollama จาก Colab ต้องเปลี่ยน HOST เป็น endpoint ที่ runtime เข้าถึงได้ เพราะ localhost ของ Colab ไม่ใช่เครื่องผู้เรียน คู่มือนี้ไม่ติดตั้งหรือเปิด Ollama บน Colab

บท 08 มีเอกสารต้นทางใน cell และใช้ LlamaIndex ทำ retrieval จริง บท 12 มีโค้ด MCP server ใน cell โดยเริ่มและปิด subprocess อัตโนมัติ ไม่ต้องเตรียมไฟล์ server เพิ่ม

ต้องใช้อินเทอร์เน็ตเพื่อติดตั้ง packages ดาวน์โหลดโมเดล และเรียก cloud API ผู้สอนควรรันบท 08 ครั้งแรกขณะมีอินเทอร์เน็ตเพื่อเตรียม tokenizer cache ก่อนเรียน

## แหล่งอ้างอิง

ตัวอย่างเกี่ยวข้องกับธุรกิจตาม [เว็บไซต์ Sri Trang](https://www.sritranggroup.com/en/home)

สำหรับผู้ดูแล: `build_notebooks.py` สร้างเฉพาะ notebooks local 03, 08 และ 12 ส่วนบท API แก้ไขในไฟล์ notebook โดยตรง ผู้เรียนไม่ต้องรัน generator
