"""Maintainer utility; all tutorial code and data live in notebook cells."""
import json
from pathlib import Path
from textwrap import dedent


def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": dedent(text).strip() + "\n"}


def code(text):
    return {"cell_type": "code", "metadata": {}, "source": dedent(text).strip() + "\n", "execution_count": None, "outputs": []}


def intro(number, title):
    return md(f"""# {number}: {title}
    แบบฝึกหัดสำหรับผู้เข้าร่วม Sri Trang

    เลือก Python kernel ที่ติดตั้ง packages แล้ว เปิด Ollama ที่มีโมเดลตาม README แล้วกด **Run All** ได้เลย
    โค้ดและข้อมูลทั้งหมดอยู่ใน cells ไม่ต้องเตรียมหรือแก้ไฟล์ประกอบ
    ตัวอย่างทั้งหมดเป็นข้อมูลสมมติสำหรับการเรียน ไม่ใช่ข้อมูลหรือ SOP จริงของบริษัท
    """)


def write(name, cells):
    for i, cell in enumerate(cells):
        cell["id"] = f"cell-{i:02d}"
    Path(name).write_text(json.dumps({"nbformat": 4, "nbformat_minor": 5,
        "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                     "language_info": {"name": "python", "version": "3.11"}},
        "cells": cells}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


chat_setup = code('''
import json
from urllib.request import Request, urlopen

HOST = "http://localhost:11434"
MODEL = "qwen3:4b"

def chat(messages, **kwargs):
    payload = {"model": MODEL, "messages": messages, "stream": False,
               "think": False, "options": {"temperature": 0}, **kwargs}
    request = Request(HOST + "/api/chat", data=json.dumps(payload).encode("utf-8"),
                      headers={"Content-Type": "application/json"})
    with urlopen(request, timeout=180) as response:
        return json.load(response)["message"]
''')

write("03_local_llm.ipynb", [
    intro("03", "Local LLM"),
    md("## 1. เชื่อมต่อ local model\nกำหนดโมเดลและฟังก์ชันส่งข้อความไปยัง Ollama บนเครื่องนี้"), chat_setup,
    md("## 2. เตรียมรายงานกะ\nSystem prompt กำหนดหน้าที่ ส่วน user prompt ให้ข้อมูลที่ต้องสรุป"),
    code('''
system_prompt = "คุณเป็นผู้ช่วยสรุปรายงานโรงงานยาง สรุปภาษาไทย 3 ข้อ ใช้เฉพาะข้อมูลที่ได้รับ"
user_prompt = """รายงานกะเช้า (สมมติ): รับน้ำยาง 12 ตัน รถขนส่งล่าช้า 30 นาที
ทีม QC กำลังตรวจตัวอย่างล็อต L-101 ยังไม่มีผลตรวจ จึงยังไม่ปล่อยล็อตนี้"""
'''),
    md("## 3. ส่ง prompt และอ่านคำตอบ\nโมเดล local สร้างสรุปจากรายงานที่ให้"),
    code('''
messages = [{"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}]
answer = chat(messages)
print(answer["content"])
'''),
    md("## 4. เปลี่ยนรูปแบบคำตอบ\nใช้รายงานเดิม แต่ให้สรุปเพียงหนึ่งประโยค"),
    code('''
short_answer = chat([
    {"role": "system", "content": "สรุปรายงานภาษาไทยหนึ่งประโยค ใช้เฉพาะข้อมูลที่ได้รับ"},
    {"role": "user", "content": user_prompt},
])
print(short_answer["content"])
'''),
    md("## 5. สรุปสิ่งที่ได้เรียน\nPrompt เดียวกันสามารถส่งไปยัง cloud หรือ local model ได้ ส่วน system prompt ช่วยกำหนดรูปแบบคำตอบ หากมีคำตอบ cloud จากบทก่อน สามารถนำมาเปรียบเทียบภายหลังได้ ไม่จำเป็นต่อการรัน notebook นี้\n\nลองเปลี่ยนรายงานในขั้นตอน 2 แล้วกด Run All อีกครั้ง"),
])

write("08_local_rag.ipynb", [
    intro("08", "Local RAG ด้วย LlamaIndex"),
    md("## 1. กำหนดโมเดล local\nใช้ bge-m3 สร้าง embeddings และ qwen3:4b สร้างคำตอบ"),
    code('''
from llama_index.core import Document, VectorStoreIndex, PromptTemplate
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama

HOST = "http://localhost:11434"
embed_model = OllamaEmbedding(model_name="bge-m3", base_url=HOST)
llm = Ollama(model="qwen3:4b", base_url=HOST, request_timeout=180,
             context_window=4096, temperature=0, thinking=False)
'''),
    md("## 2. เตรียมเอกสารโรงงานสมมติ\nข้อความนี้เป็นเอกสารต้นทางสำหรับค้นข้อมูล ไม่ใช่ผล retrieval ที่เลือกไว้ล่วงหน้า"),
    code('''
factory_notes = """เอกสารโรงงานยางสมมติสำหรับการเรียน

การรับน้ำยางเข้าคลัง
เมื่อรับน้ำยาง ให้บันทึกรหัสล็อต ชื่อผู้ส่งมอบ น้ำหนักรับเข้า และเวลารับเข้า
เพื่อให้ทีมคลังและทีม QC ตรวจสอบย้อนกลับถึงผู้ส่งมอบได้ หากเอกสารผู้ส่งมอบไม่ครบ
ให้บันทึกว่าข้อมูลขาดและส่งให้ผู้รับผิดชอบติดตาม อย่าเติมข้อมูลที่ยังไม่ได้รับ

การบันทึกข้อมูล QC
บันทึกรหัสตัวอย่าง QC ที่เชื่อมกับรหัสล็อต บันทึกเฉพาะผลที่ทีม QC ยืนยันแล้ว
หากยังไม่มีผลตรวจ ให้ระบุว่ารอผลและไม่กรอกค่าผลตรวจเอง
เอกสารนี้ไม่มีค่า DRC หรือผลตรวจจริงของล็อตใด

รายงานส่งมอบกะ
รายงานระบุปริมาณรับเข้ารวม รหัสล็อตที่รอผล QC และเอกสารผู้ส่งมอบที่ยังไม่ครบ
ระบุเวลาที่อัปเดตรายงาน และแยกข้อมูลที่ยืนยันแล้วออกจากงานที่รอติดตาม

ข้อมูลขนส่ง
บันทึกรหัสเที่ยวรถ วันเวลานัดรับ และรหัสล็อตที่เกี่ยวข้อง
หากรถล่าช้าให้บันทึกเวลาล่าช้าและแจ้งผู้ประสานงาน
เอกสารนี้ไม่มีตารางเดินรถจริงหรือราคาค่าขนส่ง"""

documents = [Document(text=factory_notes, metadata={"source": "เอกสารโรงงานสมมติ"})]
'''),
    md("## 3. สร้าง vector index\nLlamaIndex แบ่งเอกสารเป็น chunks แล้วสร้าง embeddings ด้วย Ollama เก็บ index ในหน่วยความจำ"),
    code('''
splitter = SentenceSplitter(chunk_size=180, chunk_overlap=30)
nodes = splitter.get_nodes_from_documents(documents)
for i, node in enumerate(nodes, start=1):
    node.metadata["chunk_id"] = f"FACTORY-{i:02d}"
index = VectorStoreIndex(nodes, embed_model=embed_model, show_progress=False)
retriever = index.as_retriever(similarity_top_k=2)
'''),
    md("## 4. ค้นหลักฐานที่เกี่ยวข้อง\nคำถามจะถูกแปลงเป็น embedding เพื่อค้น chunks ที่ใกล้เคียง อ่านหลักฐานที่ค้นได้ด้านล่าง"),
    code('''
question = "ต้องบันทึกข้อมูลอะไรเมื่อรับน้ำยางเข้าคลัง?"
retrieved = retriever.retrieve(question)
context = "\\n\\n".join(
    f"[{hit.node.metadata['chunk_id']}] {hit.node.text}" for hit in retrieved
)
print(context)
'''),
    md("## 5. สร้างคำตอบจากหลักฐาน\nให้โมเดลตอบเฉพาะข้อมูลใน context พร้อมอ้างอิง chunk ID"),
    code('''
qa_prompt = PromptTemplate("""ตอบภาษาไทยจากหลักฐานของโรงงานสมมติเท่านั้น
อ้างอิง chunk ID เช่น [FACTORY-01] หากข้อมูลไม่พอให้ตอบว่าไม่พบข้อมูลในเอกสาร
ห้ามเดาตัวเลขหรือผลตรวจ

หลักฐาน:
{context_str}

คำถาม: {query_str}
คำตอบ:""")
answer = llm.complete(qa_prompt.format(context_str=context, query_str=question))
print(answer.text)
'''),
    md("## เสร็จแล้ว\nลองเปลี่ยนคำถามในขั้นตอน 4 แล้วรันขั้นตอน 4–5 อีกครั้ง เช่น ‘รายงานส่งมอบกะต้องมีข้อมูลอะไร?’ หรือ ‘ล็อต L-101 มีค่า DRC เท่าไร?’\n\nเปลี่ยนเฉพาะโมเดลสร้างคำตอบสามารถใช้ index เดิมได้ หากเปลี่ยนเอกสารหรือ embedding model ให้สร้าง index ใหม่"),
])

write("12_local_mcp.ipynb", [
    intro("12", "Local LLM + MCP (บทเสริม)"),
    md("## 1. เชื่อมต่อ local model\nใช้โมเดลที่รองรับ tool calling เพื่อเลือกเครื่องมือจาก MCP"), chat_setup,
    md("## 2. เตรียม MCP server ใน cell\nเครื่องมืออ่านสถานะรับน้ำยางของโรงงานสมมติ A/B โค้ด server อยู่ที่นี่และรันเป็น subprocess โดยไม่สร้างไฟล์"),
    code('''
import sys
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

server_code = """
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Factory workshop", log_level="CRITICAL")

@mcp.tool()
def get_factory_status(factory_id: str) -> dict:
    \\\"\\\"\\\"Get fictional latex receiving and QC status for factory A or B.\\\"\\\"\\\"
    factories = {
        "A": {"received_tonnes": 12, "qc_status": "pending", "lot_id": "L-101"},
        "B": {"received_tonnes": 8, "qc_status": "completed", "lot_id": "L-102"},
    }
    return {"factory_id": factory_id, "data_type": "fictional",
            **factories.get(factory_id, {"status": "unknown"})}

mcp.run(transport="stdio")
"""
server_parameters = StdioServerParameters(command=sys.executable, args=["-c", server_code])
'''),
    md("## 3. อ่านเครื่องมือจาก MCP\nแปลงชื่อ คำอธิบาย และ input schema เป็นรูปแบบที่ Ollama รับได้"),
    code('''
async def get_tools():
    async with stdio_client(server_parameters) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            discovered = await session.list_tools()
            return [{"type": "function", "function": {
                "name": tool.name, "description": tool.description,
                "parameters": tool.inputSchema,
            }} for tool in discovered.tools]

tools = await get_tools()
'''),
    md("## 4. ให้โมเดลเลือกเครื่องมือ\nคำถามขอข้อมูลโรงงาน A ซึ่งโมเดลต้องอ่านจากเครื่องมือ"),
    code('''
question = "ใช้ get_factory_status โดย factory_id เป็น A แล้วสรุปสถานะรับน้ำยางภาษาไทย ระบุว่าเป็นข้อมูลสมมติ"
messages = [
    {"role": "system", "content": "เรียกเครื่องมือหนึ่งครั้งเพื่อตรวจสถานะโรงงานก่อนตอบ"},
    {"role": "user", "content": question},
]
selected = chat(messages, tools=tools)
messages.append(selected)
'''),
    md("## 5. เรียกเครื่องมือผ่าน MCP แล้วสรุปคำตอบ\nNotebook ส่งคำขอไปยัง MCP server และนำผลกลับให้ local LLM จากนั้นปิด server อัตโนมัติ"),
    code('''
async def execute_tools():
    async with stdio_client(server_parameters) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            for call in selected.get("tool_calls", []):
                function = call["function"]
                result = await session.call_tool(function["name"], function["arguments"])
                tool_text = "\\n".join(block.text for block in result.content if block.type == "text")
                messages.append({"role": "tool", "tool_name": function["name"], "content": tool_text})

await execute_tools()
answer = chat(messages)
print(answer["content"])
'''),
    md("## เสร็จแล้ว\nลองเปลี่ยนโรงงานเป็น B ในขั้นตอน 4 แล้วรันขั้นตอน 4–5 อีกครั้ง\n\nโมเดลเลือกเครื่องมือ ส่วน notebook เรียกเครื่องมือผ่าน MCP หากเปลี่ยนโมเดลที่รองรับ tools สามารถใช้ MCP server เดิมได้"),
])
