
# 1) JavaScript: https://developer.mozilla.org/en-US/docs/Web/JavaScript
# 2) React: https://react.dev/reference/react
# 3) Node: https://nodejs.org/docs/latest/api/
# 4) NPM: https://docs.npmjs.com
# 5) Mongoose: https://mongoosejs.com/docs/guide.html
# 6) Express: https://expressjs.com/
# 7) Next: https://nextjs.org/docs
# 8) Axios: https://axios-http.com/docs/intro
# 9) TailwindCSS: https://tailwindcss.com/docs
# 10)Vite: https://vitejs.dev/guide/




# def Javascript():
        
#             source = requests.get('https://developer.mozilla.org/en-US/docs/Web/JavaScript').text
            
#             soup = BeautifulSoup(source, 'html.parser')
#             data = soup.find('article', class_='main-page-content').text
#             return data
   




# def React():
        
#             source = requests.get('https://react.dev/reference/react').text
#             soup = BeautifulSoup(source, 'html.parser')
#             data = soup.find('article', class_='font-normal break-words text-primary dark:text-primary-dark').text
#             return data

      



# def Node():
        
#             source = requests.get('https://nodejs.org/docs/latest/api/documentation.html').text
#             soup = BeautifulSoup(source, 'html.parser')
#             data = soup.find('div', id='apicontent').text
#             return data

      

# def NPM():
        
#             source = requests.get('https://docs.npmjs.com/about-npm').text
#             soup = BeautifulSoup(source, 'html.parser')
#             data = soup.find('main', class_='Box-sc-g0xbh4-0 jrNUvm').text
#             return data

       


# def Mongoose():
        
#             source = requests.get('https://mongoosejs.com/docs/guide.html').text
#             soup = BeautifulSoup(source, 'html.parser')
#             data = soup.find('div', class_='container').text
#             return data

       

# def Express():
        
#             source = requests.get('https://expressjs.com/en/starter/installing.html').text
#             soup = BeautifulSoup(source, 'html.parser')
#             data = soup.find('div', id='page-doc').text
#             return data

      

# def Next():
        
#             source = requests.get('https://nextjs.org/docs').text
#             soup = BeautifulSoup(source, 'html.parser')
#             data = soup.find('div', class_='prose prose-vercel max-w-none').text
#             return data

       

# def Axios():
        
#             source = requests.get('https://axios-http.com/docs/intro').text
            
#             soup = BeautifulSoup(source, 'html.parser')
#             data = soup.find('div', class_='body').text
#             return data

        


# def TailwindCSS():
        
#             source = requests.get('https://tailwindcss.com/docs').text
#             soup = BeautifulSoup(source, 'html.parser')
#             data = soup.find('main', class_='max-w-3xl mx-auto relative z-20 pt-10 xl:max-w-none').text
#             return data
        


# def Vite():
        
#             source = requests.get('https://vitejs.dev/guide/').text
#             soup = BeautifulSoup(source, 'html.parser')
#             data = soup.find('div', class_='content-container').text
#             return data

       





def check_and_call(sentence):
    if "javascript" in sentence.lower():
        source = requests.get('https://developer.mozilla.org/en-US/docs/Web/JavaScript').text
        soup = BeautifulSoup(source, 'html.parser')
        data = soup.find('article', class_='main-page-content').text
        return data

    elif "react" in sentence.lower():   
        source = requests.get('https://react.dev/reference/react').text
        soup = BeautifulSoup(source, 'html.parser')
        data = soup.find('article', class_='font-normal break-words text-primary dark:text-primary-dark').text
        return data 
    
    elif "node" in sentence.lower():
        source = requests.get('https://nodejs.org/docs/latest/api/documentation.html').text
        soup = BeautifulSoup(source, 'html.parser')
        data = soup.find('div', id='apicontent').text
        return data    

    elif "npm" in sentence.lower():    
        source = requests.get('https://docs.npmjs.com/about-npm').text
        soup = BeautifulSoup(source, 'html.parser')
        data = soup.find('main', class_='Box-sc-g0xbh4-0 jrNUvm').text
        return data     

    elif "express" in sentence.lower():
        source = requests.get('https://expressjs.com/en/starter/installing.html').text
        soup = BeautifulSoup(source, 'html.parser')
        data = soup.find('div', id='page-doc').text
        return data

    elif "mongoose" in sentence.lower():
        source = requests.get('https://mongoosejs.com/docs/guide.html').text
        soup = BeautifulSoup(source, 'html.parser')
        data = soup.find('div', class_='container').text
        return data

    elif "next" in sentence.lower():
        source = requests.get('https://nextjs.org/docs').text
        soup = BeautifulSoup(source, 'html.parser')
        data = soup.find('div', class_='prose prose-vercel max-w-none').text
        return data

    elif "axios" in sentence.lower():
        source = requests.get('https://axios-http.com/docs/intro').text
        soup = BeautifulSoup(source, 'html.parser')
        data = soup.find('div', class_='body').text
        return data

    elif "tailwind" in sentence.lower():
        source = requests.get('https://tailwindcss.com/docs').text
        soup = BeautifulSoup(source, 'html.parser')
        data = soup.find('main', class_='max-w-3xl mx-auto relative z-20 pt-10 xl:max-w-none').text
        return data

    elif "vite" in sentence.lower():
        source = requests.get('https://vitejs.dev/guide/').text
        soup = BeautifulSoup(source, 'html.parser')
        data = soup.find('div', class_='content-container').text
        return data

    else:
        print("Sorry, I didn't understand that. Please try again.")





from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests


app = Flask(__name__)





@app.route('/', methods=['GET', 'POST'])
def process_sentence():
    if request.method == 'POST':
        sentence = request.form.get('sentence', '')
        if sentence:
            response = check_and_call(sentence)
            return render_template('response.html', response=response)
        else:
            return render_template('index.html', error="Please provide a sentence.")
    else:
        # For a GET request, just display the form
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)




     







