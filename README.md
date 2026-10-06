# แบบฝึกหัด Local LLM สำหรับผู้เข้าร่วม Sri Trang

แบบฝึกหัดสั้น ๆ สำหรับทดลองใช้โมเดลบนเครื่องผู้เรียน ทุก notebook มีโค้ดและข้อมูลครบใน cells เรียงขั้นตอน 1–5 เลือก runtime ที่เตรียมไว้แล้วกด **Run All** ได้เลย ไม่ต้องเปิดหรือแก้ไฟล์ประกอบ

ตัวอย่างการรับน้ำยางและงาน QC เป็นข้อมูลสมมติสำหรับการเรียน ไม่ใช่ข้อมูลหรือ SOP จริงของบริษัท

| Notebook | แบบฝึกหัด | เวลาโดยประมาณ |
| --- | --- | --- |
| [03_local_llm.ipynb](03_local_llm.ipynb) | ให้ local LLM สรุปรายงานกะ แล้วเปลี่ยนรูปแบบคำตอบ | 15–20 นาที |
| [08_local_rag.ipynb](08_local_rag.ipynb) | ใช้ LlamaIndex ค้นจากเอกสารใน cell แล้วให้ Ollama ตอบจากหลักฐาน | 25–30 นาที |
| [12_local_mcp.ipynb](12_local_mcp.ipynb) | บทเสริม: ให้ local LLM เรียกเครื่องมือผ่าน MCP server ที่อยู่ใน cell | 25–30 นาที |

Repo นี้มีเฉพาะแบบฝึกหัด local หมายเลข 03, 08 และ 12 ส่วนแบบฝึกหัดอื่นอยู่ในชุด Colab และเนื้อหา desktop app เดิม

## เตรียม runtime environment ครั้งเดียวก่อนเรียน

ติดตั้ง Python 3.11 หรือ 3.12 และ [Ollama](https://ollama.com/download) จากนั้นเปิด terminal ในโฟลเดอร์ repo แล้วรันคำสั่งทีละบรรทัด

Windows PowerShell (ตัวอย่างใช้ Python 3.11):

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\python.exe -m pip install .
.\.venv\Scripts\python.exe -m jupyterlab
```

macOS / Linux ใช้ `python3` เวอร์ชัน 3.11 หรือ 3.12:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install .
.venv/bin/python -m jupyterlab
```

เปิด Ollama แล้วดาวน์โหลดโมเดลใน terminal อีกหน้าต่าง:

```text
ollama pull qwen3:4b
ollama pull bge-m3
```

ใช้ `qwen3:4b` สร้างคำตอบและเรียกเครื่องมือ ส่วน `bge-m3` ใช้สร้าง embeddings ในบท RAG ต้องใช้อินเทอร์เน็ตตอนติดตั้ง packages และดาวน์โหลดโมเดล แต่การใช้โมเดลหลังเตรียมครบแล้วทำงาน local ไม่ต้องมี cloud API key

ผู้สอนควรเตรียม runtime และ tokenizer cache ของ LlamaIndex ก่อนอบรม โดยรันบท 08 ครั้งแรกขณะมีอินเทอร์เน็ต ความเร็วและหน่วยความจำที่ใช้ขึ้นอยู่กับเครื่อง

## เริ่มเรียน

เปิด notebook ใน JupyterLab หรือ VS Code เลือก Python kernel ของ environment ที่ติดตั้ง packages แล้วเปิด Ollama จากนั้นกด **Run All** แต่ละ notebook รันแยกกันได้ ไม่มีช่องที่ต้องกรอกเพื่อให้ตัวอย่างเริ่มทำงาน

- **03:** ส่งรายงานสมมติให้โมเดลสรุป 3 ข้อ แล้วใช้ข้อมูลเดิมสรุปเป็นหนึ่งประโยค หากมีคำตอบ cloud จากบทก่อน สามารถนำมาเปรียบเทียบภายหลังได้
- **08:** เอกสารต้นทางอยู่ใน cell จากนั้น LlamaIndex แบ่งข้อความ สร้าง embeddings และค้นใน vector index ที่อยู่ในหน่วยความจำ แสดงหลักฐานและคำตอบโดยไม่ต้องเตรียมไฟล์เอกสาร
- **12:** โค้ดเครื่องมือและ MCP server อยู่ใน cell เริ่ม server เป็น subprocess ผ่าน Python ของ kernel และปิดอัตโนมัติ ไม่ต้องเปิด server ใน terminal หรือสร้างไฟล์เอง

หลังรันครบแล้ว ลองเปลี่ยนรายงานหรือคำถามใน cell ตามคำแนะนำท้าย notebook และรันซ้ำได้ เนื้อหาหลักแสดงเฉพาะผลการเรียน เช่น หลักฐานและคำตอบ ไม่มี cells สำหรับ checks หรือ debug logging

## แหล่งอ้างอิง

ใช้ [CPF tutorial notebooks](https://github.com/biodatlab/cpf-genai-workshop/tree/main/tutorial_notebooks) เป็นแนวทางจัดคำอธิบายสั้น ๆ สลับกับ code cells บท RAG ใช้ LlamaIndex ทำ retrieval จริง โดยปรับให้ใช้ local embeddings และ Ollama

ตัวอย่างเกี่ยวข้องกับธุรกิจยางและน้ำยางตาม [เว็บไซต์ Sri Trang](https://www.sritranggroup.com/en/home) รายละเอียดการทำงานและตัวเลขในแบบฝึกหัดเป็นข้อมูลที่แต่งขึ้น

[Ollama chat API](https://docs.ollama.com/api/chat) · [LlamaIndex](https://developers.llamaindex.ai/python/framework/) · [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

สำหรับผู้ดูแล repo: `build_notebooks.py` ใช้สร้าง notebooks ใหม่ ผู้เรียนไม่ต้องรันไฟล์นี้ และ notebooks ที่แจกไม่มี outputs ที่บันทึกไว้
