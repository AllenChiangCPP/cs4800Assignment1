import google.generativeai as genai

#Google Gemini API key
genai.configure(api_key="")

#function for generating answer of expression
def generate_answer(expression):
    #create an instance of google's generative model
    model = genai.GenerativeModel('models/gemini-1.5-flash')
    
    #generate answer and explanation to expression
    response = model.generate_content("Can you solve and explain the expression " + expression + "?. Can you display the answer on the first line starting with 'Answer: ', and give an error message if the expression is not possible, and display the step by step explanation two lines after the first. The explanation should start with  'Explanation: '")
    
    #return the answer of the expression as tet
    return response.text
