from pythainlp.summarize import summarize

def gen_summarizer(text='Hello'):
    return summarize(text, n=4)
    

if __name__ == "__main__":
     print("hello")