Enterprise IQ RAG Portal
An AI chatbot for businesses. Upload your PDFs and get accurate, source-backed answers from your own files. Upload a CSV or Excel dataset and get exact numbers (totals, averages, top performers) instead of guesses. Powered by two Groq-hosted models: GPT-OSS 20B and GPT-OSS 120B.
Live demo: coming soon
Features
Document Q&A with sources - ask questions about PDFs and get grounded answers with cited evidence.
Dataset-aware answers - upload a CSV or Excel file and number questions (highest, lowest, totals, averages) are answered from exact pandas calculations, not from PDF text.
Focus areas - choose General Documents, Finance & Reports, Legal & Policies, or Business Strategy to change how the AI answers.
Model and retrieval controls - pick the model, creativity, search strategy, top-k, chunk size and overlap.
Analytics section - upload a dataset and see top and lowest performers, totals and charts.
Strict mode - the AI answers only from the uploaded material, and says so when it cannot find an answer.
How it works
PDFs: pages are loaded, split into chunks, embedded and stored in Chroma. At question time the most relevant chunks are retrieved and sent to the model.
CSV / Excel: the file is loaded with pandas. A function (build_data_facts) calculates exact statistics: totals, averages, max and min per numeric column, the rows with the highest and lowest revenue, and the top 5 groups per category. These are added to the prompt as DATA FACTS, and the AI is told to trust them for any number question.
Answer: the model combines the retrieved evidence and the data facts into one grounded answer.
Why the dataset step exists: when the same dataset was converted to PDF, the wide table was split across pages and the chatbot guessed the wrong "highest revenue". Sending number questions to the real data fixed this.
Tech stack
Python, Streamlit, LangChain (ChatGroq), Chroma, pandas, Groq API
Evaluation
I wrote an answer key by calculating the correct answers directly in pandas on a 149,112-row cafe sales dataset, then asked the chatbot the same 10 questions.
#
Question
Correct answer
Chatbot
1
Highest net_revenue and its transaction_id
360.00 (transaction 149043)
Correct
2
Total net_revenue
630,308.64
Correct
3
Store location with highest total net_revenue
Tipu Sultan
Correct
4
Product category with highest total net_revenue
Coffee
Correct (after fix)
5
Most used payment_method
Credit/Debit Card
Correct
6
Number of transactions
149,112
Correct
7
Average wait_time_min
5.66
Correct
8
Average service_rating
4.14
Correct
9
Total transaction_qty
214,463
Correct
10
Weekday with most transactions
Monday
Correct
Result: 10/10 on this test. The first run scored 9/10: question 4 failed because the data summary was too long and was cut off before the category lines. I shortened and reordered the summary, and it passed on the second run.
Limitations
The test set is small (10 questions), all about aggregates, and was checked by hand.
The chatbot can only answer number questions that build_data_facts already calculates. Custom questions such as "average net revenue per weekday" may fail.
The Retrieved Evidence panel shows PDF chunks, even when the answer came from the dataset.
The dataset must be uploaded again after a browser refresh.
Tables converted to PDF lose their structure. Use the original CSV or Excel file for number questions.
Roadmap
Run safe, on-demand pandas queries for any number question.
Automate the 10-question test so it re-runs after every change.
Deploy on Streamlit Community Cloud.