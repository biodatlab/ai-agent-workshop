# แบบฝึกหัด Generative AI สำหรับผู้เข้าร่วม Sri Trang

## ขั้นตอนเริ่มใช้งาน

### บท Colab

1. เปิดลิงก์บทเรียนจากตารางด้านล่าง
2. เลือก **Copy to Drive** เพื่อเก็บสำเนาของคุณเอง
3. แทนที่ `your_api_key` ด้วย API key จริงในบทที่ใช้ API
4. เลือก **Runtime → Run all** บท 07 และ 09 จะดาวน์โหลด PDF และภาพตัวอย่างจาก GitHub อัตโนมัติ ไม่ต้องอัปโหลดไฟล์ (ต้องเชื่อมต่ออินเทอร์เน็ต)

### บท local 03, 08 และ 12: Windows, macOS และ Linux

#### 1. ติดตั้งโปรแกรม

- **Git:** [![Download Git](https://img.shields.io/badge/Download_Git-F05032?style=flat-square&logo=git&logoColor=white)](https://git-scm.com/downloads) เลือกระบบปฏิบัติการของคุณ
- **Python 3.11:** [![Download Python 3.11](https://img.shields.io/badge/Python_3.11-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/release/python-3119/) — Windows เลือก Windows installer (64-bit) และติดตั้ง Python Launcher; macOS เลือก macOS installer
- **Linux Python 3.11:** ติดตั้ง `python3.11` และแพ็กเกจ venv ผ่าน package manager ของ distribution เช่น Ubuntu ที่มีแพ็กเกจนี้ใช้ `sudo apt install python3.11 python3.11-venv` หากไม่มี ให้ใช้ [![Python Linux installation guide](https://img.shields.io/badge/Python_Linux_Guide-3776AB?style=flat-square&logo=python&logoColor=white)](https://docs.python.org/3/using/unix.html)
- **Ollama:** [![Download Ollama](https://img.shields.io/badge/Download_Ollama-000000?style=flat-square&logo=ollama&logoColor=white)](https://ollama.com/download) เลือก Windows, macOS หรือ Linux และติดตั้งตามคำแนะนำของระบบนั้น

ติดตั้งเสร็จแล้วเปิด Terminal ใหม่ (Windows ใช้ PowerShell)

#### 2. ดาวน์โหลด repo

```sh
git clone https://github.com/biodatlab/sritrang-ai-workshop.git
cd sritrang-ai-workshop
```

#### 3. รัน setup

**Windows — PowerShell:**

```powershell
py -3.11 setup.py
```

**macOS / Linux — Terminal:**

```sh
python3.11 setup.py
```

รอจนติดตั้งเสร็จและ JupyterLab เปิดใน browser เปิด Terminal นี้ค้างไว้ระหว่างเรียน

#### 4. เปิด notebook แล้วรัน

เปิดบท **03, 08 หรือ 12** เลือก kernel **Python 3.11 (workshop)** แล้วเลือก **Run → Run All Cells**

## Notebooks

| Notebook | เนื้อหา | Runtime | เปิดใน Colab |
| --- | --- | --- | --- |
| [![Open notebook 01](https://img.shields.io/badge/Notebook_01-F37626?style=flat-square&logo=jupyter&logoColor=white)](01_llm_api.ipynb) | LLM API | Colab | [![Open in Colab](https://img.shields.io/badge/Open_in_Colab-F9AB00?style=flat-square&logo=googlecolab&logoColor=white)](https://colab.research.google.com/drive/1m-mJM4a6mCDEQRFcG4H0T_DFMa_M0NpQ?usp=sharing) |
| [![Open notebook 02](https://img.shields.io/badge/Notebook_02-F37626?style=flat-square&logo=jupyter&logoColor=white)](02_structured_output.ipynb) | Structured output | Colab | [![Open in Colab](https://img.shields.io/badge/Open_in_Colab-F9AB00?style=flat-square&logo=googlecolab&logoColor=white)](https://colab.research.google.com/drive/1ef20YWY0vV-VMNOCweiEPRbOBTiSjiD3?usp=sharing) |
| [![Open notebook 03](https://img.shields.io/badge/Notebook_03-F37626?style=flat-square&logo=jupyter&logoColor=white)](03_local_llm.ipynb) | Local LLM ผ่าน Ollama | Local | รัน local |
| [![Open notebook 04](https://img.shields.io/badge/Notebook_04-F37626?style=flat-square&logo=jupyter&logoColor=white)](04_chunking.ipynb) | Chunking | Colab | [![Open in Colab](https://img.shields.io/badge/Open_in_Colab-F9AB00?style=flat-square&logo=googlecolab&logoColor=white)](https://colab.research.google.com/drive/1kVJ2cVmKXgi2a3d9xA19NvVXte5ObjyX?usp=sharing) |
| [![Open notebook 05](https://img.shields.io/badge/Notebook_05-F37626?style=flat-square&logo=jupyter&logoColor=white)](05_semantic_search.ipynb) | Semantic search | Colab | [![Open in Colab](https://img.shields.io/badge/Open_in_Colab-F9AB00?style=flat-square&logo=googlecolab&logoColor=white)](https://colab.research.google.com/drive/1D7zy4-lcLgiwqzG0FP6djdctFH_6MCrX?usp=sharing) |
| [![Open notebook 06](https://img.shields.io/badge/Notebook_06-F37626?style=flat-square&logo=jupyter&logoColor=white)](06_basic_rag.ipynb) | Basic RAG | Colab | [![Open in Colab](https://img.shields.io/badge/Open_in_Colab-F9AB00?style=flat-square&logo=googlecolab&logoColor=white)](https://colab.research.google.com/drive/1yVNXvgDHKiJcBJ--9AHgpFIO5QGjC3s1?usp=drive_link) |
| [![Open notebook 07](https://img.shields.io/badge/Notebook_07-F37626?style=flat-square&logo=jupyter&logoColor=white)](07_pdf_rag.ipynb) | PDF RAG | Colab | [![Open in Colab](https://img.shields.io/badge/Open_in_Colab-F9AB00?style=flat-square&logo=googlecolab&logoColor=white)](https://colab.research.google.com/drive/18zSRK-AsaoEn961nRzetXxhHZyWdJmuF?usp=drive_link) |
| [![Open notebook 08](https://img.shields.io/badge/Notebook_08-F37626?style=flat-square&logo=jupyter&logoColor=white)](08_local_rag.ipynb) | Local RAG ด้วย LlamaIndex และ Ollama | Local | รัน local |
| [![Open notebook 09](https://img.shields.io/badge/Notebook_09-F37626?style=flat-square&logo=jupyter&logoColor=white)](09_multimodal_rag.ipynb) | Multimodal RAG | Colab | [![Open in Colab](https://img.shields.io/badge/Open_in_Colab-F9AB00?style=flat-square&logo=googlecolab&logoColor=white)](https://colab.research.google.com/drive/1Ndbr7FwCftYtmh-0iW6TyQ8z34eIkotx?usp=sharing) |
| [![Open notebook 10](https://img.shields.io/badge/Notebook_10-F37626?style=flat-square&logo=jupyter&logoColor=white)](10_tool_calling.ipynb) | Tool calling | Colab | [![Open in Colab](https://img.shields.io/badge/Open_in_Colab-F9AB00?style=flat-square&logo=googlecolab&logoColor=white)](https://colab.research.google.com/drive/1yJodowG5kF_ay4JmDTSv0SsQAKYmlJwn?usp=drive_link) |
| [![Open notebook 11](https://img.shields.io/badge/Notebook_11-F37626?style=flat-square&logo=jupyter&logoColor=white)](11_openai_mcp.ipynb) | OpenAI + MCP | Colab | [![Open in Colab](https://img.shields.io/badge/Open_in_Colab-F9AB00?style=flat-square&logo=googlecolab&logoColor=white)](https://colab.research.google.com/drive/1trr6mt5WsObKcaa2I6p0uK3FSXKTZjLR?usp=drive_link) |
| [![Open notebook 12](https://img.shields.io/badge/Notebook_12-F37626?style=flat-square&logo=jupyter&logoColor=white)](12_local_mcp.ipynb) | Local LLM + MCP | Local | รัน local |
| [![Open notebook 13](https://img.shields.io/badge/Notebook_13-F37626?style=flat-square&logo=jupyter&logoColor=white)](13_agent_loop.ipynb) | Agent loop | Colab | [![Open in Colab](https://img.shields.io/badge/Open_in_Colab-F9AB00?style=flat-square&logo=googlecolab&logoColor=white)](https://colab.research.google.com/drive/1kAVsZz4z_OOrxrcqCE6CKzYhQQ0penyM?usp=drive_link) |

## รายละเอียดเพิ่มเติม

ตัวอย่างโรงงานยาง น้ำยาง QC และการขนส่งเป็นข้อมูลสมมติสำหรับการเรียน ไม่ใช่ข้อมูลหรือ กฏ จริงของบริษัท

ทุกบทมีโค้ดใน notebook และติดตั้ง packages ที่ต้องใช้ด้วย `%pip install` ก่อน imports ไม่ต้องติดตั้ง repo เป็น Python package บท 04 ใช้ Python standard library จึงไม่ต้องติดตั้ง packages เพิ่ม

### Setup ทำอะไรบ้าง

Script จะทำตามลำดับ:

1. ตรวจว่าใช้ Python 3.11 และติดตั้ง Ollama แล้ว
2. สร้าง `.venv` และใช้ pip ของ `.venv` ติดตั้ง JupyterLab กับ ipykernel พร้อมตั้ง kernel **Python 3.11 (workshop)** ให้ใช้ environment นี้
3. เปิด Ollama server ใน background หากยังไม่ทำงาน ไม่ต้องเปิดแอปเอง
4. ดาวน์โหลด `qwen3:4b` สำหรับสร้างคำตอบและใช้เครื่องมือ และ `bge-m3` สำหรับ embeddings
5. ตรวจ environment และ Ollama แล้วเปิด JupyterLab ใน browser จากโฟลเดอร์ repo

รอจนติดตั้งและดาวน์โหลดเสร็จ การดาวน์โหลดครั้งแรกอาจใช้เวลาหลายนาที จากนั้นเปิด notebook เลือก kernel **Python 3.11 (workshop)** และกด **Run → Run All Cells** Packages ของแต่ละบทจะติดตั้งจาก `%pip install` ใน cell แรก ไม่ต้อง activate environment หรือตั้งค่าโมเดลเพิ่ม

เปิด Terminal ที่รัน JupyterLab ค้างไว้ระหว่างเรียน ส่วน Ollama server ทำงานใน background หาก browser ไม่เปิดอัตโนมัติ ให้เปิดลิงก์ที่ JupyterLab แสดงใน terminal

### เปิดเรียนครั้งถัดไป

ใช้คำสั่ง setup เดิมได้อีกครั้ง Script ใช้ environment และโมเดลที่มีอยู่ต่อ และตรวจให้ Ollama พร้อมก่อนเปิด JupyterLab

หากต้องการเตรียมเครื่องอย่างเดียวโดยยังไม่เปิด JupyterLab:

```powershell
# Windows
py -3.11 setup.py --no-launch
```

```sh
# macOS / Linux
python3.11 setup.py --no-launch
```

`setup.py` ใช้ขั้นตอนเดียวกันทั้งสามระบบ โดยเลือก path ของ `.venv` และวิธีเปิด background process ให้เหมาะกับระบบ ใช้ไฟล์นี้เพียงไฟล์เดียวสำหรับเตรียม environment และ Ollama

หากย้าย repo ข้ามระบบ ให้สร้าง `.venv` ใหม่บนเครื่องนั้น หาก Ollama เริ่มไม่ได้ ดูรายละเอียดใน `ollama-setup.log`

## บทที่ใช้ API: Google Colab

บท API ใช้ OpenAI API key ของผู้เรียนและมีค่าบริการตามการใช้งาน แต่ละ notebook มีตัวแปรใน cell ตั้งค่า:

```python
OPENAI_API_KEY = "your_api_key"
client = OpenAI(api_key=OPENAI_API_KEY)
```

แทนที่ `your_api_key` ด้วย API key จริงก่อนกด **Run All** รันใน Colab โดยไม่ต้องตั้ง environment variable หรือ Colab Secrets ก่อนแชร์หรือ commit notebook ให้เปลี่ยน key กลับเป็น `your_api_key`

- **บท 07:** อัปโหลด PDF ผ่านปุ่ม upload ใน Colab
- **บท 09:** อัปโหลดภาพ PNG/JPEG ของคุณ แล้วพิมพ์คำถามในขั้นตอนสุดท้าย ภาพ คำบรรยาย และ embeddings เก็บใน `image_index` ของ runtime ชั่วคราว

## บท local: Ollama

`setup.py` เปิด server และดาวน์โหลดโมเดลให้แล้ว บท 03, 08 และ 12 จึงพร้อมเรียก Ollama โดยไม่ต้องเข้า UI บท local ไม่ต้องมี cloud API key

ค่า `HOST = "http://127.0.0.1:11434"` เรียก Ollama บนเครื่องที่รัน notebook

บท 08 มีเอกสารต้นทางใน cell และใช้ LlamaIndex ทำ retrieval จริง บท 12 มีโค้ด MCP server ใน cell โดยเริ่มและปิด subprocess อัตโนมัติ ไม่ต้องเตรียมไฟล์ server เพิ่ม

ต้องใช้อินเทอร์เน็ตเพื่อติดตั้ง packages ดาวน์โหลดโมเดล และเรียก cloud API ผู้สอนควรรันบท 08 ครั้งแรกขณะมีอินเทอร์เน็ตเพื่อเตรียม tokenizer cache ก่อนเรียน

## แหล่งอ้างอิง

ตัวอย่างเกี่ยวข้องกับธุรกิจตาม [![Sri Trang official website](https://img.shields.io/badge/Sri_Trang-007A53?style=flat-square)](https://www.sritranggroup.com/en/home)

สำหรับผู้ดูแล: `build_notebooks.py` สร้างเฉพาะ notebooks local 03, 08 และ 12 ส่วนบท API แก้ไขในไฟล์ notebook โดยตรง ผู้เรียนไม่ต้องรัน generator
