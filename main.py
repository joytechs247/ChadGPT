
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


from bs4 import BeautifulSoup
import requests

def Javascript():
        try:
            source = requests.get('https://developer.mozilla.org/en-US/docs/Web/JavaScript').text
            
            soup = BeautifulSoup(source, 'html.parser')
            data = soup.find('article', class_='main-page-content').text
            print(data)

        except Exception as e:
            print(e)    




def React():
        try:
            source = requests.get('https://react.dev/reference/react').text
            
            soup = BeautifulSoup(source, 'html.parser')
            data = soup.find('article', class_='font-normal break-words text-primary dark:text-primary-dark').text
            print(data)

        except Exception as e:
            print(e)



def Node():
        try:
            source = requests.get('https://nodejs.org/docs/latest/api/').text
            
            soup = BeautifulSoup(source, 'html.parser')
            data = soup.find('div', id='apicontent').text
            print(data)

        except Exception as e:
            print(e)

def NPM():
        try:
            source = requests.get('https://docs.npmjs.com/about-npm').text
            
            soup = BeautifulSoup(source, 'html.parser')
            data = soup.find('main', class_='Box-sc-g0xbh4-0 jrNUvm').text
            print(data)

        except Exception as e:
            print(e)


def Mongoose():
        try:
            source = requests.get('https://mongoosejs.com/docs/guide.html').text
            
            soup = BeautifulSoup(source, 'html.parser')
            data = soup.find('div', class_='container').text
            print(data)

        except Exception as e:
            print(e)

def Express():
        try:
            source = requests.get('https://expressjs.com/en/starter/installing.html').text
            
            soup = BeautifulSoup(source, 'html.parser')
            data = soup.find('div', id='page-doc').text
            print(data)

        except Exception as e:
            print(e)

def Next():
        try:
            source = requests.get('https://nextjs.org/docs').text
            
            soup = BeautifulSoup(source, 'html.parser')
            data = soup.find('div', class_='prose prose-vercel max-w-none').text
            print(data)

        except Exception as e:
            print(e)

def Axios():
        try:
            source = requests.get('https://axios-http.com/docs/intro').text
            
            soup = BeautifulSoup(source, 'html.parser')
            data = soup.find('div', class_='body').text
            print(data)

        except Exception as e:
            print(e)


def TailwindCSS():
        try:
            source = requests.get('https://tailwindcss.com/docs').text
            
            soup = BeautifulSoup(source, 'html.parser')
            data = soup.find('main', class_='max-w-3xl mx-auto relative z-20 pt-10 xl:max-w-none').text
            print(data)

        except Exception as e:
            print(e)


def Vite():
        try:
            source = requests.get('https://vitejs.dev/guide/').text
            
            soup = BeautifulSoup(source, 'html.parser')
            data = soup.find('div', class_='content-container').text
            print(data)

        except Exception as e:
            print(e)



def call(name):
    if name == 'Javascript':
        Javascript()

    elif name == 'React':
        React()

    elif name == 'Node':
        Node()

    elif name == 'NPM':
        NPM()

    elif name == 'Express':
        Express()
    elif name == 'Mongoose':
        Mongoose()

    elif name == 'Next':
        Next()

    elif name == 'Axios':
        Axios()

    elif name == 'TailwindCSS':
        TailwindCSS()

    elif name == 'Vite':
        Vite()



name = input('Enter the name of the topic: ')
call(name)


