### User guide _model calling
1. Build docker using exisitng docker file
2. run docker in bash mode - e.g. docker run -p 8000:8000 -p 8889:8889 -it your_image_name bash
3. In bash run app.py using "python /Django/app.py"
4. Post request and it will download dependence for torch e.g. curl -X POST "http://localhost:8000/spam-detection/" -H "Content-Type: application/json" -d '{"text": "click here and win a fortune!!!!!"}'

INPUT: '{"text": "click here and win a fortune!!!!!"}

OUTPUT: {"result":"RESULT: Your message is 94.91 percent chance to be a scam."}
