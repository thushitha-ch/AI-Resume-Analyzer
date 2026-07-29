# start backend server 
# python
# uvicorn - python third party library / package 
# which is used to create backend server
# fastapi - to build apis in backend
# pip install fastapi uvicorn

# pip install langchain
# pip install langchain-core
# pip install pypdf
# pip install python-multipart
# pip install sentence-transformers
# pip install langchain-community
# pip install langchain-chroma
# pip install langchain-text-splitters
# pip install fastapi huggingface
# pip install langchain-groq
from fastapi import FastAPI, File, UploadFile # import FastAPI class from fastapi module
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_groq import ChatGroq

fast_api_obj=FastAPI()

llm=ChatGroq(
    api_key="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",
    model="llama-3.3-70b-versatile"
)

@fast_api_obj.post("/analyze_resume")
async def resume_taker(resume: UploadFile = File(...)):
    file_name=resume.filename         #my_resume.pdf

    with open(file_name, "wb") as f:
        f.write(await resume.read())
    # print(resume.filename)
    # print(resume.content_type)
    loader=PyPDFLoader(file_name) #you are trying to take th
    docs=loader.load() # 1 pdf to 10 
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=700, 
        chunk_overlap=150
    )
    chunks=splitter.split_documents(docs)

    e_model=HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vector_db=Chroma.from_documents(
        documents=chunks, 
        embedding=e_model,
        persist_directory="./chroma_folder"
    )
    r_docs = vector_db.similarity_search(
        query="analyze resume and give pros and cons",
        k=5
    )  #similarity_search / retreiving

    context="\n\n".join(
        [d.page_content for d in r_docs]
    )

    #prompt with context = argumentation
    prompts=f"""
You are an expert HR recruiter.

Analyze the resume and provide a concise professional review.

Use ONLY information from the resume.
Do not add or assume anything.

Return the answer in this format:

## Candidate Summary
(2-3 lines)

## Education
- Highest qualification only
- Mention degree, college name, and CGPA/percentage if available.

## Technical Skills
(List only important skills)

## Experience
(Briefly mention internships/jobs in 2-3 bullet points)

## Projects
Extract all projects mentioned in the resume.
do not say "none mentioned" unless the resume has no project section.
mention project name exactly.
For each project:
- Give only 2 line explanation

## Certifications
(List all certifications)

## Strengths
(3 bullet points)

## Weaknesses
Mention only resume-based weaknesses.
Do not give generic advice.
(2 bullet points)

## Suitable Roles
(List 4-5 job roles)

## Resume Score
Give score out of 10 with one-line reason

## Improvements
Give only 3 practical resume improvement suggestions based on the actual resume.
Avoid generic advice.


Resume:
{context}
"""

    
    response=llm.invoke(prompts) #calling chatGRoq for response with my context and prompt
    return {
        "msg" : response.content
    }
