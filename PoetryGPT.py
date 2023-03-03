import openai

# Define your OpenAI API key
openai.api_key = "YOUR_API_KEY"


# Define a function to handle incoming messages and generate responses
def handle_message(message):
    # Add any necessary preprocessing to the message here
    # (e.g. remove punctuation, convert to lowercase, etc.)
    
    # Use OpenAI's chat API to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are seeking guidance from the Urdu poets."},
            {"role": "user", "content": "I am deeply in love with someone."},
            {"role": "assistant", "content": "لاکھوں میں اک تنہا ہوں میں، راہی دور کے پاس ,دیکھتا ہوں جب کوئی تو مرے ساتھ چل کے دیکھتے ہیں"},
            {"role": "user", "content": "You are missing someone."},
            {"role": "assistant", "content": "کبھی خوابوں میں ملو اگر، تو پوچھنا کہ وہ کیسی ہے ,کبھی تو بے وفائی کے سبب، مجھ کو بھی یاد کر لیا کر"},
            {"role": "user", "content": "You are feeling nostalgic."},
            {"role": "assistant", "content": "وہ جو بچپن میں کھیلتے تھے کبھی ٹھہر کے ,سنکھوں کی تھی دھوپ اور چھتیوں کا تھا ظل"},
            {"role": "user", "content": "You are feeling hopeful."},
            {"role": "assistant", "content": "رات یوں دیکھی کہ تسکین خاطر اہلِ دل نے ,اپنے پروانے کو پھر جلا دیا کریں"},
            {"role": "user", "content": "You are feeling overwhelmed."},
            {"role": "assistant", "content": "کس قدر آسان ہے کہنا مگر مشکل ہے بھول جانا,جو کچھ دن پہلے ہوا اب دوبارہ نہیں ہوتا"},
            {"role": "user", "content": "You are feeling disappointed."},
            {"role": "assistant", "content": "تھی جو شمع تو بجھ گئی، لوٹ آئیں ہیں کچھ ادھر ,ورنہ دل کو تو یہ بھی مالوم تھا کہ جلنے والی آئے گی"},
            {"role": "user", "content": "You are feeling content."},
            {"role": "assistant", "content": "خوشیوں کا مظاہرہ کرتے ہوئے اپنی عمر گزارو ,یہ سمندر بھی تیرے دریا کے سمندر نظر آئے"},
            {"role":"user", "content":message}
            
        ])
    
    # Extract the generated response from the API's JSON output
    response_text = response #.choices[0].text
    
    # Add any necessary postprocessing to the response here
    # (e.g. format the text, remove unwanted words/phrases, etc.)
    
    return response_text

